from constraints.base_constraint import BaseConstraint
from utils.time_utils import TimeUtils

class AvailabilityConstraints(BaseConstraint):
    """Ensures employees are not double-booked with existing assignments"""
    
    def apply_constraints(self, planning_dates: list[str], time_slots: list[str], **kwargs):
        existing_assignments = self._group_existing_assignments()
        
        for (emp_id, date), time_ranges in existing_assignments.items():
            if date in planning_dates:
                for start_time, end_time in time_ranges:
                    conflicting_slots = TimeUtils.get_conflicting_time_slots(
                        start_time, end_time, time_slots
                    )
                    
                    for client in self.data.clients:
                        for slot in conflicting_slots:
                            if (emp_id in self.variables and 
                                client.id in self.variables[emp_id] and
                                date in self.variables[emp_id][client.id] and
                                slot in self.variables[emp_id][client.id][date]):
                                
                                self.model.Add(
                                    self.variables[emp_id][client.id][date][slot] == 0
                                )
    
    def _group_existing_assignments(self) -> dict:
        """Group existing assignments by employee and date"""
        existing_assignments = {}
        for assignment in self.data.assignments:
            key = (assignment.employee_id, assignment.date)
            if key not in existing_assignments:
                existing_assignments[key] = []
            existing_assignments[key].append((assignment.start_time, assignment.end_time))
        return existing_assignments