import streamlit as st
import time

# --- 1. CONFIGURATION & GOD-MODE STYLING ---
st.set_page_config(page_title="M-Cyber Terminal", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1a022d, #0d0208);
        background-attachment: fixed;
    }

    /* SCANLINE EFFECT */
    .stApp::before {
        content: " "; display: block; position: absolute; top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2; background-size: 100% 4px, 3px 100%; pointer-events: none;
    }

    /* MAIN CONTAINER */
    .block-container {
        border: 2px solid #00FF41;
        box-shadow: 0 0 20px #00FF41, inset 0 0 10px #00FF41;
        padding: 40px !important;
        background: rgba(13, 2, 8, 0.9);
        border-radius: 20px;
        margin-top: 30px;
    }

    /* STYLISH START PROMPT */
    .command-prompt {
        color: #FFFF00;
        font-family: 'Courier New', monospace;
        font-size: 24px;
        text-align: center;
        margin-bottom: 10px;
        letter-spacing: 2px;
        text-shadow: 0 0 10px #FFFF00;
    }

    /* INTEGRATED LOG FEED */
    .log-box {
        background: rgba(0, 255, 65, 0.05);
        border: 1px solid #00FF41;
        padding: 15px;
        height: 150px;
        overflow-y: auto;
        font-family: 'Courier New', monospace;
        color: #00FF41;
        margin-bottom: 20px;
        border-radius: 5px;
    }

    /* LIVE TIMER */
    .timer-display {
        color: #00FF41;
        font-size: 30px;
        text-align: right;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #00FF41;
    }

    /* GLITCH TEXT */
    @keyframes glitch { 0% { transform: translate(0); } 20% { transform: translate(-2px, 2px); } 100% { transform: translate(0); } }
    .intro-text {
        color: #BC13FE !important;
        font-size: 50px !important;
        font-weight: bold;
        text-shadow: 3px 3px #00FF41;
        animation: glitch 1.5s infinite alternate-reverse;
        text-align: center;
    }

    /* BOSS LOCKS */
    @keyframes alert-pulse { 0% { box-shadow: 0 0 10px #FF0000; } 50% { box-shadow: 0 0 40px #FF0000; } 100% { box-shadow: 0 0 10px #FF0000; } }
    .boss-lock {
        border: 4px solid #FF0000;
        padding: 40px;
        background: rgba(255, 0, 0, 0.1);
        border-radius: 15px;
        animation: alert-pulse 1.5s infinite;
        text-align: center;
    }

    /* INPUT BOX */
    .stTextInput > div > div > input {
        background-color: black !important;
        color: #FFFF00 !important;
        border: 2px solid #FFFF00 !important;
        box-shadow: 0 0 15px #FFFF00;
        font-size: 25px !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if 'level' not in st.session_state:
    st.session_state.level = 0 
    st.session_state.history = ["SYST: WAITING FOR INPUT..."]
    st.session_state.start_time = None
    st.session_state.flash = None

LEVEL_DATA = {
    1: {"q": "LEVEL 1: BIT-SHIFT. [2, 4, 16, 256, ?]", "a": "65536"},
    2: {"q": "LEVEL 2: M-CIPHER. [Sum of MEGHA: M13, E5, G7, H8, A1]", "a": "34"},
    3: {"q": "LEVEL 3: EFFICIENCY PROTOCOL. [Complexity of halving a sorted list?]", "a": "LOGN"},
    4: {"q": "LEVEL 4: LIFO STACK. [Order: M -> E -> G. Pop() once. Who is at the top?]", "a": "E"},
    5: {"q": "LEVEL 5: THE PARADOX. [(True XOR True) OR (False AND True)]", "a": "FALSE"},
}

# --- 3. AUDIO ---
st.markdown("""<iframe width="0" height="0" src="https://www.youtube.com/embed/gdTl3Vi8vvY?autoplay=1&loop=1&playlist=gdTl3Vi8vvY" frameborder="0" allow="autoplay"></iframe>""", unsafe_allow_html=True)

# --- 4. CORE LOGIC ---
def check_logic():
    raw = st.session_state.input_box.strip().upper()
    clean = raw.replace(" ", "").replace("O(", "").replace(")", "")
    
    if st.session_state.level == 0:
        if clean == "START":
            st.session_state.level = 1
            st.session_state.start_time = time.time()
            st.session_state.history.append(">> SYSTEM INITIALIZED. TIMER START.")
    
    elif 1 <= st.session_state.level <= 5:
        if clean == LEVEL_DATA[st.session_state.level]["a"]:
            st.session_state.level += 1
            st.session_state.flash = "success"
            st.session_state.history.append(f">> LEVEL {st.session_state.level-1} CLEARED.")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f">> ERR: ACCESS DENIED FOR {raw}")
            
    elif st.session_state.level == 6:
        if clean == "2014":
            st.session_state.level = 7
            st.session_state.flash = "success"
            st.session_state.history.append(">> TIMELINE SYNCED.")
        else:
            st.session_state.flash = "error"

    elif st.session_state.level == 7:
        if clean == "G-DRAGON":
            st.session_state.level = 8
            st.session_state.end_time = time.time()
            st.session_state.history.append(">> MISSION SUCCESSFUL.")
        else:
            st.session_state.flash = "error"
    
    st.session_state.input_box = ""

# --- 5. RENDER UI ---

# Flash Effects
if st.session_state.flash == "success":
    st.markdown('<div class="success-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None
elif st.session_state.flash == "error":
    st.markdown('<div class="error-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None

# Log Feed (Integrated in main view)
log_html = "".join([f"<p style='margin:0;'>{line}</p>" for line in st.session_state.history[::-1]])
st.markdown(f'<div class="log-box">{log_html}</div>', unsafe_allow_html=True)

# Main Screens
if st.session_state.level == 0:
    st.markdown('<p class="intro-text">M-CYBER TERMINAL</p>', unsafe_allow_html=True)
    st.markdown('<p class="command-prompt">SYSTEM READY. TYPE "START" TO BEGIN MISSION.</p>', unsafe_allow_html=True)
    st.text_input("CMD>", key="input_box", on_change=check_logic)

elif 1 <= st.session_state.level <= 5:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center;'>{LEVEL_DATA[st.session_state.level]['q']}</h1>", unsafe_allow_html=True)
    st.text_input("KEYCODE>", key="input_box", on_change=check_logic)
    
elif st.session_state.level == 6:
    st.markdown('<div class="boss-lock"><p style="color:#FF0000; font-size:30px; font-weight:bold;">LOCK-1: KING OF K-POP TIMELINE</p><p style="color:white;">Year of Birth + Month of Infinity + Day of Double-Eight</p></div>', unsafe_allow_html=True)
    st.text_input("SYNC CODE>", key="input_box", on_change=check_logic)

elif st.session_state.level == 7:
    st.markdown('<div class="boss-lock" style="border-color:#BC13FE; background:rgba(188,19,254,0.1);"><p style="color:#BC13FE; font-size:30px; font-weight:bold;">LOCK-2: IDENTITY GATE</p><p style="color:white;">WHO IS THE SOVEREIGN KING?</p></div>', unsafe_allow_html=True)
    st.text_input("IDENTITY>", key="input_box", on_change=check_logic)

elif st.session_state.level == 8:
    total_time = round(st.session_state.end_time - st.session_state.start_time, 2)
    st.markdown(f'<div class="victory-box"><h1 style="color:#FFFF00; font-size:60px;">MISSION ACCOMPLISHED</h1><p style="color:#FFFF00; font-size:25px;">G-DRAGON VERIFIED. MISSION TIME: {total_time}s</p></div>', unsafe_allow_html=True)
    st.balloons()
    if st.button("REBOOT TERMINAL"):
        st.session_state.level = 0
        st.rerun()

# LIVE TIMER (Only visible when game is active)
if st.session_state.level > 0 and st.session_state.level < 8:
    elapsed = round(time.time() - st.session_state.start_time, 1)
    st.markdown(f'<div class="timer-display">Uptime: {elapsed}s</div>', unsafe_allow_html=True)
    time.sleep(0.1)
    st.rerun()
