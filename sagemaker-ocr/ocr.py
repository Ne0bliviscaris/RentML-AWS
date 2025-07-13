import easyocr


def mileage_ocr(image):
    """Extract mileage from image using easyocr."""
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image)
    for _, text, _ in result:
        if text.isdigit():
            return {"mileage": text}
    return {"mileage": "Not found"}
