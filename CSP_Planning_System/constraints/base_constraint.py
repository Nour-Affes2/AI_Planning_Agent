from abc import ABC, abstractmethod
from ortools.sat.python import cp_model

class BaseConstraint(ABC):
    """Base class for all constraint types"""
    
    def __init__(self, model: cp_model.CpModel, data_manager, variables: dict):
        self.model = model
        self.data = data_manager
        self.variables = variables
    
    @abstractmethod
    def apply_constraints(self, planning_dates: list[str], time_slots: list[str], **kwargs):
        """Apply the specific constraint type"""
        pass