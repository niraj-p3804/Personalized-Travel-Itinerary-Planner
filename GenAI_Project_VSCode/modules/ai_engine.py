"""AI Engine supporting Google Gemini, Groq, and a High-Fidelity Offline Demo Engine."""

import json
import re
import requests
from typing import Dict, Any, List, Optional
from modules.config import DESTINATION_CATALOG, BUDGET_TIERS, CURRENCIES, PARTY_OPTIONS, PACE_OPTIONS

class AIEngine:
    GEMINI_MODELS = ["gemini-3.8-flash", "gemini-3.6-flash"]

    def __init__(self, provider: str = "Demo", api_key: str = "", demo_mode: bool = True):
        self.provider = provider
        self.api_key = api_key.strip() if api_key else ""
        self.demo_mode = demo_mode or not self.api_key

    def test_connection(self) -> Dict[str, Any]:
        """Test the active API connection."""
        if self.demo_mode:
            return {"success": True, "message": "Demo Mode active (Offline synthetic AI ready)."}
        
        try:
            if self.provider == "Gemini":
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.GEMINI_MODELS[0]}:generateContent?key={self.api_key}"
                payload = {
                    "contents": [{"parts": [{"text": "Reply with only: OK"}]}]
                }
                res = requests.post(url, json=payload, timeout=30)
                if res.status_code == 200:
                    return {"success": True, "message": "Google Gemini API connected successfully!"}
                else:
                    return {"success": False, "message": f"Gemini error ({res.status_code}): {res.text[:150]}"}
            
            elif self.provider == "Groq":
                url = "https://api.groq.com/openai/v1/chat/completions"
                headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
                payload = {
                    "model": "llama-3.3-70b-versatile",
                    "messages": [{"role": "user", "content": "Reply with only: OK"}],
                    "max_tokens": 10
                }
                res = requests.post(url, headers=headers, json=payload, timeout=8)
                if res.status_code == 200:
                    return {"success": True, "message": "Groq API connected successfully!"}
                else:
                    return {"success": False, "message": f"Groq error ({res.status_code}): {res.text[:150]}"}
            else:
                return {"success": True, "message": "Demo Mode ready."}
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "message": f"Connection to {self.provider} timed out while waiting for the API response. Check your network connection and retry."
            }
        except Exception as e:
            return {"success": False, "message": f"Connection failed: {str(e)}"}

    def _query_gemini(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        """Query Gemini API with automatic fallback between supported Flash models."""
        models = self.GEMINI_MODELS
        last_error = None
        for model in models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={self.api_key}"
            payload = {
                "contents": [{"parts": [{"text": f"{system_prompt}\n\n{prompt}"}]}],
                "generationConfig": {
                    "temperature": 0.4,
                    "maxOutputTokens": 3500,
                    "responseMimeType": "application/json"
                }
            }
            try:
                res = requests.post(url, json=payload, timeout=25)
                if res.status_code == 200:
                    data = res.json()
                    candidates = data.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        if parts:
                            return parts[0].get("text", "")
                else:
                    last_error = res.text
            except Exception as e:
                last_error = str(e)
        return None

    def _query_groq(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        """Query Groq API with Llama-3.3-70b."""
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": system_prompt + "\nYou MUST reply with valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.4,
            "max_tokens": 3500,
            "response_format": {"type": "json_object"}
        }
        try:
            res = requests.post(url, headers=headers, json=payload, timeout=25)
            if res.status_code == 200:
                data = res.json()
                return data["choices"][0]["message"]["content"]
        except Exception:
            pass
        return None

    def _extract_json(self, raw_text: str) -> Optional[Any]:
        """Robustly parse JSON from markdown code fences or raw text."""
        if not raw_text:
            return None
        text = raw_text.strip()
        # Check for ```json ... ```
        match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
        if match:
            text = match.group(1).strip()
        try:
            return json.loads(text)
        except Exception:
            # Try to fix trailing commas
            cleaned = re.sub(r",\s*([\]}])", r"\1", text)
            try:
                return json.loads(cleaned)
            except Exception:
                return None

    # ==========================================
    # Tab 1: Smart Destination Recommender
    # ==========================================
    def recommend_destinations(self, budget_level: str, weather_season: str, travel_vibe: str, currency: str) -> List[Dict[str, Any]]:
        """Recommend top 3 destinations based on budget, season, and travel vibe."""
        if not self.demo_mode and self.api_key:
            system_prompt = "You are a master travel curator. Return a JSON object with a single key 'destinations' containing exactly 3 recommended cities."
            user_prompt = f"""
            Recommend top 3 world destinations matching:
            - Budget Level: {budget_level}
            - Weather / Travel Season: {weather_season}
            - Travel Vibe / Mood: {travel_vibe}
            - Preferred Display Currency: {currency}

            Return JSON format:
            {{
              "destinations": [
                {{
                  "name": "City, Country",
                  "match_score": 98,
                  "weather_summary": "Sunny with crisp breezes (22°C/72°F)",
                  "estimated_daily_spend": 120,
                  "estimated_daily_spend_usd": 120,
                  "currency": "{currency}",
                  "vibe_headline": "Short punchy travel slogan",
                  "highlight_tags": ["Iconic Landmark", "Street Food Haven", "Art District"],
                  "why_perfect": "2-3 sentences explaining why it fits this mood and season.",
                  "best_season_tip": "When to visit and packing note",
                  "lat": 35.6762,
                  "lng": 139.6503
                }}
              ]
            }}
            """
            raw = self._query_gemini(user_prompt, system_prompt) if self.provider == "Gemini" else self._query_groq(user_prompt, system_prompt)
            data = self._extract_json(raw) if raw else None
            if data and isinstance(data, dict) and "destinations" in data and len(data["destinations"]) >= 3:
                return data["destinations"][:3]

        # Robust High-Fidelity Demo Fallback for Destination Recommender
        return self._demo_destination_recommender(budget_level, weather_season, travel_vibe, currency)

    def _demo_destination_recommender(self, budget: str, season: str, vibe: str, currency: str) -> List[Dict[str, Any]]:
        rate = CURRENCIES.get(currency, {"rate": 1.0})["rate"]
        candidates = []
        for key, info in DESTINATION_CATALOG.items():
            score = 75
            # Vibe matching score
            for v in info["vibe_matches"]:
                if any(w in vibe.lower() for w in v.lower().split()):
                    score += 10
            # Budget matching score
            if info["budget_level"] == budget:
                score += 12
            else:
                score -= 5
            
            candidates.append((score, info))

        candidates.sort(key=lambda x: x[0], reverse=True)
        top3 = candidates[:3]

        results = []
        for rank, (score, info) in enumerate(top3):
            daily_usd = info["daily_cost_usd"]
            # Adjust slightly for budget tier
            if budget == "Budget":
                daily_usd = int(daily_usd * 0.75)
            elif budget == "Luxury":
                daily_usd = int(daily_usd * 1.8)
            daily_local = int(daily_usd * rate)

            results.append({
                "name": info["name"],
                "match_score": min(99, score + (3 - rank)),
                "weather_summary": f"Optimal season during {season} with comfortable sightseeing conditions.",
                "estimated_daily_spend": daily_local,
                "estimated_daily_spend_usd": daily_usd,
                "currency": currency,
                "vibe_headline": f"Top pick for {vibe.split('&')[0].strip()}",
                "highlight_tags": [c["theme"].split(',')[0].strip() for c in info["clusters"][:3]],
                "why_perfect": f"{info['name']} seamlessly matches your {budget.lower()} budget and {vibe.lower()} vibe. Excellent transit and concentrated cultural hubs.",
                "best_season_tip": info["best_months"],
                "lat": info["coords"][0],
                "lng": info["coords"][1]
            })
        return results

    # ==========================================
    # Tab 2: Day-by-Day Optimized Itinerary Generator
    # ==========================================
    def generate_itinerary(
        self,
        destination: str,
        duration_days: int,
        budget_level: str,
        party: str,
        pace: str,
        interests: List[str],
        currency: str,
        start_date: str = "Day 1"
    ) -> Dict[str, Any]:
        """Generate complete day-by-day itinerary with geographic clustering and itemized costs."""
        if not self.demo_mode and self.api_key:
            system_prompt = (
                "You are an elite travel logistics architect. Return ONLY valid JSON. "
                "Ensure strict geographic clustering per day to minimize transit fatigue and prevent backtracking."
            )
            user_prompt = f"""
            Create a comprehensive {duration_days}-day travel itinerary for {destination}.
            Traveler Profile:
            - Budget Tier: {budget_level}
            - Party: {party}
            - Pace: {pace}
            - Interests: {', '.join(interests) if interests else 'General Sightseeing'}
            - Preferred Currency: {currency}
            - Start Date: {start_date}

            JSON Schema:
            {{
              "trip_title": "Memorable Trip Title",
              "destination": "{destination}",
              "duration_days": {duration_days},
              "currency": "{currency}",
              "budget_tier": "{budget_level}",
              "days": [
                {{
                  "day_number": 1,
                  "date_label": "e.g. Day 1 (Oct 25)",
                  "cluster_name": "Neighborhood / District Zone (e.g. Asakusa & Ueno Arts Quarter)",
                  "cluster_rationale": "Why these stops are clustered together to avoid backtracking",
                  "daily_transit_tip": "Metro pass recommended; all morning-to-evening stops are within 1.5 km.",
                  "lat": 35.7148,
                  "lng": 139.7967,
                  "slots": [
                    {{
                      "slot_type": "Morning Sightseeing",
                      "time": "09:00 - 12:30",
                      "title": "Specific Attraction / Landmark Name",
                      "description": "Engaging 2-sentence description of the experience tailored to interests.",
                      "location": "Specific place name or street",
                      "cost_local": 25,
                      "cost_usd": 25,
                      "transit_to_next": "8-minute pedestrian walk through park"
                    }},
                    {{
                      "slot_type": "Lunch Recommendation",
                      "time": "12:30 - 14:00",
                      "title": "Restaurant / Cafe / Food Market Name",
                      "description": "Cuisine type, signature dish recommendation, and price vibe.",
                      "location": "Local street / market hall",
                      "cost_local": 20,
                      "cost_usd": 20,
                      "transit_to_next": "Short 10-minute tram ride or walk"
                    }},
                    {{
                      "slot_type": "Afternoon Leisure & Culture",
                      "time": "14:00 - 17:30",
                      "title": "Cultural Sight / Museum / Promenade",
                      "description": "Afternoon immersive activity clustered in the same district.",
                      "location": "District center",
                      "cost_local": 15,
                      "cost_usd": 15,
                      "transit_to_next": "5-minute stroll to dining area"
                    }},
                    {{
                      "slot_type": "Evening Dining & Entertainment",
                      "time": "18:30 - 21:30",
                      "title": "Atmospheric Dinner & Night Venue / Viewpoint",
                      "description": "Evening dining and relaxed nightlife or scenic skyline viewing.",
                      "location": "District waterfront or alley",
                      "cost_local": 35,
                      "cost_usd": 35,
                      "transit_to_next": "Return to accommodation via local metro"
                    }}
                  ]
                }}
              ]
            }}
            """
            raw = self._query_gemini(user_prompt, system_prompt) if self.provider == "Gemini" else self._query_groq(user_prompt, system_prompt)
            data = self._extract_json(raw) if raw else None
            if data and isinstance(data, dict) and "days" in data and len(data["days"]) > 0:
                return self._enrich_itinerary_costs(data, currency)

        # High-Fidelity Demo Planner
        return self._generate_demo_itinerary(destination, duration_days, budget_level, party, pace, interests, currency, start_date)

    def _enrich_itinerary_costs(self, itinerary: Dict[str, Any], currency: str) -> Dict[str, Any]:
        """Validate and enrich cumulative costs across all days."""
        rate = CURRENCIES.get(currency, {"rate": 1.0})["rate"]
        running_total_local = 0.0
        running_total_usd = 0.0

        for day in itinerary.get("days", []):
            day_total_local = 0.0
            day_total_usd = 0.0
            for slot in day.get("slots", []):
                cost_usd = float(slot.get("cost_usd", 20))
                cost_local = float(slot.get("cost_local", round(cost_usd * rate, 2)))
                slot["cost_usd"] = cost_usd
                slot["cost_local"] = cost_local
                day_total_local += cost_local
                day_total_usd += cost_usd

            running_total_local += day_total_local
            running_total_usd += day_total_usd
            day["day_total_local"] = round(day_total_local, 2)
            day["day_total_usd"] = round(day_total_usd, 2)
            day["cumulative_total_local"] = round(running_total_local, 2)
            day["cumulative_total_usd"] = round(running_total_usd, 2)

        itinerary["total_cost_local"] = round(running_total_local, 2)
        itinerary["total_cost_usd"] = round(running_total_usd, 2)
        return itinerary

    def _generate_demo_itinerary(
        self,
        destination: str,
        duration_days: int,
        budget_level: str,
        party: str,
        pace: str,
        interests: List[str],
        currency: str,
        start_date: str
    ) -> Dict[str, Any]:
        """Deterministic, rich travel itinerary generator with genuine geographic clustering."""
        rate = CURRENCIES.get(currency, {"rate": 1.0})["rate"]
        party_factor = PARTY_OPTIONS.get(party, {"multiplier": 1.0})["multiplier"]
        
        # Budget tier base multipliers
        budget_base_map = {"Budget": 0.6, "Moderate": 1.0, "Luxury": 2.2}
        cost_mult = budget_base_map.get(budget_level, 1.0) * (party_factor / 1.5)

        # Check if known destination
        catalog_match = None
        for key, data in DESTINATION_CATALOG.items():
            if key.lower() in destination.lower():
                catalog_match = data
                break

        base_lat, base_lng = (catalog_match["coords"] if catalog_match else (48.8566, 2.3522))
        clusters = catalog_match["clusters"] if catalog_match else [
            {"zone": "Historic Old Town & Central Waterfront", "theme": "Cobblestone alleys, heritage cathedrals & historic squares"},
            {"zone": "Arts District & Bohemian Quarter", "theme": "Artisan cafes, street murals & indie galleries"},
            {"zone": "Garden Promenade & Royal Boulevard", "theme": "Panoramic parks, imperial palaces & scenic riversides"},
            {"zone": "Modern Downtown & Skyline District", "theme": "High-altitude views, rooftop lounges & designer hubs"},
            {"zone": "Canal Harbor & Artisan Market Sector", "theme": "Open-air food stalls, waterways & sunset vantage points"}
        ]

        days_data = []
        running_total_local = 0.0
        running_total_usd = 0.0

        for d in range(duration_days):
            day_num = d + 1
            cluster_info = clusters[d % len(clusters)]
            cluster_name = cluster_info["zone"]
            cluster_theme = cluster_info["theme"]

            # Minor geographic coordinate jitter around base center for map plotting
            day_lat = base_lat + (0.015 * ((d % 3) - 1))
            day_lng = base_lng + (0.018 * ((d % 2) * 2 - 1))

            # Slots tailored to pace and interests
            interest_focus = interests[d % len(interests)] if interests else "Iconic Landmarks"

            # Cost benchmarks per slot based on budget level
            morning_cost_usd = round(18 * cost_mult, 1)
            lunch_cost_usd = round(22 * cost_mult, 1)
            afternoon_cost_usd = round(16 * cost_mult, 1)
            evening_cost_usd = round(38 * cost_mult, 1)

            slots = [
                {
                    "slot_type": "Morning Sightseeing",
                    "time": "09:00 - 12:30",
                    "title": f"Explore {cluster_name.split('&')[0].strip()} & {interest_focus}",
                    "description": f"Start the day at the iconic heart of {cluster_name}. Wander through peaceful morning streets, avoiding tourist rushes while soaking in {cluster_theme.lower()}.",
                    "location": f"{cluster_name.split('&')[0].strip()} Center",
                    "cost_usd": morning_cost_usd,
                    "cost_local": round(morning_cost_usd * rate, 1),
                    "transit_to_next": "5 to 8-minute scenic walk to lunch quarter"
                },
                {
                    "slot_type": "Lunch Recommendation",
                    "time": "12:30 - 14:00",
                    "title": f"Artisanal Lunch in {cluster_name.split('&')[-1].strip()}",
                    "description": f"Relish authentic local flavors and seasonal specialties at a beloved neighborhood bistro renowned for farm-fresh ingredients and vibrant atmosphere.",
                    "location": f"{cluster_name.split('&')[-1].strip()} Food Alley",
                    "cost_usd": lunch_cost_usd,
                    "cost_local": round(lunch_cost_usd * rate, 1),
                    "transit_to_next": "Short 10-minute stroll across the plaza"
                },
                {
                    "slot_type": "Afternoon Leisure & Culture",
                    "time": "14:00 - 17:30",
                    "title": f"Immersion: {cluster_theme.split(',')[0].strip()}",
                    "description": f"Curated afternoon visit clustered in the same district to prevent transit fatigue. Delve into curated collections, picturesque courtyards, and local artisan shops.",
                    "location": f"{cluster_name} Cultural Pavilion",
                    "cost_usd": afternoon_cost_usd,
                    "cost_local": round(afternoon_cost_usd * rate, 1),
                    "transit_to_next": "5-minute stroll to evening dining avenue"
                },
                {
                    "slot_type": "Evening Dining & Entertainment",
                    "time": "18:30 - 22:00",
                    "title": f"Sunset Dinner & Nightlife at {cluster_name.split('&')[0].strip()}",
                    "description": f"Dine with panoramic views or lively terrace seating. Conclude with evening dessert, ambient music, or a relaxing stroll beneath illuminated city architecture.",
                    "location": f"{cluster_name.split('&')[0].strip()} Promenade",
                    "cost_usd": evening_cost_usd,
                    "cost_local": round(evening_cost_usd * rate, 1),
                    "transit_to_next": "Direct return to hotel via local metro or taxi"
                }
            ]

            day_total_usd = sum(s["cost_usd"] for s in slots)
            day_total_local = sum(s["cost_local"] for s in slots)
            running_total_usd += day_total_usd
            running_total_local += day_total_local

            days_data.append({
                "day_number": day_num,
                "date_label": f"Day {day_num} • {cluster_name.split('&')[0].strip()}",
                "cluster_name": cluster_name,
                "cluster_rationale": f"All 4 attractions are situated within {cluster_name}. Walking radius is under 1.8 km, eliminating cross-city transit fatigue.",
                "daily_transit_tip": f"Pedestrian-friendly day! Use metro/tram to arrive in {cluster_name.split('&')[0].strip()}; thereafter all stops are walking distance.",
                "lat": day_lat,
                "lng": day_lng,
                "slots": slots,
                "day_total_usd": round(day_total_usd, 2),
                "day_total_local": round(day_total_local, 2),
                "cumulative_total_usd": round(running_total_usd, 2),
                "cumulative_total_local": round(running_total_local, 2)
            })

        return {
            "trip_title": f"Wanderlust Journey: {destination}",
            "destination": destination,
            "duration_days": duration_days,
            "currency": currency,
            "budget_tier": budget_level,
            "total_cost_usd": round(running_total_usd, 2),
            "total_cost_local": round(running_total_local, 2),
            "days": days_data
        }

    # ==========================================
    # Tab 3: Vibe Customization & Dynamic Activity Swap
    # ==========================================
    def swap_activity(
        self,
        destination: str,
        cluster_name: str,
        current_slot: Dict[str, Any],
        swap_prompt: str,
        budget_level: str,
        currency: str
    ) -> Dict[str, Any]:
        """Dynamically swap a single activity slot without wiping the rest of the plan."""
        rate = CURRENCIES.get(currency, {"rate": 1.0})["rate"]
        
        if not self.demo_mode and self.api_key:
            system_prompt = "You are a dynamic travel customization assistant. Return valid JSON only for a single replaced activity slot."
            user_prompt = f"""
            In {destination}, within the geographic cluster '{cluster_name}':
            Replace this current activity:
            - Type: {current_slot.get('slot_type')}
            - Current Title: {current_slot.get('title')}
            - Current Description: {current_slot.get('description')}
            
            With this user customization request:
            "{swap_prompt}"
            
            Keep the activity inside '{cluster_name}' so geographic clustering is maintained.
            Budget tier: {budget_level}.
            Display Currency: {currency}.

            Return JSON format:
            {{
              "slot_type": "{current_slot.get('slot_type')}",
              "time": "{current_slot.get('time')}",
              "title": "New Activity Title",
              "description": "Compelling 2-sentence description tailored to the swap request.",
              "location": "Location within {cluster_name}",
              "cost_usd": 25.0,
              "cost_local": 25.0,
              "transit_to_next": "{current_slot.get('transit_to_next', 'Short walk')}"
            }}
            """
            raw = self._query_gemini(user_prompt, system_prompt) if self.provider == "Gemini" else self._query_groq(user_prompt, system_prompt)
            data = self._extract_json(raw) if raw else None
            if data and isinstance(data, dict) and "title" in data:
                cost_usd = float(data.get("cost_usd", current_slot.get("cost_usd", 25.0)))
                data["cost_usd"] = cost_usd
                data["cost_local"] = float(data.get("cost_local", round(cost_usd * rate, 1)))
                return data

        # Demo Mode Swap
        new_slot = dict(current_slot)
        clean_prompt = swap_prompt.strip()
        new_slot["title"] = f"Customized: {clean_prompt.capitalize()}"
        new_slot["description"] = f"Tailored substitution in {cluster_name}: Enjoy a curated experience focused on '{clean_prompt}'. Perfectly situated nearby to maintain your cluster schedule."
        new_slot["location"] = f"{cluster_name} Artisan Quarter"
        # Small cost adjustment based on vibe
        if "free" in clean_prompt.lower() or "budget" in clean_prompt.lower():
            new_slot["cost_usd"] = round(new_slot.get("cost_usd", 20.0) * 0.4, 1)
        elif "luxury" in clean_prompt.lower() or "fine dining" in clean_prompt.lower():
            new_slot["cost_usd"] = round(new_slot.get("cost_usd", 20.0) * 1.8, 1)
        
        new_slot["cost_local"] = round(new_slot["cost_usd"] * rate, 1)
        return new_slot

    def regenerate_single_day(
        self,
        destination: str,
        day_number: int,
        day_vibe_request: str,
        budget_level: str,
        currency: str
    ) -> Dict[str, Any]:
        """Regenerate a single day with a distinct vibe or pacing without altering other days."""
        rate = CURRENCIES.get(currency, {"rate": 1.0})["rate"]
        
        if not self.demo_mode and self.api_key:
            system_prompt = "You are a travel itinerary architect. Return ONLY valid JSON for one customized day."
            user_prompt = f"""
            Regenerate Day {day_number} of a trip to {destination} based on this request:
            "{day_vibe_request}"
            Budget level: {budget_level}, Currency: {currency}.

            JSON format:
            {{
              "day_number": {day_number},
              "date_label": "Day {day_number} • Customized",
              "cluster_name": "Specific Clustered Neighborhood",
              "cluster_rationale": "Geographic grouping rationale",
              "daily_transit_tip": "Transit advice",
              "lat": 0.0,
              "lng": 0.0,
              "slots": [
                {{
                  "slot_type": "Morning Sightseeing",
                  "time": "09:00 - 12:30",
                  "title": "Title",
                  "description": "Description",
                  "location": "Location",
                  "cost_usd": 20.0,
                  "cost_local": 20.0,
                  "transit_to_next": "Transit"
                }},
                {{
                  "slot_type": "Lunch Recommendation",
                  "time": "12:30 - 14:00",
                  "title": "Title",
                  "description": "Description",
                  "location": "Location",
                  "cost_usd": 20.0,
                  "cost_local": 20.0,
                  "transit_to_next": "Transit"
                }},
                {{
                  "slot_type": "Afternoon Leisure & Culture",
                  "time": "14:00 - 17:30",
                  "title": "Title",
                  "description": "Description",
                  "location": "Location",
                  "cost_usd": 20.0,
                  "cost_local": 20.0,
                  "transit_to_next": "Transit"
                }},
                {{
                  "slot_type": "Evening Dining & Entertainment",
                  "time": "18:30 - 22:00",
                  "title": "Title",
                  "description": "Description",
                  "location": "Location",
                  "cost_usd": 35.0,
                  "cost_local": 35.0,
                  "transit_to_next": "Transit"
                }}
              ]
            }}
            """
            raw = self._query_gemini(user_prompt, system_prompt) if self.provider == "Gemini" else self._query_groq(user_prompt, system_prompt)
            data = self._extract_json(raw) if raw else None
            if data and isinstance(data, dict) and "slots" in data:
                return data

        # Demo regeneration
        cluster_name = f"{destination} Scenic & Leisure Sector"
        slots = [
            {
                "slot_type": "Morning Sightseeing",
                "time": "09:30 - 12:30",
                "title": f"Morning: {day_vibe_request.title()}",
                "description": f"Curated morning experience catering to your custom theme: '{day_vibe_request}'. Relaxed pace and uncrowded access.",
                "location": f"{cluster_name} Hub",
                "cost_usd": 22.0,
                "cost_local": round(22.0 * rate, 1),
                "transit_to_next": "5-minute walk"
            },
            {
                "slot_type": "Lunch Recommendation",
                "time": "12:30 - 14:00",
                "title": f"Theme Lunch at {cluster_name.split()[0]} Bistro",
                "description": "Enjoy a fresh farm-to-table lunch aligned with your selected vibe.",
                "location": f"{cluster_name} Green Plaza",
                "cost_usd": 25.0,
                "cost_local": round(25.0 * rate, 1),
                "transit_to_next": "Short garden walk"
            },
            {
                "slot_type": "Afternoon Leisure & Culture",
                "time": "14:00 - 17:30",
                "title": f"Afternoon Immersion: {day_vibe_request.title()}",
                "description": "Dedicated afternoon exploration ensuring zero backtracking across town.",
                "location": f"{cluster_name} Central",
                "cost_usd": 18.0,
                "cost_local": round(18.0 * rate, 1),
                "transit_to_next": "7-minute stroll"
            },
            {
                "slot_type": "Evening Dining & Entertainment",
                "time": "18:30 - 21:30",
                "title": f"Sunset Dinner & Relaxed Nightlife",
                "description": "Reflect on your themed day with culinary artistry and evening charm.",
                "location": f"{cluster_name} Promenade",
                "cost_usd": 40.0,
                "cost_local": round(40.0 * rate, 1),
                "transit_to_next": "Return to lodging"
            }
        ]
        return {
            "day_number": day_number,
            "date_label": f"Day {day_number} • {day_vibe_request.capitalize()}",
            "cluster_name": cluster_name,
            "cluster_rationale": "Specially customized single-day loop clustered tightly in one neighborhood.",
            "daily_transit_tip": "High walkability; low transit fatigue.",
            "lat": 0.0,
            "lng": 0.0,
            "slots": slots
        }
