"""Tab 1: Smart Destination Recommender (Epic 3).

Recommends top matching destinations based on budget, weather season, and travel mood.
"""

import streamlit as st
from typing import Dict, Any, List
from modules.config import TRAVEL_VIBES, BUDGET_TIERS, CURRENCIES
from modules.ai_engine import AIEngine

def render_destination_recommender(ai_engine: AIEngine, currency: str):
    """Render Tab 1 - Smart Destination Recommender UI."""
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h3 style="margin: 0; color: #0F766E;">🧭 Smart Destination Recommender</h3>
            <p style="color: #64748B; margin: 4px 0 0 0; font-size: 0.95rem;">
                Undecided on where to travel? Let our AI match your mood, budget, and season to the perfect destinations worldwide.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.2, 1.2, 1])
    
    with col1:
        vibe = st.selectbox(
            "✨ Travel Vibe & Atmosphere",
            options=TRAVEL_VIBES,
            index=0,
            help="Select the dominant emotion or setting you envision."
        )
    
    with col2:
        season = st.selectbox(
            "☀️ Weather & Travel Season",
            options=[
                "Spring Blossom (Mild & Floral)",
                "Summer Sun (Beach, Long Days & Festivals)",
                "Crisp Autumn (Golden Foliage & Wine Harvest)",
                "Winter Wonderland / Cozy Retreat"
            ],
            index=0
        )
        
    with col3:
        budget_tier = st.selectbox(
            "💰 Budget Comfort Level",
            options=list(BUDGET_TIERS.keys()),
            index=1,
            format_func=lambda x: f"{BUDGET_TIERS[x]['icon']} {x}"
        )

    btn_col1, btn_col2 = st.columns([1, 3])
    with btn_col1:
        find_btn = st.button("🔍 Recommend Top 3 Cities", use_container_width=True, type="primary")

    if find_btn or ("recommended_destinations" in st.session_state and st.session_state.get("recommended_destinations")):
        if find_btn:
            with st.spinner("Analyzing global climates, seasonal flights, and vibe clusters..."):
                recs = ai_engine.recommend_destinations(
                    budget_level=budget_tier,
                    weather_season=season,
                    travel_vibe=vibe,
                    currency=currency
                )
                st.session_state["recommended_destinations"] = recs

        recs = st.session_state.get("recommended_destinations", [])
        if recs:
            st.markdown("<hr style='margin: 24px 0; border: none; border-top: 1px solid #E2E8F0;'/>", unsafe_allow_html=True)
            st.markdown(f"#### 🎯 Top 3 Curated Matches for **{vibe.split('&')[0].strip()}** in **{season.split('(')[0].strip()}**")
            
            curr_sym = CURRENCIES.get(currency, {"symbol": "$"}).get("symbol", "$")

            for idx, dest in enumerate(recs):
                score = dest.get("match_score", 95)
                daily_spend = dest.get("estimated_daily_spend", 100)
                daily_usd = dest.get("estimated_daily_spend_usd", 100)
                
                with st.container():
                    st.markdown(f"""
                        <div class="city-card">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                                <div>
                                    <span style="font-size: 0.8rem; font-weight: 700; color: #0D9488; text-transform: uppercase;">Top Pick #{idx+1}</span>
                                    <h3 style="margin: 2px 0 4px 0; font-size: 1.45rem; color: #0F172A;">{dest.get('name')}</h3>
                                    <div style="font-size: 0.9rem; color: #64748B; font-weight: 500;">{dest.get('vibe_headline', '')}</div>
                                </div>
                                <div style="text-align: right;">
                                    <span style="background: #ECFDF5; color: #059669; font-weight: 800; font-size: 0.95rem; padding: 5px 12px; border-radius: 9999px; border: 1px solid #A7F3D0;">
                                        ★ {score}% Match
                                    </span>
                                    <div style="font-size: 0.82rem; color: #64748B; margin-top: 6px;">
                                        Est. {curr_sym}{daily_spend:,} / day <span style="color:#94A3B8;">(${daily_usd} USD)</span>
                                    </div>
                                </div>
                            </div>
                            
                            <p style="color: #334155; font-size: 0.92rem; line-height: 1.5; margin: 10px 0 12px 0;">
                                {dest.get('why_perfect')}
                            </p>
                            
                            <div style="margin-bottom: 12px;">
                                {''.join([f'<span class="highlight-pill">✓ {tag}</span>' for tag in dest.get('highlight_tags', [])])}
                            </div>
                            
                            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.82rem; color: #64748B; border-top: 1px dashed #E2E8F0; padding-top: 10px;">
                                <div><strong>Optimal Window:</strong> {dest.get('best_season_tip', 'All year')}</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

                    c_act1, c_act2 = st.columns([1.5, 4])
                    with c_act1:
                        if st.button(f"✈️ Select {dest.get('name').split(',')[0]}", key=f"select_dest_{idx}", type="secondary"):
                            st.session_state["pref_destination"] = dest.get("name")
                            st.session_state["pref_budget"] = budget_tier
                            st.session_state["active_tab_index"] = 1
                            st.toast(f"Selected {dest.get('name')}! Switched to Itinerary Generator.", icon="🚀")
                            st.rerun()
