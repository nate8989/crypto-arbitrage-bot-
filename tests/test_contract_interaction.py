# tests/test_contract_interaction.py
import pytest
from app.contract_interaction import execute_arbitrage

def test_execute_arbitrage(monkeypatch):
    # Mock the web3 components to prevent real blockchain calls
    def mock_buildTransaction(params):
        return {"nonce": 1, "gas": 2000000, "gasPrice": 20, "from": params['from']}

    def mock_signTransaction(tx, private_key):
        return {"rawTransaction": "0xmockedrawtransaction"}

    def mock_sendRawTransaction(raw_tx):
        return "0xmockedtxhash"

    def mock_waitForTransactionReceipt(tx_hash):
        return {"transactionHash": tx_hash}

    monkeypatch.setattr('app.contract_interaction.contract.functions.checkAndExecuteArbitrage.buildTransaction', mock_buildTransaction)
    monkeypatch.setattr('app.contract_interaction.w3.eth.account.signTransaction', mock_signTransaction)
    monkeypatch.setattr('app.contract_interaction.w3.eth.sendRawTransaction', mock_sendRawTransaction)
    monkeypatch.setattr('app.contract_interaction.w3.eth.waitForTransactionReceipt', mock_waitForTransactionReceipt)

    # Call the function and verify the mocked transaction hash is returned
    token_pairs = ["0xTokenA", "0xTokenB"]
    amounts_in = [1000]
    gas_price = 20
    receipt = execute_arbitrage(token_pairs, amounts_in, gas_price)
    assert receipt['transactionHash'] == "0xmockedtxhash"
