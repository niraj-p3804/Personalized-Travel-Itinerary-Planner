"""Custom wanderlust-inspired CSS styling for the Personalized Travel Itinerary Planner."""

def get_custom_css():
    return """
    <style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap');

    /* Global typography overrides */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3.5rem;
        max-width: 1280px;
    }

    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #0F766E 0%, #0D9488 40%, #0284C7 100%);
        border-radius: 18px;
        padding: 32px 36px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 118, 110, 0.25), 0 8px 10px -6px rgba(15, 118, 110, 0.2);
        position: relative;
        overflow: hidden;
    }

    .hero-banner::after {
        content: "✈";
        position: absolute;
        right: 25px;
        bottom: -20px;
        font-size: 140px;
        opacity: 0.08;
        transform: rotate(-25deg);
        pointer-events: none;
    }

    .hero-tag {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(8px);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 8px;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.35rem;
        font-weight: 700;
        margin: 0 0 8px 0;
        line-height: 1.2;
    }

    .hero-subtitle {
        font-size: 1.02rem;
        opacity: 0.92;
        max-width: 800px;
        margin: 0;
        font-weight: 400;
    }

    /* Modern Glass Card */
    .wander-card {
        background: #ffffff;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 22px 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.04), 0 2px 6px -2px rgba(15, 23, 42, 0.02);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .wander-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px -3px rgba(15, 23, 42, 0.08);
    }

    /* Geographic Cluster Header Badge */
    .cluster-banner {
        background: linear-gradient(90deg, #F0FDFA 0%, #ECFEFF 100%);
        border-left: 4px solid #0D9488;
        border-radius: 8px;
        padding: 12px 18px;
        margin-bottom: 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .cluster-zone {
        font-weight: 700;
        color: #0F766E;
        font-size: 0.98rem;
    }

    .cluster-transit {
        font-size: 0.82rem;
        color: #64748B;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Time Slot Card */
    .slot-card {
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        padding: 16px 18px;
        margin-bottom: 14px;
        background: #FAFAFA;
        position: relative;
    }

    .slot-morning { border-left: 4px solid #F59E0B; }
    .slot-lunch { border-left: 4px solid #10B981; }
    .slot-afternoon { border-left: 4px solid #0284C7; }
    .slot-evening { border-left: 4px solid #8B5CF6; }

    .slot-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }

    .slot-time-badge {
        font-size: 0.76rem;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .badge-morning { background: #FEF3C7; color: #B45309; }
    .badge-lunch { background: #D1FAE5; color: #047857; }
    .badge-afternoon { background: #E0F2FE; color: #0369A1; }
    .badge-evening { background: #EDE9FE; color: #6D28D9; }

    .slot-cost {
        font-size: 0.86rem;
        font-weight: 700;
        color: #0F172A;
        background: #F1F5F9;
        padding: 2px 10px;
        border-radius: 9999px;
    }

    .slot-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0F172A;
        margin: 0 0 6px 0;
    }

    .slot-desc {
        font-size: 0.88rem;
        color: #475569;
        line-height: 1.5;
        margin-bottom: 6px;
    }

    .slot-transit {
        font-size: 0.78rem;
        color: #64748B;
        font-style: italic;
    }

    /* Metric Stat Tiles */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 14px;
        margin-bottom: 22px;
    }

    .metric-tile {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px 18px;
        text-align: left;
    }

    .metric-label {
        font-size: 0.78rem;
        color: #64748B;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 4px;
    }

    .metric-value {
        font-size: 1.35rem;
        font-weight: 800;
        color: #0F172A;
    }

    .metric-sub {
        font-size: 0.75rem;
        color: #0D9488;
        font-weight: 600;
    }

    /* Recommendation City Cards */
    .city-card {
        background: white;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.25s ease;
    }

    .city-card:hover {
        border-color: #0D9488;
        box-shadow: 0 10px 25px -5px rgba(13, 148, 136, 0.15);
    }

    .highlight-pill {
        display: inline-block;
        background: #F0FDFA;
        color: #0F766E;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 3px 10px;
        border-radius: 9999px;
        margin-right: 6px;
        margin-bottom: 6px;
        border: 1px solid #CCFBF1;
    }

    /* Status Pill */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.76rem;
        font-weight: 600;
    }
    .status-active { background: #D1FAE5; color: #065F46; }
    .status-demo { background: #FEF3C7; color: #92400E; }

    /* Streamlit tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        white-space: pre-wrap;
        background-color: #F8FAFC;
        border-radius: 8px 8px 0px 0px;
        gap: 8px;
        padding-top: 10px;
        padding-bottom: 10px;
        padding-left: 18px;
        padding-right: 18px;
        font-weight: 600;
        color: #475569;
        border: 1px solid #E2E8F0;
        border-bottom: none;
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #0D9488 !important;
        border-color: #CBD5E1 !important;
        border-bottom: 2px solid #0D9488 !important;
    }

    /* Custom button enhancements */
    div.stButton > button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s;
    }
    </style>
    """
