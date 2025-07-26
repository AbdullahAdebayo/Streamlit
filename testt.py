import streamlit as st

# --- Quiz Data ---
quiz_data = [
    {
        "question": "What is Arcium's core mission?",
        "options": [
            "To be an Ethereum competitor",
            "To build the universal privacy layer for Web3",
            "To launch a new NFT marketplace",
            "To create a decentralized browser"
        ],
        "answer": "To build the universal privacy layer for Web3"
    },
    {
        "question": " Which of these is a limitation of Fully Homomorphic Encryption (FHE) compared to MPC?",
        "options": [
            "FHE cannot compute on encrypted data",
            "FHE is vulnerable to side-channel hardware attacks",
            "FHE has very low transaction processing speed and high computational cost",
            "FHE requires multiple participants to share their private keys"
        ],
        "answer": "FHE has very low transaction processing speed and high computational cost"
    },
    {
        "question": "What are MXEs in Arcium?",
        "options": [
            "Multi-execution Environments for secure private computation",
            "Mining Execution Engines",
            "Modular External Encryptors",
            "Market Exchange Entities"
        ],
        "answer": "Multi-execution Environments for secure private computation"
    },
    {
        "question": "Which language is used to build MXE logic in Arcium?",
        "options": [
            "Solidity",
            "Python",
            "Rust",
            "Go"
        ],
        "answer": "Rust"
    },
    {
        "question": "Why is MPC considered more flexible than TEEs in privacy-preserving computation?",
        "options": [
            "MPC is built into hardware chips and does not require coding",
            "MPC requires less bandwidth than ZKPs",
            "MPC does not depend on trusted hardware and is resilient against side-channel attacks",
            "MPC runs computations inside a secure processor core"
        ],
        "answer": "MPC does not depend on trusted hardware and is resilient against side-channel attacks"
    },
    {
        "question": "What is the logo Arcium adopted",
        "options": [
            "☂️ Umbrella",
            "🔐 Lock",
            "🧠 Brain",
            "💜 "
        ],
        "answer": "☂️ Umbrella"
    },
    {
        "question": "What does Arcis help developers build?",
        "options": [
            "Encrypted programs for MXEs",
            "Smart contracts for Ethereum",
            "Crypto wallets",
            "Blockchain games only"
        ],
        "answer": "Encrypted programs for MXEs"
    },
    {
        "question": "When is the gMPC day?",
        "options": [
            "idk",
            "June 22nd",
            "March 15th",
            "September 15th"
        ],
        "answer": "June 22nd"
    },
    {
        "question": "What kind of use cases can Arcium support?",
        "options": [
            "Only NFTs",
            "Only gaming",
            "Anything needing privacy: DeFi, AI, games, identity",
            "Just Layer 2 scaling"
        ],
        "answer": "Anything needing privacy: DeFi, AI, games, identity"
    },
    {
        "question": "What is a key trait of MXEs?",
        "options": [
            "They are slow but secure",
            "They run on EVM natively",
            "They are off-chain and produce verifiable proofs",
            "They use GPUs for rendering"
        ],
        "answer": "They are off-chain and produce verifiable proofs"
    },
    {
        "question": "Who fools the most in the Arcium community?",
        "options": [
            "Miebi",
            "Miebi",
            "Miebi",
            "Miebi"
        ],
        "answer": "Miebi"
    },
    {
        "question": "What is the primary focus of Arcium's development?",
        "options": [
            "Building a new blockchain",
            "Creating a universal privacy layer",
            "Developing a new consensus algorithm",
            "Launching a new token"
        ],
        "answer": "Creating a universal privacy layer"
    },
    {        
        "question": "Who are the founders of Arcium?",
        "options" : [
            "YNJL",
            "WDYM",
            "LMAO",
            "IDEK"
        ],
        "answer" : "YNJL"
    },
    {     
        "question": "Serloost will be holding a talk on _____ and on day __ of the Virtual summit?",
        "options": [
            "Everything Arcium, 1",
            "The Arcium Umbrella, 2",
            "Anything Under the Umbrella, 2",
            "Arcium as a community, 2"
        ], 
        "answer": "Anything Under the Umbrella, 2"
    },
    {
        "question": "The first host of the virtual summit is___?",
        "options": [
            "Alex",
            "DoinQz",
            "Aberama",
            "RuzyTarantino"
        ],
        "answer": "DoinQz"
    },
    {        "question": "On what day will Aberama be speaking on the Virtual summit?",
        "options": [
            "Day 1",
            "Day 2",
            "Day 3",
            "Day 4"
        ],
        "answer": "Day 2"
        },
    {        "question": "The last project to announce that it's Blackbox will run as a fully integrated Arx Node in the Arcium Network is ___?",
        "options": [
            "Octra",
            "Dawn",
            "Solana",
        ],
        "answer": "Dawn"
    },
    {     
           "question": "How does Arcium improve user experience when sending confidential tokens?",
        "options": [
            "By auto converting tokens to ETH before transfer",
            "By removing the need for the sender to know the recipient",
            "By allowing senders to create confidential token accounts for recipients",
            "By using a centralized server for processing",
        ],
        "answer": "By allowing senders to create confidential token accounts for recipients"
    },
    {   
        "question": "What problem does Arcium’s Confidential SPL Token solve regarding how confidential tokens are currently handled in smart contracts?",
        "options": [
            "It allows confidential tokens to be used across Ethereum bridges",
            "It lets smart contracts control confidential balances without needing EOAs",
            "It prevents DeFi apps from using confidential tokens at all",
            "It simplifies gas estimation for private DeFi applications"
        ],
        "answer": " It lets smart contracts control confidential balances without needing EOAs"
    },
    {       
        "question": "Which of the following is the primary motivation behind Arcium developing the Confidential SPL Token Standard??",
        "options": [
            "To introduce a new Solana token unrelated to existing protocols",
            "To eliminate the need for smart contracts in token operations",
            "To replace Token 2022 entirely with a more public standard",
            "To merge existing token systems with encrypted computing for native confidentiality"
        ],
        "answer": "To merge existing token systems with encrypted computing for native confidentiality"
    }
]    

# --- App UI ---
st.set_page_config(page_title="Arcium Quiz", page_icon="🧠")
st.title("How Encrypted Are You?")
st.markdown("How well are you familiar with Arcium and its community?")
st.markdown("All questions are from Arcium's Docs and Official X account.")

user_answers = {}
score = 0

# --- Display Questions ---
for i, item in enumerate(quiz_data):
    question = item["question"]
    options = item["options"]
    user_answers[question] = st.radio(f"**{i+1}. {question}**", options, key=i)

# --- Submit Button ---
if st.button("✅ Submit Quiz"):
    for item in quiz_data:
        if user_answers[item["question"]] == item["answer"]:
            score += 1

    percentage = (score / len(quiz_data)) * 100

    # --- Style Result Output ---
    st.markdown(
        """
        <style>
        .result-box {
            background-color: #5e4b8b;
            padding: 20px;
            border-radius: 10px;
            color: white;
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- Score Status Message ---
    if percentage >= 90:
        status = "Arcium OG,fully <encrypted>!"
    elif percentage >= 70:
        status = "Almost there! Keep learning about Arcium."
    elif percentage >= 50:
        status = "Explore more about Arcium to improve your score."
    else:
        status = "A newbie spotted,get <encrypted> with Arcium!"

    # --- Show Result ---
    st.markdown(f"""
    <div class="result-box">
    <strong>Score:</strong> {score}/{len(quiz_data)}<br>
    <strong>Percentage:</strong> {int(percentage)}%<br>
    <strong>Status:</strong> {status}
    </div>
    """, unsafe_allow_html=True)

    # --- Optional: Show Answers ---
    with st.expander("📖 See All Questions & Correct Answers"):
        for i, item in enumerate(quiz_data):
            st.markdown(f"**{i+1}. {item['question']}**")
            st.markdown(f"- ✅ Correct Answer: `{item['answer']}`")
            st.markdown("---")
