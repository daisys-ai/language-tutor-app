import os
import streamlit as st

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)
LANGUAGE = "Dutch"

SYSTEM_PROMPT = f"""You are a a language tutor, for the {LANGUAGE} language. 
                    The user will provide a word to you, and you must reply back with the following things, in the specified structure.
                    * For each possible parts of speech applicable for that word
                    ** The corresponding phonemization
                    ** For each meaning of the word as that particular part of speech
                    *** An example sentence in {LANGUAGE} for the meaning
                    Structure your response clearly, and do not ask follow-up questions"""

st.title("Dictionary")
st.divider()

with st.container():
    word = st.chat_input(f"Enter the word in {LANGUAGE} here..")

    if word:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": word}
            ]
        )

        st.markdown("### Result")
        st.write(response.choices[0].message.content)