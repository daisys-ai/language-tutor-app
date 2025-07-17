import os
import streamlit as st

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)
LANGUAGE = "Dutch"
USER_LANGUAGE = "English"

SYSTEM_PROMPT = f"""You are a language tutor, for the {LANGUAGE} language. 
                    I want to practice speaking in the {LANGUAGE} language.
                    I will provide you with a scenario, and assign you a role.
                    You must then act in that assigned role, and have a turn by turn conversation with me.
                    You are not permitted to have this conversation in any language other than {LANGUAGE}.
                    You must not provide me the scenario yourself.
                    You must not generate the entire conversation. Instead, you must say something to me, then wait for me to respond.
                    If there is an action that I need to perform, I will enclose it inside <ACTION> </ACTION> tags. You must do the same as well.
                    For example, if I need to present my card to the machine, I will say <ACTION>present card to machine</ACTION>.
                    If I want to end the conversation at any time, then I will enter the tag <END>. 
                    You must not respond after the <END> tag"""

st.title("Practice conversations")
st.divider()

# Init the chat
if "messages" not in st.session_state:
    st.session_state.messages = []
if "response" not in st.session_state:
    response = client.chat.completions.create(
                                        model= "gpt-4o",
                                        messages=[
                                            {"role": "assistant", "content": SYSTEM_PROMPT}
                                        ]
                                    )
    st.session_state["response"] = response.choices[0].message.content
    messages = st.session_state.messages
    messages.append({"role": "assistant", "content": st.session_state["response"]})
    del messages

placeholder = "Enter the scenario you want to practice."

# Scrollable container for chat messages
messages = st.session_state.messages
with st.container():
    for msg in messages:
        st.chat_message(msg["role"]).write(msg["content"])
 
# Walrus operator. Assigns input if not none
if prompt := st.chat_input(placeholder=placeholder):
    messages.append({"role": "user", "content": prompt})
    # st.chat_message("user").write(prompt)

    placeholder = ""

    response = client.chat.completions.create(model="gpt-4o", messages=messages)
    st.session_state["response"] = response.choices[0].message.content
    # with st.chat_message("assistant"):
    #     messages.append({"role": "assistant", "content": st.session_state["response"]})
    #     st.write(st.session_state["response"])

    messages.append({"role": "assistant", "content": st.session_state["response"]})
    st.rerun()
