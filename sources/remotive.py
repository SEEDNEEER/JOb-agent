import requests

def fetch():
    try:
        response = requests.get(
            "https://remotive.com/api/remote-jobs",
            timeout=10
        )
        data = response.json().get("jobs", [])
        jobs = []
        for item in data:
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