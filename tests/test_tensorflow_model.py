# tests/test_tensorflow_model.py
import pytest
from app.tensorflow_model import load_model, make_prediction

def test_load_model(monkeypatch):
    # Mock the load_model function
    def mock_load_model():
        class MockModel:
            def predict(self, data):
                return [0.9]  # Mock prediction value
        return MockModel()

    monkeypatch.setattr('app.tensorflow_model.load_model', mock_load_model)

    # Test if the model loads without errors
    model = load_model()
    assert model is not None

def test_make_prediction(monkeypatch):
    # Mock the model's predict method
    def mock_predict(data):
        return [0.95]  # Mock prediction

    def mock_load_model():
        class MockModel:
            predict = mock_predict
        return MockModel()

    monkeypatch.setattr('app.tensorflow_model.load_model', mock_load_model)

    # Test the make_prediction function
    token_pairs = ["0xTokenA", "0xTokenB"]
    amounts_in = [1000]
    prediction = make_prediction(token_pairs, amounts_in)
    assert prediction == [0.95]
