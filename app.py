
import streamlit as st

st.set_page_config(page_title="ProcureThink AI Pro: Critical Reasoning for Procurement", layout="wide")

st.title("ProcureThink AI Pro")
st.subheader("Critical Reasoning for Procurement")

tab1, tab2, tab3 = st.tabs(["Root Cause Analysis", "Trade-Off Analyzer", "Logic Chain Builder"])

with tab1:
    st.header("Root Cause Analysis (5 Whys)")
    problem = st.text_input("Describe the problem")
    whys = [st.text_input(f"Why {i+1}?", key=f"why_{i}") for i in range(5)]
    if st.button("Show Root Cause"):
        st.success(f"Root Cause: {whys[-1] if whys[-1] else 'Incomplete analysis'}")

with tab2:
    st.header("Trade-Off Analyzer")
    st.write("Enter options and evaluate key trade-offs.")
    options = [st.text_input(f"Option {i+1}", key=f"option_{i}") for i in range(3)]
    criteria = [st.text_input(f"Criteria {i+1}", key=f"criteria_{i}") for i in range(3)]
    st.write("Scoring not implemented yet – placeholder interface.")

with tab3:
    st.header("Logic Chain Builder")
    premise = st.text_area("Premise")
    evidence = st.text_area("Supporting Evidence")
    conclusion = st.text_area("Conclusion")
    if st.button("Build Logic Chain"):
        st.markdown(f"**IF** {premise} **AND** {evidence} **THEN** {conclusion}")
