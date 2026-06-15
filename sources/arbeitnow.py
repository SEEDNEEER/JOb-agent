import requests

def fetch():
    try:
        response = requests.get(
            "https://www.arbeitnow.com/api/job-board-api",
            timeout=10
        )
        data = response.json().get("data", [])
        jobs = []
        for item in data:
            if not item.get("remote", False):
                continue
            jobs.append({
                "id": f"arbeitnow-{item.get('slug')}",
                "title": item.get("title", ""),
                "company": item.get("company_name", ""),
                "url": item.get("url", ""),
                "tags": item.get("tags", []),
                "job_type": ", ".join(item.get("job_types", [])),
                "source": "Arbeitnow"
            })
        return jobs
    except Exception as e:
        print(f"❌ Arbeitnow error: {e}")
        return []