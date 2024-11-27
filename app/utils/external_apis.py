# app/utils/external_apis.py
import os
import requests
from app.core.config import config

DEEPGRAM_API_KEY = config.DEEPGRAM_API_KEY


def deepgram_transcription(file_url: str) -> str:
    # Define the URL for the Deepgram API endpoint
    deepgram_endpoint = "https://api.deepgram.com/v1/listen"

    # Define the headers for the HTTP request
    deepgram_headers = {
        "Accept": "application/json",
        "Authorization": "Token " + DEEPGRAM_API_KEY,
        "Content-Type": "application/json",
    }
    # Define the data for the HTTP request
    data = {"url": file_url}

    query_params = {
        "detect_language": "true",
        "model": "nova-2",
        "smart_format": "true",
    }

    # Make the HTTP request
    response = requests.post(
        deepgram_endpoint, headers=deepgram_headers, params=query_params, json=data
    )
    json = response.json()
    transcript = json["results"]["channels"][0]["alternatives"][0]["transcript"]
    return transcript
