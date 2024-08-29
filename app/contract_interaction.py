from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("PROVIDER_URL")))
contract_address = os.getenv("CONTRACT_ADDRESS")
contract_abi = [...]  # Your contract ABI

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def execute_arbitrage(token_pairs, amounts_in, gas_price):
    txn = contract.functions.checkAndExecuteArbitrage(token_pairs, amounts_in, gas_price).buildTransaction({
        'from': w3.eth.default_account,
        'nonce': w3.eth.getTransactionCount(w3.eth.default_account),
        'gas': 2000000,
        'gasPrice': w3.toWei(gas_price, 'gwei')
    })
    signed_txn = w3.eth.account.signTransaction(txn, private_key=os.getenv("PRIVATE_KEY"))
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return w3.eth.waitForTransactionReceipt(tx_hash)
