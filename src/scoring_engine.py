from src.signal_engine import calculate_signal_score
from src.trap_detector import detect_traps


def calculate_final_score(
        features,
        semantic_score
):
    signal_score = (
        calculate_signal_score(
            features
        )
    )

    penalty, reasons = (
        detect_traps(
            features
        )
    )

    semantic_points = (
        semantic_score * 100
    )

    final_score = (
        semantic_points
        + signal_score
        - penalty
    )

    return {
        "final_score": round(
            final_score, 2
        ),
        "signal_score":
        signal_score,
        "penalty":
        penalty,
        "reasons":
        reasons
    }

 
 
    