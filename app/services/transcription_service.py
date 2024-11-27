from app.utils.external_apis import deepgram_transcription
from app.utils.helpers import get_youtube_video, upload_to_gcp, delete_gcp_file


async def transcribe_video(youtube_link: str) -> str:
    """
    Transcribes a YouTube video using Deepgram.

    Args:
        youtube_link (str): The URL of the YouTube video to transcribe.

    Returns:
        transcript (str): The transcribed text of the video.
    """

    file_info = get_youtube_video(youtube_link)

    video_url = file_info["file_url"]
    title = file_info["title"]

    signed_url = upload_to_gcp(video_url, title)

    transcript = deepgram_transcription(signed_url)

    delete_gcp_file(title)

    return transcript
