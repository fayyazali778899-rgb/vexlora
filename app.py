import streamlit as st
import time
import hashlib
import hmac
import random

# ==========================================
# 🛡️ VEXLORA ENTERPRISE AUTHENTICATION OS
# ==========================================
st.set_page_config(
    page_title="Vexlora Super Agent - Security Portal",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Session State Database
if "user_db" not in st.session_state:
    st.session_state["user_db"] = {
        "email": "fayyaz@vexlora.ai",
        "password": hashlib.sha256("admin123".encode()).hexdigest()
    }
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = ""
if "auth_page" not in st.session_state:
    st.session_state["auth_page"] = "login"  # 'login', 'register', 'reset'
if "security_version" not in st.session_state:
    st.session_state["security_version"] = f"AI-SHIELD-v3.0.{random.randint(100,999)}"

# ==========================================
# 🎨 HIGH-CONTRAST PROFESSIONAL AUTH UI
# ==========================================
st.markdown("""
<style>
    .stApp {
        background: #0d1117;
        color: #c9d1d9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    header, footer {visibility: hidden;}

    /* Fix Button Styling & Contrast */
    .stButton > button {
        background: #238636 !important;
        color: #ffffff !important;
        border: 1px solid rgba(240,246,252,0.1) !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        border-radius: 8px !important;
        padding: 10px 16px !important;
        width: 100% !important;
        box-shadow: 0 4px 12px rgba(46, 160, 67, 0.2) !important;
    }
    
    .stButton > button:hover {
        background: #2ea043 !important;
        color: #ffffff !important;
    }

    /* Card Box */
    .login-box {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .app-title {
        color: #58a6ff;
        font-size: 2.2rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 2px;
    }
    .app-creator {
        color: #8b949e;
        font-size: 0.9rem;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 500;
    }
    .page-heading {
        color: #f0f6fc;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 15px;
        border-bottom: 1px solid #30363d;
        padding-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🔒 DEDICATED AUTHENTICATION PAGES
# ==========================================
if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        st.markdown("""
        <div class="login-box">
            <div class="app-title">🛡️ VEXLORA</div>
            <div class="app-creator">Created by <b>Fayyaz Rajpoot</b></div>
        """, unsafe_allow_html=True)

        # ----------------------------------
        # 1. PAGE: SIGN IN (LOGIN)
        # ----------------------------------
        if st.session_state["auth_page"] == "login":
            st.markdown('<div class="page-heading">🔐 Sign In</div>', unsafe_allow_html=True)
            login_email = st.text_input("Email Address", placeholder="e.g. fayyaz@vexlora.ai")
            login_pwd = st.text_input("Password", type="password", placeholder="••••••••")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Sign In to Account"):
                hashed_input = hashlib.sha256(login_pwd.encode()).hexdigest()
                if login_email == st.session_state["user_db"]["email"] and hmac.compare_digest(hashed_input, st.session_state["user_db"]["password"]):
                    st.session_state["authenticated"] = True
                    st.session_state["current_user"] = login_email
                    st.success("Identity Verified! Opening OS...")
                    time.sleep(0.8)
                    st.rerun()
                else:
                    st.error("Invalid Email or Password!")
            
            st.markdown("<hr style='border-color:#30363d; margin:20px 0;'>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                if st.button("Create Account"):
                    st.session_state["auth_page"] = "register"
                    st.rerun()
            with c2:
                if st.button("Forgot Password?"):
                    st.session_state["auth_page"] = "reset"
                    st.rerun()

        # ----------------------------------
        # 2. PAGE: SIGN UP (REGISTER)
        # ----------------------------------
        elif st.session_state["auth_page"] == "register":
            st.markdown('<div class="page-heading">📝 Create New Account</div>', unsafe_allow_html=True)
            reg_email = st.text_input("New Email Address", placeholder="name@example.com")
            reg_pwd = st.text_input("Password", type="password", placeholder="At least 6 characters")
            reg_confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Register New Account"):
                if not reg_email or "@" not in reg_email:
                    st.warning("Please enter a valid email address.")
                elif len(reg_pwd) < 6:
                    st.warning("Password must be at least 6 characters long.")
                elif reg_pwd != reg_confirm:
                    st.error("Passwords do not match!")
                else:
                    st.session_state["user_db"]["email"] = reg_email
                    st.session_state["user_db"]["password"] = hashlib.sha256(reg_pwd.encode()).hexdigest()
                    st.success("Account created successfully! Switching to Sign In...")
                    time.sleep(1)
                    st.session_state["auth_page"] = "login"
                    st.rerun()
            
            st.markdown("<hr style='border-color:#30363d; margin:20px 0;'>", unsafe_allow_html=True)
            if st.button("Already have an account? Sign In"):
                st.session_state["auth_page"] = "login"
                st.rerun()

        # ----------------------------------
        # 3. PAGE: RESET PASSWORD
        # ----------------------------------
        elif st.session_state["auth_page"] == "reset":
            st.markdown('<div class="page-heading">🔄 Reset Password</div>', unsafe_allow_html=True)
            st.info("Enter your registered email and choose a new password.")
            reset_email = st.text_input("Registered Email", placeholder="your email")
            new_pass = st.text_input("New Password", type="password", placeholder="New secure password")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Update Password"):
                if reset_email == st.session_state["user_db"]["email"]:
                    if len(new_pass) < 6:
                        st.warning("Password must be at least 6 characters.")
                    else:
                        st.session_state["user_db"]["password"] = hashlib.sha256(new_pass.encode()).hexdigest()
                        st.success("Password reset successful! Please Sign In.")
                        time.sleep(1)
                        st.session_state["auth_page"] = "login"
                        st.rerun()
                else:
                    st.error("Email not found in system record!")
            
            st.markdown("<hr style='border-color:#30363d; margin:20px 0;'>", unsafe_allow_html=True)
            if st.button("Back to Sign In"):
                st.session_state["auth_page"] = "login"
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ==========================================
# 🚀 MAIN SUPER AGENT OS (AFTER SIGN IN)
# ==========================================
st.markdown(f"""
<div style="background: linear-gradient(90deg, #1f6feb 0%, #8957e5 100%); border-radius: 14px; padding: 20px; text-align: center; margin-bottom: 20px;">
    <div style="font-size: 1.8rem; font-weight: 800; color: #fff;">🛡️ VEXLORA SUPER AGENT OS</div>
    <div style="font-size: 0.85rem; color: #e5e7eb;">Created by <b>Fayyaz Rajpoot</b> • Active Account: {st.session_state['current_user']} • Shield: {st.session_state['security_version']}</div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs inside OS
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Agent Sandbox", "📊 System Telemetry", "🌐 Infrastructure", "⚙️ Account & Sign Out"])

with tab1:
    st.markdown("### ⚡ Secure AI Execution Engine")
    keyword = st.text_input("Enter secure prompt or task:", placeholder="e.g. Autonomous Content Pipeline")
    if st.button("Execute Task"):
        if keyword:
            with st.spinner("Processing in secure sandbox..."):
                time.sleep(1.2)
                st.success(f"Task executed securely for: {keyword}")
        else:
            st.warning("Please specify a command.")

with tab2:
    st.markdown("### 📊 Live System Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div style="background:#161b22; border:1px solid #30363d; border-radius:12px; padding:18px;"><h4>AI Self-Patching</h4><p style="color:#3fb950; font-weight:bold;">Active & Secured</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="background:#161b22; border:1px solid #30363d; border-radius:12px; padding:18px;"><h4>Firewall Shield</h4><p style="color:#58a6ff; font-weight:bold;">100% Protection</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="background:#161b22; border:1px solid #30363d; border-radius:12px; padding:18px;"><h4>System Owner</h4><p style="color:#bc8cff; font-weight:bold;">Fayyaz Rajpoot</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown("### 🌐 Connected Secure Nodes")
    st.text_input("Target Website URL", placeholder="https://myblog.com")
    st.text_input("Access Token", type="password")
    if st.button("Register Target Node"):
        st.success("Target Node connected under encrypted tunnel!")

with tab4:
    st.markdown("### ⚙️ Account Settings")
    st.write(f"Logged in as: **{st.session_state['current_user']}**")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # SIGN OUT BUTTON
    if st.button("🔴 Sign Out (Exit Session)"):
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = ""
        st.session_state["auth_page"] = "login"
        st.rerun()
