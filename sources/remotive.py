import requests
from datetime import datetime, timezone

CATEGORIES = [
    "Marketing",
    "Copywriting",
    "Sales"
]

def fetch():
    try:
        jobs = []
        for category in CATEGORIES:
            response = requests.get(
                f"https://remotive.com/api/remote-jobs?category={category}",
                timeout=10
            )
            data = response.json().get("jobs", [])
            for item in data:
                date_str = item.get("publication_date", "")
                if date_str:
                    try:
                        job_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
                        job_date = job_date.replace(tzinfo=timezone.utc)
                        age_hours = (datetime.now(timezone.utc) - job_date).total_seconds() / 3600
                        if age_hours > 48:
                            continue
                    except:
                        pass

                jobs.append({
                    "id": f"remotive-{item.get('id')}",
                    "title": item.get("title", ""),
                    "company": item.get("company_name", ""),
                    "url": item.get("url", ""),
                    "tags": item.get("tags", []),
                    "job_type": item.get("job_type", "Not specified"),
                    "source": "Remotive"
                })
        return jobs
    except Exception as e:
        print(f"❌ Remotive error: {e}")
        return []