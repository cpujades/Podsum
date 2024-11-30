from dotenv import load_dotenv
import os
from supabase import create_client

# Load environment variables from .env file
load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GROK_API_KEY = os.getenv("GROK_API_KEY")

    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API")

    VOYAGEAI_API_KEY = os.getenv("VOYAGEAI_API_KEY")

    # Google Cloud credentials
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_SECRET")
    # Create Supabase client
    SUPABASE_CLIENT = create_client(SUPABASE_URL, SUPABASE_KEY)

    DB_CONNECTION = os.getenv("DB_CONNECTION")

    SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")


config = Config()
