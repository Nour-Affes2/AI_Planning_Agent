class TimeUtils:
    """Utility functions for time-related operations"""
    
    @staticmethod
    def get_conflicting_time_slots(start_time: str, end_time: str, 
                                  time_slots: list[str]) -> list[str]:
        """Get time slots that conflict with given time range"""
        conflicting = []
        start_hour = int(start_time.split(':')[0])
        end_hour = int(end_time.split(':')[0])
        
        for slot in time_slots:
            slot_hour = int(slot.split(':')[0])
            if start_hour <= slot_hour < end_hour:
                conflicting.append(slot)
        
        return conflicting