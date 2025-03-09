from groq import Groq
from .config import AppConfig

class GroqClient:
    """Handles Groq API interactions for sustainability recommendations."""
    
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)
        self.config = AppConfig()

    def get_recommendations(self, user_data: dict) -> str:
        """Get AI-powered sustainability recommendations."""
        prompt = self._build_prompt(user_data)
        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.config.model_name,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Groq API Error: {str(e)}") from e

    def _build_prompt(self, user_data: dict) -> str:
        return f"""
        Analyse the given user data {user_data} and Create recommendations using dark-mode compatible in markdown fomat:
        
        🌟 Your Sustainability Action Plan
        
        📊 **Annual Reduction Potential**: {{percentage}}% ({{kg}} kg CO2)
         
        🔋 **Current Footprint Tier**: Tier {{tier}}
         
        ⚡ **Quick Wins Available**: {{number}}
        
        draw something line of information with --> for A[Current Impact] --> B[Target Impact]
        ```mermaid
        flowchart LR
            A[Current Impact] --> B[Target Impact]
            style A fill:#888,stroke:#666
            style B fill:#2ecc71,stroke:#27ae60
        ```
        Also give in tabular format
        
         🚦 Priority Areas
        
        | Category       | Impact | Difficulty | Progress       |
        |----------------|--------|------------|----------------|
        | Transportation | 🔥 High | 🟢 Easy    | ▰▰▰▰▱ 80%      |
        | Energy         | 🟠 Medium | 🟡 Moderate | ▰▰▱▱▱ 40%      |
        | Diet           | 🟢 Low  | 🔴 Hard    | ▰▱▱▱▱ 20%      |
        
         🛠️ Recommended Actions
        
        ```mermaid
        graph TD
            A[Start Here] --> B[Car Pooling]
            A --> C[LED Bulbs]
            B --> D[Reduce 200kg CO2]
            C --> E[Save $150/year]
        ```
        Also give in tabular format
        📉 **CO2 Reduction** |💰 **Savings**| ⏱️ **Effort**
            
        💡 Pro Tips:
        """