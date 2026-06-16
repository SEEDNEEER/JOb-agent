import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "909363302"

def send_jobs(jobs):
    for job in jobs:
        text = (
            f"🚨 *NEW JOB ALERT*\n\n"
            f"🧑‍💼 *Role:* {job.get('title', 'N/A')}\n"
            f"🏢 *Company:* {job.get('company', 'N/A')}\n"
            f"📌 *Source:* {job.get('source', 'N/A')}\n"
            f"💼 *Type:* {job.get('job_type', 'Not specified')}\n"
            f"🌍 *Remote:* Yes\n\n"
            f"🔗 [Apply Here]({job.get('url', '#')})"
        )

        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "Markdown",
                "disable_web_page_preview": False
            }
        )

        if not response.json().get("ok"):
            print(f"❌ Failed to send: {job.get('title')} — {response.json()}")
        else:
            print(f"✅ Sent: {job.get('title')}")

def send_error(source, error):
    text = f"⚠️ *Job Agent Error*\n\nSource: {source}\nError: {error}"
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    )