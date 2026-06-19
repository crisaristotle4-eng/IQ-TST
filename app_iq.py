import streamlit as st
import time

# --- STYLING & THEME CONFIG ---
st.set_page_config(page_title="CRIS' IQ OVERRIDE", page_icon="🧠", layout="centered")

# Custom Cyberpunk/Anime CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #00FFCC; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00FFCC; }
    .stButton>button {
        background-color: #FF007F !important; color: white !important;
        font-weight: bold; border-radius: 10px; border: none;
        box-shadow: 0 0 15px #FF007F; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 25px #FF007F; }
    .success-text { color: #00FFCC; font-weight: bold; font-size: 20px; }
    .fail-text { color: #FF007F; font-weight: bold; font-size: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'step' not in st.session_state:
    st.session_state.step = 'intro'
if 'IQ_score' not in st.session_state:
    st.session_state.IQ_score = 0
if 'current_q' not in st.session_state:
    st.session_state.current_q = 1

total_questions = 22

# --- THE RIDDLE DATABASE ---
questions = {
    1: {"p": "What has a head and a tail but no body?", "a": ["coin"], "t": 15},
    2: {"p": "Aint having a mouth but I speak, not legs but I run, not hands but i can carry stuff. What am I?", "a": ["river"], "t": 20},
    3: {"p": "Imagine you are in a room with no doors nor windows nor escape ways nor weapons and its filing up with water. How can you escape the problem?", "a": ["stop imagining", "stop the imagination"], "t": 20},
    4: {"p": "What has hands but cannot clap?", "a": ["clock"], "t": 20},
    5: {"p": "What goes up but never comes down?", "a": ["age"], "t": 20},
    6: {"p": "The more of them you take the more you leave?", "a": ["footsteps"], "t": 20},
    7: {"p": "David’s parents have three sons: Snap, Crackle, and who is the third?", "a": ["david"], "t": 20},
    8: {"p": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?", "a": ["map"], "t": 20},
    9: {"p": "What is seen in the middle of March and April that can’t be seen at the beginning or end of either month?", "a": ["r"], "t": 20},
    10: {"p": "What word in the dictionary is spelled incorrectly?", "a": ["incorrectly"], "t": 20},
    11: {"p": "What can you catch, but not throw?", "a": ["cold"], "t": 20},
    12: {"p": "A girl fell off a 20-foot ladder but didn't get hurt. Why?", "a": ["she was on the bottom step", "she was at the bottom step"], "t": 20},
    13: {"p": "If you’re running in a race and you pass the person in second place, what place are you in?", "a": ["second"], "t": 20},
    14: {"p": "What has one eye, but can’t see anything at all?", "a": ["needle"], "t": 20},
    15: {"p": "What has many keys but can’t open a single lock?", "a": ["piano"], "t": 20},
    16: {"p": "What can travel around the world while staying in a corner?", "a": ["stamp"], "t": 20},
    17: {"p": "What has a thumb and four fingers, but is not a hand?", "a": ["glove"], "t": 20},
    18: {"p": "I have keys but no doors. I have space but no room. You can enter but can’t leave. What am I?", "a": ["keyboard"], "t": 20},
    19: {"p": "What building has the most stories?", "a": ["library"], "t": 20},
    20: {"p": "What can you cheat or hold in your left hand but never in your right hand?", "a": ["right elbow"], "t": 20},
    21: {"p": "You see a boat filled with people. It has not sunk, but when you look again you don’t see a single person on the boat. Why?", "a": ["they were all married"], "t": 20},
    22: {"p": "I am tall when I am young, and I am short when I am old. What am I?", "a": ["candle"], "t": 20}
}

# --- STAGE 1: INTRO ---
if st.session_state.step == 'intro':
    st.title("⚡ CRIS' MAINFRAME SYSTEM ⚡")
    st.subheader("Hi Bruh! Welcome to one of Cris' Programs.")
    st.write("This application dynamically analyzes your cognitive metrics via structural syntax percentage evaluation.")
    
    name = st.text_input("ENTER COGNOMEN (What's your name?):")
    age = st.number_input("ENTER AGE CHRONOLOGY:", min_value=0, max_value=120, value=0)
    
    if st.button("INITIALIZE SYSTEM OVERRIDE"):
        if name and age >= 15:
            st.session_state.name = name.lower().strip()
            st.session_state.age = age
            st.session_state.step = 'proceed_check'
            st.rerun()
        elif age < 15 and age > 0:
            st.error("SYSTEM ERROR: You aint eligible. Return when your processing unit matures.")
        else:
            st.warning("Input valid metadata to unlock system access.")

# --- STAGE 2: ACCESS CONFIRMATION ---
elif st.session_state.step == 'proceed_check':
    st.title(f"Target Acquired: {st.session_state.name.upper()}")
    st.write(f"Age {st.session_state.age} verified. Neural pathways ready.")
    st.info("Shall we proceed to execution layer?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YAP / YES / GO AHEAD"):
            st.session_state.step = 'quiz'
            with st.spinner("Loading Mainframe Execution Layers..."):
                time.sleep(1.0)
            st.rerun()
    with col2:
        if st.button("ABORT MISSION"):
            st.session_state.step = 'intro'
            st.rerun()

# --- STAGE 3: THE QUIZ INTERFACE ---
elif st.session_state.step == 'quiz':
    q_idx = st.session_state.current_q
    
    if q_idx <= len(questions):
        q_data = questions[q_idx]
        
        st.title(f"🧠 QUESTION {q_idx} / {len(questions)}")
        st.progress(q_idx / len(questions))
        st.markdown(f"### ⏱️ TIME MATRIX CONSTANCE: `{q_data['t']} SECONDS`")
        st.info(q_data['p'])
        
        with st.form(key=f"q_form_{q_idx}"):
            user_ans = st.text_input("Enter Answer Matrix:", key=f"input_{q_idx}").lower().strip()
            submit = st.form_submit_button(label="TRANSMIT DATA")
            
            if submit:
                if user_ans in q_data['a']:
                    st.session_state.IQ_score += 1
                    st.toast("⚡ CALIBRATION SUCCESSFUL!", icon="✅")
                else:
                    fails = ["Men you're dead!", "Bruh!!!", "Its over men its over", "Bruh, you missed it!"]
                    st.toast(fails[q_idx % len(fails)], icon="❌")
                
                st.session_state.current_q += 1
                st.rerun()
    else:
        st.session_state.step = 'results'
        st.rerun()

# --- STAGE 4: RESULTS ---
elif st.session_state.step == 'results':
    st.title("📊 SYSTEM ANALYSIS MATRIX")
    st.write(f"Yep, that's the end of it, {st.session_state.name.upper()}.")
    
    percentage = (st.session_state.IQ_score / total_questions) * 100
    st.metric(label="FINAL CALCULATED COGNITIVE PERCENTAGE", value=f"{percentage:.2f}%")
    
    if percentage >= 90:
        st.balloons()
        st.markdown(f"<p class='success-text'>Congrats! You are pretty smart {st.session_state.name.title()}. Scoring over 90% in CRIS' test is impressive I guess!</p>", unsafe_allow_html=True)
        st.success("Give CRIS my regards for creating this test!")
    elif percentage >= 50:
        st.markdown(f"<p class='success-text'>Nice effort {st.session_state.name.title()}! Even this percentage in CRIS' test is fair!</p>", unsafe_allow_html=True)
    elif percentage == 0:
        st.markdown("<p class='fail-text'>YOU STUPID BRO YOU STUPID 💀</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p class='fail-text'>Aaaaha walai its over men! But at least you tried.</p>", unsafe_allow_html=True)
        
    if st.button("REBOOT MAIN ENGINE"):
        st.session_state.clear()
        st.rerun()
