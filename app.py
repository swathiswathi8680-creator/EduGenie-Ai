import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(
    page_title="SmartLearn AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 SmartLearn AI")
st.subheader("Your Personal AI Learning Assistant")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Gemini API key is not configured.")
    st.info("API key will be added securely in Render Environment Variables.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

st.markdown("### 💬 Ask SmartLearn AI")

question = st.text_area(
    "Enter your question:",
    placeholder="Example: Explain Artificial Intelligence in simple words..."
)

if st.button("🚀 Ask AI"):
    if question.strip():
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(
                    f"""
                    You are SmartLearn AI, a friendly educational assistant.

                    Explain the following question clearly and simply.
                    Use headings, bullet points and examples when useful.
                    Make the answer easy for college students to understand.

                    Question:
                    {question}
                    """
                )

                st.markdown("### 📚 Answer")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
