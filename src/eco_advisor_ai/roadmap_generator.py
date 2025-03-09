 
from .groq_client import GroqClient

class RoadmapGenerator:
    def __init__(self, groq_client):
        self.groq = groq_client
        
    def generate_roadmap(self, user_data):
        prompt = f"""
        Create a 12-month sustainability roadmap for a user with these metrics:
        {user_data}
        
        Structure the plan with:
        - 3 phases: Immediate Wins (0-3 months), Habit Building (3-6), Long-Term (6-12)
        - Concrete monthly actions
        - Estimated CO2 savings per action
        - Difficulty level (1-5)
        Format as markdown with emojis
        """
        
        return self.groq.get_recommendations({'content': prompt})