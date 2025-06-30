import streamlit as st

# Init all pages
home_page = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)
dictionary_page = st.Page("pages/tools/dictionary.py", title="Dictionary", icon=":material/dictionary:")
translate_page = st.Page("pages/tools/translate.py", title="Translate", icon=":material/convert_to_text:")
conversation_page = st.Page("pages/practice/conversation.py", title="Conversation", icon=":material/dictionary:")
listening_page = st.Page("pages/practice/listening.py", title="Listening", icon=":material/interpreter_mode:")
analytics_page = st.Page("pages/analytics.py", title="Analytics", icon=":material/analytics:")
pages = {
    'Home': [home_page],
    'Tools': [dictionary_page, translate_page],
    'Practice': [conversation_page, listening_page],
    'Analytics': [analytics_page]
}

pg = st.navigation(pages)
st.set_page_config(page_title="Language Tutor App", page_icon=":material/school:")
pg.run()
