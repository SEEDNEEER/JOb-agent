import requests

BOT_TOKEN = "8998876003:AAGhh95ClkzhuerbNKlAdF4vd65cLmR6zIA"
CHAT_ID = "909363302"

message = """
🚨 TEST JOB FOUND

Role: Content Writer

Company: OpenAI

Location: Remote

Apply:
https://example.com
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Status Code:", response.status_code)
print("Response:", response.text)