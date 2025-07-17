import os
import streamlit as st

from dotenv import load_dotenv
from openai import OpenAI
from streamlit import session_state as ss


def submit_1(client, prompt):
    def callback():
        response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": ss['text_area_1']}
                ]
            )
        
        ss['text_area_2'] = response.choices[0].message.content

    return callback

def submit_2(client, prompt):
    def callback():
        response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": ss['text_area_2']}
                ]
            )
        
        ss['text_area_1'] = response.choices[0].message.content
    
    return callback

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)
LANGUAGE_1 = "Dutch"
LANGUAGE_2 = "English"
SYSTEM_PROMPT_1 = f"""You are a a language tutor, for the {LANGUAGE_1} language. 
                    The user will provide some text to you, and you must respond with the translation to {LANGUAGE_2}. 
                    Do not add any extra text to the response, apart from the translation.
                    Structure your response clearly, and do not ask follow-up questions."""

SYSTEM_PROMPT_2 = f"""You are a a language tutor, for the {LANGUAGE_2} language. 
                    The user will provide some text to you, and you must respond with the translation to {LANGUAGE_1}. 
                    Do not add any extra text to the response, apart from the translation.
                    Structure your response clearly, and do not ask follow-up questions."""

ss.setdefault('text_area_1', '')
ss.setdefault('text_area_2', '')

st.title("Translate")
st.divider()

with st.container():
    text_1 = st.text_area(label=LANGUAGE_1,
                          key='text_area_1')
    button_1 = st.button(label="Translate",
                         key='button_1',
                         on_click=submit_1(client, SYSTEM_PROMPT_1),
                         use_container_width=True)
    
    text_2 = st.text_area(label=LANGUAGE_2,
                          key='text_area_2',
                          placeholder="Translation")
    button_2 = st.button(label="Translate",
                         key='button_2',
                         on_click=submit_2(client, SYSTEM_PROMPT_2),
                         use_container_width=True)