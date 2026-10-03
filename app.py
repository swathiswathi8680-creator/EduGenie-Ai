import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(
    page_title="SmartLearn AI",
    page_icon="🎓",
    layout="wide"
)

# Login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.title("🎓 SmartLearn AI")
    st.subheader("🔐 Login")

    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login 🚀"):

        if username.strip() and password.strip():

            st.session_state.logged_in = True
            st.session_state.username = username

            st.rerun()

        else:
            st.error("Please enter Username and Password")

    st.stop()


# ---------------- WELCOME PAGE ----------------

st.title("🎓 Welcome to SmartLearn AI")

st.success(
    f"👋 Welcome, {st.session_state.username}!"
)

st.write("Your Personal AI Learning Assistant")

if st.sidebar.button("Logout 🔒"):
    st.session_state.logged_in = False
    st.rerun()


# ---------------- GEMINI AI ----------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Gemini API key is not configured.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


# ---------------- ASK AI ----------------

st.subheader("💬 Ask SmartLearn AI")

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
                    You are SmartLearn AI,
                    a friendly educational assistant.

                    Explain this question clearly
                    and simply for students.

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
