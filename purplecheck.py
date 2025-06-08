import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Arcium Score Generator", page_icon="🛡️", layout="centered")


st.markdown("""
    <style>
        body {
            background-color: #1a001f;
        }
        .stApp {
            background: linear-gradient(135deg, #1a001f 0%, #330033 100%);
            color: #e0b3ff;
        }
        h1 {
            color: #d580ff !important;
            text-align: center;
            font-size: 40px !important;
        }
        .purple-box {
            background-color: #3d0066;
            border-radius: 12px;
            padding: 20px;
            color: white;
            margin-top: 20px;
            box-shadow: 0 0 10px #cc66ff;
        }
        .stButton>button {
            background-color: #a64dff;
            color: white;
            border: none;
            padding: 0.5em 1em;
            border-radius: 8px;
            transition: 0.3s;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #cc66ff;
            box-shadow: 0 0 10px #e699ff;
        }
        .stSelectbox label, .stTextInput label {
            color: #e0b3ff;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Arcium Encrypted Score Generator")

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
            st.markdown(
                f"<div class='purple-box'><p style='font-size: 24px;'>{username} not &lt;encrypted&gt; ❌</p></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(f"""
                <div class='purple-box'>
                    <p style='font-size: 24px;'>{username} is &lt;encrypted&gt; ✅</p>
                    <p style='font-size: 20px;'>Role: <b>{selected_role}</b></p>
                    <p style='font-size: 20px;'>Encrypted Score: <b>{score}</b></p>
                </div>
            """, unsafe_allow_html=True)
