def generate_reason(
        features,
        semantic_score,
        signal_score,
        reasons
):
    explanation = []

    # Semantic fit
    if semantic_score >= 0.30:
        explanation.append(
            "Strong alignment with Senior AI Engineer requirements."
        )
    elif semantic_score >= 0.15:
        explanation.append(
            "Moderate alignment with Senior AI Engineer requirements."
        )
    else:
        explanation.append(
            "Limited alignment with Senior AI Engineer requirements."
        )

    # Experience
    if features["years_experience"] >= 5:
        explanation.append(
            f"{features['years_experience']} years of experience."
        )

    # Availability
    if features["open_to_work"]:
        explanation.append(
            "Open to work."
        )

    # Recruiter response
    if features["response_rate"] >= 0.25:
        explanation.append(
            "Good recruiter response rate."
        )

    # GitHub activity
    if features["github_score"] >= 20:
        explanation.append(
            "Shows engineering activity through GitHub."
        )

    # Penalty reasons
    for reason in reasons:
        explanation.append(reason)

    return " ".join(explanation)

 