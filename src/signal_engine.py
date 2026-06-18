def calculate_signal_score(features):
    score = 0

    # Open to work
    if features["open_to_work"]:
        score += 20

    # Recruiter response rate
    if features["response_rate"] >= 0.50:
        score += 20
    elif features["response_rate"] >= 0.25:
        score += 10

    # Notice period
    if features["notice_period"] <= 30:
        score += 15
    elif features["notice_period"] <= 60:
        score += 5

    # GitHub activity
    if features["github_score"] >= 50:
        score += 15
    elif features["github_score"] >= 20:
        score += 8

    # Relocation
    if features["willing_to_relocate"]:
        score += 10

    return score

 