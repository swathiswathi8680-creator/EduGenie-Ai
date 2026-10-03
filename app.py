import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(
    page_title="SmartLearn AI",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# ADMIN LOGIN DETAILS
# -----------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
ADMIN_NAME = "Swathi"

# -----------------------------
# LOGIN PAGE
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🎓 SmartLearn AI")
    st.subheader("🔐 Login to Continue")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login 🚀"):

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("❌ Invalid username or password")

    st.stop()


# -----------------------------
# WELCOME PAGE
# -----------------------------
st.title("🎓 Welcome to SmartLearn AI")

st.success(f"👋 Welcome, {ADMIN_NAME}!")

st.markdown(
    """
    ### 📚 Your Personal AI Learning Assistant

    Ask questions, learn concepts and get simple explanations
    with the power of AI.
    """
)

st.divider()


# -----------------------------
# LOGOUT
# -----------------------------
if st.sidebar.button("Logout 🔒"):
    st.session_state.logged_in = False
    st.rerun()


# -----------------------------
# GEMINI AI
# -----------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Gemini API key is not configured.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


# -----------------------------
# AI QUESTION
# -----------------------------
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
