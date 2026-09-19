import streamlit as st

st.set_page_config(
    page_title="A Little Something 💛",
    page_icon="💛",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fffde7, #fff3b0);
}

/* Title */
h1 {
    text-align: center;
    color: #d4a017;
}

/* Text */
p {
    font-size: 20px;
    line-height: 1.8;
    text-align: center;
    color: #5c4b00;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 20px;
    border: 2px solid #f0c419;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    background-color: #ffd84d;
    color: #5c4b00;
}

.stButton > button:hover {
    background-color: #f5c400;
    color: white;
    transform: scale(1.02);
}

/* Hide Streamlit stuff */
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
    
