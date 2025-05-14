from flask import Flask, render_template, request
from web3 import Web3
import json

app = Flask(__name__)

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

with open("contract_info.json", "r") as f:
    contract_info = json.load(f)

abi = contract_info["abi"]
address = contract_info["address"]

contract = w3.eth.contract(address=address, abi=abi)

@app.route('/')
def index():
    account = w3.eth.accounts[0]
    balance = w3.eth.get_balance(account)
    balance_eth = w3.from_wei(balance, 'ether')
    return render_template("index.html", account=account, balance=balance_eth)

@app.route('/buy', methods=['POST'])
def buy_ticket():
    name = request.form['name']
    account = w3.eth.accounts[0]  # atau request.form['account'] jika pakai input dari user

    tx_hash = contract.functions.buyTicket(name).transact({
        'from': account,
        'gas': 2000000
    })
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    ticket_id = contract.functions.ticketCount().call()
    return render_template("ticket.html", name=name, ticket_id=ticket_id, tx_hash=tx_hash.hex())

if __name__ == '__main__':
    app.run(debug=True)
