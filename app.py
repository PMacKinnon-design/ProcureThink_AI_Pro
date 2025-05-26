
import streamlit as st
import openai

st.set_page_config(page_title="ProcureThink AI Pro", layout="wide")

st.title("ProcureThink AI Pro")
st.subheader("Critical Reasoning for Procurement")

st.markdown("### 🧠 Decision Assistant")

# Step 1: Freeform input
problem_description = st.text_area("Describe your procurement issue in your own words:", height=200)

# Generate prompt suggestions (placeholder logic for now)
prompt_suggestions = []
if problem_description:
    st.markdown("#### 🔍 Suggested GenAI Prompts:")
    prompt_suggestions = [
        f"What strategic options exist to resolve the following procurement issue: '{problem_description}'?",
        f"Identify risks, trade-offs, and alternatives for this problem: '{problem_description}'",
        f"How should a procurement executive approach this situation: '{problem_description}'?"
    ]
    for i, prompt in enumerate(prompt_suggestions):
        st.text_area(f"Prompt {i+1}", value=prompt, key=f"prompt_{i}")

    selected_prompt = st.radio("Select the prompt you want to use:", prompt_suggestions, key="selected_prompt")

    # Submit for recommendation
    if st.button("Generate Recommendations"):
        st.markdown("### 📝 Recommendations")
        st.info("Recommendations will be generated here based on the selected prompt. (GPT API integration to be added)")
        st.markdown("""
        **Option 1: Extend current supplier with performance clause**
        - Logic: Ensures continuity while holding supplier accountable
        - Risk: May not fix core issue; perceived as weak enforcement

        **Option 2: Launch limited-source competitive RFP**
        - Logic: Drives urgency while allowing faster vendor comparison
        - Risk: Still time-consuming, might unsettle existing supplier

        **Option 3: Split award between current and new vendor**
        - Logic: Balances risk, tests alternatives
        - Risk: Increased management complexity, possible inconsistencies
        """)

else:
    st.warning("Please describe your procurement issue to begin.")

# Spacer for future Classic Mode tab
st.markdown("---")
st.caption("Coming soon: 'Think It Through' Classic Prompting Tool")
