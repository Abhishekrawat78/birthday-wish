import streamlit as st
import base64
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Birthday", layout="centered")

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

# --- Fireworks Animation (looping with auto reload) ---
def show_fireworks():
    fireworks_html = """
    <div style="display: flex; justify-content: center;">
      <iframe src="https://embed.lottiefiles.com/animation/4773" width="400" height="400" frameBorder="0" allowfullscreen></iframe>
    </div>
    <script>
      setInterval(() => window.location.reload(), 30000); // reload page every 30s
    </script>
    """
    components.html(fireworks_html, height=420)

# --- Password Gate ---
password = st.text_input("Enter password to unlock surprise", type="password")
if password != "1234":
    st.warning("Oops! Wrong password.")
    st.stop()

st.success("Welcome, bhai! ❤️")

play_music("birthday.mp3")
show_fireworks()

# --- Step 1: Show Happy Birthday First ---
st.markdown("<h1 style='text-align: center; color: red;'>🎉 Happy Birthday Bhai ❤ 🎉</h1>", unsafe_allow_html=True)
time.sleep(2)

# --- Step 2: Show Image Slideshow ---
st.image([
    "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg",
    "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg",
    "WhatsApp Image 2025-07-16 at 19.02.17_98af8857.jpg"
], use_container_width=True)
time.sleep(2)

# --- Step 3: Typing Effect Message ---
def typing_message(message, delay=0.02):
    for line in message.strip().split("\n"):
        st.markdown(f"<p style='font-size:18px; text-align: center;'>{line}</p>", unsafe_allow_html=True)
        time.sleep(delay * len(line))

# --- Final Message ---
full_message = """
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

# --- Balloons (centered and repeated using JavaScript) ---
st.markdown("""
<div style='text-align: center;'>🎈🎈🎈</div>
<script>
    function triggerBalloons() {
        const event = new Event("keydown");
        event.key = "b";
        document.dispatchEvent(event);
    }
    setInterval(triggerBalloons, 2000);
</script>
""", unsafe_allow_html=True)

st.balloons()
