from dataclasses import dataclass
from typing import Optional

@dataclass
class Employee:
    id: int
    name: str
    address: str
    city: str

@dataclass
class Client:
    id: int
    name: str
    address: str
    city: str

@dataclass
class Assignment:
    id: int
    employee_id: int
    client_id: int
    date: str
    start_time: str
    end_time: str

@dataclass
class Skill:
    id: int
    name: str

@dataclass
class Task:
    id: int
    name: str
    required_skill: int

@dataclass
class EmployeeSkill:
    employee_id: int
    skill_id: int

@dataclass
class PlanningRequest:
    """Request parameters for planning"""
    planning_dates: list[str]
    time_slots: list[str]
    task_assignments: dict[int, int]  # {client_id: task_id}
    required_coverage: Optional[dict[int, dict[str, int]]] = None
    objective_type: str = "maximize_assignments"