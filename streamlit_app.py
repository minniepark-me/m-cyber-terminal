import streamlit as st
import time

# --- 1. CONFIGURATION & STYLING ---
st.set_page_config(page_title="M-Cyber God-Mode", page_icon="🐉", layout="wide")

# Initialize session state variables
if 'level' not in st.session_state:
    st.session_state.level = 0 
    st.session_state.history = [">>> M-CYBER TERMINAL READY..."]
    st.session_state.flash = None
    st.session_state.shake_counter = 0 # Unique key to force re-animation

# Determine if we should apply the shake class
shake_class = "shake-input" if st.session_state.flash == "error" else ""

st.markdown(f"""
    <style>
    /* MOBILE OPTIMIZATION LINE */
    @media (max-width: 768px) {{ .block-container {{ padding: 20px !important; margin-top: 10px; }} .one-of-a-kind {{ font-size: 35px !important; }} }}

    .stApp {{
        background: radial-gradient(circle, #1a022d, #0d0208);
        background-attachment: fixed;
        overflow: hidden;
    }}
    
    /* SHAKE ANIMATION */
    @keyframes rattle {{
        0% {{ transform: translateX(0); }}
        20% {{ transform: translateX(-15px); }}
        40% {{ transform: translateX(15px); }}
        60% {{ transform: translateX(-15px); }}
        80% {{ transform: translateX(15px); }}
        100% {{ transform: translateX(0); }}
    }}

    /* Applies shake specifically to the input field on error */
    .{shake_class} .stTextInput > div {{
        animation: rattle 0.3s ease-in-out !important;
        border: 2px solid #FF0000 !important;
        box-shadow: 0 0 20px #FF0000 !important;
    }}

    /* FULL SCREEN FLASHES */
    @keyframes red-flash-anim {{ 0% {{ background: rgba(255, 0, 0, 0.8); }} 100% {{ background: transparent; }} }}
    @keyframes green-flash-anim {{ 0% {{ background: rgba(0, 255, 65, 0.8); }} 100% {{ background: transparent; }} }}
    .error-trigger {{ animation: red-flash-anim 0.5s forwards; position: fixed; top:0; left:0; width:100vw; height:100vh; z-index:9999; pointer-events:none; }}
    .success-trigger {{ animation: green-flash-anim 0.5s forwards; position: fixed; top:0; left:0; width:100vw; height:100vh; z-index:9999; pointer-events:none; }}

    .block-container {{
        border: 2px solid #00FF41;
        box-shadow: 0 0 20px #00FF41, inset 0 0 10px #00FF41;
        padding: 50px !important;
        background: rgba(13, 2, 8, 0.9);
        border-radius: 20px;
        margin-top: 20px;
        z-index: 5;
    }}

    /* INPUT BOX STYLING */
    .stTextInput > div > div > input {{
        text-align: center !important;
        background-color: black !important;
        color: #00CCFF !important;
        border: 2px solid #00CCFF !important;
        font-size: 25px !important;
        height: 60px;
        text-shadow: 0 0 10px #00CCFF;
    }}

    .log-container {{
        background: rgba(0, 0, 0, 0.7); border: 1px solid #00FF41;
        padding: 15px; height: 120px; overflow-y: auto;
        font-family: 'Courier New', monospace; color: #00FF41;
        margin-bottom: 30px; border-radius: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. GAME LOGIC ---
LEVEL_DATA = {
    1: {"q": "LEVEL 1: BIT-SHIFT. [2, 4, 16, 256, ?]", "a": "65536"},
    2: {"q": "LEVEL 2: M-CIPHER. [Sum of MEGHA: M13, E5, G7, H8, A1]", "a": "34"},
    3: {"q": "LEVEL 3: EFFICIENCY PROTOCOL. [Complexity of halving a sorted list?]", "a": "LOGN"},
    4: {"q": "LEVEL 4: LIFO STACK. [Order: M -> E -> G. Pop() once. Who is at the top?]", "a": "E"},
    5: {"q": "LEVEL 5: THE PARADOX. [(True XOR True) OR (False AND True)]", "a": "FALSE"},
}

def check_logic():
    # Use the counter in the key name to grab the latest input
    current_key = f"input_L{st.session_state.level}_S{st.session_state.shake_counter}"
    raw = st.session_state[current_key].strip().upper()
    clean = raw.replace(" ", "").replace("O(", "").replace(")", "")
    
    if st.session_state.level == 0 and clean == "START":
        st.session_state.level = 1
        st.session_state.history.append(">> SECURITY OVERRIDDEN. COMMENCING.")
    elif 1 <= st.session_state.level <= 5:
        if clean == LEVEL_DATA[st.session_state.level]["a"]:
            st.session_state.flash = "success"
            st.session_state.level += 1
            st.session_state.history.append(f">> L{st.session_state.level-1} SECURED.")
        else:
            st.session_state.flash = "error"
            st.session_state.shake_counter += 1 # Forces input box to rebuild for shake
            st.session_state.history.append(f">> ACCESS DENIED: '{raw}'")
    # ... logic for level 6 and 7 omitted for brevity but follows same pattern

# --- 3. RENDER ---

# The id="{time.time()}" forces the browser to play the flash every single time
if st.session_state.flash == "error":
    st.markdown(f'<div class="error-trigger" id="{time.time()}"></div>', unsafe_allow_html=True)
elif st.session_state.flash == "success":
    st.markdown(f'<div class="success-trigger" id="{time.time()}"></div>', unsafe_allow_html=True)

log_html = "".join([f"<div style='margin-bottom:5px;'>{l}</div>" for l in st.session_state.history[::-1]])
st.markdown(f'<div class="log-container">{log_html}</div>', unsafe_allow_html=True)

# THE SHAKE WRAPPER
st.markdown(f'<div class="{shake_class}">', unsafe_allow_html=True)

# Dynamic key ensures the input field is "new" to the browser on every error
dynamic_key = f"input_L{st.session_state.level}_S{st.session_state.shake_counter}"

if st.session_state.level == 0:
    st.text_input("SYSTEM IDLE. TYPE 'START'", key=dynamic_key, on_change=check_logic)
elif 1 <= st.session_state.level <= 5:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center;'>{LEVEL_DATA[st.session_state.level]['q']}</h1>", unsafe_allow_html=True)
    st.text_input("ENTER KEYCODE:", key=dynamic_key, on_change=check_logic)

st.markdown('</div>', unsafe_allow_html=True)

# Reset flash after rendering so it doesn't shake on next correct action
if st.session_state.flash == "error":
    st.session_state.flash = None

if st.session_state.level == 8:
    st.balloons()
