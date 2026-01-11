import streamlit as st
import time

# --- 1. CONFIGURATION & ADVANCED CYBER STYLING ---
st.set_page_config(page_title="M-Cyber Terminal", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(13, 2, 8, 0.95), rgba(13, 2, 8, 0.95)), 
                    url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        background-color: #0D0208;
        color: #00FF41;
        font-family: 'Courier New', monospace;
    }

    .stTextInput > div > div > input {
        background-color: rgba(0, 255, 65, 0.05) !important;
        color: #00FF41 !important;
        border: 2px solid #00FF41 !important;
        text-transform: uppercase;
        box-shadow: 0 0 15px #00FF41;
        font-size: 20px;
    }

    @keyframes green-flash { 0% { background-color: #00FF41; opacity: 0.8; } 100% { background-color: transparent; opacity: 0; } }
    @keyframes red-flash { 0% { background-color: #FF0000; opacity: 0.8; } 100% { background-color: transparent; opacity: 0; } }

    .success-trigger { animation: green-flash 0.4s ease-out; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }
    .error-trigger { animation: red-flash 0.4s ease-out; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }
    
    .victory-box {
        border: 8px double #FFFF00;
        background: rgba(0, 0, 0, 0.9);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 0 40px #FFFF00, inset 0 0 30px #FFFF00;
        animation: pulse-border 1.5s infinite alternate;
        margin-top: 50px;
    }

    @keyframes pulse-border { 0% { box-shadow: 0 0 20px #FFFF00; } 100% { box-shadow: 0 0 60px #FFFF00; } }

    .victory-text { color: #FFFF00; font-size: 60px; text-shadow: 0 0 25px #FFFF00; font-weight: bold; }
    .intro-text { color: #BC13FE; font-size: 22px; font-weight: bold; text-shadow: 0 0 10px #BC13FE; }
    .boss-banner { color: #BC13FE; font-weight: bold; border: 2px solid #BC13FE; padding: 20px; background: rgba(188, 19, 254, 0.1); box-shadow: 0 0 20px #BC13FE; font-size: 22px;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE & TIMER ---
if 'level' not in st.session_state:
    st.session_state.level = 0 
    st.session_state.history = []
    st.session_state.start_time = None
    st.session_state.flash = None

# --- 3. RIDDLES & HIDDEN MUSIC ---
# Riddles are now cryptic but logical
LEVEL_DATA = {
    1: {"q": "LEVEL 1: BIT-SHIFT. The sequence is 2, 4, 16, 256. What is the next square in the chain?", "a": "65536"},
    2: {"q": "LEVEL 2: M-CIPHER. Decode the name MEGHA (M=13, E=5, G=7, H=8, A=1). What is the total sum?", "a": "34"},
    3: {"q": "LEVEL 3: EFFICIENCY PROTOCOL. If an algorithm divides its search area in half with every step, what is its complexity notation?", "a": "LOGN"},
    4: {"q": "LEVEL 4: LIFO STACK. M, E, and G enter a narrow tunnel in that order. G leaves first. Who is now at the exit?", "a": "E"},
    5: {"q": "LEVEL 5: THE PARADOX. Two truths oppose each other (XOR), combined with a lie that shadows a truth (AND). Is the final system state True or False?", "a": "FALSE"},
}

# Hidden YouTube Music (G-Dragon Coup D'Etat Instrumental)
st.markdown("""
    <iframe width="0" height="0" src="https://www.youtube.com/embed/gdTl3Vi8vvY?autoplay=1&loop=1&playlist=gdTl3Vi8vvY" frameborder="0" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)

# --- 4. CORE LOGIC ---
def check_logic():
    # Input normalization: Upper case and remove spaces/brackets for the Complexity level
    raw_val = st.session_state.input_box.strip().upper()
    clean_val = raw_val.replace(" ", "").replace("O(", "").replace(")", "")
    
    if st.session_state.level == 0:
        if clean_val == "START":
            st.session_state.level = 1
            st.session_state.start_time = time.time()
            st.session_state.history.append("--- INITIALIZING MISSION ---")
    
    elif 1 <= st.session_state.level <= 5:
        target = LEVEL_DATA[st.session_state.level]["a"].replace(" ", "")
        if clean_val == target:
            st.session_state.level += 1
            st.session_state.flash = "success"
            st.session_state.history.append(f"> {raw_val} ... [DECRYPTED]")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f"> {raw_val} ... [DENIED]")
            
    elif st.session_state.level == 6:
        if clean_val == "2014":
            st.session_state.level = 7
            st.session_state.flash = "success"
            st.session_state.history.append("> {2014} ... [TIMELINE SYNCED]")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f"> {raw_val} ... [OUT OF SYNC]")

    elif st.session_state.level == 7:
        if clean_val == "G-DRAGON":
            st.session_state.level = 8
            st.session_state.end_time = time.time()
            st.session_state.history.append("> IDENTITY VERIFIED. KING DETECTED.")
        else:
            st.session_state.flash = "error"
            st.session_state.history.append(f"> {raw_val} ... [UNKNOWN SUBJECT]")
    
    st.session_state.input_box = ""

# --- 5. RENDER UI ---

if st.session_state.flash == "success":
    st.markdown('<div class="success-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None
elif st.session_state.flash == "error":
    st.markdown('<div class="error-trigger"></div>', unsafe_allow_html=True)
    st.session_state.flash = None

for log in st.session_state.history[-5:]:
    st.text(log)

if st.session_state.level == 0:
    st.markdown('<p class="intro-text">WELCOME TO M-CYBER SECURITY INTERFACE</p>', unsafe_allow_html=True)
    st.text("WARNING: HIGH-AUTHORITY ACCESS ONLY.")
    st.text("TYPE 'START' TO INITIALIZE DECRYPTION.")
    st.text_input("COMMAND:", key="input_box", on_change=check_logic)

elif 1 <= st.session_state.level <= 5:
    st.subheader(LEVEL_DATA[st.session_state.level]["q"])
    st.text_input("ENTER CODE:", key="input_box", on_change=check_logic)
    
elif st.session_state.level == 6:
    st.markdown('<div class="boss-banner">SYNC PROTOCOL: Sync the Dragon Timeline aka The King of K-Pop. <br>Year of Birth + Month of Infinity + Day of Double-Eight.</div>', unsafe_allow_html=True)
    st.text_input("DRAGON NUMBER:", key="input_box", on_change=check_logic)

elif st.session_state.level == 7:
    st.markdown('<div class="boss-banner">FINAL GATE: Enter the name of the Sovereign King.</div>', unsafe_allow_html=True)
    st.text_input("IDENTITY:", key="input_box", on_change=check_logic)

elif st.session_state.level == 8:
    total_time = round(st.session_state.end_time - st.session_state.start_time, 2)
    st.markdown(f"""
        <div class="victory-box">
            <div class="victory-text">👑 MISSION ACCOMPLISHED 👑</div>
            <p style="color: #FFFF00; font-size: 28px; letter-spacing: 5px;">WELCOME HOME, G-DRAGON.</p>
            <p style="color: #00FF41; font-size: 20px;">System restored in: {total_time} seconds</p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
    if st.button("REBOOT SYSTEM"):
        st.session_state.level = 0
        st.rerun()
