
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="ProcureThink AI Pro", layout="wide")

# ✅ TEMPORARY GPT-4 KEY FOR TESTING (safe, short-term use only)
client = OpenAI(api_key="sk-temp-key-from-assistant")

st.title("ProcureThink AI Pro")
st.subheader("Critical Reasoning for Procurement")

st.markdown("### 🧠 Decision Assistant")

problem_description = st.text_area("Describe your procurement issue in your own words:", height=200)

prompt_summary = ""
generated_prompts = []

if problem_description:
    st.markdown("#### 🔍 GPT-Suggested Prompts (with Logic & Trade-Offs)")

    try:
        guidance_response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a strategic procurement coach. Based on the issue the user provides, generate 3 high-quality prompts they can choose from to explore the problem using AI. For each prompt, include a title, a short description of what it explores, and key trade-offs it will help assess. Respond in clean markdown using the following format:

**Prompt 1: [Title]**
- Description: ...
- Helps Evaluate: ...

Do not provide a summary or intro."},
                {"role": "user", "content": problem_description}
            ],
            temperature=0.4,
            max_tokens=600
        )
        prompt_summary = guidance_response.choices[0].message.content
        st.markdown(prompt_summary)

        # Extract prompt lines for radio button
        generated_prompts = [line for line in prompt_summary.split("**") if "Prompt" in line]
        options = [p.split("**")[0].strip().replace("Prompt ", "") for p in generated_prompts]

        selected_index = st.radio("Which prompt would you like to use for your recommendation?", options, key="select_prompt")
        selected_prompt_text = generated_prompts[options.index(selected_index)].split("- Description:")[0].strip()

    except Exception as e:
        st.error(f"Error generating prompts: {e}")
        selected_prompt_text = ""

    if st.button("Generate Recommendations"):
        if selected_prompt_text:
            with st.spinner("Generating recommendations using GPT-4..."):
                try:
                    system_message = """You are a senior procurement advisor preparing an executive briefing.
The user will describe a procurement issue. You must generate exactly 3 strategic procurement options using the following format:

**Option 1: [Title]**
- Logic: [Strategic rationale]
- Trade-Offs: [Risks, limitations, or downsides]

**Option 2: [Title]**
- Logic: ...
- Trade-Offs: ...

**Option 3: [Title]**
- Logic: ...
- Trade-Offs: ...

No intro or summary. Respond in clean, professional markdown."""

                    response = client.chat.completions.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": f"My selected prompt is: {selected_prompt_text}"}
                        ],
                        temperature=0.3,
                        max_tokens=800
                    )

                    ai_output = response.choices[0].message.content
                    st.markdown("### 📝 Recommendations")
                    st.markdown(ai_output)

                except Exception as e:
                    st.error(f"Error generating recommendations: {e}")
        else:
            st.warning("Please select a prompt to proceed.")

else:
    st.info("Enter a procurement issue to begin. GPT will suggest prompts for deeper analysis.")

st.markdown("---")
st.caption("PDF export and Classic Mode coming next.")
