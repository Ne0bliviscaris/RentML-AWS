import io

from detection_model import identify_car


def model_fn(model_dir):
    """Load model for inference."""
    return None


def input_fn(input_data, content_type):
    """Deserialize input data for inference."""
    if content_type == "application/x-image":
        return io.BytesIO(input_data)
    raise ValueError("Unsupported content type")


def predict_fn(input_data, model):
    """Make prediction."""
    car_type = identify_car(input_data)
    return {"car_type": car_type}
