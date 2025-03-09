 
from eco_advisor_ai.calculations import CarbonCalculator
import pytest

@pytest.fixture
def calculator():
    return CarbonCalculator()

def test_calculations(calculator):
    inputs = {
        "electricity": 300,
        "gas": 50,
        "car_km": 100,
        "flight_hours": 5,
        "diet_type": "Meat-based",
        "bus_km": 30
    }
    
    result = calculator.calculate_emissions(inputs)
    assert pytest.approx(result["Total"], rel=0.01) == 6108.5
    assert result["Electricity"] == 300 * 0.5 * 12
    assert result["Diet"] == 365 * 2.5

def test_vegetarian_diet(calculator):
    inputs = {
        "electricity": 0,
        "gas": 0,
        "car_km": 0,
        "flight_hours": 0,
        "diet_type": "Vegetarian",
        "bus_km": 0
    }
    
    result = calculator.calculate_emissions(inputs)
    assert result["Diet"] == 365 * 1.0