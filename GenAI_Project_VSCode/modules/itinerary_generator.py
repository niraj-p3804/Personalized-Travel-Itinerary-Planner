"""Tab 2: Day-by-Day Optimized Itinerary Generator (Epic 4).

Features sequential time slots, geographic clustering to prevent backtracking,
and running cumulative budget tracker in local currencies & USD.
"""

import streamlit as st
import pandas as pd
from typing import Dict, Any, List
from modules.config import CURRENCIES, BUDGET_TIERS, PARTY_OPTIONS
from modules.ai_engine import AIEngine

def render_itinerary_generator(
    ai_engine: AIEngine,
    destination: str,
    duration_days: int,
    budget_level: str,
    party: str,
    pace: str,
    interests: List[str],
    currency: str,
    start_date: str
):
    """Render Tab 2 - Day-by-Day Itinerary Generator."""
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h3 style="margin: 0; color: #0F766E;">🗺️ Day-by-Day Optimized Itinerary Generator</h3>
            <p style="color: #64748B; margin: 4px 0 0 0; font-size: 0.95rem;">
                AI-sequenced schedule with <strong>Intelligent Geographic Clustering</strong> to eliminate transit fatigue and prevent cross-city backtracking.
            </p>
        </div>
    """, unsafe_allow_html=True)

    curr_sym = CURRENCIES.get(currency, {"symbol": "$"}).get("symbol", "$")

    # Top Status Bar & Generation Action
    header_col1, header_col2, header_col3 = st.columns([2.5, 1.2, 1.3])
    
    with header_col1:
        st.markdown(f"""
            <div style="background: white; border: 1px solid #E2E8F0; border-radius: 10px; padding: 10px 16px;">
                <span style="font-size: 0.8rem; color: #64748B; font-weight: 600; text-transform: uppercase;">Active Trip Parameters</span>
                <div style="font-size: 1.05rem; font-weight: 700; color: #0F172A;">
                    📍 {destination} • {duration_days} Days • {party} • {budget_level}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with header_col2:
        st.markdown(f"""
            <div style="background: white; border: 1px solid #E2E8F0; border-radius: 10px; padding: 10px 16px;">
                <span style="font-size: 0.8rem; color: #64748B; font-weight: 600; text-transform: uppercase;">Target Daily Budget</span>
                <div style="font-size: 1.05rem; font-weight: 700; color: #0D9488;">
                    ${BUDGET_TIERS[budget_level]['min_usd']}-${BUDGET_TIERS[budget_level]['max_usd']} USD/day
                </div>
            </div>
        """, unsafe_allow_html=True)

    with header_col3:
        gen_button = st.button("✨ Generate Itinerary", type="primary", use_container_width=True)

    # Trigger generation
    if gen_button or ("current_itinerary" not in st.session_state and destination):
        with st.spinner(f"Architecting optimal geographic clusters for {destination} ({duration_days} days)..."):
            itinerary = ai_engine.generate_itinerary(
                destination=destination,
                duration_days=duration_days,
                budget_level=budget_level,
                party=party,
                pace=pace,
                interests=interests,
                currency=currency,
                start_date=start_date
            )
            st.session_state["current_itinerary"] = itinerary

    itinerary = st.session_state.get("current_itinerary")
    if not itinerary:
        st.info("👋 Select or enter your destination above and click **Generate Itinerary** to build your route.")
        return

    # Render Executive Summary Metrics
    total_usd = itinerary.get("total_cost_usd", 0.0)
    total_local = itinerary.get("total_cost_local", 0.0)
    days_count = len(itinerary.get("days", []))
    daily_avg_local = round(total_local / max(1, days_count), 1)
    daily_avg_usd = round(total_usd / max(1, days_count), 1)

    party_mult = PARTY_OPTIONS.get(party, {"multiplier": 1.0})["multiplier"]
    target_budget_usd = BUDGET_TIERS[budget_level]["max_usd"] * days_count * party_mult
    budget_usage_pct = min(100.0, round((total_usd / max(1.0, target_budget_usd)) * 100, 1))

    st.markdown(f"""
        <div class="metric-grid" style="margin-top: 18px;">
            <div class="metric-tile">
                <div class="metric-label">Estimated Total Cost</div>
                <div class="metric-value">{curr_sym}{total_local:,.1f}</div>
                <div class="metric-sub">${total_usd:,.1f} USD total</div>
            </div>
            <div class="metric-tile">
                <div class="metric-label">Daily Average Spend</div>
                <div class="metric-value">{curr_sym}{daily_avg_local:,.1f}</div>
                <div class="metric-sub">${daily_avg_usd:,.1f} USD / day</div>
            </div>
            <div class="metric-tile">
                <div class="metric-label">Geographic Clusters</div>
                <div class="metric-value">{days_count} Zones</div>
                <div class="metric-sub">Zero Backtracking Logic</div>
            </div>
            <div class="metric-tile">
                <div class="metric-label">Budget Tier Tracker</div>
                <div class="metric-value">{budget_usage_pct}%</div>
                <div class="metric-sub">{budget_level} Cap (${target_budget_usd:,.0f} USD)</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Budget Progress Bar
    bar_color = "normal" if budget_usage_pct <= 90 else "off"
    st.progress(budget_usage_pct / 100.0, text=f"Budget Allocation: {curr_sym}{total_local:,.1f} of ~{curr_sym}{(target_budget_usd * CURRENCIES[currency]['rate']):,.1f} target ({budget_level} Tier)")

    # Map visualization of geographic clusters
    map_points = []
    for d in itinerary.get("days", []):
        lat = d.get("lat")
        lng = d.get("lng")
        if lat and lng and (lat != 0.0 or lng != 0.0):
            map_points.append({
                "lat": float(lat),
                "lon": float(lng),
                "Day": f"Day {d.get('day_number')}: {d.get('cluster_name')}"
            })

    if map_points:
        with st.expander("📍 Geographic Cluster Map & Transit Hubs", expanded=False):
            df_map = pd.DataFrame(map_points)
            st.map(df_map, latitude="lat", longitude="lon", zoom=11)
            st.caption("Each point represents the central focal anchor of each day's localized itinerary.")

    st.markdown("<hr style='margin: 22px 0 16px 0; border: none; border-top: 1px solid #E2E8F0;'/>", unsafe_allow_html=True)
    st.markdown("### 🗓️ Detailed Day-by-Day Timeline")

    # Render day by day
    for day in itinerary.get("days", []):
        day_num = day.get("day_number", 1)
        cluster_name = day.get("cluster_name", "District Center")
        cluster_rationale = day.get("cluster_rationale", "")
        transit_tip = day.get("daily_transit_tip", "")
        day_cost_local = day.get("day_total_local", 0.0)
        day_cost_usd = day.get("day_total_usd", 0.0)
        cum_cost_local = day.get("cumulative_total_local", 0.0)
        cum_cost_usd = day.get("cumulative_total_usd", 0.0)

        with st.expander(f"📍 Day {day_num} — {cluster_name} | Daily Total: {curr_sym}{day_cost_local:,.1f} (${day_cost_usd:.1f} USD)", expanded=(day_num == 1)):
            # Geographic Cluster Rationale Banner
            st.markdown(f"""
                <div class="cluster-banner">
                    <div>
                        <div style="font-size: 0.75rem; text-transform: uppercase; color: #0D9488; font-weight: 700;">Day {day_num} Geographic Hub</div>
                        <div class="cluster-zone">📍 {cluster_name}</div>
                        <div style="font-size: 0.85rem; color: #334155; margin-top: 3px;">{cluster_rationale}</div>
                    </div>
                    <div style="text-align: right; min-width: 140px;">
                        <span style="font-size: 0.78rem; font-weight: 700; color: #475569; background: white; padding: 4px 10px; border-radius: 6px; border: 1px solid #CBD5E1;">
                            Cumul: {curr_sym}{cum_cost_local:,.0f} (${cum_cost_usd:,.0f})
                        </span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            if transit_tip:
                st.markdown(f"""
                    <div style="background: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 8px; padding: 8px 14px; margin-bottom: 14px; font-size: 0.84rem; color: #475569;">
                        🚆 <strong>Transit Advice:</strong> {transit_tip}
                    </div>
                """, unsafe_allow_html=True)

            # Slots Timeline
            for slot in day.get("slots", []):
                slot_type = slot.get("slot_type", "Sightseeing")
                time_str = slot.get("time", "")
                title = slot.get("title", "")
                desc = slot.get("description", "")
                location = slot.get("location", "")
                cost_l = slot.get("cost_local", 0.0)
                cost_u = slot.get("cost_usd", 0.0)
                transit = slot.get("transit_to_next", "")

                # Slot CSS class mapping
                st_class = "slot-morning"
                badge_class = "badge-morning"
                icon = "🌅"
                if "Lunch" in slot_type:
                    st_class = "slot-lunch"
                    badge_class = "badge-lunch"
                    icon = "🍽️"
                elif "Afternoon" in slot_type:
                    st_class = "slot-afternoon"
                    badge_class = "badge-afternoon"
                    icon = "🏛️"
                elif "Evening" in slot_type or "Dinner" in slot_type:
                    st_class = "slot-evening"
                    badge_class = "badge-evening"
                    icon = "🌙"

                st.markdown(f"""
                    <div class="slot-card {st_class}">
                        <div class="slot-header">
                            <div>
                                <span class="slot-time-badge {badge_class}">{icon} {slot_type} • {time_str}</span>
                                <span style="font-size: 0.8rem; color: #64748B; margin-left: 8px;">📌 {location}</span>
                            </div>
                            <div class="slot-cost">
                                {curr_sym}{cost_l:,.1f} <span style="color:#64748B; font-weight:400;">(${cost_u:.1f})</span>
                            </div>
                        </div>
                        <div class="slot-title">{title}</div>
                        <div class="slot-desc">{desc}</div>
                        {f'<div class="slot-transit">🚶‍♂️ <strong>Next Leg:</strong> {transit}</div>' if transit else ''}
                    </div>
                """, unsafe_allow_html=True)

    # Bottom Actions
    st.markdown("<br/>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.5, 3])
    with c1:
        if st.button("✨ Customize or Swap Activities in Tab 3 →", type="secondary", use_container_width=True):
            st.session_state["active_tab_index"] = 2
            st.rerun()
