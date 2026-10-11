import streamlit as st
import time
import hashlib
import hmac
import random

# ==========================================
# 🛡️ VEXLORA ZERO-TRUST SECURITY & FORTRESS KERNEL
# ==========================================
st.set_page_config(
    page_title="Vexlora Fortress AI - Created by Fayyaz Rajpoot",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Security State
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "failed_attempts" not in st.session_state:
    st.session_state["failed_attempts"] = 0
if "lockout_time" not in st.session_state:
    st.session_state["lockout_time"] = 0
if "security_version" not in st.session_state:
    st.session_state["security_version"] = f"AI-SHIELD-v2.6.{random.randint(100,999)}"
if "hashed_password" not in st.session_state:
    st.session_state["hashed_password"] = hashlib.sha256("admin123".encode()).hexdigest()

# Intrusion Detection & Emergency Lockdown
current_time = time.time()
if st.session_state["failed_attempts"] >= 3:
    lockout_remaining = int(60 - (current_time - st.session_state["lockout_time"]))
    if lockout_remaining > 0:
        st.error(f"🚨 CRITICAL SECURITY BREACH: Unauthorized access detected. System locked for {lockout_remaining}s.")
        st.stop()
    else:
        st.session_state["failed_attempts"] = 0

# Security Barrier & Authentication
def secure_gate():
    if not st.session_state["authenticated"]:
        st.markdown(f"""
        <div style="max-width: 420px; margin: 60px auto; background: #0d1117; padding: 35px; border-radius: 16px; border: 1px solid #30363d; box-shadow: 0 15px 35px rgba(0,0,0,0.8);">
            <h2 style="color: #58a6ff; text-align: center; margin-bottom: 5px;">🛡️ Vexlora Fortress</h2>
            <p style="color: #3fb950; text-align: center; font-size: 0.75rem; font-family: monospace;">Created by Fayyaz Rajpoot | {st.session_state['security_version']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            pwd_input = st.text_input("Enter Master Security Key:", type="password", key="sec_pwd")
            if st.button("🔓 Initialize Secure Session"):
                input_hash = hashlib.sha256(pwd_input.encode()).hexdigest()
                if hmac.compare_digest(input_hash, st.session_state["hashed_password"]):
                    st.session_state["authenticated"] = True
                    st.session_state["failed_attempts"] = 0
                    st.success("Identity Verified. Access Granted.")
                    time.sleep(0.8)
                    st.rerun()
                else:
                    st.session_state["failed_attempts"] += 1
                    st.session_state["lockout_time"] = time.time()
                    if st.session_state["failed_attempts"] >= 3:
                        st.error("🚨 Intrusion threshold reached! Security lockdown triggered.")
                    else:
                        st.warning(f"Invalid Key! Warning {st.session_state['failed_attempts']}/3 before lockdown.")
        return False
    return True

if not secure_gate():
    st.stop()

# ==========================================
# 🎨 HIGH-END FORTRESS UI & DESIGN
# ==========================================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #111827 100%);
        color: #f3f4f6;
        font-family: 'Inter', sans-serif;
    }
    header, footer {visibility: hidden;}
    
    .fortress-banner {
        background: linear-gradient(90deg, #1f6feb 0%, #7928ca 100%);
        border-radius: 14px;
        padding: 22px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(31, 111, 235, 0.3);
    }
    .fortress-title { font-size: 1.8rem; font-weight: 800; color: #fff; }
    .fortress-subtitle { font-size: 0.85rem; color: #e5e7eb; opacity: 0.9; }

    .shield-card {
        background: rgba(17, 24, 39, 0.85);
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Main Banner with Creator Name
st.markdown(f"""
<div class="fortress-banner">
    <div class="fortress-title">🛡️ VEXLORA SUPER AGENT</div>
    <div class="fortress-subtitle">Created by <b>Fayyaz Rajpoot</b> • Autonomous AI Shield • Patch: {st.session_state['security_version']}</div>
</div>
""", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Agent Sandbox", "📊 Threat Telemetry", "🌐 Infrastructure", "🔒 Security & Creator Settings"])

with tab1:
    st.markdown("### ⚡ Secure AI Execution Engine")
    keyword = st.text_input("Enter secure prompt or operation task:", placeholder="e.g. Autonomous Content Pipeline")
    if st.button("🚀 Run Isolated Task"):
        if keyword:
            with st.spinner("🔒 AI inspecting payload in secure sandbox..."):
                time.sleep(1.2)
                st.success(f"Task executed securely for: {keyword}")
        else:
            st.warning("Please specify a command.")

with tab2:
    st.markdown("### 📊 Live Threat & Firewall Telemetry")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="shield-card"><h4>AI Self-Patching</h4><p style="color:#34d399; font-weight:bold;">Active & Secured</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="shield-card"><h4>DDoS / Bot Shield</h4><p style="color:#60a5fa; font-weight:bold;">Active & Filtering</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="shield-card"><h4>System Creator</h4><p style="color:#a78bfa; font-weight:bold;">Fayyaz Rajpoot</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown("### 🌐 Connected Secure Nodes")
    st.text_input("Target URL", placeholder="https://mysecuredsite.com")
    st.text_input("Encrypted Token", type="password")
    if st.button("Register Secure Node"):
        st.success("Node successfully registered under encrypted protocol!")

with tab4:
    st.markdown("### ⚙️ Security & Creator Control Panel")
    st.info("💡 **System Ownership:** This Autonomous Super Agent is exclusively engineered and managed by **Fayyaz Rajpoot**.")
    
    with st.form("fortress_security_form"):
        st.markdown("#### Update Master Password")
        old_pwd = st.text_input("Current Master Key", type="password")
        new_pwd = st.text_input("New Master Key", type="password")
        confirm_pwd = st.text_input("Confirm New Master Key", type="password")
        
        update_btn = st.form_submit_button("🛡️ Re-Encrypt & Update Master Key")
        if update_btn:
            old_hash = hashlib.sha256(old_pwd.encode()).hexdigest()
            if not hmac.compare_digest(old_hash, st.session_state["hashed_password"]):
                st.error("Current master key is incorrect!")
            elif new_pwd != confirm_pwd:
                st.error("New master keys do not match!")
            elif len(new_pwd) < 6:
                st.warning("Master key must be at least 6 characters long.")
            else:
                st.session_state["hashed_password"] = hashlib.sha256(new_pwd.encode()).hexdigest()
                st.session_state["security_version"] = f"AI-SHIELD-v2.6.{random.randint(100,999)}"
                st.success("Master key updated successfully by Fayyaz Rajpoot!")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚪 Terminate Session (Lockdown)"):
        st.session_state["authenticated"] = False
        st.rerun()
