import streamlit as st
import time

# --- 1. CONFIGURATION & STYLING ---
st.set_page_config(page_title="M-Cyber God-Mode", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1a022d, #0d0208);
        background-attachment: fixed;
        overflow: hidden;
    }
    
    /* SCANLINE EFFECT */
    .stApp::before {
        content: " "; display: block; position: absolute; top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2; background-size: 100% 4px, 3px 100%; pointer-events: none;
    }

    .block-container {
        border: 2px solid #00FF41;
        box-shadow: 0 0 20px #00FF41, inset 0 0 10px #00FF41;
        padding: 50px !important;
        background: rgba(13, 2, 8, 0.9);
        border-radius: 20px;
        margin-top: 20px;
        z-index: 5;
    }
    
    /* INTENSE DANGER VIBRATIONS */
    @keyframes intense-red {
        0% { transform: translate(0); filter: brightness(1); }
        10% { transform: translate(-3px, -2px); filter: brightness(1.5); }
        20% { transform: translate(3px, 2px); }
        30% { transform: translate(-3px, 2px); }
        40% { transform: translate(3px, -2px); }
        50% { transform: translate(-1px, -1px); filter: brightness(1.2); }
        100% { transform: translate(0); }
    }

    @keyframes intense-violet {
        0% { transform: translate(0); box-shadow: 0 0 10px #BC13FE; }
        20% { transform: translate(2px, 2px); box-shadow: 0 0 25px #BC13FE; }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, -2px); }
        80% { transform: translate(-2px, 2px); }
        100% { transform: translate(0); }
    }

    .danger-box-red {
        text-align: center; border: 5px solid #FF0000; padding: 25px; color: #FF0000;
        animation: intense-red 0.1s infinite; background: rgba(255, 0, 0, 0.15);
        border-radius: 15px; text-shadow: 0 0 10px #FF0000;
    }

    .danger-box-violet {
        text-align: center; border: 5px solid #BC13FE; padding: 25px; color: #BC13FE;
        animation: intense-violet 0.15s infinite; background: rgba(188, 19, 254, 0.15);
        border-radius: 15px; text-shadow: 0 0 10px #BC13FE;
    }

    /* INPUT BOX CENTERING */
    .stTextInput > div > div > input {
        text-align: center !important;
        background-color: black !important;
        color: #FFFF00 !important;
        border: 2px solid #FFFF00 !important;
        font-size: 25px !important;
        height: 60px;
    }

    /* GLITCH TITLE */
    @keyframes glitch {
        0% { transform: translate(0); text-shadow: 2px 2px #00FF41; }
        25% { transform: translate(-2px, 2px); text-shadow: -2px -2px #BC13FE; }
        50% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
    .intro-text {
        color: #BC13FE !important; font-size: 45px !important; font-weight: bold;
        animation: glitch 0.4s infinite; text-align: center;
    }

    /* FLASH EFFECTS */
    @keyframes green-flash-anim { 0% { background: rgba(0, 255, 65, 0.8); } 100% { background: transparent; } }
    @keyframes red-flash-anim { 0% { background: rgba(255, 0, 0, 0.8); } 100% { background: transparent; } }
    .success-trigger { animation: green-flash-anim 0.5s forwards; position: fixed; top:0; left:0; width:100vw; height:100vh; z-index:9999; pointer-events:none; }
    .error-trigger { animation: red-flash-anim 0.5s forwards; position: fixed; top:0; left:0; width:100vw; height:100vh; z-index:9999; pointer-events:none; }

    /* LOG FEED */
    .log-container {
        background: rgba(0, 0, 0, 0.5); border: 1px solid #00FF41;
        padding: 10px; height: 120px; overflow-y: auto;
        font-family: 'Courier New', monospace; color: #00FF41; margin-bottom: 20px;
    }

    /* VICTORY BOX */
    .one-of-a-kind {
        color: #00FF41; font-size: 65px !important; font-weight: bold;
        text-shadow: 0 0 20px #00FF41, 0 0 40px #00FF41;
        font-family: 'Courier New', monospace;
        text-align: center; margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if 'level' not in st.session_state:
    st.session_state.level = 0 
    st.session_state.history = [">>> M-CYBER TERMINAL READY..."]
    st.session_state.flash = None

# --- 3. STABLE AUDIO ENGINE ---
st.markdown("""
    <div id="cyber-audio-node">
        <iframe width="0" height="0" 
        src="https://www.youtube.com/embed/gdTl3Vi8vvY?autoplay=1&loop=1&playlist=gdTl3Vi8vvY&enablejsapi=1" 
        frameborder="0" allow="autoplay"></iframe>
    </div>
    <script>
        function playAudio() {
            var iframe = document.querySelector('iframe');
            if (iframe) {
                iframe.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
            }
        }
        window.parent.document.addEventListener('mousedown', playAudio, {once: true});
        window.parent.document.addEventListener('keydown', playAudio, {once: true});
    </script>
""", unsafe_allow_html=True)

# --- 4. GAME DATA ---
LEVEL_DATA = {
    1: {"q": "LEVEL 1: BIT-SHIFT. [2, 4, 16, 256, ?]", "a": "65536"},
    2: {"q": "LEVEL 2: M-CIPHER. [Sum of MEGHA: M13, E5, G7, H8, A1]", "a": "34"},
    3: {"q": "LEVEL 3: EFFICIENCY PROTOCOL. [Complexity of halving a sorted list?]", "a": "LOGN"},
    4: {"q": "LEVEL 4: LIFO STACK. [Order: M -> E -> G. Pop() once. Who is at the top?]", "a": "E"},
    5: {"q": "LEVEL 5: THE PARADOX. [(True XOR True) OR (False AND True)]", "a": "FALSE"},
}

# --- 5. LOGIC & LOADING SCREEN ---
def trigger_loading(message):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown(f"<h2 style='color:#00FF41; text-align:center;'>{message}</h2>", unsafe_allow_html=True)
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)
    placeholder.empty()

def check_logic():
    raw = st.session_state.input_box.strip().upper()
    clean = raw.replace(" ", "").replace("O(", "").replace(")", "")
    
    if st.session_state.level == 0 and clean == "START":
        trigger_loading("INITIALIZING CYBER CORE...")
        st.session_state.level = 1
        st.session_state.history.append(">> SECURITY OVERRIDDEN. COMMENCING.")
    
    elif 1 <= st.session_state.level <= 5:
        if clean == LEVEL_DATA[st.session_state.level]["a"]:
            st.session_state.flash = "success"
            trigger_loading(f"DECRYPTING LEVEL {st.session_state.level}...")
            st.session_state.level += 1
            st.session_state.history.append(f">> L{st.session_state.level-1} SECURED.")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f">> ACCESS DENIED: '{raw}'")
            
    elif st.session_state.level == 6 and clean == "2014":
        trigger_loading("SYNCING TIMELINE...")
        st.session_state.level = 7
        st.session_state.flash = "success"
    
    elif st.session_state.level == 7 and clean == "G-DRAGON":
        trigger_loading("VERIFYING SOVEREIGN IDENTITY...")
        st.session_state.level = 8
        st.session_state.flash = "success"

    st.session_state.input_box = ""

# --- 6. RENDER ---

if st.session_state.flash == "success":
    st.markdown('<div class="success-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None
elif st.session_state.flash == "error":
    st.markdown('<div class="error-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None

log_html = "".join([f"<div>{l}</div>" for l in st.session_state.history[::-1]])
st.markdown(f'<div class="log-container">{log_html}</div>', unsafe_allow_html=True)

if st.session_state.level == 0:
    st.markdown('<p class="intro-text">M-CYBER SECURITY TERMINAL</p>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#FFFF00;'>SYSTEM IDLE. TYPE 'START' TO BEGIN.</p>", unsafe_allow_html=True)
    st.text_input("", key="input_box", on_change=check_logic)

elif 1 <= st.session_state.level <= 5:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center;'>{LEVEL_DATA[st.session_state.level]['q']}</h1>", unsafe_allow_html=True)
    st.text_input("ENTER KEYCODE:", key="input_box", on_change=check_logic)

elif st.session_state.level == 6:
    st.markdown('<div class="danger-box-red"><h1>⚠️ ENCRYPTION LOCK: LEVEL 1 ⚠️</h1> <p>SYNC THE KING OF K-POP TIMELINE</p> <p>YEAR OF BIRTH + MONTH OF INFINITY + DAY OF DOUBLE-EIGHT</p></div>', unsafe_allow_html=True)
    st.text_input("SYNC CODE:", key="input_box", on_change=check_logic)

elif st.session_state.level == 7:
    st.markdown('<div class="danger-box-violet"><h1>🚨 FINAL GATE 🚨</h1><p>WHO IS THE ONE TRUE KING?</p></div>', unsafe_allow_html=True)
    st.text_input("AUTHORIZE:", key="input_box", on_change=check_logic)

elif st.session_state.level == 8:
    st.markdown(f"""
        <div style="border:10px solid #FFFF00; padding:50px; background:black; border-radius:30px; text-align:center;">
            <h1 style="color:#FFFF00; font-size:60px;">👑 MISSION ACCOMPLISHED</h1>
            <div class="one-of-a-kind">Yes, sir ONE OF A KIND 💸 🐉</div>
            <p style="color:#00FF41; font-size:20px;">SYSTEM SECURED. WELCOME HOME, G-DRAGON.</p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
    if st.button("RESTART"):
        st.session_state.level = 0
        st.rerun()
