import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1
    st.rerun()


# PAGE 1
if st.session_state.page == 1:
    st.write("""
    Heyy its been a few weeks since i first met you. Andaming nangyari haha, and I’m thankful for that. This band really did give me a lot of experiences and memories that really hit me hard. This is not my first time in a band, pero I can say na this is one of the most memorable bands in my life, and you guys helped me realize that.
    """)

    if st.button("Next"):
        next_page()


# PAGE 2
elif st.session_state.page == 2:
    st.write("""
    Lalo ka na.
    """)

    if st.button("Next"):
        next_page()


# PAGE 3
elif st.session_state.page == 3:
    st.write("""
    I just wanna be genuine and tell you this. U can say na siguro medjo torpe ako or what for not telling you this in person, but still. Kahit sa gantong way lang, I want you to know that I, Mark Dayrek Dimacali Dipasupil—HAHAHAHA (with haha react kungwari HAHAHA).
    """)

    if st.button("Next"):
        next_page()


# PAGE 4
elif st.session_state.page == 4:
    st.write("""
    You are one in a billion.
    """)

    if st.button("Next"):
        next_page()


# PAGE 5
elif st.session_state.page == 5:
    st.write("""
    In my world of black and white, you are the only one who can give it colors. And even if there's no such thing as perfect in this world, in my eyes, you are the most perfect girl I've ever seen.
    """)

    if st.button("Next"):
        next_page()


# PAGE 6
elif st.session_state.page == 6:
    st.write("""
    I like you the way you are. And no flaws could ever change the feeling I have for you.
    """)

    if st.button("Next"):
        next_page()


# PAGE 7
elif st.session_state.page == 7:
    st.write("""
    You're the risk I'm willing to take, even if there's a possibility that you don't feel the same way I do. But I'd still do it, just for you.
    """)

    if st.button("Next"):
        next_page()


# PAGE 8
elif st.session_state.page == 8:
    st.write("""
    And just to be direct to the point, I like you.
    """)

    if st.button("Next"):
        next_page()


# PAGE 9
elif st.session_state.page == 9:
    st.write("""
    Medjo corny ko man nasimulan pero I just wanted you to know that among all the people I could've met, somehow, I met you. And maybe that's what makes you so special to me.
    """)

    if st.button("Next"):
        next_page()


# PAGE 10
elif st.session_state.page == 10:
    st.write("""
    Out of billions of people, you're the one I happened to find.
    """)

    if st.button("Next"):
        next_page()


# PAGE 11
elif st.session_state.page == 11:
    st.write("""
    I don't know what happens after this. Maybe things will change, maybe they won't. But regardless of what happens, I'm glad I got to meet you. And if liking you means taking a risk, then I guess this is one risk I'm willing to take.
    """)

    if st.button("Next"):
        next_page()


# PAGE 12
elif st.session_state.page == 12:
    st.write("""
    Because you're worth it.
    """)

    if st.button("Next"):
        next_page()


# PAGE 13
elif st.session_state.page == 13:
    st.write("""
    Every single second with you feels like eternity.
    """)

    if st.button("Next"):
        next_page()


# PAGE 14
elif st.session_state.page == 14:
    st.write("""
    I never want it to end.
    """)

    if st.button("Next"):
        next_page()


# PAGE 15
elif st.session_state.page == 15:
    st.write("""
    So im here. And i wanna ask you a genuine question.
    """)

    if st.button("Next"):
        next_page()


# PAGE 16
elif st.session_state.page == 16:
    st.write("""
    Can i court you?
    """)

    if st.button("Yes 💗"):
        st.session_state.page = 17
        st.rerun()

    if st.button("No"):
        st.session_state.page = 18
        st.rerun()


# PAGE 17 - YES
elif st.session_state.page == 17:
    st.write("""
    WAIT REALLY?? YESSS!!!! THANKYOUUUU!! THIS REALLY MEAN A LOT FOR ME 😭😭
    """)


# PAGE 18 - NO
elif st.session_state.page == 18:
    st.write("""
    Oh... Okayyy! Thankyouuuu for that answer, i deeply appreciate your efforts just to answer this thingy i dont even know what to call haha. Uhmmm... Ayon thankyou and wag kalimutan streak, okayy?? B-byeee!
    """)
