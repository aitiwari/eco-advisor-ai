 
class ImpactSimulator:
    def __init__(self, calculator):
        self.calculator = calculator
        self.financial_rates = {
            'electricity': 0.12,  # $ per kWh
            'gas': 0.8,           # $ per m³
            'transport': 0.15      # $ per km
        }
    
    def simulate_scenario(self, current_data, changes):
        simulated = current_data.copy()
        results = {}
        
        # Apply changes
        for category, value in changes.items():
            simulated[category] = value
            
        # Calculate new emissions
        new_emissions = self.calculator.calculate_emissions(simulated)
        
        # Calculate financial savings
        financial = self._calculate_savings(current_data, changes)
        
        # Ecosystem impact (simplified)
        co2_reduction = current_data['Total'] - new_emissions['Total']
        ecosystem = {
            'trees_equivalent': co2_reduction / 21.77,  # kg CO2 per tree/year
            'ice_saved': co2_reduction * 3.2e-8         # km³ ice per kg CO2
        }
        
        return {
            'emissions': new_emissions,
            'financial': financial,
            'ecosystem': ecosystem
        }
    
    def _calculate_savings(self, original, changes):
        savings = {}
        for category, new_value in changes.items():
            if category in self.financial_rates:
                original_value = original[category]
                rate = self.financial_rates[category]
                savings[category] = (original_value - new_value) * rate
        return savings