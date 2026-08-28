import feedparser
import requests
import os
import json
import html

FEED_URL = "https://dynamicbytes.blog/feed.xml"
DISCORD_WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHANNEL_ID = os.environ["TELEGRAM_CHANNEL_ID"]
BREVO_API_KEY = os.environ["BREVO_API_KEY"]
CACHE_FILE = "scripts/last_post.json"

# "Your first list" in Brevo (Contacts -> Lists). Update this if you ever
# rename/replace the list new subscribers land in after confirming.
BREVO_LIST_ID = 2

BREVO_SENDER_NAME = "DynamicBytes"
BREVO_SENDER_EMAIL = "dynamicbytes.noreply@dynamicbytes.blog"


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


def build_campaign_html(post):
    title = html.escape(post.title)
    excerpt = html.escape(getattr(post, "summary", "") or "")
    link = post.link

    excerpt_block = ""
    if excerpt:
        excerpt_block = f"""
        <tr>
          <td align="left" style="padding:0 20px;text-align:left;font-size:16px;color:#676a6c;line-height:24px;font-family:Arial, Helvetica, sans-serif;" valign="middle" width="100%">
            {excerpt}
          </td>
        </tr>
        <tr><td height="24" width="100%"></td></tr>
        """

    return f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>DynamicBytes</title>
</head>
<body style="margin:0; padding:0;">
<table width="100%" cellspacing="0" cellpadding="0" border="0" align="center" bgcolor="#ffffff" style="background:#ffffff;">
  <tbody>
  <tr>
    <td>
      <table align="center" width="570" border="0" cellpadding="0" cellspacing="0" style="padding:0 5px;">
        <tbody>
        <tr><td height="30" width="100%"></td></tr>

        <tr>
          <td align="center" style="padding:0 20px;text-align:center;font-size:20px;color:#676a6c;line-height:30px;font-weight:600;font-family:Arial, Helvetica, sans-serif;" valign="middle" width="100%">
            New post on DynamicBytes
          </td>
        </tr>
        <tr><td height="24" width="100%"></td></tr>

        <tr>
          <td align="left" style="padding:0 20px;text-align:left;font-size:18px;color:#3C4858;line-height:26px;font-weight:600;font-family:Arial, Helvetica, sans-serif;" valign="middle" width="100%">
            {title}
          </td>
        </tr>
        <tr><td height="16" width="100%"></td></tr>
        {excerpt_block}
        <tr>
          <td align="center" style="padding:0 20px;text-align:center;" valign="middle" width="100%">
            <table cellspacing="0" cellpadding="0" border="0" align="center">
              <tbody>
              <tr>
                <td style="background:#4ca4e0;border-radius:5px;padding:0 30px;font-weight:600;color:#ffffff;text-transform:uppercase;" align="center" bgcolor="#4ca4e0" height="45">
                  <a href="{link}" target="_blank" style="color:#ffffff;font-size:14px;text-decoration:none;line-height:24px;width:100%;">Read the post</a>
                </td>
              </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr><td height="30" width="100%"></td></tr>

        <tr>
          <td align="left" style="padding:0 20px;text-align:left;font-size:16px;color:#676a6c;line-height:24px;font-family:Arial, Helvetica, sans-serif;" valign="middle" width="100%">
            - Ahmad
          </td>
        </tr>
        <tr><td height="40" width="100%"></td></tr>

        </tbody>
      </table>
    </td>
  </tr>
  </tbody>
</table>
</body>
</html>"""


def send_brevo_campaign(post):
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    campaign_payload = {
        "name": f"New Post - {post.title}"[:100],
        "subject": f"New post: {post.title}",
        "sender": {"name": BREVO_SENDER_NAME, "email": BREVO_SENDER_EMAIL},
        "type": "classic",
        "htmlContent": build_campaign_html(post),
        "recipients": {"listIds": [BREVO_LIST_ID]}
    }

    try:
        create_resp = requests.post(
            "https://api.brevo.com/v3/emailCampaigns",
            json=campaign_payload,
            headers=headers
        )
        create_resp.raise_for_status()
        campaign_id = create_resp.json()["id"]

        send_resp = requests.post(
            f"https://api.brevo.com/v3/emailCampaigns/{campaign_id}/sendNow",
            headers=headers
        )
        send_resp.raise_for_status()
        print(f"Brevo campaign {campaign_id} created and sent.")
    except requests.exceptions.RequestException as e:
        # Don't let a Brevo failure take down Discord/Telegram notifications
        # or block the cache update - just log it loudly so it shows in the
        # Action's run log.
        print(f"Brevo campaign failed: {e}")
        if e.response is not None:
            print(f"Brevo response: {e.response.text}")


def main():
    post = get_latest_post()
    if not post:
        return
    cache = load_cache()
    if cache.get("last_id") == post.id:
        return
    post_to_discord(post)
    post_to_telegram(post)
    send_brevo_campaign(post)
    save_cache(post)


if __name__ == "__main__":
    main()
