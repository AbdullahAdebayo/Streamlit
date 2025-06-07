import streamlit as st
import random

st.set_page_config(page_title="Arcium Score Generator", page_icon="🛡️")

st.title("🔐 Arcium Encrypted Score Generator")

# Username input
username = st.text_input("Enter your username")

# Role selection
roles = [
    "Select your role",
    "No role yet",
    "Apprentice",
    "Adventurer",
    "Confidant",
    "Parasol",
    "Emerging Chad",
    "Growing Chad",
    "Proven Chad",
    "gMPChad"
]
selected_role = st.selectbox("Choose your Arcium Role:", roles)

# Score calculation
score = None
if selected_role == "No role yet":
    score = 0
elif selected_role == "Apprentice":
    score = random.randint(6, 20)
elif selected_role == "Adventurer":
    score = random.randint(40, 60)
elif selected_role == "Confidant":
    score = random.randint(60, 80)
elif selected_role == "Parasol":
    score = random.randint(80, 100)
elif selected_role == "Emerging Chad":
    score = random.randint(20, 40)
elif selected_role == "Growing Chad":
    score = random.randint(40, 60)
elif selected_role == "Proven Chad":
    score = random.randint(60, 80)
elif selected_role == "gMPChad":
    score = random.randint(81, 100)

# Output result
if st.button("Generate Score"):
    if not username:
        st.warning("Please enter your username")
    elif selected_role == "Select your role":
        st.warning("Please select a role")
    else:
        if selected_role == "No role yet":
            st.markdown(f"<p style='color: purple; font-size: 24px;'>{username} not &lt;encrypted&gt; ❌</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: purple; font-size: 24px;'>{username} is &lt;encrypted&gt; ✅</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: purple; font-size: 20px;'>Role: {selected_role}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: purple; font-size: 20px;'>Encrypted Score: {score}</p>", unsafe_allow_html=True)