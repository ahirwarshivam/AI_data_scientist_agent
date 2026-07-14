import streamlit as st

from agents.cleaning_agent import CleaningAgent

st.title("Cleaning Agent")

if "dataset" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

dataframe = st.session_state["dataset"]

agent = CleaningAgent()

missing_report = agent.analyze_missing_values(dataframe)

st.subheader("Missing Value Analysis")

if missing_report.empty:
    st.success("No missing values found.")
else:
    st.dataframe(
        missing_report,
        use_container_width=True
    )