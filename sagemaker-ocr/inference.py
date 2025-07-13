import io

from ocr import mileage_ocr


def model_fn(model_dir):
    """Load OCR model (not needed for easyocr)."""
    return None


def input_fn(input_data, content_type):
    """Deserialize input data for inference."""
    if content_type == "application/x-image":
        return io.BytesIO(input_data)
    raise ValueError("Unsupported content type")


def predict_fn(input_data, model):
    """Make OCR prediction."""
    return mileage_ocr(input_data)
