import os

SENT_JOBS_FILE = "data/sent_jobs.txt"

def load_sent_jobs():
    if not os.path.exists(SENT_JOBS_FILE):
        return set()
    with open(SENT_JOBS_FILE, "r") as f:
        return set(line.strip() for line in f if line.strip())

def save_sent_jobs(job_ids):
    os.makedirs(os.path.dirname(SENT_JOBS_FILE), exist_ok=True)
    with open(SENT_JOBS_FILE, "a") as f:
        for job_id in job_ids:
            f.write(job_id + "\n")