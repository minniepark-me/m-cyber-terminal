import streamlit as st
import time

# --- 1. CONFIGURATION & STYLING ---
st.set_page_config(page_title="M-Cyber Terminal", page_icon="🐉", layout="centered")

# Custom CSS for the "Deep Void" UI and Full-Screen Flashes
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0D0208;
        color: #00FF41;
        font-family: 'Courier New', monospace;
    }

    /* Input Box Styling */
    input {
        background-color: #0D0208 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
    }

    /* Success/Error Animations */
    @keyframes green-pulse {
        0% { background-color: #00FF41; }
        100% { background-color: #0D0208; }
    }
    @keyframes red-glitch {
        0% { background-color: #FF0000; }
        100% { background-color: #0D0208; }
    }

    .success-flash {
        animation: green-pulse 0.6s ease-out;
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: 999; pointer-events: none; opacity: 0.3;
    }
    .error-flash {
        animation: red-glitch 0.4s ease-out;
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: 999; pointer-events: none; opacity: 0.3;
    }
    
    .terminal-text { font-size: 18px; line-height: 1.6; }
    .boss-banner { color: #BC13FE; font-weight: bold; border: 2px solid #BC13FE; padding: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GAME STATE INITIALIZATION ---
if 'level' not in st.session_state:
    st.session_state.level = 1
    st.session_state.history = ["--- M-CYBER TERMINAL v2.0 ---", "SYST: CONNECTION ESTABLISHED.", "SYST: ACCESSING ENCRYPTED LAYERS..."]
    st.session_state.flash = None

# --- 3. THE ANSWERS DATASET ---
LEVEL_DATA = {
    1: {"q": "Level 1: BIT-SHIFT SEQUENCE. [2, 4, 16, 256, ?]", "a": "65536"},
    2: {"q": "Level 2: M-CIPHER. [Sum of MEGHA: M=13, E=5, G=7, H=8, A=1]", "a": "34"},
    3: {"q": "Level 3: COMPLEXITY PROTOCOL. [Big O of Binary Search? (Format: O(log n))]", "a": "O(log n)"},
    4: {"q": "Level 4: LIFO STACK. [Push(M), Push(E), Push(G), Pop(). Who is on top?]", "a": "E"},
    5: {"q": "Level 5: BOOLEAN PARADOX. [(True XOR True) OR (False AND True). (True/False?)]", "a": "False"},
}

# --- 4. GAME LOGIC ---
def process_input():
    user_val = st.session_state.user_input.strip()
    current_lvl = st.session_state.level
    
    if current_lvl <= 5:
        if user_val == LEVEL_DATA[current_lvl]["a"]:
            st.session_state.flash = "success"
            st.session_state.history.append(f"> {user_val}")
            st.session_state.history.append(f"[OK] Layer {current_lvl} Decrypted.")
            st.session_state.level += 1
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f"> {user_val}")
            st.session_state.history.append("[ERR] Invalid Key. Try Again.")
            
    elif current_lvl == 6: # Boss Level Phase 1
        if user_val == "41":
            st.session_state.flash = "success"
            st.session_state.history.append("> Authority Key Verified.")
            st.session_state.level = 7
        else:
            st.session_state.flash = "error"
            st.session_state.history.append("[ERR] Unauthorized Dragon Number.")

    elif current_lvl == 7: # Boss Level Phase 2
        if user_val.lower() == "g-dragon":
            st.session_state.level = 8
            st.session_state.history.append("--- SYSTEM REBOOT COMPLETE ---")
    
    st.session_state.user_input = "" # Clear input

# --- 5. UI DISPLAY ---
# Flash Effect Trigger
if st.session_state.flash == "success":
    st.markdown('<div class="success-flash"></div>', unsafe_allow_html=True)
    st.session_state.flash = None
elif st.session_state.flash == "error":
    st.markdown('<div class="error-flash"></div>', unsafe_allow_html=True)
    st.session_state.flash = None

# Terminal History
for line in st.session_state.history[-10:]: # Show last 10 lines
    st.markdown(f'<p class="terminal-text">{line}</p>', unsafe_allow_html=True)

# Current Question Display
if st.session_state.level <= 5:
    st.markdown(f"**{LEVEL_DATA[st.session_state.level]['q']}**")
elif st.session_state.level == 6:
    st.markdown('<div class="boss-banner">CRITICAL: ENTER DRAGON NUMBER (LVL 2 + 7)</div>', unsafe_allow_html=True)
elif st.session_state.level == 7:
    st.markdown('<div class="boss-banner">IDENTITY REQUIRED: WHO IS THE KING OF THE G-MATRIX?</div>', unsafe_allow_html=True)
elif st.session_state.level == 8:
    st.header("👑 M-CYBER REBOOTED")
    st.success("Welcome, G-Dragon. The system is yours.")
    st.balloons()

# Bottom Input CLI
if st.session_state.level < 8:
    st.text_input(f"M-Cyber@User:~$ ", key="user_input", on_change=process_input)
