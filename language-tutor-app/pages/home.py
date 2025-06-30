import streamlit as st

# st.title("Language Tutor App")
# st.divider()

with st.container():
    st.markdown("""
    # Language Tutor App
    This app is designed to have multiple subtools that allow the you to navigate and learn new language more efficiently
    - Tools
        - **Dictionary** : Look up words and the various meanings that they can have.
        - **Translate** : Translate unfamiliar text to the language you understand.
    - Practice
        - **Conversation** : Give the AI a scenario, set the difficulty, and then practice having a (written or spoken) conversation. After the conversation is done, 
                        you will then get a report of your conversation, with suggestions for improvement.
        - **Listening** : This section is for improving your listening and understanding skills. Listen to the audio and try to transcribe it as accurately
                        as possible.
    - **Analytics** : Learning without measuring progress can be frustrating. Check out how many words you've not needed to translate in a while.
                        Or the ones that need that extra bit of attention.

    We hope that this tool makes your journey easier and more enjoyable!!.            
    """)