import base64
import json

import boto3
import requests

import streamlit as st


def call_lambda_ocr(image_bytes):
    """Call Lambda function for OCR processing"""
    lambda_client = boto3.client("lambda", region_name="us-east-1")

    payload = {"image": base64.b64encode(image_bytes).decode("utf-8")}

    response = lambda_client.invoke(FunctionName="rentml-ocr", Payload=json.dumps(payload))

    result = json.loads(response["Payload"].read())
    return json.loads(result["body"])


def call_sagemaker_detection(image_bytes):
    """Call SageMaker endpoint for car detection"""
    sagemaker_client = boto3.client("sagemaker-runtime", region_name="us-east-1")

    response = sagemaker_client.invoke_endpoint(
        EndpointName="rentml-car-detection", ContentType="application/x-image", Body=image_bytes
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
            try:
                ocr_result = call_lambda_ocr(image_bytes)
                detection_result = call_sagemaker_detection(image_bytes)

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Mileage (OCR)")
                    st.write(f"Detected: {ocr_result.get('mileage', 'Not found')}")

                with col2:
                    st.subheader("Car Type (AI)")
                    st.write(f"Type: {detection_result.get('car_type', 'Unknown')}")
                    st.write(f"Confidence: {detection_result.get('confidence', 0):.2f}")

            except Exception as e:
                st.error(f"Error: {str(e)}")
