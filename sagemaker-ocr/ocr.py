import re

import easyocr


def mileage_ocr(image_bytes):
    """Extract mileage from image using easyocr."""
    ocr = easyocr.Reader(["en"])
    ocr_result = ocr.readtext(image_bytes, allowlist="0123456789")
    SIX_DIGITS = r"\b\d{6}\b"
    six_digit_numbers = re.findall(SIX_DIGITS, str(ocr_result))
    if six_digit_numbers:
        return {"mileage": six_digit_numbers[0]}
    return {"mileage": "Not found"}
