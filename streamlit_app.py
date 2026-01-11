import streamlit as st
import time

# --- 1. CONFIGURATION & GOD-MODE STYLING ---
st.set_page_config(page_title="M-Cyber Terminal", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1a022d, #0d0208); background-attachment: fixed; }
    
    /* SCANLINE EFFECT */
    .stApp::before {
        content: " "; display: block; position: absolute; top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2; background-size: 100% 4px, 3px 100%; pointer-events: none;
    }

    /* FLASH EFFECTS */
    @keyframes green-pulse { 0% { background-color: #00FF41; } 100% { background-color: transparent; } }
    @keyframes red-pulse { 0% { background-color: #FF0000; } 100% { background-color: transparent; } }
    .success-flash { animation: green-pulse 0.8s ease-out; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; opacity: 0.3; }
    .error-flash { animation: red-pulse 0.8s ease-out; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; opacity: 0.3; }

    /* MAIN SYSTEM BOX */
    .block-container { border: 2px solid #00FF41; box-shadow: 0 0 20px #00FF41; background: rgba(13, 2, 8, 0.9); border-radius: 20px; padding: 40px !important; }
    
    /* INTEGRATED LOG BOX */
    .log-box { 
        background: rgba(0, 255, 65, 0.1); 
        border: 1px solid #00FF41; 
        padding: 15px; 
        height: 120px; 
        overflow-y: auto; 
        color: #00FF41; 
        font-family: 'Courier New', monospace;
        margin-bottom: 20px;
        border-radius: 10px;
    }

    /* TIMER STYLING */
    .timer-display { color: #FFFF00; font-size: 35px; text-align: right; font-family: monospace; text-shadow: 0 0 10px #FFFF00; font-weight: bold; margin-bottom: -20px;}

    /* START PROMPT */
    .start-hint {
        color: #FFFF00;
        font-family: 'Courier New', monospace;
        font-size: 22px;
        text-align: center;
        letter-spacing: 3px;
        text-shadow: 0 0 10px #FFFF00;
        padding: 10px;
        border: 1px dashed #FFFF00;
        width: 60%;
        margin: 20px auto;
    }

    .intro-text { color: #BC13FE !important; font-size: 50px !important; font-weight: bold; text-shadow: 3px 3px #00FF41; text-align: center; }
    
    /* BOSS LOCKS (REMAINS THE SAME) */
    .boss-lock { border: 4px solid #FF0000; padding: 30px; background: rgba(255, 0, 0, 0.1); border-radius: 15px; text-align: center; }
    .boss-title { color: #FF0000 !important; font-size: 35px !important; font-weight: bold; text-shadow: 0 0 20px #FF0000; letter-spacing: 5px; }

    .stTextInput > div > div > input { background-color: black !important; color: #FFFF00 !important; border: 2px solid #FFFF00 !important; font-size: 25px !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if 'level' not in st.session_state:
    st.session_state.level = 0 
    st.session_state.history = ["SYST: WAITING FOR START COMMAND..."]
    st.session_state.start_time = None
    st.session_state.flash = None
    st.session_state.end_time = None

LEVEL_DATA = {
    1: {"q": "LEVEL 1: BIT-SHIFT. [2, 4, 16, 256, ?]", "a": "65536"},
    2: {"q": "LEVEL 2: M-CIPHER. [Sum of MEGHA: M13, E5, G7, H8, A1]", "a": "34"},
    3: {"q": "LEVEL 3: EFFICIENCY PROTOCOL. [Complexity of halving a sorted list?]", "a": "LOGN"},
    4: {"q": "LEVEL 4: LIFO STACK. [Order: M -> E -> G. Pop() once. Who is at the top?]", "a": "E"},
    5: {"q": "LEVEL 5: THE PARADOX. [(True XOR True) OR (False AND True)]", "a": "FALSE"},
}

# --- 3. AUDIO ---
st.markdown("""
    <iframe width="0" height="0" src="https://www.youtube.com/embed/gdTl3Vi8vvY?autoplay=1&loop=1&playlist=gdTl3Vi8vvY" frameborder="0" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)

# --- 4. CORE LOGIC ---
def check_logic():
    raw = st.session_state.input_box.strip().upper()
    clean = raw.replace(" ", "").replace("O(", "").replace(")", "")
    
    if st.session_state.level == 0 and clean == "START":
        st.session_state.level = 1
        st.session_state.start_time = time.time()
        st.session_state.history.append(">> TERMINAL ONLINE. UPTIME TRACKING START.")
    
    elif 1 <= st.session_state.level <= 5:
        if clean == LEVEL_DATA[st.session_state.level]["a"]:
            st.session_state.level += 1
            st.session_state.flash = "success"
            st.session_state.history.append(f">> L{st.session_state.level-1} DECRYPTED SUCCESSFULLY.")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f">> ACCESS DENIED: {raw}")
            
    elif st.session_state.level == 6:
        if clean == "2014":
            st.session_state.level = 7
            st.session_state.flash = "success"
            st.session_state.history.append(">> TIMELINE SYNCED. FINAL GATE OPEN.")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f">> SYNC FAILED: {raw}")

    elif st.session_state.level == 7:
        if clean == "G-DRAGON":
            st.session_state.level = 8
            st.session_state.end_time = time.time()
            st.session_state.history.append(">> IDENTITY VERIFIED. MISSION ACCOMPLISHED.")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f">> SUBJECT UNKNOWN: {raw}")
    
    st.session_state.input_box = ""

# --- 5. RENDER UI ---

# Flash Effects
if st.session_state.flash == "success":
    st.markdown('<div class="success-flash"></div>', unsafe_allow_html=True)
    st.session_state.flash = None 
elif st.session_state.flash == "error":
    st.markdown('<div class="error-flash"></div>', unsafe_allow_html=True)
    st.session_state.flash = None 

# 1. INTEGRATED LOG FEED (Top of the Main System)
log_html = "".join([f"<p style='margin:0;'>{line}</p>" for line in st.session_state.history[::-1]])
st.markdown(f'<div class="log-box">{log_html}</div>', unsafe_allow_html=True)

# 2. MAIN SCREENS
if st.session_state.level == 0:
    st.markdown('<p class="intro-text">M-CYBER SECURITY TERMINAL</p>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#00FF41;'>ACCESS RESTRICTED</h2>", unsafe_allow_html=True)
    st.markdown('<div class="start-hint">ENTER COMMAND "START" TO INITIALIZE SYSTEM</div>', unsafe_allow_html=True)
    st.text_input("CMD>", key="input_box", on_change=check_logic)

elif 1 <= st.session_state.level <= 5:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center;'>{LEVEL_DATA[st.session_state.level]['q']}</h1>", unsafe_allow_html=True)
    st.text_input("KEYCODE>", key="input_box", on_change=check_logic)
    
elif st.session_state.level == 6:
    st.markdown("""
        <div class="boss-lock">
            <p class="boss-title">⚠️ ENCRYPTION LOCK: LEVEL 1 ⚠️</p>
            <p style='color: white; font-size: 20px;'>SYNC THE KING OF K-POP TIMELINE</p>
            <p style='color: #FF0000; font-weight: bold;'>YEAR OF BIRTH + MONTH OF INFINITY + DAY OF DOUBLE-EIGHT</p>
        </div>
    """, unsafe_allow_html=True)
    st.text_input("SYNC CODE>", key="input_box", on_change=check_logic)

elif st.session_state.level == 7:
    st.markdown("""
        <div class="boss-lock" style="border-color: #BC13FE; background: rgba(188, 19, 254, 0.1);">
            <p class="boss-title" style="color: #BC13FE; text-shadow: 0 0 20px #BC13FE;">🚨 FINAL IDENTITY GATE 🚨</p>
            <p style='color: white; font-size: 20px;'>SYSTEM CORE REACHED. VERIFY THE SOVEREIGN.</p>
            <p style='color: #BC13FE; font-weight: bold;'>WHO IS THE ONE TRUE KING?</p>
        </div>
    """, unsafe_allow_html=True)
    st.text_input("IDENTITY>", key="input_box", on_change=check_logic)

elif st.session_state.level == 8:
    final_time = round(st.session_state.end_time - st.session_state.start_time, 2)
    st.markdown(f"""
        <div style="text-align:center; border:8px double #FFFF00; padding:50px; border-radius:30px; background:black; box-shadow: 0 0 50px #FFFF00;">
            <h1 style="color:#FFFF00; font-size:60px;">👑 MISSION ACCOMPLISHED</h1>
            <p style="color:#FFFF00; font-size:30px; letter-spacing:10px;">WELCOME HOME, G-DRAGON.</p>
            <h2 style="color:#00FF41; border-top:1px solid #00FF41; padding-top:20px;">DECRYPTION TIME: {final_time}s</h2>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
    if st.button("REBOOT TERMINAL"):
        st.session_state.level = 0
        st.rerun()

# 3. CONTINUOUS LIVE TIMER (At the Bottom)
if st.session_state.level > 0 and st.session_state.level < 8:
    current_elapsed = round(time.time() - st.session_state.start_time, 1)
    st.markdown(f'<div class="timer-display">SYSTEM_UPTIME: {current_elapsed}s</div>', unsafe_allow_html=True)
    time.sleep(0.1)
    st.rerun()
