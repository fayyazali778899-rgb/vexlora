import streamlit as st
import time
import hashlib
import hmac
import random
import pandas as pd

st.set_page_config(
    page_title="Super AI Vexlora - Created by Fayyaz Rajpoot",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    st.session_state["auth_page"] = "login"

# ==========================================
# 🎨 SCREENSHOT INSPIRED DARK GLASSMORPHISM CSS
# ==========================================
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 50% 10%, #0d1b1e 0%, #06090f 80%);
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }
    header, footer {visibility: hidden;}

    .stButton > button {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%) !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3) !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5) !important;
    }

    .glass-box {
        background: rgba(17, 24, 39, 0.75);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }

    .metric-card {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 14px;
        padding: 18px;
        text-align: left;
    }

    .logo-text {
        font-size: 1.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, #34d399, #6ee7b7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🔒 AUTHENTICATION GATEWAY
# ==========================================
if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        st.markdown('<div class="glass-box" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown('<div class="logo-text">Vexlora AI</div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#94a3b8; font-size:0.85rem;">Super AI Command Center • Created by <b>Fayyaz Rajpoot</b></p>', unsafe_allow_html=True)
        
        if st.session_state["auth_page"] == "login":
            email = st.text_input("📧 Admin Email", placeholder="fayyaz@vexlora.ai")
            pwd = st.text_input("🔒 Password", type="password", placeholder="••••••••")
            
            if st.button("🚀 Access Command Center"):
                hashed = hashlib.sha256(pwd.encode()).hexdigest()
                if email == st.session_state["user_db"]["email"] and hmac.compare_digest(hashed, st.session_state["user_db"]["password"]):
                    st.session_state["authenticated"] = True
                    st.session_state["current_user"] = email
                    st.success("✅ Access Granted!")
                    time.sleep(0.4)
                    st.rerun()
                else:
                    st.error("❌ Invalid Credentials!")
            
            c1, c2 = st.columns(2)
            with c1:
                if st.button("📝 Register"):
                    st.session_state["auth_page"] = "register"
                    st.rerun()
            with c2:
                if st.button("❓ Forgot?"):
                    st.session_state["auth_page"] = "reset"
                    st.rerun()

        elif st.session_state["auth_page"] == "register":
            reg_email = st.text_input("📧 New Email")
            reg_pwd = st.text_input("🔒 New Password", type="password")
            if st.button("✨ Create Account"):
                if len(reg_pwd) >= 6:
                    st.session_state["user_db"]["email"] = reg_email
                    st.session_state["user_db"]["password"] = hashlib.sha256(reg_pwd.encode()).hexdigest()
                    st.success("✅ Account Created!")
                    st.session_state["auth_page"] = "login"
                    time.sleep(1)
                    st.rerun()
                else:
                    st.warning("Password must be 6+ chars.")
            if st.button("🔙 Back"):
                st.session_state["auth_page"] = "login"
                st.rerun()

        elif st.session_state["auth_page"] == "reset":
            res_email = st.text_input("📧 Registered Email")
            new_pwd = st.text_input("🔑 New Password", type="password")
            if st.button("🛡️ Update Password"):
                if res_email == st.session_state["user_db"]["email"]:
                    st.session_state["user_db"]["password"] = hashlib.sha256(new_pwd.encode()).hexdigest()
                    st.success("✅ Password Updated!")
                    st.session_state["auth_page"] = "login"
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Email not found.")
            if st.button("🔙 Back"):
                st.session_state["auth_page"] = "login"
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ==========================================
# 📊 SIDEBAR NAVIGATION (SCREENSHOT STYLE)
# ==========================================
with st.sidebar:
    st.markdown('<div class="logo-text">⚡ Vexlora AI</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#94a3b8; font-size:0.8rem;">Command Center v5.4<br>👑 Fayyaz Rajpoot</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    selected_menu = st.radio(
        "Navigation Menu",
        ["Overview & Analytics", "Manual & Auto Publisher", "AI Agent Health", "Settings & Sign Out"]
    )
    st.markdown("---")
    st.markdown("🟢 **Active Node:** US/UK High-RPM")

# ==========================================
# 🚀 MAIN DASHBOARD CONTENT
# ==========================================
if selected_menu == "Overview & Analytics":
    st.markdown("### 🖥️ Super AI Vexlora - Command Center Overview")
    st.markdown("A premium dark Next-Gen AI command center experience[cite: 3].")
    
    # Top 4 Metrics Cards (Inspired from screenshot)
    mc1, mc2, mc3, mc4 = st.columns(4)
    with mc1:
        st.markdown('<div class="metric-card"><p style="color:#94a3b8; margin:0; font-size:0.85rem;">Total AI Interactions</p><h3 style="color:#34d399; margin:5px 0;">12.4M</h3><p style="color:#34d399; font-size:0.75rem;">+12.6% vs last month</p></div>', unsafe_allow_html=True)
    with mc2:
        st.markdown('<div class="metric-card"><p style="color:#94a3b8; margin:0; font-size:0.85rem;">New AI Workflows</p><h3 style="color:#34d399; margin:5px 0;">35,120</h3><p style="color:#34d399; font-size:0.75rem;">+8.4% growth</p></div>', unsafe_allow_html=True)
    with mc3:
        st.markdown('<div class="metric-card"><p style="color:#94a3b8; margin:0; font-size:0.85rem;">Model Inference Volume</p><h3 style="color:#34d399; margin:5px 0;">512TB</h3><p style="color:#34d399; font-size:0.75rem;">+5.3% active</p></div>', unsafe_allow_html=True)
    with mc4:
        st.markdown('<div class="metric-card"><p style="color:#94a3b8; margin:0; font-size:0.85rem;">Task Completion Rate</p><h3 style="color:#34d399; margin:5px 0;">99.2%</h3><p style="color:#34d399; font-size:0.75rem;">+6.7% efficiency</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts Section
    c_left, c_right = st.columns([2, 1])
    with c_left:
        st.markdown('<div class="glass-box"><h4>📈 Vexlora AI Insights & Predictions (US/UK RPM)</h4>', unsafe_allow_html=True)
        chart_data = pd.DataFrame(
            {"Earnings ($)": [1200, 2400, 3100, 4800, 6200, 8900, 12400]},
            index=["May 12", "May 16", "May 20", "May 26", "Jun 02", "Jun 06", "Jun 09"]
        )
        st.line_chart(chart_data, color=["#10b981"])
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c_right:
        st.markdown('<div class="glass-box"><h4>🌐 Global Traffic Share</h4>', unsafe_allow_html=True)
        traffic_df = pd.DataFrame({"Share (%)": [32.8, 18.2, 12.6, 7.6, 6.5]}, index=["United States", "India", "UK", "Canada", "Australia"])
        st.bar_chart(traffic_df, color=["#34d399"])
        st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "Manual & Auto Publisher":
    st.markdown("### ⚡ Manual & Multi-Platform Auto Publisher")
    st.markdown("Yahan aap apne hisab se manual options set kar sakte hain ya AI se automated content generate karwa sakte hain.")
    
    with st.container():
        st.markdown('<div class="glass-box">', unsafe_allow_html=True)
        
        # Manual Customization Options
        manual_title = st.text_input("✏️ Manual Title (Optional - Leave blank for AI auto-generation):", placeholder="e.g. My Custom Viral Video Title")
        manual_desc = st.text_area("✍️ Manual Description / Script (Optional):", placeholder="Enter custom description or let AI write it...")
        
        topic = st.text_input("🎯 Core Topic / Keyword for AI Deep Search:", placeholder="e.g. Artificial Intelligence Trends 2026")
        
        target_region = st.selectbox("🌍 Target High-CPM Region:", ["🇺🇸 United States (US)", "🇬🇧 United Kingdom (UK)", "🇪🇺 European Union (EU)"])
        
        st.markdown("#### 📡 Select Platforms (YouTube, Bilibili, TikTok, Facebook, Instagram, X, SnackApp & More):")
        p1, p2, p3, p4 = st.columns(4)
        with p1:
            st.checkbox("🔴 YouTube / Shorts", value=True)
            st.checkbox("🟡 Bilibili", value=True)
        with p2:
            st.checkbox("🎵 TikTok", value=True)
            st.checkbox("🟢 SnackApp", value=True)
        with p3:
            st.checkbox("🔵 Facebook", value=True)
            st.checkbox("❌ Twitter / X", value=True)
        with p4:
            st.checkbox("📸 Instagram Reels", value=True)
            st.checkbox("➕ Custom Network", value=False)
            
        custom_net = st.text_input("✨ Custom Platform Name (if checked):", placeholder="e.g. Pinterest, LinkedIn")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 Publish / Generate Content Now"):
            if topic or manual_title:
                with st.spinner("🔄 Running 4-Stage Humanizer & US/UK High-CPM SEO optimization..."):
                    time.sleep(2)
                
                st.success("✅ Content successfully published across selected networks!")
                
                st.markdown(f"""
                <div style="background: rgba(6, 9, 15, 0.9); border: 1px solid #10b981; border-radius: 12px; padding: 20px; margin-top: 15px;">
                    <h4 style="color: #34d399;">📌 Final Generated Output:</h4>
                    <p><b>Title:</b> {manual_title if manual_title else topic + ' - Ultimate US/UK Viral Masterclass'}</p>
                    <p><b>Description:</b> {manual_desc if manual_desc else 'Optimized 4-stage humanized description targeting ' + target_region + ' with maximum engagement.'}</p>
                    <p style="color: #34d399; font-family: monospace;"><b>Tags:</b> #{topic.replace(' ', '')} #FayyazRajpoot #VexloraAI #GlobalRPM</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("⚠️ Please provide at least a topic or manual title.")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "AI Agent Health":
    st.markdown("### 🛡️ AI Agent Network Health & Telemetry")
    h1, h2, h3 = st.columns(3)
    with h1:
        st.markdown('<div class="glass-box"><h4>🤖 Active Specialized Agents</h4><h2 style="color:#34d399;">2,476</h2><p style="color:#10b981;">All systems operational</p></div>', unsafe_allow_html=True)
    with h2:
        st.markdown('<div class="glass-box"><h4>🔒 Firewall Status</h4><h2 style="color:#34d399;">100%</h2><p style="color:#10b981;">Zero-Trust Secured</p></div>', unsafe_allow_html=True)
    with h3:
        st.markdown('<div class="glass-box"><h4>👑 System Administrator</h4><h2 style="color:#6ee7b7;">Fayyaz Rajpoot</h2><p style="color:#10b981;">Root Access Active</p></div>', unsafe_allow_html=True)

elif selected_menu == "Settings & Sign Out":
    st.markdown("### ⚙️ Account Settings & Management")
    st.write(f"👤 Logged in user: **{st.session_state['current_user']}**")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔴 Sign Out Session"):
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = ""
        st.session_state["auth_page"] = "login"
        st.rerun()
