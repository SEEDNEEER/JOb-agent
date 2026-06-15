import os
import requests

BOT_TOKEN = os.environ["8998876003:AAGhh95ClkzhuerbNKlAdF4vd65cLmR6zIA"]
CHAT_ID = os.environ["909363302"]

message = """
🚀 Job Agent Running

This message was sent from GitHub Actions.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print(response.text)