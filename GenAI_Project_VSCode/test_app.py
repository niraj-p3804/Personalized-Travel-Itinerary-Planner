"""Comprehensive Automated Test Suite for Personalized Travel Itinerary Planner."""

import os
import json
from unittest.mock import patch
import requests
from modules.config import CURRENCIES, DESTINATION_CATALOG, BUDGET_TIERS
from modules.ai_engine import AIEngine
from modules.pdf_generator import generate_itinerary_pdf
from modules.trip_manager import _generate_turnkey_sample_trips

def run_tests():
    print("=== STARTING COMPREHENSIVE SYSTEM VERIFICATION ===")
    
    # Test 1: Config and Currencies
    print("\n[Test 1] Verifying Currencies & Catalogs...")
    assert "USD" in CURRENCIES
    assert "INR" in CURRENCIES
    assert "Tokyo" in DESTINATION_CATALOG
    for destination in (
        "Delhi", "Mumbai", "Kolkata", "Hyderabad", "Hampi", "Mysuru",
        "Agra", "Jodhpur", "Jaisalmer", "Pushkar", "Bikaner", "Mount Abu",
        "Shimla", "Dharamshala", "Dalhousie", "Spiti Valley", "Srinagar",
        "Gulmarg", "Pahalgam", "Gangtok", "Darjeeling", "Shillong",
        "Cherrapunji", "Kaziranga", "Guwahati", "Tawang", "Bhubaneswar",
        "Puri", "Konark", "Chennai", "Bengaluru", "Ooty", "Coorg",
        "Puducherry", "Andaman Islands", "Lakshadweep",
    ):
        assert destination in DESTINATION_CATALOG
        assert DESTINATION_CATALOG[destination]["country"] == "India"
        assert DESTINATION_CATALOG[destination]["clusters"]
    print("[PASS] Currencies and destination catalog intact.")

    # Test 2: AI Engine - Destination Recommender
    print("\n[Test 2] Testing Destination Recommender (Tab 1)...")
    engine = AIEngine(demo_mode=True)
    recs = engine.recommend_destinations(
        budget_level="Moderate",
        weather_season="Spring Blossom",
        travel_vibe="Cultural & Historical Heritage",
        currency="USD"
    )
    assert len(recs) == 3, f"Expected 3 recommendations, got {len(recs)}"
    assert "name" in recs[0]
    assert "match_score" in recs[0]
    print(f"[PASS] Recommended Top 3: {[r['name'] for r in recs]}")

    # Test 3: AI Engine - Day-by-Day Itinerary Generation
    print("\n[Test 3] Testing Day-by-Day Itinerary Generation (Tab 2)...")
    itinerary = engine.generate_itinerary(
        destination="Tokyo, Japan",
        duration_days=3,
        budget_level="Moderate",
        party="Couple",
        pace="Moderate",
        interests=["Street Food & Gastronomy", "Art & Architecture"],
        currency="USD"
    )
    assert len(itinerary["days"]) == 3, f"Expected 3 days, got {len(itinerary['days'])}"
    for day in itinerary["days"]:
        assert "cluster_name" in day
        assert "slots" in day
        assert len(day["slots"]) == 4, f"Expected 4 slots per day, got {len(day['slots'])}"
        for slot in day["slots"]:
            assert "cost_usd" in slot
            assert "cost_local" in slot
            assert "transit_to_next" in slot
    print(f"[PASS] Generated 3 days for {itinerary['destination']}. Total cost: ${itinerary['total_cost_usd']} USD.")

    # Test 4: AI Engine - Dynamic Activity Swap
    print("\n[Test 4] Testing Dynamic Activity Slot Swap (Tab 3)...")
    day1 = itinerary["days"][0]
    slot0 = day1["slots"][0]
    original_title = slot0["title"]
    swapped_slot = engine.swap_activity(
        destination="Tokyo, Japan",
        cluster_name=day1["cluster_name"],
        current_slot=slot0,
        swap_prompt="Swap for a peaceful traditional tea ceremony in a Zen garden",
        budget_level="Moderate",
        currency="USD"
    )
    assert swapped_slot["title"] != original_title
    print(f"[PASS] Swapped '{original_title}' -> '{swapped_slot['title']}'")

    # Test 5: AI Engine - Single Day Regeneration
    print("\n[Test 5] Testing Single Day Regeneration (Tab 3)...")
    regen_day = engine.regenerate_single_day(
        destination="Tokyo, Japan",
        day_number=2,
        day_vibe_request="Full day food safari and ramen tasting",
        budget_level="Moderate",
        currency="USD"
    )
    assert regen_day["day_number"] == 2
    assert len(regen_day["slots"]) == 4
    print(f"[PASS] Regenerated Day 2 with custom theme. Slots: {len(regen_day['slots'])}")

    # Test 6: ReportLab PDF Compilation
    print("\n[Test 6] Testing ReportLab Offline PDF Compilation (Tab 4)...")
    pdf_buffer = generate_itinerary_pdf(itinerary, currency="USD")
    pdf_bytes = pdf_buffer.getvalue()
    assert len(pdf_bytes) > 2000, f"PDF file size too small: {len(pdf_bytes)} bytes"
    print(f"[PASS] Generated PDF Guide successfully! Size: {len(pdf_bytes):,} bytes.")

    # Also test PDF with INR
    pdf_buffer_inr = generate_itinerary_pdf(itinerary, currency="INR")
    assert len(pdf_buffer_inr.getvalue()) > 2000
    print("[PASS] PDF Guide with INR currency compiled without error.")

    # Test 7: Turnkey Sample Trips Generation
    print("\n[Test 7] Testing Turnkey Sample Trips...")
    samples = _generate_turnkey_sample_trips(currency="USD")
    assert len(samples) >= 2
    print(f"[PASS] Generated {len(samples)} turnkey sample trips.")

    # Test 8: Gemini connection timeout handling
    print("\n[Test 8] Testing Gemini connection timeout handling...")
    gemini_engine = AIEngine(provider="Gemini", api_key="test-key", demo_mode=False)
    with patch("modules.ai_engine.requests.post", side_effect=requests.exceptions.ReadTimeout):
        connection = gemini_engine.test_connection()
    assert not connection["success"]
    assert "timed out" in connection["message"]
    print("[PASS] Gemini API timeouts return a clear, actionable message.")

    print("\n=== ALL 8 SYSTEM TESTS PASSED PERFECTLY ===")

if __name__ == "__main__":
    run_tests()
