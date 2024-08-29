# tests/test_bot.py
import pytest
from app.bot import run_bot

def test_run_bot(monkeypatch):
    # Mocking the execute_arbitrage function to avoid real blockchain interaction during testing
    def mock_execute_arbitrage(token_pairs, amounts_in, gas_price):
        return {"transactionHash": "0xmockedhash"}

    monkeypatch.setattr('app.bot.execute_arbitrage', mock_execute_arbitrage)
    
    # Run the bot function and assert no exceptions are raised
    try:
        run_bot()
    except Exception as e:
        pytest.fail(f"run_bot raised an exception: {e}")
