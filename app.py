import streamlit as st

st.set_page_config(
    page_title="A Little Something 💌",
    page_icon="💗"
)

st.title("💌 A Little Something 💌")
st.write("If you can see this, the app is working!")

if st.button("Next"):
    st.write("It works! 😭💗")
