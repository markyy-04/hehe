import streamlit as st

# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="Somewhere Along The Way 💛",
    page_icon="🌻",
    layout="centered"
)

# -----------------------------
# DESIGN
# -----------------------------

st.markdown("""
<style>

.stApp {
    background:
        linear-gradient(
            rgba(255, 253, 231, 0.88),
            rgba(255, 243, 176, 0.88)
        ),
        url("https://images.unsplash.com/photo-1597848212624-a19eb35e2651?auto=format&fit=crop&w=2000&q=80");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Center the whole app */
.block-container {
    max-width: 700px;
    margin: auto;
    padding-top: 70px;
    padding-bottom: 70px;
}

/* Letter */
.letter {
    background: #fff9d6;
    padding: 45px;
    border-radius: 25px;
    border: 2px solid #e6c84f;
    box-shadow: 0px 10px 30px rgba(92, 75, 0, 0.20);
    text-align: center;
    margin-bottom: 25px;
}

/* Letter text */
.letter p {
    color: #5c4b00 !important;
    font-size: 20px;
    line-height: 1.8;
    text-align: center;
}

/* Titles */
h1, h2, h3 {
    text-align: center;
    color: #8a6500 !important;
}

/* Normal text */
p, span {
    color: #5c4b00 !important;
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
    transition: 0.2s;
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


# -----------------------------
# PAGE SYSTEM
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = 1


def next_page():
    st.session_state.page += 1
    st.rerun()


def show_letter(text):
    st.markdown(
        f"""
        <div class="letter">
            <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# PAGE 1 - INTRODUCTION
# -----------------------------

if st.session_state.page == 1:

    st.title("💛Somewhere Along The Way💛")

    show_letter("""
    I honestly didn’t know how else to say all of this, so somehow, I ended up making an entire website.

    <br><br>

    ’Cause there are just some things that are easier to write than to say out loud. So I guess this is my way of finally saying them.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 2
# -----------------------------

elif st.session_state.page == 2:

    show_letter("""
    Heyy its been a few weeks since i first met you. Andaming nangyari haha, and I’m thankful for that. This band really did give me a lot of experiences and memories that really hit me hard. This is not my first time in a band, pero I can say na this is one of the most memorable bands in my life, and you guys helped me realize that.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 3
# -----------------------------

elif st.session_state.page == 3:

    show_letter("""
    Lalo ka na.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 4
# -----------------------------

elif st.session_state.page == 4:

    show_letter("""
    I just wanna be genuine and tell you this. U can say na siguro medjo torpe ako or what for not telling you this in person, but still. Kahit sa gantong way lang, I want you to know that I, Mark Dayrek Dimacali Dipasupil(with haha react kungwari HAHAHA).
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 5
# -----------------------------

elif st.session_state.page == 5:

    show_letter("""
    You are one in a billion.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 6
# -----------------------------

elif st.session_state.page == 6:

    show_letter("""
    In my world of black and white, you are the only one who can give it colors. And even if there's no such thing as perfect in this world, in my eyes, you are the most perfect girl I've ever seen.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 7
# -----------------------------

elif st.session_state.page == 7:

    show_letter("""
    I like you the way you are. And no flaws could ever change the feeling I have for you.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 8
# -----------------------------

elif st.session_state.page == 8:

    show_letter("""
    You're the risk I'm willing to take, even if there's a possibility that you don't feel the same way I do. But I'd still do it, just for you.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 9
# -----------------------------

elif st.session_state.page == 9:

    show_letter("""
    And just to be direct to the point, I like you.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 10
# -----------------------------

elif st.session_state.page == 10:

    show_letter("""
    Medjo corny ko man nasimulan pero I just wanted you to know that among all the people I could've met, somehow, I met you. And maybe that's what makes you so special to me.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 11
# -----------------------------

elif st.session_state.page == 11:

    show_letter("""
    Out of billions of people, you're the one I happened to find.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 12
# -----------------------------

elif st.session_state.page == 12:

    show_letter("""
    I don't know what happens after this. Maybe things will change, maybe they won't. But regardless of what happens, I'm glad I got to meet you. And if liking you means taking a risk, then I guess this is one risk I'm willing to take.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 13
# -----------------------------

elif st.session_state.page == 13:

    show_letter("""
    Because you're worth it.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 14
# -----------------------------

elif st.session_state.page == 14:

    show_letter("""
    Every single second with you feels like eternity.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 15
# -----------------------------

elif st.session_state.page == 15:

    show_letter("""
    I never want it to end.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 16
# -----------------------------

elif st.session_state.page == 16:

    show_letter("""
    So im here. And i wanna ask you a genuine question.
    """)

    if st.button("Next"):
        next_page()


# -----------------------------
# PAGE 17 - QUESTION
# -----------------------------

elif st.session_state.page == 17:

    st.title("Can i court you? 💛")

    if st.button("YES 💛"):
        st.session_state.page = 18
        st.rerun()

    if st.button("NO"):
        st.session_state.page = 19
        st.rerun()


# -----------------------------
# PAGE 18 - YES
# -----------------------------

elif st.session_state.page == 18:

    st.title("WAIT REALLY?? 😭💛")

    show_letter("""
    YESSS!!!! THANKYOUUUU!! THIS REALLY MEAN A LOT FOR ME 😭😭
    """)

    st.balloons()


# -----------------------------
# PAGE 19 - NO
# -----------------------------

elif st.session_state.page == 19:

    show_letter("""
    Oh... Okayyy! Thankyouuuu for that answer, i deeply appreciate your efforts just to answer this thingy i dont even know what to call haha. Uhmmm... Ayon thankyou and wag kalimutan streak, okayy?? B-byeee!
    """)
