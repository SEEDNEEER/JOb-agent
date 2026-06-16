KEYWORDS = [
    "performance marketing",
    "digital marketing",
    "growth marketing",
    "growth hacker",
    "paid media",
    "ppc",
    "google ads",
    "meta ads",
    "facebook ads",
    "content writer",
    "content writing",
    "copywriter",
    "copywriting",
    "seo content",
    "content strategist",
    "content marketing",
    "social media marketing",
    "Lead generation",
    "email marketing",
    "affiliate marketing",
    "brand strategist",
    "marketing manager",
    "marketing specialist",
    "marketing coordinator",
    "marketing intern",
    "inbound marketing",
    "demand generation",
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
    "data analyst",
    "accountant",
    "finance",
    "lawyer",
    "legal",
    "nurse",
    "doctor",
]

def is_relevant(job):
    title = job.get("title", "").lower()

    has_keyword = any(kw in title for kw in KEYWORDS)
    has_negative = any(neg in title for neg in NEGATIVE_KEYWORDS)

    return has_keyword and not has_negative