from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_candidate_text(candidate):
    profile = candidate.get("profile", {})
    history = candidate.get("career_history", [])
    skills = candidate.get("skills", [])

    text = ""

    text += profile.get("headline", "") + " "
    text += profile.get("summary", "") + " "

    for job in history:
        text += job.get("description", "") + " "

    for skill in skills:
        text += skill.get("name", "") + " "

    return text


def compute_similarity(jd_text, candidate_text):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [jd_text, candidate_text]
    )

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    return similarity
