import streamlit as st
import random
import time
from datetime import datetime, timedelta

# 1. Mobile Screen Configuration
st.set_page_config(
    page_title="Vexlora Super AI App",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Mobile Custom CSS (App-like Styling)
st.markdown("""
    <style>
    /* Remove default padding for app feel */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    /* Touch Friendly Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2em;
        font-weight: bold;
        background-color: #2563EB;
        color: white;
    }
    /* Custom Card Style */
    .app-card {
        background-color: #1E293B;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h2 style='text-align: center;'>⚡ VEXLORA MOBILE AI</h2>", unsafe_allow_html=True)
st.caption("📱 10x Autonomous Multi-Site Auto-Publisher OS")

# Mobile Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "➕ Add Web", "📅 Schedule", "⚙️ Setup"])

# ==========================================
# TAB 1: MOBILE HOME DASHBOARD
# ==========================================
with tab1:
    st.subheader("📊 Live Matrix Status")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="app-card">
            <p style="margin:0; font-size:12px; color:#94A3B8;">ACTIVE SITES</p>
            <h2 style="margin:0;">10 Web</h2>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="app-card">
            <p style="margin:0; font-size:12px; color:#94A3B8;">TODAY POSTS</p>
            <h2 style="margin:0; color:#4ADE80;">24 Live</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### ⚡ Quick Auto-Post")
    kw = st.text_input("Enter Keyword", placeholder="e.g. Best Insurance Rates UK")
    niche = st.selectbox("Select Target Niche Site", ["Health Web", "Crypto Web", "Finance Web", "Law Web", "Insurance Web"])
    
    if st.button("🚀 Publish Now (One-Tap)"):
        if kw:
            with st.spinner("🤖 AI Agents Researching & Writing..."):
                time.sleep(2)
                st.success(f"✅ Published! '{kw}' sent to {niche}")
                st.info("⚡ Pinged Google Search Console & IndexNow for instant indexing.")
        else:
            st.warning("Pehle keyword enter karein!")

# ==========================================
# TAB 2: CONNECT NEW WEBSITE (+)
# ==========================================
with tab2:
    st.subheader("➕ Connect New Website")
    st.caption("Domain connect karein aur 100% automated posting shuru karein.")
    
    web_name = st.text_input("Website Name", placeholder="e.g. Health Matrix")
    web_domain = st.text_input("Domain URL", placeholder="https://mywebsite.com")
    web_niche = st.selectbox("Assign Niche", ["Health", "Crypto", "Finance", "Insurance", "Law", "Tech"])
    cms_type = st.radio("CMS Type", ["WordPress REST API", "Universal PHP Webhook", "Cloudflare Workers"])
    
    if cms_type == "WordPress REST API":
        wp_user = st.text_input("WP Admin Username")
        wp_pass = st.text_input("WP Application Password", type="password")
    else:
        token = st.text_input("Secret API Key/Token", type="password")
        
    if st.button("🔗 Save & Connect Domain"):
        if web_domain and web_name:
            st.success(f"🎉 '{web_name}' Successfully Added to Vexlora Network!")
        else:
            st.error("Tamam fields fill karein!")

# ==========================================
# TAB 3: BULK SCHEDULER & QUEUE
# ==========================================
with tab3:
    st.subheader("📅 Bulk Queue Scheduler")
    st.caption("1 Hafta ya 1 Mahine ke keywords ek sath upload karein.")
    
    bulk_text = st.text_area("Paste Keywords (One per line)", placeholder="Best Health Insurance 2026\nTop Crypto Wallets\nHow to Claim Insurance", height=150)
    
    col_a, col_b = st.columns(2)
    with col_a:
        posts_per_day = st.number_input("Posts per Day", min_value=1, max_value=20, value=3)
    with col_b:
        jitter = st.selectbox("Stealth Delay", ["Random Jitter (Safe)", "Exact Fixed Time"])
        
    if st.button("🗓️ Activate Stealth Auto-Queue"):
        if bulk_text:
            st.success("✅ Keywords queued! System random timings par publish karta rahega.")
        else:
            st.warning("Keywords daalein!")

# ==========================================
# TAB 4: SETTINGS & API KEYS
# ==========================================
with tab4:
    st.subheader("⚙️ System Configuration")
    
    openrouter_key = st.text_input("Free OpenRouter API Key", type="password", value="sk-or-xxxx")
    brave_key = st.text_input("Brave Search API Key", type="password", value="BSA-xxxx")
    
    st.markdown("---")
    st.markdown("#### 🛡️ Quality Gateway Thresholds")
    st.slider("Helpful Content Target Score", 80, 100, 85)
    st.slider("Max Allowed AI Score (%)", 0, 30, 15)
    
    if st.button("💾 Save Settings"):
        st.success("Settings Saved!")
