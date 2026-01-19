from fastapi import APIRouter, BackgroundTasks, Depends
from app.models.website_post import WebsitePost
from app.services.twitter_formatter import format_for_twitter
from app.services.twitter_service import post_tweet
from app.core.security import verify_api_key

router = APIRouter()

@router.post("/ingest/post", dependencies=[Depends(verify_api_key)])
def ingest_post(post: WebsitePost, bg: BackgroundTasks):
    tweet_text = format_for_twitter(post)
    bg.add_task(post_tweet, tweet_text)

    return {
        "status": "accepted",
        "post_id": post.post_id
    }
