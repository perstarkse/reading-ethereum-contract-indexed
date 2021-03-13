from eth_typing import abi
from web3 import Web3
import json

with open("abi_indexed.json") as abi_data_ndx:
    info_abi_ndx = json.load(abi_data_ndx)
    
_abi_ndx = info_abi_ndx

with open("abi_rewards.json") as abi_data_rewards:
    info_abi_rewards = json.load(abi_data_rewards)
    
_abi_rewards = info_abi_rewards

#set eth_provider_url to your liking, I used infura to great sucess.
eth_provider_url = ""
#set eth_adress to the adress you would like to call the ndx contract from. 
eth_address = ""
w3 = Web3(Web3.HTTPProvider(eth_provider_url))

ndx_contract = "0x86772b1409b61c639EaAc9Ba0AcfBb6E238e5F83"
contract_ndx = w3.eth.contract(ndx_contract, abi=_abi_ndx)
contract_ndx_symbol = contract_ndx.functions.symbol().call()

defi_5_contract_address = "0x11bf850D1B85eA02eF9F06Cf09488E443655b586"
d5_contract = w3.eth.contract(defi_5_contract_address, abi=_abi_rewards)
d5_earned = d5_contract.functions.earned(eth_address).call()
d5_earned_total = str(w3.fromWei(d5_earned, 'ether'))

def balance_of(_address):
    balance_gwei = contract_ndx.functions.balanceOf(_address).call()
    balance = w3.fromWei(balance_gwei, 'ether')
    return str(balance)

print("You have " + balance_of(eth_address) + " " + contract_ndx_symbol + " in your address, and " + d5_earned_total + " more " + contract_ndx_symbol + " to claim. ")
