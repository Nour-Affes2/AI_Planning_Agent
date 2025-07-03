from constraints.base_constraint import BaseConstraint

class CapacityConstraints(BaseConstraint):
    """Ensures each employee works at most one assignment per time slot"""
    
    def apply_constraints(self, planning_dates: list[str], time_slots: list[str], **kwargs):
        for emp in self.data.employees:
            for date in planning_dates:
                for time_slot in time_slots:
                    assignments_in_slot = []
                    
                    for client in self.data.clients:
                        if (emp.id in self.variables and 
                            client.id in self.variables[emp.id] and
                            date in self.variables[emp.id][client.id] and
                            time_slot in self.variables[emp.id][client.id][date]):
                            
                            assignments_in_slot.append(
                                self.variables[emp.id][client.id][date][time_slot]
                            )
                    
                    if assignments_in_slot:
                        self.model.Add(sum(assignments_in_slot) <= 1)