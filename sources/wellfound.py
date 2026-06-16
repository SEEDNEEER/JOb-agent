import requests
from datetime import datetime, timezone

def fetch():
    try:
        jobs = []
        categories = ["marketing", "copywriting", "seo", "smm"]

        for category in categories:
            response = requests.get(
                f"https://jobicy.com/api/v2/remote-jobs?count=20&jobCategory={category}",
                timeout=10
            )
            data = response.json().get("jobs", [])
            for item in data:
                date_str = item.get("pubDate", "")
                if date_str:
                    try:
                        job_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                        age_hours = (datetime.now(timezone.utc) - job_date).total_seconds() / 3600
                        if age_hours > 48:
                            continue
                    except:
                        pass

                jobs.append({
                    "id": f"jobicy-{item.get('id')}",
                    "title": item.get("jobTitle", ""),
                    "company": item.get("companyName", ""),
                    "url": item.get("url", ""),
                    "tags": [item.get("jobIndustry", "")],
                    "job_type": item.get("jobType", "Not specified"),
                    "source": "Jobicy"
                })

        return jobs
    except Exception as e:
        print(f"❌ Jobicy error: {e}")
        return []