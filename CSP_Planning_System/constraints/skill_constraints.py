from constraints.base_constraint import BaseConstraint

class SkillConstraints(BaseConstraint):
    """Ensures employees have required skills for assigned tasks"""
    
    def apply_constraints(self, planning_dates: list[str], time_slots: list[str], 
                         task_assignments: dict[int, int] = None, **kwargs):
        if not task_assignments:
            return
        
        employee_skill_map = self.data.get_employee_skills_map()
        task_skill_map = self.data.get_task_skill_map()
        
        for client_id, task_id in task_assignments.items():
            required_skill = task_skill_map[task_id]
            
            for emp in self.data.employees:
                emp_skills = employee_skill_map.get(emp.id, set())
                
                if required_skill not in emp_skills:
                    # Employee cannot be assigned to this client
                    for date in planning_dates:
                        for time_slot in time_slots:
                            if (emp.id in self.variables and 
                                client_id in self.variables[emp.id] and
                                date in self.variables[emp.id][client_id] and
                                time_slot in self.variables[emp.id][client_id][date]):
                                
                                self.model.Add(
                                    self.variables[emp.id][client_id][date][time_slot] == 0
                                )
