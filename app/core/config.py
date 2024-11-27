from dotenv import load_dotenv
import os
from supabase import create_client

# Load environment variables from .env file
load_dotenv()


class Config:
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API")
    VOYAGEAI_API_KEY = os.getenv("VOYAGEAI_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    DB_CONNECTION = os.getenv("DB_CONNECTION")

    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_SECRET")

    # Create Supabase client
    SUPABASE_CLIENT = create_client(SUPABASE_URL, SUPABASE_KEY)


config = Config()
