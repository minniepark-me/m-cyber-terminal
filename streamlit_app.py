import streamlit as st
import time

# --- 1. CONFIGURATION & HYPER-CYBER STYLING ---
st.set_page_config(page_title="M-Cyber God-Mode", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1a022d, #0d0208);
        background-attachment: fixed;
        overflow: hidden;
    }
    .stApp::before {
        content: " ";
        display: block;
        position: absolute;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2;
        background-size: 100% 4px, 3px 100%;
        pointer-events: none;
    }
    .block-container {
        border: 2px solid #00FF41;
        box-shadow: 0 0 20px #00FF41, inset 0 0 10px #00FF41;
        padding: 50px !important;
        background: rgba(13, 2, 8, 0.85);
        border-radius: 20px;
        margin-top: 20px;
    }
    .integrated-log {
        background: rgba(0, 255, 65, 0.05);
        border: 1px solid rgba(0, 255, 65, 0.3);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 25px;
        height: 150px;
        overflow-y: auto;
        font-family: 'Courier New', monospace;
        color: #00FF41;
        font-size: 14px;
    }
    .log-entry { margin: 0; padding: 2px 0; border-bottom: 1px solid rgba(0, 255, 65, 0.1); }
    
    /* GLITCH ANIMATION FOR THE TERMINAL TITLE */
    @keyframes glitch {
        0% { transform: translate(0); text-shadow: 2px 2px #00FF41; }
        20% { transform: translate(-3px, 3px); text-shadow: -2px -2px #ff00ff; }
        40% { transform: translate(-3px, -3px); }
        60% { transform: translate(3px, 3px); }
        80% { transform: translate(3px, -3px); }
        100% { transform: translate(0); }
    }
    .intro-text {
        color: #BC13FE !important;
        font-size: 45px !important;
        font-weight: bold;
        text-shadow: 3px 3px #00FF41;
        text-align: center;
        animation: glitch 0.3s infinite; /* Fixed: Added infinite animation */
    }

    .stTextInput > div > div > input {
        background-color: black !important;
        color: #FFFF00 !important;
        border: 2px solid #FFFF00 !important;
        font-size: 25px !important;
        height: 60px;
        text-align: center;
    }

    /* SUCCESS/ERROR FLASHES */
    @keyframes green-flash { 0% { background-color: #00FF41; opacity: 0.5; } 100% { background-color: transparent; opacity: 0; } }
    @keyframes red-flash { 0% { background-color: #FF0000; opacity: 0.5; } 100% { background-color: transparent; opacity: 0; } }
    .success-trigger { animation: green-flash 0.5s ease-out; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }
    .error-trigger { animation: red-flash 0.5s ease-out; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }
    
    .victory-box {
        border: 10px solid #FFFF00;
        padding: 60px;
        background: black;
        box-shadow: 0 0 50px #FFFF00, inset 0 0 30px #FFFF00;
        text-align: center;
        border-radius: 30px;
    }

    /* GLOWING ONE OF A KIND TEXT */
    @keyframes neon-glow {
        0% { text-shadow: 0 0 10px #00FF41, 0 0 20px #00FF41; }
        50% { text-shadow: 0 0 25px #00FF41, 0 0 50px #00FF41; }
        100% { text-shadow: 0 0 10px #00FF41, 0 0 20px #00FF41; }
    }
    .glowing-final {
        color: #00FF41;
        font-family: 'Courier New', monospace;
        font-size: 45px !important;
        margin-top: 30px;
        font-weight: bold;
        animation: neon-glow 1.5s infinite;
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if 'level' not in st.session_state:
    st.session_state.level = 0 
    st.session_state.history = ["SYST_READY: Awaiting User..."]
    st.session_state.flash = None

# --- 3. AUDIO (FIXED WITH AUTO-START SCRIPT) ---
# We use a hidden iframe plus a small script to trigger audio on the first click
st.markdown("""
    <div id="audio-container">
        <iframe id="youtube-audio" width="0" height="0" 
        src="https://www.youtube.com/embed/gdTl3Vi8vvY?autoplay=1&loop=1&playlist=gdTl3Vi8vvY&enablejsapi=1" 
        frameborder="0" allow="autoplay"></iframe>
    </div>
    <script>
        // Browsers block audio until a user clicks. 
        // This triggers the play function as soon as the user interacts with the app.
        window.parent.document.addEventListener('mousedown', function() {
            var iframe = window.parent.document.getElementById('youtube-audio');
            if (iframe) {
                iframe.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
            }
        }, {once: true});
    </script>
    """, unsafe_allow_html=True)

# --- 4. DATA ---
LEVEL_DATA = {
    1: {"q": "LEVEL 1: BIT-SHIFT. [2, 4, 16, 256, ?]", "a": "65536"},
    2: {"q": "LEVEL 2: M-CIPHER. [Sum of MEGHA: M13, E5, G7, H8, A1]", "a": "34"},
    3: {"q": "LEVEL 3: EFFICIENCY PROTOCOL. [Complexity of halving a sorted list?]", "a": "LOGN"},
    4: {"q": "LEVEL 4: LIFO STACK. [Order: M -> E -> G. Pop() once. Who is at the top?]", "a": "E"},
    5: {"q": "LEVEL 5: THE PARADOX. [(True XOR True) OR (False AND True)]", "a": "FALSE"},
}

# --- 5. LOGIC ---
def check_logic():
    raw = st.session_state.input_box.strip().upper()
    clean = raw.replace(" ", "").replace("O(", "").replace(")", "")
    
    if st.session_state.level == 0 and clean == "START":
        st.session_state.level = 1
        st.session_state.history.append(">> TERMINAL ONLINE. ENCRYPTION ACTIVE.")
    elif 1 <= st.session_state.level <= 5:
        if clean == LEVEL_DATA[st.session_state.level]["a"]:
            st.session_state.level += 1
            st.session_state.flash = "success"
            st.session_state.history.append(f">> L{st.session_state.level-1} DECRYPTED.")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f">> ERR: ACCESS DENIED.")
    elif st.session_state.level == 6 and clean == "2014":
        st.session_state.level = 7
        st.session_state.flash = "success"
        st.session_state.history.append(">> TIMELINE SYNCED.")
    elif st.session_state.level == 7 and clean == "G-DRAGON":
        st.session_state.level = 8
        st.session_state.history.append(">> IDENTITY VERIFIED. CORE UNLOCKED.")
    st.session_state.input_box = ""

# --- 6. RENDER ---
if st.session_state.flash == "success":
    st.markdown('<div class="success-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None
elif st.session_state.flash == "error":
    st.markdown('<div class="error-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None

log_html = "".join([f"<p class='log-entry'>{log}</p>" for log in st.session_state.history[::-1]])
st.markdown(f'<div class="integrated-log">{log_html}</div>', unsafe_allow_html=True)

if st.session_state.level == 0:
    st.markdown('<p class="intro-text">M-CYBER SECURITY TERMINAL</p>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#FFFF00;'>TYPE 'START' TO INITIALIZE MISSION.</p>", unsafe_allow_html=True)
    st.text_input("", key="input_box", on_change=check_logic)

elif 1 <= st.session_state.level <= 5:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center;'>{LEVEL_DATA[st.session_state.level]['q']}</h1>", unsafe_allow_html=True)
    st.text_input("ENTER KEYCODE:", key="input_box", on_change=check_logic)

elif st.session_state.level == 6:
    st.markdown('<div class="boss-lock-container"><p style="color:#FF0000; font-size:30px; font-weight:bold;">⚠️ ENCRYPTION LOCK: LEVEL 1 ⚠️</p><p style="color:white;">YEAR OF BIRTH + MONTH OF INFINITY + DAY OF DOUBLE-EIGHT</p></div>', unsafe_allow_html=True)
    st.text_input("SYNC CODE:", key="input_box", on_change=check_logic)

elif st.session_state.level == 7:
    st.markdown('<div class="boss-lock-container" style="border-color:#BC13FE;"><p style="color:#BC13FE; font-size:30px; font-weight:bold;">🚨 FINAL IDENTITY GATE 🚨</p><p style="color:white;">SYSTEM CORE REACHED. VERIFY THE SOVEREIGN.</p></div>', unsafe_allow_html=True)
    st.text_input("AUTHORIZE IDENTITY:", key="input_box", on_change=check_logic)

elif st.session_state.level == 8:
    st.markdown(f"""
        <div class="victory-box">
            <h1 style="font-size:70px; color:#FFFF00;">👑 MISSION ACCOMPLISHED</h1>
            <p style="color:#FFFF00; font-size:30px; letter-spacing:5px; opacity: 0.8;">WELCOME HOME, G-DRAGON</p>
            <div class="glowing-final">
                Yes sir, You are ONE OF A KIND 💸 🐉
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
    if st.button("REBOOT SYSTEM"):
        st.session_state.level = 0
        st.rerun()
