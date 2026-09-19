import streamlit as st

st.set_page_config(
    page_title="A Little Something 💌",
    page_icon="💗",
    layout="centered"
)

st.markdown("""
<style>

body {
    background-color: #fff5f7;
}

.stApp {
    background: linear-gradient(135deg, #fff5f7, #ffe4ec);
}

/* Main text */
p {
    font-size: 20px;
    line-height: 1.8;
    text-align: center;
}

/* Headings */
h1, h2, h3 {
    text-align: center;
    color: #d6336c;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 20px;
    border: none;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    background-color: #ff8fab;
    color: white;
}

.stButton > button:hover {
    background-color: #ff6f91;
    transform: scale(1.02);
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)
