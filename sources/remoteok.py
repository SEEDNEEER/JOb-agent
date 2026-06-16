import requests
from datetime import datetime, timezone

def fetch():
    try:
        response = requests.get(
            "https://remoteok.com/api",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        data = response.json()
        jobs = []
        for item in data:
            if not isinstance(item, dict) or "id" not in item:
                continue

            # Filter jobs older than 48 hours
            date_str = item.get("date", "")
            if date_str:
                job_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                age_hours = (datetime.now(timezone.utc) - job_date).total_seconds() / 3600
                if age_hours > 48:
                    continue

            jobs.append({
                "id": f"remoteok-{item.get('id')}",
                "title": item.get("position", ""),
                "company": item.get("company", ""),
                "url": f"https://remoteok.com/remote-jobs/{item.get('id')}",
                "tags": item.get("tags", []),
                "job_type": "Not specified",
                "source": "RemoteOK"
            })
        return jobs
    except Exception as e:
        print(f"❌ RemoteOK error: {e}")
        return []