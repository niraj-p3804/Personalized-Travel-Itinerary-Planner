


"""Personalized Travel Itinerary Planner (Skill Wallet Capstone Project 4).

Production-ready Streamlit application featuring:
1. Configuration & User Preferences with Gemini/Groq & Demo Mode
2. Smart Destination Recommender based on budget, season, and travel mood
3. Day-by-Day Optimized Itinerary with Geographic Clustering & Budget Tracker
4. Vibe Customization & Dynamic Activity Swap (slot and day levels)
5. Simulated Database Persistence & Publication-Ready Offline PDF Guide
"""

import os
from datetime import date, timedelta
from dotenv import load_dotenv
import streamlit as st

# Automatically load API keys from .env file if available
load_dotenv()

# Set page configuration FIRST before any other streamlit call
st.set_page_config(
    page_title="Personalized Travel Itinerary Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from modules.config import (
    APP_NAME, APP_SUBTITLE, CAPSTONE_PROJECT,
    CURRENCIES, BUDGET_TIERS, PARTY_OPTIONS, PACE_OPTIONS,
    INTEREST_TAGS, DESTINATION_CATALOG
)
from modules.styles import get_custom_css
from modules.ai_engine import AIEngine
from modules.recommender import render_destination_recommender
from modules.itinerary_generator import render_itinerary_generator
from modules.vibe_customizer import render_vibe_customizer
from modules.trip_manager import render_trip_manager

# Inject custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Session State Initialization
# -----------------------------------------------------------------------------
if "active_tab_index" not in st.session_state:
    st.session_state["active_tab_index"] = 1  # Default to Itinerary Generator

if "pref_destination" not in st.session_state:
    st.session_state["pref_destination"] = "Tokyo, Japan"

if "pref_duration" not in st.session_state:
    st.session_state["pref_duration"] = 5

if "pref_budget" not in st.session_state:
    st.session_state["pref_budget"] = "Moderate"

if "pref_party" not in st.session_state:
    st.session_state["pref_party"] = "Couple"

if "pref_pace" not in st.session_state:
    st.session_state["pref_pace"] = "Moderate"

if "pref_interests" not in st.session_state:
    st.session_state["pref_interests"] = [
        "Street Food & Gastronomy", "Art & Architecture", "History & Heritage", "Photography Hotspots"
    ]

if "pref_currency" not in st.session_state:
    st.session_state["pref_currency"] = "USD"

# -----------------------------------------------------------------------------
# Sidebar: AI Configuration & Trip Preferences (Epic 3)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span style="font-size: 1.8rem;">✈️</span>
            <div>
                <div style="font-weight: 800; font-size: 1.15rem; color: #0F766E; line-height: 1.1;">Travel Planner</div>
                <div style="font-size: 0.72rem; color: #64748B; font-weight: 600;">Skill Wallet Capstone 4</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Module 1: AI Provider & Secure API Key
    st.markdown("### 🔑 AI Engine Configuration")
    provider = st.selectbox(
        "AI Intelligence Engine",
        options=["Demo Mode (Simulated AI / Offline)", "Google Gemini (Gemini 3.8 Flash)", "Groq (Llama-3.3 70B)"],
        index=0,
        help="Select your AI engine. Demo mode requires zero API keys and works 100% offline!"
    )

    api_key_val = ""
    demo_active = provider.startswith("Demo")

    if not demo_active:
        env_var_name = "GEMINI_API_KEY" if "Gemini" in provider else "GROQ_API_KEY"
        default_env = os.environ.get(env_var_name, "")
        api_key_val = st.text_input(
            f"{'Gemini' if 'Gemini' in provider else 'Groq'} API Key",
            value=default_env,
            type="password",
            placeholder=f"Paste {env_var_name} here...",
            help="Your key is never logged or stored outside this browser session."
        )

    clean_provider_name = "Gemini" if "Gemini" in provider else ("Groq" if "Groq" in provider else "Demo")
    ai_engine = AIEngine(
        provider=clean_provider_name,
        api_key=api_key_val,
        demo_mode=demo_active
    )

    # API Connection Test
    c_test1, c_test2 = st.columns([1.5, 2])
    with c_test1:
        if st.button("🔌 Test API", use_container_width=True):
            conn_res = ai_engine.test_connection()
            if conn_res["success"]:
                st.toast(conn_res["message"], icon="🟢")
            else:
                st.error(conn_res["message"])

    with c_test2:
        if demo_active:
            st.markdown('<span class="status-badge status-demo">🟡 Demo Mode (Offline)</span>', unsafe_allow_html=True)
        else:
            st.markdown(f'<span class="status-badge status-active">🟢 {clean_provider_name} Armed</span>', unsafe_allow_html=True)

    st.markdown("---")

    # Module 2: Comprehensive Trip Preferences Form
    st.markdown("### 🧭 Trip Preferences (Epic 3)")

    # Destination selector / text input
    dest_suggestions = [destination["name"] for destination in DESTINATION_CATALOG.values()]
    dest_suggestions.append("Custom Destination...")
    dest_choice = st.selectbox(
        "Destination or Open Vibe",
        options=dest_suggestions,
        index=0 if st.session_state["pref_destination"] not in dest_suggestions else dest_suggestions.index(st.session_state["pref_destination"])
    )

    if dest_choice == "Custom Destination...":
        custom_dest = st.text_input("Enter City, Country or Vibe", value=st.session_state["pref_destination"])
        selected_destination = custom_dest if custom_dest else "Tokyo, Japan"
    else:
        selected_destination = dest_choice

    st.session_state["pref_destination"] = selected_destination

    # Trip Duration
    duration_days = st.slider("Trip Duration (Days)", min_value=1, max_value=10, value=st.session_state["pref_duration"])
    st.session_state["pref_duration"] = duration_days

    # Travel Dates
    today = date.today()
    default_start = today + timedelta(days=14)
    travel_dates = st.date_input(
        "Travel Dates",
        value=(default_start, default_start + timedelta(days=duration_days - 1)),
        min_value=today
    )
    start_date_str = str(travel_dates[0]) if isinstance(travel_dates, (tuple, list)) and len(travel_dates) > 0 else str(default_start)

    # Budget Level
    budget_level = st.selectbox(
        "Budget Tier",
        options=list(BUDGET_TIERS.keys()),
        index=list(BUDGET_TIERS.keys()).index(st.session_state["pref_budget"]),
        format_func=lambda k: f"{BUDGET_TIERS[k]['icon']} {k} (${BUDGET_TIERS[k]['min_usd']}-${BUDGET_TIERS[k]['max_usd']}/day)"
    )
    st.session_state["pref_budget"] = budget_level

    # Travel Party
    party = st.selectbox(
        "Travel Party",
        options=list(PARTY_OPTIONS.keys()),
        index=list(PARTY_OPTIONS.keys()).index(st.session_state["pref_party"]),
        format_func=lambda p: f"{PARTY_OPTIONS[p]['icon']} {PARTY_OPTIONS[p]['label']}"
    )
    st.session_state["pref_party"] = party

    # Pace
    pace = st.select_slider(
        "Travel Pace",
        options=list(PACE_OPTIONS.keys()),
        value=st.session_state["pref_pace"]
    )
    st.session_state["pref_pace"] = pace

    # Display Currency
    currency = st.selectbox(
        "Currency Display",
        options=list(CURRENCIES.keys()),
        index=list(CURRENCIES.keys()).index(st.session_state["pref_currency"]),
        format_func=lambda c: f"{CURRENCIES[c]['symbol']} {c} ({CURRENCIES[c]['name']})"
    )
    st.session_state["pref_currency"] = currency

    # Interests
    selected_interests = st.multiselect(
        "Travel Interests",
        options=INTEREST_TAGS,
        default=st.session_state["pref_interests"]
    )
    st.session_state["pref_interests"] = selected_interests

    st.markdown("---")
    st.caption("✨ Developed for Skill Wallet Capstone Project 4 • Production-Ready SaaS Architecture")

# -----------------------------------------------------------------------------
# Main Application Content Area
# -----------------------------------------------------------------------------

# Hero Banner
st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-tag">SaaS Travel Platform • {CAPSTONE_PROJECT}</span>
        <h1 class="hero-title">{APP_NAME}</h1>
        <p class="hero-subtitle">
            {APP_SUBTITLE}. Eliminate transit fatigue with intelligent geographic clustering, dynamic activity hot-swapping, and 1-click publication-grade offline PDF field guides.
        </p>
    </div>
""", unsafe_allow_html=True)

# Tab Navigation (4 Core Modules)
tab_names = [
    "🧭 Tab 1: Smart Destination Recommender",
    "🗺️ Tab 2: Day-by-Day Optimized Itinerary",
    "⚡ Tab 3: Vibe Customization & Dynamic Activity Swap",
    "💼 Tab 4: Trip Management & Offline PDF Export"
]

# Render Tabs
tab1, tab2, tab3, tab4 = st.tabs(tab_names)

# Tab 1: Smart Destination Recommender
with tab1:
    render_destination_recommender(ai_engine=ai_engine, currency=currency)

# Tab 2: Day-by-Day Itinerary Generator
with tab2:
    render_itinerary_generator(
        ai_engine=ai_engine,
        destination=selected_destination,
        duration_days=duration_days,
        budget_level=budget_level,
        party=party,
        pace=pace,
        interests=selected_interests,
        currency=currency,
        start_date=start_date_str
    )

# Tab 3: Vibe Customization & Dynamic Activity Swap
with tab3:
    render_vibe_customizer(ai_engine=ai_engine, currency=currency)

# Tab 4: Trip Management & Offline PDF Export
with tab4:
    render_trip_manager(currency=currency)
