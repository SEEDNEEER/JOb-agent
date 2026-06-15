import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

KEYWORDS = [
    "content", "writer", "copywriter", "copywriting",
    "content writer", "content strategist", "content manager",
    "seo", "marketing", "performance marketing", "digital marketing",
    "growth marketing", "social media", "paid media", "ppc",
    "advertising", "marketing specialist", "marketing coordinator",
    "marketing associate", "marketing intern"
]

SENT_JOBS_FILE = "sent_jobs.txt"

# ✅ Fix 1: Don't crash if file doesn't exist yet
try:
    with open(SENT_JOBS_FILE, "r") as f:
        sent_jobs = set(f.read().splitlines())
except FileNotFoundError:
    sent_jobs = set()

# ✅ Fix 3: Fetch and skip the first metadata item
response = requests.get(
    "https://remoteok.com/api",
    headers={"User-Agent": "Mozilla/5.0"}
)
response.raise_for_status()
all_items = response.json()
jobs = [j for j in all_items if isinstance(j, dict) and "id" in j and "position" in j]

print(f"Total jobs fetched: {len(jobs)}")

matches = []
for job in jobs:
    job_id = str(job.get("id", ""))
    if job_id in sent_jobs:
        continue

    title = str(job.get("position", "")).lower()
    if any(keyword in title for keyword in KEYWORDS):
        matches.append(job)

print(f"New matching jobs: {len(matches)}")

if not matches:
    print("No new jobs found.")
    exit()

top = matches[:5]

lines = ["🚨 JOB ALERTS 🚨\n"]
for job in top:
    lines.append(
        f"Role: {job.get('position')}\n"
        f"Company: {job.get('company')}\n"
        f"Link: https://remoteok.com/remote-jobs/{job.get('id')}\n"
    )

message = "\n".join(lines)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# ✅ Fix 4: Check if Telegram actually accepted the message
tg_response = requests.post(url, json={"chat_id": CHAT_ID, "text": message})
tg_data = tg_response.json()

if tg_data.get("ok"):
    print("✅ Message sent to Telegram")
    # ✅ Fix 2: Save sent job IDs so you don't get duplicates
    with open(SENT_JOBS_FILE, "a") as f:
        for job in top:
            f.write(str(job.get("id")) + "\n")
else:
    print("❌ Telegram error:", tg_data)