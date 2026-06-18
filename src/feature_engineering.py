def extract_features(candidate):
    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})
    history = candidate.get("career_history", [])
    skills = candidate.get("skills", [])

    features = {}

    features["candidate_id"] = candidate.get("candidate_id")

    features["years_experience"] = profile.get(
        "years_of_experience", 0
    )

    features["current_company"] = profile.get(
        "current_company", ""
    )

    features["industry"] = profile.get(
        "current_industry", ""
    )

    features["skills"] = [
        s.get("name", "")
        for s in skills
    ]

    features["open_to_work"] = signals.get(
        "open_to_work_flag", False
    )

    features["response_rate"] = signals.get(
        "recruiter_response_rate", 0
    )

    features["last_active"] = signals.get(
        "last_active_date"
    )

    features["notice_period"] = signals.get(
        "notice_period_days", 999
    )

    features["github_score"] = signals.get(
        "github_activity_score", 0
    )

    features["willing_to_relocate"] = signals.get(
        "willing_to_relocate", False
    )

    features["career_history"] = history

    return features

 