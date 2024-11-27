import os
import requests
from app.core.config import config
from langchain.text_splitter import RecursiveCharacterTextSplitter


DEEPGRAM_API_KEY = config.DEEPGRAM_API_KEY

VOYAGEAI_API_KEY = config.VOYAGEAI_API_KEY

voyageai_headers = {
    "Authorization": "Bearer " + VOYAGEAI_API_KEY,
    "content-type": "application/json",
}

voyageai_endpoint = "https://api.voyageai.com/v1/embeddings"


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


def create_embeddings(text, input_type):
    voyageai_params = {
        "model": "voyage-3",
        "input_type": input_type,
    }

    if input_type == "document":
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1024, chunk_overlap=20
        )
        chunks = text_splitter.split_text(text)
        voyageai_params["input"] = chunks
    else:
        voyageai_params["input"] = text

    voyageai_response = requests.post(
        voyageai_endpoint, headers=voyageai_headers, json=voyageai_params
    )
    voyageai_json = voyageai_response.json()
    embeddings = voyageai_json["data"]

    return embeddings
