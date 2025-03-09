from dataclasses import asdict
from .config import EmissionFactors, AppConfig

class CarbonCalculator:
    """Handles carbon footprint calculations."""
    
    def __init__(self):
        self.factors = EmissionFactors()
        self.config = AppConfig()

    def calculate_emissions(self, user_inputs: dict) -> dict:
        """Calculate emissions for all categories."""
        emissions = {
            "Electricity": self._calculate_electricity(user_inputs["electricity"]),
            "Gas": self._calculate_gas(user_inputs["gas"]),
            "Car Travel": self._calculate_car(user_inputs["car_km"]),
            "Public Transport": self._calculate_public_transport(user_inputs["bus_km"]),
            "Flights": self._calculate_flights(user_inputs["flight_hours"]),
            "Diet": self._calculate_diet(user_inputs["diet_type"])
        }
        emissions["Total"] = sum(emissions.values())
        return emissions

    def _calculate_electricity(self, usage: float) -> float:
        return usage * self.factors.electricity * 12

    def _calculate_gas(self, usage: float) -> float:
        return usage * self.factors.gas * 12

    def _calculate_car(self, km: float) -> float:
        return km * self.factors.car * 52

    def _calculate_public_transport(self, km: float) -> float:
        return km * self.factors.bus * 52

    def _calculate_flights(self, hours: float) -> float:
        return hours * self.config.flight_speed_kmh * self.factors.flight_short

    def _calculate_diet(self, diet_type: str) -> float:
        factor = self.factors.meat_diet if diet_type == "Meat-based" else self.factors.vegetarian_diet
        return 365 * factor

    def get_emission_factors(self) -> dict:
        """Return emission factors as dictionary."""
        return asdict(self.factors)
