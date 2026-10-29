# ✈️ Personalized Travel Itinerary Planner
### Skill Wallet Capstone Project 4 — Full-Stack Travel SaaS Architecture

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)

> An enterprise-grade, production-ready AI travel planning platform designed to generate **geographically clustered, fatigue-minimized itineraries**, perform **surgical activity hot-swapping**, and export **publication-ready offline PDF travel guides**.

---

## 🌟 Core Modules & Epic Mapping

```
                                ┌──────────────────────────────────────────────┐
                                │       Personalized Travel Planner            │
                                └──────────────────────┬───────────────────────┘
                                                       │
         ┌─────────────────────────┬───────────────────┴───────────────┬─────────────────────────┐
         ▼                         ▼                                   ▼                         ▼
   ┌───────────┐             ┌───────────┐                       ┌───────────┐             ┌───────────┐
   │  Epic 3   │             │  Epic 3   │                       │  Epic 4   │             │  Epic 5   │
   │  Config   │             │   Tab 1   │                       │Tabs 2 & 3 │             │   Tab 4   │
   └─────┬─────┘             └─────┬─────┘                       └─────┬─────┘             └─────┬─────┘
         │                         │                                   │                         │
  • API Key/Demo            • Top 3 Cities                      • Day-by-Day               • Simulated DB
  • Preference Form         • Vibe/Season/Budget                • Geo-Clustering           • Trip History
  • Currencies (USD/INR)    • 1-Click Select                    • Activity Swap            • 1-Click PDF
```

### 1. Configuration & User Preferences (Epic 3)
- **Multi-Engine AI Integration**: Direct support for **Google Gemini (Gemini 3.8 Flash, with Gemini 3.6 Flash fallback)** and **Groq (Llama-3.3 70B)** via lightweight REST calls, plus an **Offline High-Fidelity Demo Engine** requiring zero API keys.
- **Trip Preference Engine**:
  - Destination input (catalog suggestions + freeform custom destinations/vibes).
  - Duration slider (1 to 10 days).
  - Dynamic travel date picker with automatic offset calculations.
  - Budget Tiers: **Budget** (`$35-$75/day`), **Moderate** (`$80-$190/day`), and **Luxury** (`$240-$650/day`).
  - Travel Party: Solo (`1.0x`), Couple (`1.85x`), Family (`2.8x`), and Friends Group (`3.2x`).
  - Pace: Relaxed (3 slots), Moderate (4 slots), Fast-Paced (5 slots).
  - Multi-Currency Display: USD ($), INR (₹), EUR (€), GBP (£), JPY (¥), AUD (A$), CAD (C$).

### 2. Tab 1 — Smart Destination Recommender (Epic 3)
- For undecided travelers, curates the **top 3 matching world cities** based on travel mood (Beach, Alpine, Cultural, Urban, Romantic, Foodie, Adventure), travel season/weather, and budget tier.
- Highlights match score (e.g. `98% Match`), seasonal tips, weather summaries, estimated daily spend, and a **1-Click "Select Destination"** button that automatically populates the itinerary generator and switches tabs.

### 3. Tab 2 — Day-by-Day Optimized Itinerary Generator (Epic 4)
- **Sequential Time Slots**:
  - `09:00 - 12:30`: Morning Sightseeing & Cultural Anchor
  - `12:30 - 14:00`: Lunch Recommendation (Cuisine, signature dishes, vibe)
  - `14:00 - 17:30`: Afternoon Leisure & Neighborhood Immersion
  - `18:30 - 22:00`: Evening Dining, Promenade & Nightlife
- **Geographic Clustering Logic**:
  - Automatically groups nearby attractions within the same day into tight neighborhood hubs (e.g., *Shibuya & Harajuku*, *Montmartre*, *Eixample & Gaudí*).
  - Prominent cluster badge with transit rationale and walking directions to eliminate transit fatigue and prevent cross-city backtracking.
- **Itemized Costs & Cumulative Budget Tracker**:
  - Calculates slot-level and day-level costs with running cumulative totals in both local currency and USD.
  - Visual budget tier tracker comparing projected spend against target budget allowances.
- **Geographic Coordinate Map**: Integrated map view visualizing geographic cluster hubs.

### 4. Tab 3 — Vibe Customization & Dynamic Activity Swap (Epic 4)
- **Surgical Single-Slot Hot-Swapping**:
  - Pick any day and any time slot (e.g. Day 2 Lunch) and swap it without altering or resetting the rest of the trip.
  - Quick presets: *Vegetarian/Vegan Foodie Spot*, *Artisan Outdoor Market*, *Rainy Day Museum*, *Kid-Friendly Family Activity*, *Adrenaline Thrill*, *Budget Scenic Alternative*.
  - Custom freeform prompts (e.g., *"Swap museum for a traditional matcha tea ceremony"*).
- **Single-Day Theme Regeneration**:
  - Refresh an entire single day (e.g., *"Convert Day 3 into a relaxed thermal spa and wellness day"*) while preserving Day 1, 2, 4, etc.
- **Manual Slot Fine-Tuning**: Full manual editing of title, notes, and costs.

### 5. Tab 4 — Trip Management & Offline PDF Export (Epic 5)
- **Simulated Database Persistence**:
  - Saves multiple trips with custom names, dates, and notes to local storage (`saved_trips.json`) + session state.
  - Trip history viewer with options to **Load Active**, **Duplicate**, **Delete**, or **Download PDF** directly from archive cards.
  - Turnkey sample trips seeder (Tokyo, Paris, Bali) for instant 1-click exploration.
- **Publication-Ready Offline PDF Travel Guide**:
  - Generated using pure-Python `reportlab` with zero external binary or OS dependencies.
  - Executive Trip Metrics summary table.
  - **Emergency Contacts Checklist** (Local Police, Ambulance, Tourist Helpline, Embassy alert).
  - **Smart Packing Checklist** tailored to destination and climate.
  - Geographically clustered day-by-day table with transit instructions, times, and itemized costs.
  - Two-pass `NumberedCanvas` with "Page X of Y" pagination.
- **JSON Portability**: 1-click JSON export and import for seamless backup and sharing.

---

## 🏗️ Technical Architecture & File Structure

```
GenAI project/
├── .streamlit/
│   └── config.toml             # Wanderlust visual theme & server parameters
├── modules/
│   ├── __init__.py             # Package initializer
│   ├── config.py               # Catalogs, exchange rates, budget tiers & anchors
│   ├── styles.py               # Custom CSS (glassmorphism cards, badges, timeline)
│   ├── ai_engine.py            # Unified LLM client (Gemini/Groq) & Demo Engine
│   ├── recommender.py          # Tab 1: Smart Destination Recommender UI
│   ├── itinerary_generator.py  # Tab 2: Day-by-Day Planner & Budget Tracker
│   ├── vibe_customizer.py      # Tab 3: Dynamic Activity Swap & Day Regeneration
│   ├── trip_manager.py         # Tab 4: Simulated DB Persistence & History Viewer
│   └── pdf_generator.py        # ReportLab Offline PDF Travel Guide Compiler
├── app.py                      # Main Streamlit SaaS Application Entry Point
├── test_app.py                 # Automated 7-stage end-to-end test suite
├── saved_trips.json            # Local simulated database store (auto-created)
├── requirements.txt            # Zero-dependency cloud deployment manifest
└── README.md                   # System documentation & architectural blueprint
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.10, 3.11, 3.12, 3.13, or 3.14
- pip package manager

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Automated Test Suite
Verify that all 7 core subsystems (catalogs, recommendation engine, clustering generator, activity swap, single-day regeneration, ReportLab PDF compiler with multi-currency sanitization, and turnkey sample loader) pass:
```bash
python test_app.py
```

### 4. Launch the Streamlit SaaS Application
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🔒 Security & Deployment Notes

- **Zero External Database Overhead**: Uses local JSON persistence and Streamlit session state, eliminating external PostgreSQL/MongoDB requirements and making it **100% turnkey for Streamlit Community Cloud, Hugging Face Spaces, or Docker**.
- **Secure Key Handling**: API keys are held strictly in browser session memory and never persisted to disk or sent to third-party trackers.
- **Offline / Demo Resilience**: If no API key is supplied or if network quotas are exceeded, the high-fidelity offline engine generates realistic, authentic itineraries seamlessly without throwing runtime errors.


## Run locally in VS Code

1. Install Python 3.10 or newer and VS Code.
2. Extract this project ZIP, then open the `GenAI_Project_VSCode` folder in VS Code (`File → Open Folder`).
3. In the VS Code terminal, run `python -m venv .venv`.
4. Activate the environment:
   - **Windows PowerShell:** `.venv\\Scripts\\Activate.ps1`
   - **Windows Command Prompt:** `.venv\\Scripts\\activate.bat`
   - **macOS/Linux:** `source .venv/bin/activate`
5. Install packages: `python -m pip install -r requirements.txt`
6. Start the app: `python -m streamlit run app.py`
7. Open the local URL printed in the terminal (usually `http://localhost:8501`).

**Windows shortcut:** double-click `run.bat` to create the environment, install dependencies, and start the app automatically.

The app starts in **Demo Mode**, so you can use its main features without API keys. Gemini/Groq modes require your own API key. If you use `.env`, copy `.env.example` to `.env` and replace the placeholder values with your keys. Keep `.env` private and never commit it.
