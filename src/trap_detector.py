SERVICE_COMPANIES = {
    "tcs",
    "infosys",
    "wipro",
    "accenture",
    "cognizant",
    "capgemini",
    "mindtree",
    "hcl"
}


def detect_traps(features):
    penalty = 0
    reasons = []

    company = features["current_company"].lower()

    # Service-company background
    if company in SERVICE_COMPANIES:
        penalty += 20
        reasons.append(
            "Service-company background"
        )

    # Low recruiter response
    if features["response_rate"] < 0.10:
        penalty += 20
        reasons.append(
            "Low recruiter response"
        )

    # Long notice period
    if features["notice_period"] > 60:
        penalty += 10
        reasons.append(
            "Long notice period"
        )

    return penalty, reasons