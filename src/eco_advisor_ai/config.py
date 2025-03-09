 
from dataclasses import dataclass

@dataclass
class EmissionFactors:
    """Emission factors in kg CO2e per unit."""
    electricity: float = 0.5
    gas: float = 2.0
    car: float = 0.2
    bus: float = 0.1
    flight_short: float = 0.25
    meat_diet: float = 2.5
    vegetarian_diet: float = 1.0

@dataclass
class AppConfig:
    """Application configuration constants."""
    page_title: str = "🌍 EcoAdvisor AI"
    page_icon: str = "🌍"
    layout: str = "centered"
    model_name: str = "mixtral-8x7b-32768"
    flight_speed_kmh: float = 800.0
    progress_bar_categories: tuple = (
        "Electricity", "Gas", "Car Travel", 
        "Public Transport", "Flights", "Diet"
    )