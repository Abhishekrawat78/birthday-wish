import streamlit as st
import time
import base64

# Set page config
st.set_page_config(page_title="🎉 Happy Birthday Bhai!", layout="centered", initial_sidebar_state="collapsed")

# Background music function
def play_music(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# Fireworks animation (using HTML/CSS)
def fireworks_animation():
    fire_css = """
    <style>
    body {
        background-color: black;
        overflow: hidden;
    }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles@2.11.1/tsparticles.bundle.min.js"></script>
    <script>
    tsParticles.load("tsparticles", {
        "fullScreen": {"enable": true},
        "particles": {
            "number": {"value": 0},
            "color": {"value": ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff"]},
            "shape": {"type": "circle"},
            "opacity": {"value": 1},
            "size": {"value": 5},
            "move": {
                "enable": true,
                "speed": 10,
                "direction": "none",
                "outModes": {"default": "destroy"}
            }
        },
        "emitters": {
            "direction": "top",
            "rate": {"quantity": 10, "delay": 0.1},
            "size": {"width": 100, "height": 0},
            "position": {"x": 50, "y": 100}
        }
    });
    </script>
    <div id="tsparticles"></div>
    """
    st.components.v1.html(fire_css, height=0)

# Typing animation message
def typing_message(msg, delay=0.05):
    display = ""
    for char in msg:
        display += char
        st.markdown(f"<h4 style='color:#ff4b4b'>{display}</h4>", unsafe_allow_html=True)
        time.sleep(delay)

# App logic
password = st.text_input("Enter password to unlock your surprise 🎁", type="password")

if password == "1234":
    st.success("Welcome, bhai! ❤️")

    # Start music
    play_music("birthday.mp3")

    # Fireworks
    fireworks_animation()

    # Typing message
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
“Dalle Brothers Pvt. Ltd.” 😎🔥

Jab tak tu sath hai, mujhe kisi cheez ka darr nahi.
Tu hai toh sab hai.

Janamdin mubarak ho bhai – khush reh, aage badh,
aur ek din duniya ko dikha denge ki asli bhai log kaun hote hain!
❤🎂💪
"""
    typing_message(full_message, delay=0.02)

    # Image slideshow (single image repeated)
    st.image([
        "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg",
        "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg",
        "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg"
    ], use_container_width=True)

else:
    st.warning("Please enter the correct password to view your surprise.")
