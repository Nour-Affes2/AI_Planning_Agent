from ortools.sat.python import cp_model
from data.data_manager import DataManager
from data.sample_data_generator import SampleDataGenerator
from constraints.skill_constraints import SkillConstraints
from constraints.availability_constraints import AvailabilityConstraints
from constraints.capacity_constraints import CapacityConstraints
from constraints.coverage_constraints import CoverageConstraints
from objectives.maximize_assignments import MaximizeAssignments
from objectives.minimize_travel import MinimizeTravel
from solver.solution_formatter import SolutionFormatter
from models.data_models import PlanningRequest

class CSPSolver:
    """Main CSP solver orchestrating the planning process"""
    
    def __init__(self, data_dir: str = "data_files"):
        self.data_manager = DataManager(data_dir)
        self.model = cp_model.CpModel()
        self.solver = cp_model.CpSolver()
        self.variables = {}
        self.solution_formatter = None
    
    def initialize(self):
        """Initialize the solver with data"""
        try:
            self.data_manager.load_all_data()
        except FileNotFoundError:
            print("Data files not found. Creating sample data...")
            generator = SampleDataGenerator(self.data_manager.data_dir)
            generator.generate_all_sample_data()
            self.data_manager.load_all_data()
        
        self.solution_formatter = SolutionFormatter(self.data_manager)
    
    def solve(self, request: PlanningRequest) -> dict:
        """Main solving method"""
        # Reset model for new problem
        self.model = cp_model.CpModel()
        
        # Create decision variables
        self._create_variables(request.planning_dates, request.time_slots)
        
        # Apply constraints
        self._apply_constraints(request)
        
        # Set objective
        self._set_objective(request.objective_type)
        
        # Solve
        status = self.solver.Solve(self.model)
        
        # Format and return solution
        return self.solution_formatter.format_solution(
            self.solver, self.variables, status, 
            request.planning_dates, request.time_slots
        )
    
    def _create_variables(self, planning_dates: list[str], time_slots: list[str]):
        """Create decision variables"""
        self.variables = {}
        
        for emp in self.data_manager.employees:
            self.variables[emp.id] = {}
            for client in self.data_manager.clients:
                self.variables[emp.id][client.id] = {}
                for date in planning_dates:
                    self.variables[emp.id][client.id][date] = {}
                    for time_slot in time_slots:
                        var_name = f"assign_{emp.id}_{client.id}_{date}_{time_slot}"
                        self.variables[emp.id][client.id][date][time_slot] = \
                            self.model.NewBoolVar(var_name)
    
    def _apply_constraints(self, request: PlanningRequest):
        """Apply all constraint types"""
        constraint_types = [
            SkillConstraints,
            AvailabilityConstraints,
            CapacityConstraints,
            CoverageConstraints
        ]
        
        for constraint_class in constraint_types:
            constraint = constraint_class(self.model, self.data_manager, self.variables)
            constraint.apply_constraints(
                request.planning_dates,
                request.time_slots,
                task_assignments=request.task_assignments,
                required_coverage=request.required_coverage
            )
    
    def _set_objective(self, objective_type: str):
        """Set the optimization objective"""
        objective_map = {
            "maximize_assignments": MaximizeAssignments,
            "minimize_travel": MinimizeTravel
        }
        
        objective_class = objective_map.get(objective_type, MaximizeAssignments)
        objective = objective_class(self.model, self.variables)
        objective.set_objective(data_manager=self.data_manager)