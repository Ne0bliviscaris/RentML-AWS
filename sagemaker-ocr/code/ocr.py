import io
import re

import easyocr
import numpy as np
from PIL import Image


def mileage_ocr(image_bytes):
    """Extract mileage from image using easyocr."""
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image_np = np.array(image)
    reader = easyocr.Reader(["en"])
    ocr_result = reader.readtext(image_np, allowlist="0123456789")
    SIX_DIGITS = r"\b\d{6}\b"
    six_digit_numbers = re.findall(SIX_DIGITS, str(ocr_result))
    if six_digit_numbers:
        return {"mileage": six_digit_numbers[0]}
    return {"mileage": "Not found"}
