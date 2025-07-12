import base64
import json

from modules.ocr import mileage_ocr


def lambda_handler(event, context):
    """Handle OCR processing for mileage extraction."""
    image_b64 = event.get("image")
    if not image_b64:
        return {"statusCode": 400, "body": json.dumps({"error": "No image provided"})}
    image_bytes = base64.b64decode(image_b64)
    mileage = mileage_ocr(image_bytes)
    return {"statusCode": 200, "body": json.dumps({"mileage": mileage})}
