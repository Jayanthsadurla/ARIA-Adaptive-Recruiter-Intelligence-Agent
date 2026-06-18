import csv
from src.ranker import rank_candidates

results = rank_candidates()

with open(
    "team_aria.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(
        [
            "rank",
            "candidate_id",
            "score",
            "reason"
        ]
    )

    for i, row in enumerate(
            results,
            start=1):

        writer.writerow(
            [
                i,
                row["candidate_id"],
                row["score"],
                row["reason"]
            ]
        )

print("team_aria.csv created successfully.")