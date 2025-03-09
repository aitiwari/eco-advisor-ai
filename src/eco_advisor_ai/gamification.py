 
class SustainabilityGame:
    BADGES = {
        'starter': {'threshold': 100, 'emoji': '🌱'},
        'hero': {'threshold': 500, 'emoji': '🦸'},
        'champion': {'threshold': 1000, 'emoji': '🏆'}
    }
    
    def __init__(self):
        self.users = {}
        
    def update_progress(self, user_id, co2_reduction):
        if user_id not in self.users:
            self.users[user_id] = {'total': 0, 'badges': []}
            
        self.users[user_id]['total'] += co2_reduction
        new_badges = []
        
        for badge, criteria in self.BADGES.items():
            if criteria['threshold'] <= self.users[user_id]['total'] and badge not in self.users[user_id]['badges']:
                new_badges.append(f"{criteria['emoji']} {badge.capitalize()}")
                self.users[user_id]['badges'].append(badge)
                
        return new_badges
    
    def get_xp(self, user_id):
        return self.users.get(user_id, {}).get('total', 0) * 10