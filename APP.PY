import streamlit as st
from groq import Groq

# Streamlit page settings
st.set_page_config(
    page_title="Groq AI Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖AI ChatBot")
st.write("Generate a response using Llama 3.3 70B Versatile")

# Get API key from Streamlit Secrets
api_key = st.secrets["GROQ_API_KEY"]

# Initialize Groq client
client = Groq(api_key=api_key)

# User input
user_prompt = st.text_area(
    "Enter your prompt",
    "Explain the importance of fast language models in three sentences. Precise and Important Points"
)

if st.button("Generate Response"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        try:
            with st.spinner("Generating response..."):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an expert in Generative AI and "
                                "Fast Language Models. You are a helpful assistant."
                            ),
                        },
                        {
                            "role": "user",
                            "content": user_prompt,
                        },
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.7,
                    max_tokens=256,
                )

                response = chat_completion.choices[0].message.content

            st.success("Response Generated")
            st.write(response)

        except Exception as e:
            st.error(f"Error: {e}")
