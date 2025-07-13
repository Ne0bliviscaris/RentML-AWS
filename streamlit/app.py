import io
import json

import boto3

import streamlit as st


def show_ocr_result(ocr_result=None):
    """Display OCR result."""
    if ocr_result:
        st.subheader("Mileage (OCR)")
        st.write(f"Detected: {ocr_result.get('mileage', 'Not found')}")
    else:
        st.subheader("Mileage (OCR)")
        st.write("No OCR result available.")


def show_detection_result(detection_result):
    """Display car detection result."""
    if detection_result:
        st.subheader("Car Type (AI)")
        st.write(f"Type: {detection_result.get('car_type', 'Unknown')}")
    else:
        st.subheader("Car Type (AI)")
        st.write("No detection result available.")


def call_sagemaker_detection(image_bytes):
    """Call SageMaker endpoint for car detection"""
    sagemaker_client = boto3.client("sagemaker-runtime", region_name="us-east-1")

    response = sagemaker_client.invoke_endpoint(
        EndpointName="rentml-car-detection", ContentType="application/x-image", Body=image_bytes
    )

    result = json.loads(response["Body"].read())
    return result


def call_sagemaker_ocr(image_bytes):
    """Call SageMaker endpoint for OCR"""
    sagemaker_client = boto3.client("sagemaker-runtime", region_name="us-east-1")

    response = sagemaker_client.invoke_endpoint(
        EndpointName="rentml-ocr", ContentType="application/x-image", Body=image_bytes
    )

    result = json.loads(response["Body"].read())
    return result


st.title("RentML - Car Rental Image Analysis")

uploaded_file = st.file_uploader("Upload car image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")

    if st.button("Analyze Image"):
        image_bytes = uploaded_file.read()

        with st.spinner("Processing..."):
            # ocr_result = call_sagemaker_ocr(image_bytes)
            detection_result = call_sagemaker_detection(image_bytes)

            st.header("Results")
            col1, col2 = st.columns(2)
            with col1:
                # show_ocr_result(ocr_result)
                st.write("OCR result is currently disabled - issues with dependencies.")
            with col2:
                show_detection_result(detection_result)
