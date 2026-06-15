def deduplicate(jobs):
    seen = set()
    unique = []
    for job in jobs:
        key = (job.get("title", "").lower().strip(), job.get("company", "").lower().strip())
        if key not in seen:
            seen.add(key)
            unique.append(job)
    return unique