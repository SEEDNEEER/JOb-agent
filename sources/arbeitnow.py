import requests
from datetime import datetime, timezone

def fetch():
    try:
        jobs = []
        keywords = ["marketing", "content", "copywriter", "seo", "ppc"]
        
        for keyword in keywords:
            response = requests.get(
                f"https://himalayas.app/jobs/api/search?q={keyword}&sort=recent&limit=20",
                timeout=10
            )
            data = response.json().get("jobs", [])
            for item in data:
                date_str = item.get("createdAt", "")
                if date_str:
                    try:
                        job_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                        age_hours = (datetime.now(timezone.utc) - job_date).total_seconds() / 3600
                        if age_hours > 48:
                            continue
                    except:
                        pass

                jobs.append({
                    "id": f"himalayas-{item.get('slug')}",
                    "title": item.get("title", ""),
                    "company": item.get("companyName", ""),
                    "url": item.get("applicationLink", ""),
                    "tags": item.get("categories", []),
                    "job_type": item.get("employmentType", "Not specified"),
                    "source": "Himalayas"
                })

        return jobs
    except Exception as e:
        print(f"❌ Himalayas error: {e}")
        return []