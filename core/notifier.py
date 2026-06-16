import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "909363302"

def send_jobs(jobs):
    for job in jobs:
        text = (
            f"🚨 NEW JOB ALERT\n\n"
            f"🧑‍💼 Role: {job.get('title', 'N/A')}\n"
            f"🏢 Company: {job.get('company', 'N/A')}\n"
            f"📌 Source: {job.get('source', 'N/A')}\n"
            f"🌍 Remote: Yes\n"
            f"💼 Type: {job.get('job_type', 'Not specified')}\n"
            f"🔗 Link: {job.get('url', 'N/A')}"
        )

        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": text}
        )

        if not response.json().get("ok"):
            print(f"❌ Failed to send: {job.get('title')} — {response.json()}")
        else:
            print(f"✅ Sent: {job.get('title')}")