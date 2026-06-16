import requests

def fetch():
    try:
        response = requests.get(
            "https://www.themuse.com/api/public/jobs?page=1&per_page=100",
            timeout=10
        )
        data = response.json().get("results", [])
        jobs = []
        for item in data:
            locations = item.get("locations", [])
            is_remote = any("remote" in loc.get("name", "").lower() for loc in locations)
            if not is_remote:
                continue
            jobs.append({
                "id": f"themuse-{item.get('id')}",
                "title": item.get("name", ""),
                "company": item.get("company", {}).get("name", ""),
                "url": item.get("refs", {}).get("landing_page", ""),
                "tags": [],
                "job_type": "Not specified",
                "source": "The Muse"
            })
        return jobs
    except Exception as e:
        print(f"❌ The Muse error: {e}")
        return []