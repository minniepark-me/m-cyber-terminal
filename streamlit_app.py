import streamlit as st
import time

# --- 1. CONFIGURATION & HYPER-CYBER STYLING ---
st.set_page_config(page_title="M-Cyber God-Mode", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    /* 1. ANIMATED CYBER BACKGROUND */
    .stApp {
        background: radial-gradient(circle, #1a022d, #0d0208);
        background-attachment: fixed;
        overflow: hidden;
    }

    /* 2. SCANLINE EFFECT */
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

    /* 3. NEON GLOWING BORDER */
    .block-container {
        border: 2px solid #00FF41;
        box-shadow: 0 0 20px #00FF41, inset 0 0 10px #00FF41;
        padding: 50px !important;
        background: rgba(13, 2, 8, 0.85);
        border-radius: 20px;
        margin-top: 20px;
    }

    /* 4. GLITCH TEXT EFFECT */
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
    .intro-text {
        color: #BC13FE !important;
        font-size: 45px !important;
        font-weight: bold;
        text-shadow: 3px 3px #00FF41;
        animation: glitch 1s infinite alternate-reverse;
        text-align: center;
    }

    /* 5. INPUT BOX STYLING */
    .stTextInput > div > div > input {
        background-color: black !important;
        color: #FFFF00 !important;
        border: 2px solid #FFFF00 !important;
        box-shadow: 0 0 15px #FFFF00;
        font-size: 25px !important;
        height: 60px;
        text-align: center;
        letter-spacing: 3px;
    }

    /* 6. FLASH EFFECTS */
    @keyframes green-flash { 0% { background-color: #00FF41; opacity: 1; } 100% { background-color: transparent; opacity: 0; } }
    @keyframes red-flash { 0% { background-color: #FF0000; opacity: 1; } 100% { background-color: transparent; opacity: 0; } }
    .success-trigger { animation: green-flash 0.5s ease-out; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }
    .error-trigger { animation: red-flash 0.5s ease-out; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }

    /* 7. VICTORY BOX */
    .victory-box {
        border: 10px solid #FFFF00;
        padding: 60px;
        background: black;
        box-shadow: 0 0 50px #FFFF00, inset 0 0 30px #FFFF00;
        text-align: center;
        border-radius: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if 'level' not in st.session_state:
    st.session_state.level = 0 
    st.session_state.history = []
    st.session_state.start_time = None
    st.session_state.flash = None

# --- 3. RIDDLES & AUDIO ---
LEVEL_DATA = {
    1: {"q": "LEVEL 1: BIT-SHIFT. [2, 4, 16, 256, ?]", "a": "65536"},
    2: {"q": "LEVEL 2: M-CIPHER. [Sum of MEGHA: M13, E5, G7, H8, A1]", "a": "34"},
    3: {"q": "LEVEL 3: EFFICIENCY PROTOCOL. [Complexity of halving a sorted list?]", "a": "LOGN"},
    4: {"q": "LEVEL 4: LIFO STACK. [Order: M -> E -> G. Pop() once. Who is at the top?]", "a": "E"},
    5: {"q": "LEVEL 5: THE PARADOX. [(True XOR True) OR (False AND True)]", "a": "FALSE"},
}

# Music Loop (G-Dragon Coup D'Etat Instrumental)
st.markdown("""
    <iframe width="0" height="0" src="https://www.youtube.com/embed/gdTl3Vi8vvY?autoplay=1&loop=1&playlist=gdTl3Vi8vvY" frameborder="0" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)

# --- 4. LOGIC & LOADING BAR ---
def check_logic():
    raw = st.session_state.input_box.strip().upper()
    clean = raw.replace(" ", "").replace("O(", "").replace(")", "")
    
    if st.session_state.level == 0:
        if clean == "START":
            with st.spinner('INITIALIZING M-CYBER...'):
                time.sleep(1.5)
            st.session_state.level = 1
            st.session_state.start_time = time.time()
            st.session_state.history.append(">> INITIALIZING M-CYBER PROTOCOL...")
    
    elif 1 <= st.session_state.level <= 5:
        target = LEVEL_DATA[st.session_state.level]["a"]
        if clean == target:
            # Progress bar for "Decrypting" vibe
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
            
            st.session_state.level += 1
            st.session_state.flash = "success"
            st.session_state.history.append(f">> LEVEL {st.session_state.level-1} DECRYPTED.")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f">> ERROR: {raw} IS INCORRECT.")
            
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
        else:
            st.session_state.flash = "error"
    
    st.session_state.input_box = ""

# --- 5. RENDER ---
if st.session_state.flash == "success":
    st.markdown('<div class="success-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None
elif st.session_state.flash == "error":
    st.markdown('<div class="error-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None

# Sidebar History
st.sidebar.title("LOG_FEED")
for log in st.session_state.history:
    st.sidebar.markdown(f"**{log}**")

# MAIN GAMEPLAY
if st.session_state.level == 0:
    st.markdown('<p class="intro-text">M-CYBER SECURITY TERMINAL</p>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#00FF41;'>ACCESS RESTRICTED</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>TYPE 'START' TO INITIALIZE DECRYPTION SEQUENCES</p>", unsafe_allow_html=True)
    st.text_input("", key="input_box", on_change=check_logic)

elif 1 <= st.session_state.level <= 5:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center; text-shadow: 0 0 10px #00FF41;'>{LEVEL_DATA[st.session_state.level]['q']}</h1>", unsafe_allow_html=True)
    st.text_input("ENTER KEYCODE:", key="input_box", on_change=check_logic)
    
elif st.session_state.level == 6:
    st.markdown('<div class="boss-banner" style="text-align:center;">SYNC PROTOCOL: Sync the King of K-pop Timeline. <br>Year of Birth + Month of Infinity + Day of Double-Eight.</div>', unsafe_allow_html=True)
    st.text_input("DRAGON CODE:", key="input_box", on_change=check_logic)

elif st.session_state.level == 7:
    st.markdown('<div class="boss-banner" style="text-align:center;">FINAL IDENTITY GATE: WHO IS THE SOVEREIGN KING?</div>', unsafe_allow_html=True)
    st.text_input("NAME:", key="input_box", on_change=check_logic)

elif st.session_state.level == 8:
    total_time = round(st.session_state.end_time - st.session_state.start_time, 2)
    st.markdown(f"""
        <div class="victory-box">
            <h1 class="victory-text" style="font-size:80px;">👑 MISSION ACCOMPLISHED</h1>
            <p style="color: #FFFF00; font-size: 35px; letter-spacing: 10px; font-weight: bold;">WELCOME HOME, G-DRAGON.</p>
            <p style="color: #00FF41; font-size: 25px; border-top: 1px solid #00FF41; padding-top: 20px;">TOTAL DECRYPTION TIME: {total_time}s</p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
    if st.button("RESTART SYSTEM"):
        st.session_state.level = 0
        st.rerun()
