import json


def model_fn(model_dir):
    """Load model for inference."""
    return "dummy_model"


def predict_fn(input_data, model):
    """Make prediction."""
    return {"car_type": "sedan", "confidence": 0.95}
