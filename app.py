
import streamlit as st
import openai

st.set_page_config(page_title="ProcureThink AI Pro", layout="wide")

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("ProcureThink AI Pro")
st.subheader("Critical Reasoning for Procurement")

st.markdown("### 🧠 Decision Assistant")

# Step 1: Freeform input
problem_description = st.text_area("Describe your procurement issue in your own words:", height=200)

# Generate prompt suggestions
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
        with st.spinner("Generating recommendations using GPT-4..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a senior procurement consultant writing for executives. For the user's issue, generate exactly 3 strategic procurement options. For each option, format it as:\n\n**Option X: [Title]**\n- Logic: [Short explanation of why this option is valid]\n- Trade-Offs: [What risks, challenges, or downsides should be considered]\n\nRespond in clear, concise language, suitable for executive briefing. Do not exceed 500 words."},
                        {"role": "user", "content": selected_prompt}
                    ],
                    temperature=0.4,
                    max_tokens=800
                )

                ai_output = response.choices[0].message["content"]
                st.markdown("### 📝 Recommendations")
                st.markdown(ai_output)

            except Exception as e:
                st.error(f"Error generating recommendations: {e}")

else:
    st.warning("Please describe your procurement issue to begin.")

# Footer
st.markdown("---")
st.caption("Coming soon: 'Think It Through' Classic Prompting Tool")
