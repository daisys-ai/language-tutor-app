import streamlit as st

st.title("Analytics")
st.divider()

with st.container():
    st.markdown("""
    The hope is to have analytics and insights available to the user, so they can track their growth
    - Top new words that have not needed translation in a while
    - Top words that still need translation
    - Overall rate of learning new words everyday
    - Overall improvement in speed of speech that you're able to listen to
    """)