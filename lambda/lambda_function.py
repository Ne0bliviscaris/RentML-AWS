import json


def lambda_handler(event, context):
    """Handle OCR processing for mileage extraction."""
    return {"statusCode": 200, "body": json.dumps({"mileage": 12345, "message": "dummy lambda response"})}
