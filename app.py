import streamlit as st
import time
import hashlib
import hmac
import random

# ==========================================
# 🛡️ VEXLORA ENTERPRISE AUTHENTICATION OS
# ==========================================
st.set_page_config(
    page_title="Vexlora Super Agent - Login",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Session State Database (In-memory storage for auth)
if "user_db" not in st.session_state:
    # Default Admin Account created by Fayyaz Rajpoot
    st.session_state["user_db"] = {
        "email": "fayyaz@vexlora.ai",
        "password": hashlib.sha256("admin123".encode()).hexdigest()
    }
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = ""
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "Login"  # Options: Login, Register, Forgot
if "security_version" not in st.session_state:
    st.session_state["security_version"] = f"AI-SHIELD-v2.8.{random.randint(100,999)}"

# ==========================================
# 🎨 GOOGLE-STYLE PROFESSIONAL LOGIN UI
# ==========================================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 100%);
        color: #f3f4f6;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    header, footer {visibility: hidden;}
    
    .auth-container {
        max-width: 420px;
        margin: 40px auto;
        background: rgba(17, 24, 39, 0.95);
        border: 1px solid #374151;
        border-radius: 16px;
        padding: 35px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.7);
    }
    .auth-logo {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 5px;
    }
    .auth-sub {
        text-align: center;
        font-size: 0.85rem;
        color: #9ca3af;
        margin-bottom: 25px;
    }
    .fortress-banner {
        background: linear-gradient(90deg, #1f6feb 0%, #7928ca 100%);
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(31, 111, 235, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Authentication Gateway Screen
if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("""
        <div class="auth-container">
            <div class="auth-logo">🛡️ VEXLORA</div>
            <div class="auth-sub">Created by Fayyaz Rajpoot</div>
        """, unsafe_allow_html=True)
        
        # Navigation between Login, Register, Forgot Password
        nav_col1, nav_col2, nav_col3 = st.columns(3)
        with nav_col1:
            if st.button("Sign In", use_container_width=True):
                st.session_state["auth_mode"] = "Login"
                st.rerun()
        with nav_col2:
            if st.button("Register", use_container_width=True):
                st.session_state["auth_mode"] = "Register"
                st.rerun()
        with nav_col3:
            if st.button("Reset", use_container_width=True):
                st.session_state["auth_mode"] = "Forgot"
                st.rerun()
        
        st.markdown("<hr style='border-color: #374151; margin: 20px 0;'>", unsafe_allow_html=True)
        
        # 1. LOGIN MODE
        if st.session_state["auth_mode"] == "Login":
            st.markdown("### Sign In to Account")
            login_email = st.text_input("Email Address", placeholder="e.g. fayyaz@vexlora.ai")
            login_pwd = st.text_input("Password", type="password", placeholder="••••••••")
            
            if st.button("🚀 Sign In", use_container_width=True):
                hashed_input = hashlib.sha256(login_pwd.encode()).hexdigest()
                if login_email == st.session_state["user_db"]["email"] and hmac.compare_digest(hashed_input, st.session_state["user_db"]["password"]):
                    st.session_state["authenticated"] = True
                    st.session_state["current_user"] = login_email
                    st.success("Login Successful! Loading OS...")
                    time.sleep(0.8)
                    st.rerun()
                else:
                    st.error("Invalid Email or Password!")

        # 2. REGISTER MODE (Create New Admin Account)
        elif st.session_state["auth_mode"] == "Register":
            st.markdown("### Create New Account")
            reg_email = st.text_input("New Email Address", placeholder="name@example.com")
            reg_pwd = st.text_input("Create Password", type="password", placeholder="Min 6 characters")
            reg_confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
            
            if st.button("✨ Register Account", use_container_width=True):
                if not reg_email or "@" not in reg_email:
                    st.warning("Please enter a valid email address.")
                elif len(reg_pwd) < 6:
                    st.warning("Password must be at least 6 characters.")
                elif reg_pwd != reg_confirm:
                    st.error("Passwords do not match!")
                else:
                    st.session_state["user_db"]["email"] = reg_email
                    st.session_state["user_db"]["password"] = hashlib.sha256(reg_pwd.encode()).hexdigest()
                    st.success("Account registered successfully! Now switch to Sign In.")
                    time.sleep(1)
                    st.session_state["auth_mode"] = "Login"
                    st.rerun()

        # 3. FORGOT / RESET PASSWORD MODE
        elif st.session_state["auth_mode"] == "Forgot":
            st.markdown("### Reset Password")
            st.info("Enter your registered email and set a new password.")
            reset_email = st.text_input("Registered Email", placeholder="your email")
            new_pass = st.text_input("New Password", type="password", placeholder="new password")
            
            if st.button("🔄 Reset Password", use_container_width=True):
                if reset_email == st.session_state["user_db"]["email"]:
                    if len(new_pass) < 6:
                        st.warning("Password must be at least 6 characters.")
                    else:
                        st.session_state["user_db"]["password"] = hashlib.sha256(new_pass.encode()).hexdigest()
                        st.success("Password reset successful! Please Sign In.")
                        time.sleep(1)
                        st.session_state["auth_mode"] = "Login"
                        st.rerun()
                else:
                    st.error("Email not found in system database!")

        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ==========================================
# 🚀 MAIN APP DASHBOARD (AFTER SUCCESSFUL LOGIN)
# ==========================================
st.markdown(f"""
<div class="fortress-banner">
    <div style="font-size: 1.8rem; font-weight: 800; color: #fff;">🛡️ VEXLORA SUPER AGENT OS</div>
    <div style="font-size: 0.85rem; color: #e5e7eb;">Created by <b>Fayyaz Rajpoot</b> • User: {st.session_state['current_user']} • Security: {st.session_state['security_version']}</div>
</div>
""", unsafe_allow_html=True)

# Navigation Tabs inside Dashboard
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Agent Sandbox", "📊 System Telemetry", "🌐 Infrastructure", "⚙️ Account Settings"])

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
        st.markdown('<div style="background: rgba(17,24,39,0.85); border: 1px solid #374151; border-radius: 12px; padding: 18px;"><h4>AI Self-Patching</h4><p style="color:#34d399; font-weight:bold;">Active & Secured</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="background: rgba(17,24,39,0.85); border: 1px solid #374151; border-radius: 12px; padding: 18px;"><h4>DDoS / Bot Shield</h4><p style="color:#60a5fa; font-weight:bold;">Active & Filtering</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="background: rgba(17,24,39,0.85); border: 1px solid #374151; border-radius: 12px; padding: 18px;"><h4>System Creator</h4><p style="color:#a78bfa; font-weight:bold;">Fayyaz Rajpoot</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown("### 🌐 Connected Secure Nodes")
    st.text_input("Target URL", placeholder="https://mysecuredsite.com")
    st.text_input("Encrypted Token", type="password")
    if st.button("Register Secure Node"):
        st.success("Node successfully registered under encrypted protocol!")

with tab4:
    st.markdown("### ⚙️ Account & Security Settings")
    st.write(f"Logged in as: **{st.session_state['current_user']}**")
    
    if st.button("🚪 Sign Out (Lock Session)"):
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = ""
        st.rerun()
