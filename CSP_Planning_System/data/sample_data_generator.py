import json
from pathlib import Path

class SampleDataGenerator:
    """Generates sample data for testing"""
    
    def __init__(self, output_dir: str = "data_files"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_all_sample_data(self):
        """Generate all sample data files"""
        self._generate_employees()
        self._generate_clients()
        self._generate_skills()
        self._generate_tasks()
        self._generate_employee_skills()
        self._generate_assignments()
    
    def _generate_employees(self):
        data = [
            {"id": 1, "name": "Alice Johnson", "address": "123 Main St", "city": "New York"},
            {"id": 2, "name": "Bob Smith", "address": "456 Oak Ave", "city": "Boston"},
            {"id": 3, "name": "Carol Davis", "address": "789 Pine Rd", "city": "Chicago"},
            {"id": 4, "name": "David Wilson", "address": "321 Elm St", "city": "Seattle"}
        ]
        self._write_json("employees.json", data)
    
    def _generate_clients(self):
        data = [
            {"id": 1, "name": "Tech Corp", "address": "100 Business Blvd", "city": "New York"},
            {"id": 2, "name": "Healthcare Inc", "address": "200 Medical Dr", "city": "Boston"},
            {"id": 3, "name": "Finance Ltd", "address": "300 Money St", "city": "Chicago"},
            {"id": 4, "name": "Retail Group", "address": "400 Shop Ave", "city": "Seattle"}
        ]
        self._write_json("clients.json", data)
    
    def _generate_skills(self):
        data = [
            {"id": 1, "name": "Python Programming"},
            {"id": 2, "name": "Data Analysis"},
            {"id": 3, "name": "Project Management"},
            {"id": 4, "name": "System Administration"},
            {"id": 5, "name": "Customer Service"}
        ]
        self._write_json("skills.json", data)
    
    def _generate_tasks(self):
        data = [
            {"id": 1, "name": "Software Development", "required_skill": 1},
            {"id": 2, "name": "Data Processing", "required_skill": 2},
            {"id": 3, "name": "Team Leadership", "required_skill": 3},
            {"id": 4, "name": "Server Maintenance", "required_skill": 4},
            {"id": 5, "name": "Client Support", "required_skill": 5}
        ]
        self._write_json("tasks.json", data)
    
    def _generate_employee_skills(self):
        data = [
            {"employee_id": 1, "skill_id": 1},
            {"employee_id": 1, "skill_id": 2},
            {"employee_id": 2, "skill_id": 3},
            {"employee_id": 2, "skill_id": 5},
            {"employee_id": 3, "skill_id": 2},
            {"employee_id": 3, "skill_id": 4},
            {"employee_id": 4, "skill_id": 1},
            {"employee_id": 4, "skill_id": 3}
        ]
        self._write_json("employee_skills.json", data)
    
    def _generate_assignments(self):
        data = [
            {"id": 1, "employee_id": 1, "client_id": 1, "date": "2024-01-15", "start_time": "09:00", "end_time": "17:00"},
            {"id": 2, "employee_id": 2, "client_id": 2, "date": "2024-01-15", "start_time": "10:00", "end_time": "18:00"}
        ]
        self._write_json("assignments.json", data)
    
    def _write_json(self, filename: str, data: list):
        filepath = self.output_dir / filename
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)