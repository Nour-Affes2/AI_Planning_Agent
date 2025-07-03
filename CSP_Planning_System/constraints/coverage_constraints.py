from constraints.base_constraint import BaseConstraint

class CoverageConstraints(BaseConstraint):
    """Ensures clients get minimum required coverage"""
    
    def apply_constraints(self, planning_dates: list[str], time_slots: list[str], 
                         required_coverage: dict[int, dict[str, int]] = None, **kwargs):
        if not required_coverage:
            return
        
        for client_id, date_requirements in required_coverage.items():
            for date, min_assignments in date_requirements.items():
                if date in planning_dates:
                    total_assignments = []
                    
                    for emp in self.data.employees:
                        for time_slot in time_slots:
                            if (emp.id in self.variables and 
                                client_id in self.variables[emp.id] and
                                date in self.variables[emp.id][client_id] and
                                time_slot in self.variables[emp.id][client_id][date]):
                                
                                total_assignments.append(
                                    self.variables[emp.id][client_id][date][time_slot]
                                )
                    
                    if total_assignments:
                        self.model.Add(sum(total_assignments) >= min_assignments)