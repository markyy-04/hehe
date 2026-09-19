import streamlit as st

st.set_page_config(
    page_title="A Little Something 💛",
    page_icon="🌻",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background:
        linear-gradient(rgba(255, 253, 231, 0.90), rgba(255, 243, 176, 0.90)),
        url("https://images.unsplash.com/photo-1597848212624-a19eb35e2651?auto=format&fit=crop&w=2000&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Main text */
p, span {
    color: #5c4b00 !important;
}

p {
    font-size: 20px;
    line-height: 1.8;
    text-align: center;
}

/* Titles */
h1, h2, h3 {
    text-align: center;
    color: #8a6500 !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 20px;
    border: 2px solid #d4a017;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    background-color: #ffd84d;
    color: #5c4b00 !important;
}

.stButton > button:hover {
    background-color: #f5c400;
    color: #3d3200 !important;
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


st.title("💛 A Little Something 💛")

st.write("I have something I want to tell you...")

if st.button("Next"):
    st.write("It works! 😭💛")
