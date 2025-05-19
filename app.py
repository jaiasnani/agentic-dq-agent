import streamlit as st
from agents.ingest_agent import ingest_csv_from_gdrive
from agents.dq_agent import run_dq_checks
from agents.report_agent import generate_report

st.title("AutoDQ Agent: Data Quality with Agentic AI")

if st.button("Run DQ Checks on Sample Data"):
    with st.spinner("Ingesting and analyzing sample_data_file.csv..."):
        df = ingest_csv_from_gdrive()
        st.write("Sample Data:", df.head())
        issues = run_dq_checks(df)
        report = generate_report(issues)
        st.markdown("### Report")
        st.code(report)
