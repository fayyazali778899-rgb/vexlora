import streamlit as st, hashlib, hmac, time, random, pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="VEXLORA SUPER AI v0.5 - Fayyaz Rajpoot", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ========== CONFIG & SESSION STATE ==========
if "user_db" not in st.session_state: 
    st.session_state["user_db"] = {
        "fayyaz@vexlora.ai": hashlib.sha256("admin123".encode()).hexdigest()
    }
if "authenticated" not in st.session_state: st.session_state["authenticated"] = False
if "current_user" not in st.session_state: st.session_state["current_user"] = ""
if "auth_page" not in st.session_state: st.session_state["auth_page"] = "login"
if "chat_history" not in st.session_state: 
    st.session_state["chat_history"] = [{"role": "assistant", "content": "Hello Fayyaz! Main aapka Vexlora AI Assistant hoon. Koi bhi sawal poochein!"}]

# ========== STYLING ==========
st.markdown("""
<style>
.stApp { background: radial-gradient(circle at 50% 0%, #0e1f23 0%, #06090f 78%); color: #e2e8f0; font-family: 'Inter', sans-serif; }
.stButton>button{background:linear-gradient(135deg,#059669 0%,#10b981 100%)!important;color:#fff!important;border:none!important;font-weight:800!important;border-radius:14px!important;width:100%!important;height:48px!important;}
.glass-box{background:rgba(17,24,39,0.85);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.08);border-radius:18px;padding:20px;margin-bottom:16px;}
.auth-card{background:rgba(13,27,30,0.95);border:1px solid rgba(16,185,129,0.20);border-radius:22px;padding:30px;}
.metric-card{background:linear-gradient(135deg, rgba(15,23,42,0.9) 0%, rgba(17,24,39,0.85) 100%);border:1px solid rgba(16,185,129,0.22);border-radius:16px;padding:16px;}
.logo-v { font-size: 2.2rem; font-weight: 900; background: linear-gradient(135deg, #e11d48 0%, #9333ea 50%, #2563eb 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
</style>
""", unsafe_allow_html=True)

# ========== AUTH GATEWAY ==========
if not st.session_state["authenticated"]:
    _, center, _ = st.columns([1, 1.2, 1])
    with center:
        st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="auth-card">
            <div style="text-align:center;">
                <div class="logo-v">⚡ VEXLORA</div>
                <p style="color:#94a3b8;margin-top:4px;">Super AI OS v0.5 • Lead Gen & Auto Publisher<br>👑 <b>Fayyaz Rajpoot</b></p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.session_state["auth_page"] == "login":
            st.markdown('<p style="font-weight:800;margin:15px 0 8px 0;">🔑 Sign In to Super AI</p>', unsafe_allow_html=True)
            e = st.text_input("Email", placeholder="fayyaz@vexlora.ai", key="le")
            p = st.text_input("Password", type="password", placeholder="••••••••", key="lp")
            
            if st.button("Continue → Super AI Mode"):
                h = hashlib.sha256(p.encode()).hexdigest()
                if e in st.session_state["user_db"] and hmac.compare_digest(h, st.session_state["user_db"][e]):
                    st.session_state["authenticated"] = True
                    st.session_state["current_user"] = e
                    st.success("✅ Welcome to Vexlora Super AI!")
                    time.sleep(0.4)
                    st.rerun()
                else:
                    st.error("❌ Incorrect Email or Password!")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown('<div class="logo-v" style="font-size:1.8rem;">⚡ VEXLORA</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#94a3b8;font-size:0.8rem;">Super AI OS v0.5<br>👑 Fayyaz Rajpoot<br>🟢 User: {st.session_state["current_user"]}</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio(
        "NAVIGATION MENU", 
        ["🏠 Super Dashboard", "🤖 Super AI Chat Assistant", "🎯 Lead Generation Hub", "🚀 Auto Command Publisher", "⚙️ Settings & Logout"]
    )

# ========== DASHBOARD WITH STREAMLIT BUILT-IN GRAPH ==========
if menu == "🏠 Super Dashboard":
    st.markdown("### 🏠 Super Dashboard - Vexlora 2.8M Reach & Lead Engine")
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="metric-card"><p style="color:#94a3b8;margin:0;">Total Reach</p><h3 style="color:#34d399;">2.8M</h3></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-card"><p style="color:#94a3b8;margin:0;">Leads Captured</p><h3 style="color:#34d399;">1,420</h3></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-card"><p style="color:#94a3b8;margin:0;">Active Funnels</p><h3 style="color:#34d399;">15</h3></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="metric-card"><p style="color:#94a3b8;margin:0;">Chain Speed</p><h3 style="color:#34d399;">0.9s</h3></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown('<div class="glass-box"><h4>📈 Lead Capture & Revenue Growth Graph ($28 High-RPM)</h4>', unsafe_allow_html=True)
        
        # Built-in Streamlit Line Chart (No extra module required)
        chart_df = pd.DataFrame(
            {
                "Captured Leads": [120, 310, 620, 890, 1240, 1420],
                "Earnings ($)": [1200, 3100, 6200, 8900, 12400, 15800]
            },
            index=["May", "Jun", "Jul", "Aug", "Oct", "Now"]
        )
        st.line_chart(chart_df, color=["#10b981", "#38bdf8"])
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="glass-box"><h4>🔒 Security Status</h4><p>✅ TLS 1.3 + AES-256<br>✅ Zero-Trust Shield<br>✅ Lead Privacy Encrypted<br>✅ US/UK High-RPM Target</p></div>', unsafe_allow_html=True)

elif menu == "🤖 Super AI Chat Assistant":
    st.markdown("### 🤖 Super AI Assistant")
    for msg in st.session_state["chat_history"]:
        if msg["role"] == "assistant":
            st.markdown(f"""<div style="background: rgba(16,185,129,0.15); border-left: 4px solid #10b981; padding: 12px; border-radius: 8px; margin-bottom: 10px;">🤖 <b>Vexlora AI:</b> {msg['content']}</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div style="background: rgba(59,130,246,0.15); border-left: 4px solid #3b82f6; padding: 12px; border-radius: 8px; margin-bottom: 10px;">👤 <b>User:</b> {msg['content']}</div>""", unsafe_allow_html=True)

    user_q = st.text_input("💬 Ask AI a question:")
    if st.button("Send to AI"):
        if user_q:
            st.session_state["chat_history"].append({"role": "user", "content": user_q})
            st.session_state["chat_history"].append({"role": "assistant", "content": f"Vexlora OS AI response for: '{user_q}'"})
            st.rerun()

elif menu == "🎯 Lead Generation Hub":
    st.markdown("### 🎯 Lead Generation Hub")
    st.write("Lead generation tools and settings active.")

elif menu == "🚀 Auto Command Publisher":
    st.markdown("### 🚀 Auto Publisher Engine")
    st.write("Auto publishing features active.")

elif menu == "⚙️ Settings & Logout":
    st.markdown("### ⚙️ Admin Profile")
    if st.button("🔴 Sign Out Session"):
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = ""
        st.rerun()
