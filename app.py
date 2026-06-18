import streamlit as st
import pandas as pd
from src.ranker import rank_candidates

st.set_page_config(
    page_title="ARIA",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 ARIA")
st.subheader(
    "Adaptive Recruiter Intelligence Agent"
)

st.write(
    "AI-powered candidate discovery and ranking system."
)

if st.button("Rank Candidates"):

    with st.spinner(
        "Ranking candidates..."
    ):
        results = rank_candidates()

    df = pd.DataFrame(results)

    st.success(
        f"Found {len(df)} candidates."
    )

    st.dataframe(df)

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download Results",
        csv,
        "team_aria.csv",
        "text/csv"
    )
