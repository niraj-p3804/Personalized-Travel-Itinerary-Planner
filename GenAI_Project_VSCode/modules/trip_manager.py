"""Tab 4: Trip Management & Offline PDF Export (Epic 5).

Handles simulated database persistence (local JSON + session state), trip history viewer,
1-click PDF travel guide export, JSON import/export, and turnkey sample trips.
"""

import os
import json
import time
from datetime import datetime
import streamlit as st
from typing import Dict, Any, List
from modules.config import CURRENCIES, DESTINATION_CATALOG
from modules.pdf_generator import generate_itinerary_pdf

SAVED_TRIPS_FILE = "saved_trips.json"

def _load_saved_trips_from_disk() -> List[Dict[str, Any]]:
    """Load saved trips from local JSON file or return empty list."""
    if os.path.exists(SAVED_TRIPS_FILE):
        try:
            with open(SAVED_TRIPS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def _save_trips_to_disk(trips: List[Dict[str, Any]]) -> None:
    """Save trips list to local JSON file for persistence."""
    try:
        with open(SAVED_TRIPS_FILE, "w", encoding="utf-8") as f:
            json.dump(trips, f, indent=2, ensure_ascii=False)
    except Exception as e:
        st.error(f"Failed to persist trips to disk: {str(e)}")

def render_trip_manager(currency: str):
    """Render Tab 4 - Trip Management & Offline PDF Export."""
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h3 style="margin: 0; color: #0F766E;">💼 Trip Management & Offline PDF Export</h3>
            <p style="color: #64748B; margin: 4px 0 0 0; font-size: 0.95rem;">
                Persist itineraries to your simulated database, review trip history, or generate 
                <strong>1-Click publication-ready offline PDF field guides</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Initialize persistence in session_state if needed
    if "saved_trips" not in st.session_state:
        st.session_state["saved_trips"] = _load_saved_trips_from_disk()

    curr_itinerary = st.session_state.get("current_itinerary")
    curr_sym = CURRENCIES.get(currency, {"symbol": "$"}).get("symbol", "$")

    col_export, col_save = st.columns([1.6, 1.4])

    # -------------------------------------------------------------------------
    # Section 1: Offline PDF Export
    # -------------------------------------------------------------------------
    with col_export:
        st.markdown("#### 📄 1-Click Offline PDF Travel Guide")
        if curr_itinerary and curr_itinerary.get("days"):
            st.markdown(f"""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; padding: 16px; margin-bottom: 14px;">
                    <div style="font-weight: 700; color: #0F172A; font-size: 1.05rem;">
                        {curr_itinerary.get('trip_title', 'Active Itinerary')}
                    </div>
                    <div style="font-size: 0.85rem; color: #64748B; margin-top: 2px;">
                        📍 {curr_itinerary.get('destination')} • {len(curr_itinerary.get('days', []))} Days • Total: {curr_sym}{curr_itinerary.get('total_cost_local', 0):,.1f} (${curr_itinerary.get('total_cost_usd', 0):,.1f} USD)
                    </div>
                    <ul style="font-size: 0.82rem; color: #475569; margin: 8px 0 0 0; padding-left: 18px;">
                        <li>Emergency Contacts & Embassy Checklist included</li>
                        <li>Essential smart packing list tailored to climate</li>
                        <li>Geographic clustering tables with zero backtracking</li>
                        <li>Sequential time slots & itemized cost breakdown</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

            try:
                pdf_bytes = generate_itinerary_pdf(curr_itinerary, currency)
                dest_clean = curr_itinerary.get("destination", "trip").replace(" ", "_").replace(",", "")
                st.download_button(
                    label="📥 Download Publication-Ready PDF Guide",
                    data=pdf_bytes,
                    file_name=f"Travel_Guide_{dest_clean}.pdf",
                    mime="application/pdf",
                    type="primary",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Error compiling PDF: {str(e)}")

            # JSON Export option
            json_str = json.dumps(curr_itinerary, indent=2)
            st.download_button(
                label="💾 Export Itinerary as JSON",
                data=json_str,
                file_name=f"itinerary_{dest_clean}.json",
                mime="application/json",
                use_container_width=True
            )
        else:
            st.info("ℹ️ No active itinerary to export. Generate a trip in Tab 2 or load a saved trip below.")

    # -------------------------------------------------------------------------
    # Section 2: Save to Simulated Database
    # -------------------------------------------------------------------------
    with col_save:
        st.markdown("#### 💾 Save Current Trip to Database")
        if curr_itinerary and curr_itinerary.get("days"):
            default_name = curr_itinerary.get("trip_title", f"{curr_itinerary.get('destination')} Vacation")
            trip_name_input = st.text_input("Trip Name / Label", value=default_name)
            trip_notes = st.text_area("Personal Notes / Flight Ref", placeholder="e.g. Flight QR891, Hotel booked near Station...", height=70)
            
            if st.button("💾 Save Trip to History", type="secondary", use_container_width=True):
                new_record = {
                    "id": f"trip_{int(time.time())}",
                    "name": trip_name_input,
                    "destination": curr_itinerary.get("destination"),
                    "duration_days": len(curr_itinerary.get("days", [])),
                    "budget_tier": curr_itinerary.get("budget_tier", "Moderate"),
                    "total_cost_local": curr_itinerary.get("total_cost_local", 0.0),
                    "total_cost_usd": curr_itinerary.get("total_cost_usd", 0.0),
                    "currency": currency,
                    "notes": trip_notes,
                    "saved_at": datetime.now().strftime("%b %d, %Y - %I:%M %p"),
                    "itinerary": curr_itinerary
                }
                st.session_state["saved_trips"].insert(0, new_record)
                _save_trips_to_disk(st.session_state["saved_trips"])
                st.toast(f"Trip '{trip_name_input}' saved to database!", icon="✅")
                st.rerun()
        else:
            st.caption("Active itinerary required to save.")

        # JSON Import option
        st.markdown("##### 📤 Import Existing Itinerary JSON")
        uploaded_file = st.file_uploader("Upload JSON File", type=["json"], label_visibility="collapsed")
        if uploaded_file is not None:
            try:
                imported_data = json.load(uploaded_file)
                if "days" in imported_data:
                    st.session_state["current_itinerary"] = imported_data
                    st.toast("Itinerary loaded successfully from JSON!", icon="🚀")
                    st.rerun()
                else:
                    st.error("Invalid itinerary format: 'days' array missing.")
            except Exception as e:
                st.error(f"Failed to parse JSON: {str(e)}")

    st.markdown("<hr style='margin: 28px 0 20px 0; border: none; border-top: 1px solid #E2E8F0;'/>", unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # Section 3: Simulated Database Trip History Viewer
    # -------------------------------------------------------------------------
    st.markdown("### 🗄️ Saved Trips & History Viewer")
    saved_list = st.session_state.get("saved_trips", [])

    # Sample Trips Seeder if empty
    if not saved_list:
        st.info("Your trip archive is currently empty. You can save your active itinerary or seed turnkey sample trips.")
        if st.button("🌟 Load Turnkey Sample Trips (Tokyo, Paris, Bali)"):
            sample_trips = _generate_turnkey_sample_trips(currency)
            st.session_state["saved_trips"] = sample_trips
            _save_trips_to_disk(sample_trips)
            st.rerun()
        return

    # Render History Cards
    for idx, item in enumerate(saved_list):
        t_id = item.get("id", f"trip_{idx}")
        t_name = item.get("name", "Trip")
        t_dest = item.get("destination", "Destination")
        t_days = item.get("duration_days", 1)
        t_tier = item.get("budget_tier", "Moderate")
        t_cost_l = item.get("total_cost_local", 0.0)
        t_cost_u = item.get("total_cost_usd", 0.0)
        t_date = item.get("saved_at", "Recently")
        t_notes = item.get("notes", "")

        with st.container():
            st.markdown(f"""
                <div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div>
                            <span style="font-size: 0.75rem; font-weight: 700; color: #0D9488; text-transform: uppercase;">Saved Trip #{idx+1} • {t_date}</span>
                            <div style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin: 2px 0;">{t_name}</div>
                            <div style="font-size: 0.88rem; color: #475569;">
                                📍 <strong>{t_dest}</strong> • {t_days} Days • <span style="background: #F1F5F9; padding: 2px 6px; border-radius: 4px;">{t_tier} Tier</span>
                            </div>
                            {f'<div style="font-size: 0.82rem; color: #64748B; margin-top: 4px; font-style: italic;">📝 {t_notes}</div>' if t_notes else ''}
                        </div>
                        <div style="text-align: right;">
                            <div style="font-size: 1.15rem; font-weight: 800; color: #0F172A;">{curr_sym}{t_cost_l:,.1f}</div>
                            <div style="font-size: 0.78rem; color: #64748B;">(${t_cost_u:,.1f} USD)</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            b_col1, b_col2, b_col3, b_col4 = st.columns([1.2, 1.4, 1.2, 1.2])
            with b_col1:
                if st.button(f"📥 Load Active", key=f"load_{t_id}"):
                    st.session_state["current_itinerary"] = item["itinerary"]
                    st.toast(f"Loaded '{t_name}' as active itinerary!", icon="🚀")
                    st.session_state["active_tab_index"] = 1
                    st.rerun()

            with b_col2:
                # PDF quick download from history
                try:
                    p_bytes = generate_itinerary_pdf(item["itinerary"], currency)
                    st.download_button(
                        label=f"📄 PDF Guide",
                        data=p_bytes,
                        file_name=f"Guide_{t_name.replace(' ', '_')}.pdf",
                        mime="application/pdf",
                        key=f"dl_pdf_{t_id}"
                    )
                except Exception:
                    st.caption("PDF preview unavailable")

            with b_col3:
                if st.button(f"📋 Duplicate", key=f"dup_{t_id}"):
                    dup_trip = dict(item)
                    dup_trip["id"] = f"trip_{int(time.time())}"
                    dup_trip["name"] = f"Copy of {t_name}"
                    dup_trip["saved_at"] = datetime.now().strftime("%b %d, %Y - %I:%M %p")
                    st.session_state["saved_trips"].insert(idx + 1, dup_trip)
                    _save_trips_to_disk(st.session_state["saved_trips"])
                    st.rerun()

            with b_col4:
                if st.button(f"🗑️ Delete", key=f"del_{t_id}"):
                    st.session_state["saved_trips"].pop(idx)
                    _save_trips_to_disk(st.session_state["saved_trips"])
                    st.rerun()

def _generate_turnkey_sample_trips(currency: str) -> List[Dict[str, Any]]:
    """Seed ready-to-test sample trips for Tokyo, Paris, and Bali."""
    from modules.ai_engine import AIEngine
    engine = AIEngine(demo_mode=True)
    
    samples = []
    
    # 1. Tokyo
    tokyo_plan = engine.generate_itinerary(
        destination="Tokyo, Japan",
        duration_days=5,
        budget_level="Moderate",
        party="Couple",
        pace="Moderate",
        interests=["Street Food & Gastronomy", "Art & Architecture", "History & Heritage"],
        currency=currency
    )
    samples.append({
        "id": "sample_tokyo",
        "name": "Tokyo Spring Blossom Trail",
        "destination": "Tokyo, Japan",
        "duration_days": 5,
        "budget_level": "Moderate",
        "total_cost_local": tokyo_plan["total_cost_local"],
        "total_cost_usd": tokyo_plan["total_cost_usd"],
        "currency": currency,
        "notes": "Cherry blossom photography, Asakusa temples, and Tsukiji morning food stalls.",
        "saved_at": "Sample Preload",
        "itinerary": tokyo_plan
    })

    # 2. Paris
    paris_plan = engine.generate_itinerary(
        destination="Paris, France",
        duration_days=4,
        budget_level="Luxury",
        party="Solo",
        pace="Relaxed",
        interests=["Art & Architecture", "Museums & Galleries", "Coffee Culture"],
        currency=currency
    )
    samples.append({
        "id": "sample_paris",
        "name": "Parisian Bohemian & Art Odyssey",
        "destination": "Paris, France",
        "duration_days": 4,
        "budget_level": "Luxury",
        "total_cost_local": paris_plan["total_cost_local"],
        "total_cost_usd": paris_plan["total_cost_usd"],
        "currency": currency,
        "notes": "Montmartre cobblestones, Le Marais boutique galleries, and Seine sunset cruise.",
        "saved_at": "Sample Preload",
        "itinerary": paris_plan
    })

    return samples
