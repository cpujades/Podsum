import os
import requests
from app.core.config import config
from app.schemas.summarize import SummarizeFormat
from openai import OpenAI

DEEPGRAM_API_KEY = config.DEEPGRAM_API_KEY

SYSTEM_PROMPT = config.SYSTEM_PROMPT

OPENAI_API_KEY = config.OPENAI_API_KEY
GEMINI_API_KEY = config.GEMINI_API_KEY
ANTHROPIC_API_KEY = config.ANTHROPIC_API_KEY
GROK_API_KEY = config.GROK_API_KEY


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


def summarize_podcast(transcript: str, model: str) -> str:
    if "grok" in model:
        api_key = GROK_API_KEY
        base_url = "https://api.x.ai/v1"
    elif "gemini" in model:
        api_key = GEMINI_API_KEY
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    else:
        api_key = OPENAI_API_KEY
        base_url = "https://api.openai.com/v1"

    client = OpenAI(api_key=api_key, base_url=base_url)
    response = client.beta.chat.completions.parse(
        model=model,
        max_completion_tokens=900,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"<transcription> {transcript} </transcription>",
            },
        ],
        response_format=SummarizeFormat,
    )

    summary = response.choices[0].message.parsed.summary

    return summary
