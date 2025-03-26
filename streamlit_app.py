import streamlit as st
import google.genai as genai
from google.genai import types

# Show title and description.
st.title("💬 Chatbot")
st.write(
    "This is a simple chatbot that uses the Gemini 2.0 Flash Lite model to generate responses. "
    "To use this app, you need to provide a Gemini API key, which you can get [here](https://aistudio.google.com/). "
)

# Ask user for their API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
gemini_api_key = st.text_input("Gemini API Key", type="password")
if not gemini_api_key:
    st.info("Please add your Gemini API key to continue.", icon="🗝️")
else:

    # Create an Gemini client.
    client = genai.Client(api_key=gemini_api_key)

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the Gemini API.
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", contents=prompt)

        # Stream the response to the chat using `st.write_stream`, then store it in
        # session state.
        with st.chat_message("assistant"):
            st.write(response.text)
