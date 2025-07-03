from solver.csp_solver import CSPSolver
from models.data_models import PlanningRequest

def main():
    """Example usage of the modular CSP planning system"""
    
    # Initialize solver
    solver = CSPSolver()
    solver.initialize()
    
    # Create planning request
    request = PlanningRequest(
        planning_dates=["2024-01-16", "2024-01-17"],
        time_slots=["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"],
        task_assignments={
            1: 1,  # Tech Corp needs Software Development
            2: 5,  # Healthcare Inc needs Client Support
            3: 2,  # Finance Ltd needs Data Processing
            4: 3   # Retail Group needs Team Leadership
        },
        required_coverage={
            1: {"2024-01-16": 2, "2024-01-17": 1},
            2: {"2024-01-16": 1, "2024-01-17": 1},
        },
        objective_type="maximize_assignments"
    )
    
    # Solve the problem
    solution = solver.solve(request)
    
    # Print results
    print(f"Planning Status: {solution['status']}")
    print(f"Total Assignments: {solution['statistics'].get('total_assignments', 0)}")
    print("\nAssignments:")
    for assignment in solution['assignments']:
        print(f"  {assignment['employee_name']} -> {assignment['client_name']} "
              f"on {assignment['date']} at {assignment['time_slot']}")

if __name__ == "__main__":
    main()