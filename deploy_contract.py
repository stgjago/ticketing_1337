from web3 import Web3
import json

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))
w3.eth.default_account = w3.eth.accounts[0]

with open("contract_info.json", "r") as f:
    contract_info = json.load(f)

abi = contract_info["abi"]
bytecode = contract_info["bytecode"]

Ticketing = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Ticketing.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Simpan alamat
contract_address = tx_receipt.contractAddress
contract_info["address"] = contract_address

with open("contract_info.json", "w") as f:
    json.dump(contract_info, f)

print(f"Contract deployed at: {contract_address}")
