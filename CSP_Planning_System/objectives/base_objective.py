from abc import ABC, abstractmethod
from ortools.sat.python import cp_model

class BaseObjective(ABC):
    """Base class for objective functions"""
    
    def __init__(self, model: cp_model.CpModel, variables: dict):
        self.model = model
        self.variables = variables
    
    @abstractmethod
    def set_objective(self, **kwargs):
        """Set the objective function"""
        pass