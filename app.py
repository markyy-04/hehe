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

/* Center letter */
.block-container {
    max-width: 700px;
    margin: auto;
    padding-top: 80px;
}

/* Letter card */
.letter {
    background: #fff9d6;
    padding: 45px;
    border-radius: 25px;
    box-shadow: 0px 10px 30px rgba(92, 75, 0, 0.20);
    border: 2px solid #e6c84f;
    text-align: center;
}

/* Text */
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
    transform: scale(1.02);
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)
