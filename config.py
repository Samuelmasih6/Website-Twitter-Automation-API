from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

    INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

settings = Settings()
