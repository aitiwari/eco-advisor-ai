 
class ClimateCommunity:
    def __init__(self):
        self.challenges = {}
        self.leaderboard = {}
        
    def create_challenge(self, name, target, duration):
        self.challenges[name] = {
            'participants': {},
            'target': target,
            'duration': duration,
            'progress': 0
        }
        
    def join_challenge(self, user_id, challenge_name):
        if challenge_name in self.challenges:
            self.challenges[challenge_name]['participants'][user_id] = 0
            
    def update_progress(self, user_id, challenge_name, reduction):
        if challenge_name in self.challenges:
            self.challenges[challenge_name]['participants'][user_id] += reduction
            self.challenges[challenge_name]['progress'] += reduction
            
    def get_leaderboard(self, challenge_name):
        if challenge_name in self.challenges:
            participants = self.challenges[challenge_name]['participants']
            return sorted(participants.items(), key=lambda x: x[1], reverse=True)
        return []