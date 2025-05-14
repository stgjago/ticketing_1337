from solcx import compile_standard, install_solc
import json

install_solc("0.8.0")

with open("Ticketing.sol", "r") as file:
    source_code = file.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Ticketing.sol": {
            "content": source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "evm.bytecode"]
            }
        }
    }
}, solc_version="0.8.0")

# Simpan hasil compile
with open("compiled_ticketing.json", "w") as f:
    json.dump(compiled_sol, f)

# Simpan ABI dan Bytecode
contract_interface = compiled_sol['contracts']['Ticketing.sol']['Ticketing']
abi = contract_interface['abi']
bytecode = contract_interface['evm']['bytecode']['object']

with open("contract_info.json", "w") as f:
    json.dump({"abi": abi, "bytecode": bytecode}, f)
