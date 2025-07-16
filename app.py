import streamlit as st
import base64
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Birthday", layout="centered")

# --- Password Gate ---
password = st.text_input("Enter password to unlock surprise", type="password")
if password != "1234":
    st.warning("Oops! Wrong password.")
    st.stop()

st.success("Welcome, bhai! ❤️")

# --- Background Music ---
def play_music(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'''
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        '''
        st.markdown(md, unsafe_allow_html=True)

play_music("birthday.mp3")

# --- Fireworks Animation ---
fireworks_html = """
<iframe src="https://embed.lottiefiles.com/animation/4773" width="100%" height="300" frameBorder="0"></iframe>
"""
components.html(fireworks_html, height=300)

# --- Typing Effect ---
def typing_message(message, delay=0.05):
    typed = ""
    for char in message:
        typed += char
        st.markdown(f"<h5>{typed}</h5>", unsafe_allow_html=True)
        time.sleep(delay)

# --- Final Message ---
full_message = """
Happy Birthday Bhai ❤

Zindagi mein kai log aaye aur gaye,
Lekin tu wo hai jo har waqt mere saath khada raha.
Dost toh kehte hain sab, par tu toh mere liye bhai se bhi badhkar hai.
Jab main girta hoon, tu uthata hai,
Jab main haar maanta hoon, tu kehta hai –
"Bhai, tu kar lega... tu tod dega!"

Tu sirf mera support nahi, mera fuel hai bhai –
Jisne mujhe kabhi rukhne nahi diya.

Aur bhai, yaad rakh –
Ek din, hum dono milke apna business kholenge.
Apna kaam, apna naam –
"Dalle Brothers Pvt. Ltd." 😎🔥

Jab tak tu sath hai, mujhe kisi cheez ka darr nahi.
Tu hai toh sab hai.

Janamdin mubarak ho bhai – khush reh, aage badh,
aur ek din duniya ko dikha denge ki asli bhai log kaun hote hain!
❤🎂💪
"""
typing_message(full_message, delay=0.02)

# --- Image Slideshow ---
st.image([
    "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg",
    "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg",
    "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg"
], use_container_width=True)

st.balloons()
