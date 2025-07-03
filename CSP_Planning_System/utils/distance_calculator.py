class DistanceCalculator:
    """Calculates distances between employees and clients"""
    
    def calculate_distance_matrix(self, employees: list, clients: list) -> dict:
        """Calculate distance matrix between employees and clients"""
        distance_matrix = {}
        
        for emp in employees:
            for client in clients:
                # Simplified distance calculation
                if emp.city == client.city:
                    distance = 5.0  # Same city
                else:
                    distance = 50.0  # Different city
                distance_matrix[(emp.id, client.id)] = distance
        
        return distance_matrix