 
from web3 import Web3

class CarbonOffset:
    def __init__(self, provider_url):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract_address = "0x..."
        
    def purchase_offset(self, amount, project_id):
        # Simplified blockchain interaction
        tx_hash = self.w3.eth.send_transaction({
            'to': self.contract_address,
            'value': self.w3.to_wei(amount, 'ether')
        })
        return tx_hash.hex()
    
    def get_supported_projects(self):
        return [
            {'id': 1, 'name': 'Amazon Reforestation', 'co2_per_dollar': 2.5},
            {'id': 2, 'name': 'Solar Farm Kenya', 'co2_per_dollar': 1.8}
        ]