import streamlit as st

st.set_page_config(page_title="🎉 Birthday Surprise 🎉", page_icon="🎂", layout="centered")

# Password input
password = st.text_input("Enter password to unlock your surprise 🎁", type="password")

# Replace this with your secret password
correct_password = "happy123"

if password == correct_password:
    st.success("Welcome, bhai! ❤️")
    
    st.markdown("<h1 style='text-align: center; color: #ff1493;'>🎉 Happy Birthday, Bhai! 🎉</h1>", unsafe_allow_html=True)
    
    st.image("C:/Users/abhishek/Downloads/Telegram Desktop/WhatsApp Image 2025-07-15 at 21.12.19_d10d3987.jpg", use_container_width=True)

    
    st.markdown("""
    <div style='text-align: center; font-size: 20px;'>
        <p>happy birthday bhai  🥳</p>
        <p>kub mehnat kar bada admi bann 💪✨</p>
        <p>Enjoy your life ! 🎉</p>
        <p>– Tera bhai, Abhishek ❤️</p>
    </div>
    """, unsafe_allow_html=True)
else:
    if password != "":
        st.error("Oops! Galat password daala bhai 😅")
