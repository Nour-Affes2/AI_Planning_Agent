from objectives.base_objective import BaseObjective

class MaximizeAssignments(BaseObjective):
    """Objective to maximize total number of assignments"""
    
    def set_objective(self, **kwargs):
        total_assignments = []
        
        for emp_id in self.variables:
            for client_id in self.variables[emp_id]:
                for date in self.variables[emp_id][client_id]:
                    for time_slot in self.variables[emp_id][client_id][date]:
                        total_assignments.append(
                            self.variables[emp_id][client_id][date][time_slot]
                        )
        
        self.model.Maximize(sum(total_assignments))