from ortools.sat.python import cp_model

class SolutionFormatter:
    """Formats solver solutions into readable output"""
    
    def __init__(self, data_manager):
        self.data = data_manager
    
    def format_solution(self, solver: cp_model.CpSolver, variables: dict, 
                       status: int,
                       planning_dates: list[str], time_slots: list[str]) -> dict:
        """Format the solution into a structured dictionary"""
        result = {
            "status": self._get_status_string(status),
            "assignments": [],
            "statistics": {}
        }
        
        if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
            # Extract assignments
            for emp in self.data.employees:
                for client in self.data.clients:
                    for date in planning_dates:
                        for time_slot in time_slots:
                            if (emp.id in variables and 
                                client.id in variables[emp.id] and
                                date in variables[emp.id][client.id] and
                                time_slot in variables[emp.id][client.id][date]):
                                
                                var = variables[emp.id][client.id][date][time_slot]
                                if solver.Value(var) == 1:
                                    result["assignments"].append({
                                        "employee_id": emp.id,
                                        "employee_name": emp.name,
                                        "client_id": client.id,
                                        "client_name": client.name,
                                        "date": date,
                                        "time_slot": time_slot
                                    })
            
            # Add statistics
            result["statistics"] = {
                "total_assignments": len(result["assignments"]),
                "objective_value": solver.ObjectiveValue(),
                "solve_time": solver.WallTime()
            }
        
        return result
    
    def _get_status_string(self, status: int) -> str:  
        """Convert status to readable string"""
        status_map = {
            cp_model.OPTIMAL: "Optimal",
            cp_model.FEASIBLE: "Feasible",
            cp_model.INFEASIBLE: "Infeasible",
            cp_model.MODEL_INVALID: "Model Invalid",
            cp_model.UNKNOWN: "Unknown"
        }
        return status_map.get(status, "Unknown")