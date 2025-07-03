from objectives.base_objective import BaseObjective
from utils.distance_calculator import DistanceCalculator

class MinimizeTravel(BaseObjective):
    """Objective to minimize total travel distance/cost"""
    
    def set_objective(self, data_manager=None, **kwargs):
        if not data_manager:
            return
        
        distance_calc = DistanceCalculator()
        distance_matrix = distance_calc.calculate_distance_matrix(
            data_manager.employees, data_manager.clients
        )
        
        travel_cost = []
        for emp_id in self.variables:
            for client_id in self.variables[emp_id]:
                distance = distance_matrix.get((emp_id, client_id), 0)
                for date in self.variables[emp_id][client_id]:
                    for time_slot in self.variables[emp_id][client_id][date]:
                        travel_cost.append(
                            self.variables[emp_id][client_id][date][time_slot] * int(distance * 100)
                        )
        
        self.model.Minimize(sum(travel_cost))