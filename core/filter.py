KEYWORDS = [
    "performance marketing",
    "digital marketing",
    "growth marketing",
    "paid media",
    "ppc",
    "google ads",
    "meta ads",
    "content writer",
    "content writing",
    "copywriter",
    "copywriting",
    "seo content",
    "content strategist",
    "content marketing",
    "social media marketing",
]

NEGATIVE_KEYWORDS = [
    "engineer",
    "developer",
    "software",
    "backend",
    "frontend",
    "data scientist",
    "machine learning",
    "devops",
    "product manager",
    "designer",
    "ui/ux",
    "ios",
    "android",
]

def is_relevant(job):
    title = job.get("title", "").lower()

    has_keyword = any(kw in title for kw in KEYWORDS)
    has_negative = any(neg in title for neg in NEGATIVE_KEYWORDS)

    return has_keyword and not has_negative