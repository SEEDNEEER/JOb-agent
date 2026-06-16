import os
print("BOT_TOKEN:", os.environ.get("BOT_TOKEN", "NOT FOUND"))
print("CHAT_ID:", os.environ.get("CHAT_ID", "NOT FOUND"))
from sources import remoteok, arbeitnow, remotive, wellfound
from core.filter import is_relevant
from core.deduplicator import deduplicate
from core.tracker import load_sent_jobs, save_sent_jobs
from core.notifier import send_jobs

MAX_JOBS_PER_RUN = 10

def run():
    print("🔍 Fetching jobs from all sources...")

    all_jobs = (
        remoteok.fetch() +
        arbeitnow.fetch() +
        remotive.fetch() +
        wellfound.fetch()
    )

    print(f"📦 Total fetched: {len(all_jobs)}")

    relevant = [job for job in all_jobs if is_relevant(job)]
    print(f"✅ Relevant jobs: {len(relevant)}")

    unique = deduplicate(relevant)
    print(f"🔁 After deduplication: {len(unique)}")

    sent_jobs = load_sent_jobs()
    new_jobs = [job for job in unique if job["id"] not in sent_jobs]
    print(f"🆕 New jobs to send: {len(new_jobs)}")

    if not new_jobs:
        print("😴 No new jobs found. Done.")
        return

    top_jobs = new_jobs[:MAX_JOBS_PER_RUN]
    send_jobs(top_jobs)
    save_sent_jobs([job["id"] for job in top_jobs])
    print(f"📨 Done. Sent {len(top_jobs)} jobs.")

if __name__ == "__main__":
    run()