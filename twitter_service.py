import tweepy
from app.core.config import settings

client = tweepy.Client(
    consumer_key=settings.TWITTER_API_KEY,
    consumer_secret=settings.TWITTER_API_SECRET,
    access_token=settings.TWITTER_ACCESS_TOKEN,
    access_token_secret=settings.TWITTER_ACCESS_SECRET
)

def post_tweet(text: str):
    response = client.create_tweet(text=text)
    return response.data["id"]
