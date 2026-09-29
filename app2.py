import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import personalities
# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Study Assistant",
    page_icon="📚",
    layout="centered"
)


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is not found in the .env file.")
    st.stop()


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(api_key=api_key)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# HEADER
# ============================================================

st.title("📚 Study Assistant")
st.caption("Your AI-powered learning companion")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Settings")

    personality = st.selectbox(
        "Choose Assistant Style",
        list(personalities.keys())
    )

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# USER INPUT
# ============================================================

question = st.chat_input(
    "Ask your study question..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # Display user question
    with st.chat_message("user"):
        st.markdown(question)

    # Save user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Studying your question..."):

            try:

                system_prompt = personalities[personality]

                response = client.models.generate_content(

                    model="gemini-3.5-flash",

                    config=types.GenerateContentConfig(
                        temperature=0.7,
                        max_output_tokens=500,
                        system_instruction=system_prompt
                    ),

                    contents=question
                )

                answer = response.text

                st.markdown(answer)

            except Exception as e:

                answer = f"Something went wrong: {e}"

                st.error(answer)

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )