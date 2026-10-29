"""Tab 3: Vibe Customization & Dynamic Activity Swap (Epic 4).

Allows selective single-slot swapping and single-day regeneration without
wiping the remaining itinerary, preserving geographic clustering.
"""

import streamlit as st
from typing import Dict, Any, List
from modules.config import CURRENCIES, BUDGET_TIERS
from modules.ai_engine import AIEngine

SWAP_PRESETS = [
    "🥦 Swap for an authentic vegetarian/vegan foodie gem",
    "🛍️ Swap for an outdoor artisan market & street food",
    "🌧️ Swap for a rainy-day indoor cultural museum/gallery",
    "🧒 Swap for a kid-friendly & interactive family experience",
    "⚡ Swap for an adrenaline/outdoor adventure activity",
    "💸 Swap for a budget-friendly/free scenic alternative",
    "✨ Swap for a high-end luxury/romantic sunset experience"
]

DAY_THEME_PRESETS = [
    "Relaxed Wellness, Thermal Spa & Tranquil Parks",
    "Street Food Safari & Local Craft Beverage Trail",
    "Hidden Speakeasies, Vintage Boutiques & Indie Arts",
    "Active Hiking & Coastal Panoramic Viewpoints",
    "Heritage Architecture, Cathedrals & Palace Tour"
]

def render_vibe_customizer(ai_engine: AIEngine, currency: str):
    """Render Tab 3 - Vibe Customization & Dynamic Activity Swap UI."""
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h3 style="margin: 0; color: #0F766E;">⚡ Vibe Customization & Dynamic Activity Swap</h3>
            <p style="color: #64748B; margin: 4px 0 0 0; font-size: 0.95rem;">
                Surgically replace individual slots or whole days based on your mood, dietary preferences, or weather changes — 
                <strong>without resetting or erasing your remaining trip</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    itinerary = st.session_state.get("current_itinerary")
    if not itinerary or not itinerary.get("days"):
        st.warning("⚠️ No active itinerary found. Please generate or load an itinerary from Tab 2 first.")
        if st.button("← Go to Tab 2 to Generate"):
            st.session_state["active_tab_index"] = 1
            st.rerun()
        return

    days = itinerary.get("days", [])
    day_options = [f"Day {d['day_number']}: {d.get('cluster_name', 'Hub')}" for d in days]
    
    col_day, col_mode = st.columns([1.5, 1.5])
    with col_day:
        selected_day_idx = st.selectbox(
            "📅 Select Target Day to Modify",
            options=range(len(days)),
            format_func=lambda i: day_options[i]
        )
    
    with col_mode:
        custom_mode = st.radio(
            "🛠️ Customization Mode",
            options=["Swap a Single Activity Slot", "Regenerate Entire Day Theme", "Manual Slot Fine-Tuning"],
            horizontal=True
        )

    target_day = days[selected_day_idx]
    destination = itinerary.get("destination", "Destination")
    budget_level = itinerary.get("budget_tier", "Moderate")
    curr_sym = CURRENCIES.get(currency, {"symbol": "$"}).get("symbol", "$")

    st.markdown("<hr style='margin: 16px 0; border: none; border-top: 1px solid #E2E8F0;'/>", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # Mode 1: Swap Single Activity Slot
    # -------------------------------------------------------------------------
    if custom_mode == "Swap a Single Activity Slot":
        slots = target_day.get("slots", [])
        slot_labels = [f"{s.get('slot_type')} ({s.get('time')}) — {s.get('title')[:35]}..." for s in slots]
        
        slot_idx = st.selectbox(
            "⏰ Select Slot to Replace",
            options=range(len(slots)),
            format_func=lambda i: slot_labels[i]
        )
        current_slot = slots[slot_idx]

        # Display Current Slot Card
        st.markdown(f"""
            <div style="background: #FFFBEB; border: 1px solid #FCD34D; border-radius: 10px; padding: 14px 18px; margin-bottom: 16px;">
                <div style="font-size: 0.75rem; font-weight: 700; color: #B45309; text-transform: uppercase;">Current Activity in Slot</div>
                <div style="font-size: 1.05rem; font-weight: 700; color: #78350F; margin: 3px 0;">{current_slot.get('title')}</div>
                <div style="font-size: 0.88rem; color: #92400E;">{current_slot.get('description')}</div>
                <div style="font-size: 0.82rem; color: #B45309; margin-top: 4px;">
                    📍 Cluster: <strong>{target_day.get('cluster_name')}</strong> | Est. Cost: {curr_sym}{current_slot.get('cost_local')} (${current_slot.get('cost_usd')} USD)
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("##### 💡 Choose Quick Swap Preset or Enter Custom Vibe:")
        preset_choice = st.selectbox("Quick Preset Inspirations", options=["-- Custom Prompt (Enter below) --"] + SWAP_PRESETS)
        
        custom_swap_input = st.text_input(
            "Or Type Your Specific Swap Prompt:",
            value="" if preset_choice != "-- Custom Prompt (Enter below) --" else "Swap museum for an outdoor street market with local crafts",
            help="Describe what you want to do instead, retaining the same neighborhood cluster."
        )

        final_prompt = preset_choice if preset_choice != "-- Custom Prompt (Enter below) --" else custom_swap_input

        if st.button("🔄 Execute Activity Slot Swap", type="primary"):
            if not final_prompt:
                st.error("Please provide a swap request or select a preset.")
            else:
                with st.spinner(f"Curating replacement for '{current_slot.get('slot_type')}' in {target_day.get('cluster_name')}..."):
                    new_slot = ai_engine.swap_activity(
                        destination=destination,
                        cluster_name=target_day.get("cluster_name", destination),
                        current_slot=current_slot,
                        swap_prompt=final_prompt,
                        budget_level=budget_level,
                        currency=currency
                    )
                    # Replace slot in place
                    target_day["slots"][slot_idx] = new_slot
                    # Recompute costs across itinerary
                    itinerary = ai_engine._enrich_itinerary_costs(itinerary, currency)
                    st.session_state["current_itinerary"] = itinerary
                    st.toast(f"Slot updated to: {new_slot.get('title')}!", icon="✅")
                    st.rerun()

    # -------------------------------------------------------------------------
    # Mode 2: Regenerate Entire Day Theme
    # -------------------------------------------------------------------------
    elif custom_mode == "Regenerate Entire Day Theme":
        st.markdown(f"""
            <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 10px; padding: 14px 18px; margin-bottom: 16px;">
                <div style="font-size: 0.75rem; font-weight: 700; color: #166534; text-transform: uppercase;">Regenerate Entire Day {target_day.get('day_number')}</div>
                <div style="font-size: 0.92rem; color: #15803D;">
                    This will refresh all 4 slots for <strong>Day {target_day.get('day_number')}</strong> with a new theme, while keeping Day 1-{len(days)} before and after completely intact.
                </div>
            </div>
        """, unsafe_allow_html=True)

        theme_preset = st.selectbox("Popular Day Themes", options=["-- Custom Theme (Enter below) --"] + DAY_THEME_PRESETS)
        custom_theme_text = st.text_input(
            "Or Enter Custom Day Theme:",
            value="" if theme_preset != "-- Custom Theme (Enter below) --" else "Full wellness & scenic nature photography day",
            placeholder="e.g. Focus on historic libraries, jazz cafes, and underground music"
        )

        final_theme = theme_preset if theme_preset != "-- Custom Theme (Enter below) --" else custom_theme_text

        if st.button("🚀 Regenerate Day with This Theme", type="primary"):
            if not final_theme:
                st.error("Please enter or select a theme.")
            else:
                with st.spinner(f"Architecting new theme for Day {target_day.get('day_number')}..."):
                    new_day = ai_engine.regenerate_single_day(
                        destination=destination,
                        day_number=target_day.get("day_number", 1),
                        day_vibe_request=final_theme,
                        budget_level=budget_level,
                        currency=currency
                    )
                    # Preserve lat/lng if not provided
                    if "lat" not in new_day or new_day["lat"] == 0.0:
                        new_day["lat"] = target_day.get("lat", 0.0)
                        new_day["lng"] = target_day.get("lng", 0.0)
                    
                    days[selected_day_idx] = new_day
                    itinerary["days"] = days
                    itinerary = ai_engine._enrich_itinerary_costs(itinerary, currency)
                    st.session_state["current_itinerary"] = itinerary
                    st.toast(f"Day {target_day.get('day_number')} refreshed with theme: {final_theme}!", icon="✨")
                    st.rerun()

    # -------------------------------------------------------------------------
    # Mode 3: Manual Slot Fine-Tuning
    # -------------------------------------------------------------------------
    elif custom_mode == "Manual Slot Fine-Tuning":
        slots = target_day.get("slots", [])
        slot_labels = [f"{s.get('slot_type')} — {s.get('title')}" for s in slots]
        slot_idx = st.selectbox("Select Slot to Edit Manually", options=range(len(slots)), format_func=lambda i: slot_labels[i])
        current_slot = slots[slot_idx]

        with st.form(key=f"manual_edit_form_{selected_day_idx}_{slot_idx}"):
            m_title = st.text_input("Activity Title", value=current_slot.get("title", ""))
            m_desc = st.text_area("Description / Notes", value=current_slot.get("description", ""), height=80)
            m_loc = st.text_input("Specific Location / Venue", value=current_slot.get("location", ""))
            c_c1, c_c2 = st.columns(2)
            with c_c1:
                m_cost_usd = st.number_input("Cost (USD)", value=float(current_slot.get("cost_usd", 20.0)), step=1.0)
            with c_c2:
                m_transit = st.text_input("Transit To Next", value=current_slot.get("transit_to_next", ""))

            save_manual = st.form_submit_button("💾 Save Manual Edits", type="primary")
            if save_manual:
                rate = CURRENCIES.get(currency, {"rate": 1.0})["rate"]
                current_slot["title"] = m_title
                current_slot["description"] = m_desc
                current_slot["location"] = m_loc
                current_slot["cost_usd"] = m_cost_usd
                current_slot["cost_local"] = round(m_cost_usd * rate, 1)
                current_slot["transit_to_next"] = m_transit
                
                itinerary = ai_engine._enrich_itinerary_costs(itinerary, currency)
                st.session_state["current_itinerary"] = itinerary
                st.toast("Slot edits saved!", icon="✅")
                st.rerun()

    # Preview Modified Day Summary
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown(f"#### 👁️ Preview of Day {target_day.get('day_number')}: {target_day.get('cluster_name')}")
    for slot in target_day.get("slots", []):
        st.markdown(f"""
            <div style="background: white; border-left: 3px solid #0D9488; border-radius: 6px; padding: 10px 14px; margin-bottom: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                <strong>{slot.get('time')} [{slot.get('slot_type')}]:</strong> {slot.get('title')} — 
                <span style="color: #0D9488; font-weight: 700;">{curr_sym}{slot.get('cost_local')}</span>
                <div style="font-size: 0.85rem; color: #475569;">{slot.get('description')}</div>
            </div>
        """, unsafe_allow_html=True)
