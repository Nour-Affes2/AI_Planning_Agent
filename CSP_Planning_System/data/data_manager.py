import json
import sys
from pathlib import Path
from typing import List
sys.path.append(str(Path(__file__).parent.parent))
from models.data_models import *

class DataManager:
    """Handles loading and managing JSON data files"""
    
    def __init__(self, data_dir: str = "./../../data_files"):
        self.data_dir = Path(data_dir)
        self.employees: List[Employee] = []
        self.clients: List[Client] = []
        self.assignments: List[Assignment] = []
        self.skills: List[Skill] = []
        self.tasks: List[Task] = []
        self.employee_skills: List[EmployeeSkill] = []
    
    def load_all_data(self):
        """Load all data from JSON files"""
        self.employees = self._load_employees()
        self.clients = self._load_clients()
        self.assignments = self._load_assignments()
        self.skills = self._load_skills()
        self.tasks = self._load_tasks()
        self.employee_skills = self._load_employee_skills()
    
    def _load_employees(self) -> List[Employee]:
        return self._load_json_as_dataclass("employees.json", Employee)
    
    def _load_clients(self) -> List[Client]:
        return self._load_json_as_dataclass("clients.json", Client)
    
    def _load_assignments(self) -> List[Assignment]:
        return self._load_json_as_dataclass("assignments.json", Assignment)
    
    def _load_skills(self) -> List[Skill]:
        return self._load_json_as_dataclass("skills.json", Skill)
    
    def _load_tasks(self) -> List[Task]:
        return self._load_json_as_dataclass("tasks.json", Task)
    
    def _load_employee_skills(self) -> List[EmployeeSkill]:
        return self._load_json_as_dataclass("employee_skills.json", EmployeeSkill)
    
    def _load_json_as_dataclass(self, filename: str, dataclass_type):
        """Generic method to load JSON and convert to dataclass"""
        filepath = self.data_dir / filename
        with open(filepath, 'r') as f:
            data = json.load(f)
        return [dataclass_type(**item) for item in data]
    
    def get_employee_skills_map(self) -> dict[int, set[int]]:
        """Get mapping of employee_id -> set of skill_ids"""
        skill_map = {}
        for emp_skill in self.employee_skills:
            if emp_skill.employee_id not in skill_map:
                skill_map[emp_skill.employee_id] = set()
            skill_map[emp_skill.employee_id].add(emp_skill.skill_id)
        return skill_map
    
    def get_task_skill_map(self) -> dict[int, int]:
        """Get mapping of task_id -> required_skill_id"""
        return {task.id: task.required_skill for task in self.tasks}
