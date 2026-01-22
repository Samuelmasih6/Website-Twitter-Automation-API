def format_for_twitter(post):
    hashtags = " ".join([f"#{tag}" for tag in post.tags[:3]])

    tweet = (
        f"{post.title}\n\n"
        f"{post.body[:180]}...\n\n"
        f"{hashtags}\n"
        f"{post.url or ''}"
    )

    return tweet[:280]
