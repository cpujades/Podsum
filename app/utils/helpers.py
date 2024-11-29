import requests
from google.cloud import storage
from pytubefix import YouTube
import requests
from datetime import timedelta
import os
from app.core.config import config
import tiktoken


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.GOOGLE_APPLICATION_CREDENTIALS


def get_youtube_video(yotutube_url):
    """
    Downloads a YouTube video from the given URL.

    Args:
        youtube_url (str): The URL of the YouTube video to download.

    Returns:
        info (dict): A dictionary containing the title, length, and URL of the downloaded video
    """
    yt = YouTube(yotutube_url)
    url = yt.streaming_data["formats"][0]["url"]
    title = yt.title
    length = yt.length

    info = {"title": title, "length": length, "file_url": url}
    return info


def upload_to_gcp(video_url, title):
    """
    Uploads content to a Google Cloud Storage bucket.

    Args:
        video_url (str): The URL of the video to upload.

    Returns:
        str: The public URL of the uploaded content.
    """
    client = storage.Client()

    bucket = client.get_bucket("podsum_tmp_files_bucket")

    video_file = requests.get(video_url)
    blob_name = f"{title}.mp4"
    blob = bucket.blob(blob_name)
    blob.upload_from_string(video_file.content, content_type="video/mp4")
    signed_url = blob.generate_signed_url(expiration=timedelta(minutes=5))
    return signed_url


def delete_gcp_file(title):
    """
    Deletes a file from a Google Cloud Storage bucket.

    Args:
        title (str): The title of the file to delete.
    """
    client = storage.Client()

    bucket = client.get_bucket("podsum_tmp_files_bucket")

    blob_name = f"{title}.mp4"
    blob = bucket.blob(blob_name)
    blob.delete()


def count_tokens(text):
    """
    Counts the number of tokens in a given text.

    Args:
        text (str): The text to count the tokens in.

    Returns:
        int: The number of tokens in the text.
    """
    encoding = tiktoken.get_encoding("o200k_base")
    num_tokens = len(encoding.encode(text))

    return num_tokens
