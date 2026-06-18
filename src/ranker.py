from src.load_data import load_candidates
from src.feature_engineering import extract_features
from src.semantic_matcher import (
    build_candidate_text,
    compute_similarity
)
from src.scoring_engine import (
    calculate_final_score
)
from src.reason_generator import (
    generate_reason
)


JD_TEXT = """
Senior AI Engineer.
Embeddings.
Retrieval systems.
Ranking systems.
Vector databases.
Python.
Evaluation frameworks.
Recommendation systems.
Search systems.
Product company experience.
LLM systems.
"""


def rank_candidates():

    candidates = load_candidates(
        "data/candidates.jsonl"
    )

    results = []

    for candidate in candidates:

        features = extract_features(
            candidate
        )

        candidate_text = (
            build_candidate_text(
                candidate
            )
        )

        similarity = (
            compute_similarity(
                JD_TEXT,
                candidate_text
            )
        )

        score_result = (
            calculate_final_score(
                features,
                similarity
            )
        )

        reason = generate_reason(
            features,
            similarity,
            score_result[
                "signal_score"
            ],
            score_result[
                "reasons"
            ]
        )

        results.append(
            {
                "candidate_id":
                features[
                    "candidate_id"
                ],
                "score":
                score_result[
                    "final_score"
                ],
                "reason":
                reason
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    top_100 = results[:100]

    return top_100
 