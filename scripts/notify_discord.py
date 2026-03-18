import feedparser
import requests
import os
import json

FEED_URL = "https://dynamicbytes.blog/feed.xml"
DISCORD_WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHANNEL_ID = os.environ["TELEGRAM_CHANNEL_ID"]
CACHE_FILE = "scripts/last_post.json"

def get_latest_post():
    feed = feedparser.parse(FEED_URL)
    return feed.entries[0] if feed.entries else None

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(post):
    with open(CACHE_FILE, "w") as f:
        json.dump({"last_id": post.id}, f)

def post_to_discord(post):
    message = {
        "content": f"📝 **New post on DynamicBytes!**\n\n**{post.title}**\n{post.link}"
    }
    requests.post(DISCORD_WEBHOOK_URL, json=message)

def post_to_telegram(post):
    message = f"📝 *New post on DynamicBytes!*\n\n*{post.title}*\n{post.link}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def main():
    post = get_latest_post()
    if not post:
        return
    cache = load_cache()
    if cache.get("last_id") == post.id:
        return
    post_to_discord(post)
    post_to_telegram(post)
    save_cache(post)

if __name__ == "__main__":
    main()
