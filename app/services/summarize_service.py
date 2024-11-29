from app.utils.external_apis import summarize_podcast
from IPython.display import Markdown


async def summarize_transcription(transcript: str, model: str) -> str:
    summary = summarize_podcast(transcript, model)
    formatted_summary = Markdown(summary)

    return formatted_summary
