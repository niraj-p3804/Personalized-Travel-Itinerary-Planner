"""Configuration, constants, currency exchange rates, and reference data for Travel Itinerary Planner."""

APP_NAME = "Personalized Travel Itinerary Planner"
APP_SUBTITLE = "AI-Driven Intelligent Route Clustering & Dynamic Vibe Customization"
CAPSTONE_PROJECT = "Skill Wallet Capstone Project 4"

# Supported Currencies and Baseline Exchange Rates relative to USD
CURRENCIES = {
    "USD": {"symbol": "$", "rate": 1.0, "name": "US Dollar"},
    "INR": {"symbol": "₹", "rate": 83.5, "name": "Indian Rupee"},
    "EUR": {"symbol": "€", "rate": 0.92, "name": "Euro"},
    "GBP": {"symbol": "£", "rate": 0.79, "name": "British Pound"},
    "JPY": {"symbol": "¥", "rate": 155.0, "name": "Japanese Yen"},
    "AUD": {"symbol": "A$", "rate": 1.52, "name": "Australian Dollar"},
    "CAD": {"symbol": "C$", "rate": 1.38, "name": "Canadian Dollar"},
}

# Budget Tier Specifications (per person / day in USD equivalent)
BUDGET_TIERS = {
    "Budget": {
        "label": "Backpacker / Budget Traveler",
        "min_usd": 35,
        "max_usd": 75,
        "icon": "🎒",
        "desc": "Hostels/budget guesthouses, local public transit, street food & free entry sights."
    },
    "Moderate": {
        "label": "Comfort / Mid-Range Explorer",
        "min_usd": 80,
        "max_usd": 190,
        "icon": "🏨",
        "desc": "3-4 star boutique hotels, scenic cafes, key museum passes, occasional taxis."
    },
    "Luxury": {
        "label": "Boutique & Premium Connoisseur",
        "min_usd": 240,
        "max_usd": 650,
        "icon": "✨",
        "desc": "5-star luxury stays, private transfers, fine dining, skip-the-line VIP tours."
    }
}

# Travel Party Options
PARTY_OPTIONS = {
    "Solo": {"label": "Solo Explorer", "multiplier": 1.0, "icon": "🚶"},
    "Couple": {"label": "Couple / Duo", "multiplier": 1.85, "icon": "💑"},
    "Family": {"label": "Family (Adults + Kids)", "multiplier": 2.8, "icon": "👨‍👩‍👧‍👦"},
    "Friends": {"label": "Friends Squad (3-4)", "multiplier": 3.2, "icon": "👥"}
}

# Travel Pace Options
PACE_OPTIONS = {
    "Relaxed": {
        "label": "Relaxed & Unhurried",
        "slots_per_day": 3,
        "desc": "Late mornings, leisurely cafe stops, ample time to soak in atmosphere."
    },
    "Moderate": {
        "label": "Balanced & Steady",
        "slots_per_day": 4,
        "desc": "A harmonious blend of cultural sightseeing, food discovery, and resting time."
    },
    "Fast-Paced": {
        "label": "Action-Packed & Vibrant",
        "slots_per_day": 5,
        "desc": "Early starts, high-efficiency route checklists, maximum landmarks."
    }
}

# Open-ended Travel Vibes
TRAVEL_VIBES = [
    "Beach & Tropical Coastal",
    "Mountain & Alpine Nature",
    "Cultural & Historical Heritage",
    "Urban Pulse & Modern Architecture",
    "Romantic Getaways & Sunsets",
    "Culinary & Street Food Trail",
    "Adrenaline & Outdoor Adventure",
    "Wellness, Hot Springs & Yoga"
]

# Common Travel Interests
INTEREST_TAGS = [
    "Art & Architecture", "Street Food & Gastronomy", "History & Heritage",
    "Nightlife & Speakeasies", "Outdoor Hiking & Scenic Nature", "Local Markets & Souvenirs",
    "Photography Hotspots", "Off-the-Beaten-Path Secrets", "Museums & Galleries",
    "Water Sports & Beaches", "Coffee Culture", "Relaxation & Spas"
]

# Destination Reference Library with GPS Coordinates & Geographic Clustering Anchors
DESTINATION_CATALOG = {
    "Tokyo": {
        "name": "Tokyo, Japan",
        "country": "Japan",
        "coords": [35.6762, 139.6503],
        "currency": "JPY",
        "best_months": "March - May (Cherry Blossom) & October - November (Autumn Foliage)",
        "vibe_matches": ["Urban Pulse & Modern Architecture", "Culinary & Street Food Trail", "Cultural & Historical Heritage"],
        "budget_level": "Moderate",
        "daily_cost_usd": 120,
        "emergency": {"police": "110", "ambulance": "119", "tourist_hotline": "+81 3-3201-3331"},
        "clusters": [
            {"zone": "Shibuya & Harajuku", "theme": "Pop Culture, Fashion & Neon Crossings"},
            {"zone": "Asakusa & Ueno", "theme": "Edo Temples, Street Food & Museum Park"},
            {"zone": "Shinjuku & Omoide Yokocho", "theme": "Skyscrapers, Shinjuku Gyoen & Nightlife"},
            {"zone": "Ginza & Tsukiji Outer Market", "theme": "Artisanal Seafood & High Fashion Avenue"},
            {"zone": "Akihabara & Imperial Palace", "theme": "Otaku Tech Haven & Regal Gardens"}
        ]
    },
    "Paris": {
        "name": "Paris, France",
        "country": "France",
        "coords": [48.8566, 2.3522],
        "currency": "EUR",
        "best_months": "April - June & September - October (Mild Weather, Low Crowds)",
        "vibe_matches": ["Cultural & Historical Heritage", "Romantic Getaways & Sunsets", "Culinary & Street Food Trail"],
        "budget_level": "Moderate",
        "daily_cost_usd": 150,
        "emergency": {"police": "17", "ambulance": "15", "tourist_hotline": "+33 1 49 52 42 63"},
        "clusters": [
            {"zone": "1st & 4th Arr. (Louvre & Le Marais)", "theme": "Iconic Art Galleries & Chic Boutiques"},
            {"zone": "7th & 15th Arr. (Eiffel Tower & Seine)", "theme": "Monumental Architecture & River Cruises"},
            {"zone": "18th Arr. (Montmartre)", "theme": "Bohemian Cobblestones & Sacré-Cœur Panoramas"},
            {"zone": "5th & 6th Arr. (Latin Quarter & St-Germain)", "theme": "Literary Cafes, Sorbonne & Luxembourg Gardens"},
            {"zone": "Canal Saint-Martin & Belleville", "theme": "Hipster Bistros & Street Murals"}
        ]
    },
    "Bali": {
        "name": "Bali, Indonesia",
        "country": "Indonesia",
        "coords": [-8.4095, 115.1889],
        "currency": "IDR",
        "best_months": "April - October (Dry Season, Sunny Surf Days)",
        "vibe_matches": ["Beach & Tropical Coastal", "Wellness, Hot Springs & Yoga", "Adrenaline & Outdoor Adventure"],
        "budget_level": "Budget",
        "daily_cost_usd": 65,
        "emergency": {"police": "110", "ambulance": "118", "tourist_hotline": "+62 361 751011"},
        "clusters": [
            {"zone": "Ubud & Tegallalang", "theme": "Emerald Rice Terraces, Sacred Monkey Forest & Artisan Spas"},
            {"zone": "Uluwatu & Bukit Peninsula", "theme": "Cliffside Kecak Fire Dance & Ocean Waves"},
            {"zone": "Canggu & Seminyak", "theme": "Sunset Beach Clubs & Specialty Coffee Cafes"},
            {"zone": "Nusa Penida Island", "theme": "Kelingking T-Rex Cliffs & Manta Ray Snorkeling"},
            {"zone": "Mount Batur & Kintamani", "theme": "Sunrise Volcano Trek & Volcanic Hot Springs"}
        ]
    },
    "Rome": {
        "name": "Rome, Italy",
        "country": "Italy",
        "coords": [41.9028, 12.4964],
        "currency": "EUR",
        "best_months": "April - May & September - October",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Romantic Getaways & Sunsets"],
        "budget_level": "Moderate",
        "daily_cost_usd": 130,
        "emergency": {"police": "112", "ambulance": "118", "tourist_hotline": "+39 06 0608"},
        "clusters": [
            {"zone": "Colosseo & Ancient Forum", "theme": "Gladiatorial Arenas & Palatine Hill"},
            {"zone": "Centro Storico & Pantheon", "theme": "Trevi Fountain, Piazza Navona & Artisan Gelato"},
            {"zone": "Vatican City & Borgo", "theme": "St. Peter's Basilica & Sistine Chapel Frescoes"},
            {"zone": "Trastevere & Gianicolo Hill", "theme": "Ivy-Covered Cobblestones & Roman Trattorias"}
        ]
    },
    "New York City": {
        "name": "New York City, USA",
        "country": "United States",
        "coords": [40.7128, -74.0060],
        "currency": "USD",
        "best_months": "September - November (Crisp Autumn) & April - June",
        "vibe_matches": ["Urban Pulse & Modern Architecture", "Nightlife & Speakeasies", "Art & Architecture"],
        "budget_level": "Luxury",
        "daily_cost_usd": 240,
        "emergency": {"police": "911", "ambulance": "911", "tourist_hotline": "311"},
        "clusters": [
            {"zone": "Midtown & Broadway", "theme": "Times Square, Theatre District & Top of the Rock"},
            {"zone": "Lower Manhattan & Financial District", "theme": "One World Trade, Wall St & Brooklyn Bridge Walk"},
            {"zone": "Central Park & Museum Mile", "theme": "Metropolitan Museum & Strawberry Fields"},
            {"zone": "Greenwich Village & Chelsea High Line", "theme": "Art Galleries, Jazz Clubs & Chelsea Market"},
            {"zone": "DUMBO & Williamsburg Brooklyn", "theme": "Skyline Views, Vintage Markets & Craft Breweries"}
        ]
    },
    "Barcelona": {
        "name": "Barcelona, Spain",
        "country": "Spain",
        "coords": [41.3879, 2.1699],
        "currency": "EUR",
        "best_months": "May - June & September - October (Warm Mediterranean Days)",
        "vibe_matches": ["Beach & Tropical Coastal", "Cultural & Historical Heritage", "Culinary & Street Food Trail"],
        "budget_level": "Moderate",
        "daily_cost_usd": 115,
        "emergency": {"police": "112", "ambulance": "061", "tourist_hotline": "+34 93 285 3834"},
        "clusters": [
            {"zone": "Eixample & Gaudí Modernism", "theme": "Sagrada Família, Casa Batlló & Paseo de Gràcia"},
            {"zone": "Gothic Quarter & El Born", "theme": "Medieval Labyrinths, Picasso Museum & Tapas Bars"},
            {"zone": "Barceloneta & Port Olímpic", "theme": "Seaside Promenade, Paella & Mediterranean Sands"},
            {"zone": "Park Güell & Gràcia", "theme": "Mosaic Terraces & Bohemian Village Plazas"},
            {"zone": "Montjuïc Hill", "theme": "Castle Panoramas & Magic Fountain Light Show"}
        ]
    },
    "Bangkok": {
        "name": "Bangkok, Thailand",
        "country": "Thailand",
        "coords": [13.7563, 100.5018],
        "currency": "THB",
        "best_months": "November - February (Cool & Dry Monsoon-Free)",
        "vibe_matches": ["Culinary & Street Food Trail", "Cultural & Historical Heritage", "Urban Pulse & Modern Architecture"],
        "budget_level": "Budget",
        "daily_cost_usd": 55,
        "emergency": {"police": "191", "tourist_police": "1155", "ambulance": "1669"},
        "clusters": [
            {"zone": "Rattanakosin Historic Isle", "theme": "Grand Palace, Wat Pho Reclining Buddha & Wat Arun"},
            {"zone": "Chinatown (Yaowarat)", "theme": "Legendary Wok Street Food & Neon Alleys"},
            {"zone": "Riverside & Chao Phraya Express", "theme": "IconSIAM & Longtail Boat Canals"},
            {"zone": "Sukhumvit & Thonglor", "theme": "Rooftop Skybars & Modern Gastronomy"},
            {"zone": "Chatuchak & Ari", "theme": "World's Largest Weekend Market & Third-Wave Coffee"}
        ]
    },
    "Jaipur": {
        "name": "Jaipur, India",
        "country": "India",
        "coords": [26.9124, 75.7873],
        "currency": "INR",
        "best_months": "October - March (Pleasant Sunny Winter Days)",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Romantic Getaways & Sunsets"],
        "budget_level": "Budget",
        "daily_cost_usd": 45,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 141 220 1888"},
        "clusters": [
            {"zone": "Walled Pink City Center", "theme": "Hawa Mahal, City Palace & Johari Bazaar"},
            {"zone": "Amer & Jaigarh Ridge", "theme": "Majestic Amber Fort & World's Largest Wheeled Cannon"},
            {"zone": "Nahargarh & Sunset Bastion", "theme": "Stepwells (Panna Meena Ka Kund) & Hilltop Forts"},
            {"zone": "C-Scheme & MI Road", "theme": "Royal Rajasthani Thali & Heritage Havelis"}
        ]
    },
    "Delhi": {
        "name": "Delhi, India",
        "country": "India",
        "coords": [28.6139, 77.2090],
        "currency": "INR",
        "best_months": "October - March (Cooler Days for Monument Visits)",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Urban Pulse & Modern Architecture"],
        "budget_level": "Budget",
        "daily_cost_usd": 50,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Old Delhi & Chandni Chowk", "theme": "Red Fort, Jama Masjid & Legendary Street Food"},
            {"zone": "New Delhi & Lutyens' District", "theme": "India Gate, Rashtrapati Bhavan & Wide Tree-Lined Avenues"},
            {"zone": "Mehrauli & Qutub Minar", "theme": "UNESCO Heritage Ruins, Stepwells & Garden Tombs"},
            {"zone": "Humayun's Tomb & Lodhi Gardens", "theme": "Mughal Architecture, Landscaped Tombs & Peaceful Garden Walks"}
        ]
    },
    "Mumbai": {
        "name": "Mumbai, India",
        "country": "India",
        "coords": [19.0760, 72.8777],
        "currency": "INR",
        "best_months": "November - February (Mild Weather and Clear Skies)",
        "vibe_matches": ["Urban Pulse & Modern Architecture", "Culinary & Street Food Trail", "Beach & Tropical Coastal"],
        "budget_level": "Moderate",
        "daily_cost_usd": 65,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Colaba & Fort", "theme": "Gateway of India, Historic Architecture & Kala Ghoda Galleries"},
            {"zone": "Marine Drive & Malabar Hill", "theme": "Seafront Promenade, Art Deco Buildings & Sunset Views"},
            {"zone": "Bandra & Juhu", "theme": "Street Art, Film City Culture & Beachside Food Stalls"},
            {"zone": "Dadar & Lower Parel", "theme": "Local Markets, Textile Heritage & Contemporary Dining"}
        ]
    },
    "Kolkata": {
        "name": "Kolkata, India",
        "country": "India",
        "coords": [22.5726, 88.3639],
        "currency": "INR",
        "best_months": "October - March (Comfortable Weather and Festival Season)",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Art & Architecture"],
        "budget_level": "Budget",
        "daily_cost_usd": 40,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Maidan & Victoria Memorial", "theme": "Colonial-Era Architecture, Museum Galleries & Green Esplanades"},
            {"zone": "College Street & North Kolkata", "theme": "Historic Bookshops, Coffee House & Heritage Mansions"},
            {"zone": "Kumartuli & Sovabazar", "theme": "Traditional Artisan Workshops, Temples & Festival Heritage"},
            {"zone": "Park Street & New Market", "theme": "Classic Bakeries, Local Markets & Bengali Food"}
        ]
    },
    "Hyderabad": {
        "name": "Hyderabad, India",
        "country": "India",
        "coords": [17.3850, 78.4867],
        "currency": "INR",
        "best_months": "October - February (Milder Days for Forts and Old City Walks)",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Urban Pulse & Modern Architecture"],
        "budget_level": "Budget",
        "daily_cost_usd": 45,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Charminar & Laad Bazaar", "theme": "Historic Minarets, Bangles & Old City Food Lanes"},
            {"zone": "Golconda Fort & Qutb Shahi Tombs", "theme": "Deccan Fortifications, Royal Tombs & Hilltop Views"},
            {"zone": "Hussain Sagar & Necklace Road", "theme": "Lakeside Promenade, City Museums & Sunset Views"},
            {"zone": "Jubilee Hills & Banjara Hills", "theme": "Modern Cafes, Contemporary Culture & Hyderabadi Dining"}
        ]
    },
    "Hampi": {
        "name": "Hampi, India",
        "country": "India",
        "coords": [15.3350, 76.4600],
        "currency": "INR",
        "best_months": "November - February (Cooler Weather for Exploring the Ruins)",
        "vibe_matches": ["Cultural & Historical Heritage", "Outdoor Hiking & Scenic Nature", "Photography Hotspots"],
        "budget_level": "Budget",
        "daily_cost_usd": 35,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Sacred Center & Virupaksha Temple", "theme": "Ancient Temple Streets, Hampi Bazaar & Riverside Ghats"},
            {"zone": "Royal Center & Zenana Enclosure", "theme": "Lotus Mahal, Elephant Stables & Vijayanagara Palace Ruins"},
            {"zone": "Vittala Temple & Riverside Ruins", "theme": "Stone Chariot, Musical Pillars & Bouldered Landscapes"},
            {"zone": "Matanga Hill & Hemakuta Hill", "theme": "Sunrise Hikes, Temple Views & Sunset Over the Tungabhadra"}
        ]
    },
    "Mysuru": {
        "name": "Mysuru, India",
        "country": "India",
        "coords": [12.2958, 76.6394],
        "currency": "INR",
        "best_months": "October - March (Pleasant Weather and Festive Celebrations)",
        "vibe_matches": ["Cultural & Historical Heritage", "Romantic Getaways & Sunsets", "Culinary & Street Food Trail"],
        "budget_level": "Budget",
        "daily_cost_usd": 40,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Mysore Palace & Devaraja Market", "theme": "Royal Halls, Flower Stalls & Local Sweets"},
            {"zone": "Chamundi Hills & Nandi Statue", "theme": "Hilltop Temple, City Panoramas & Scenic Road"},
            {"zone": "St. Philomena's Church & Heritage Quarter", "theme": "Gothic Architecture, Old Markets & Historic Streets"},
            {"zone": "Brindavan Gardens & KRS", "theme": "Terraced Gardens, Musical Fountain & Evening Walks"}
        ]
    },
    "Cape Town": {
        "name": "Cape Town, South Africa",
        "country": "South Africa",
        "coords": [-33.9249, 18.4241],
        "currency": "ZAR",
        "best_months": "December - March (Glorious Summer Sun & Beach Days)",
        "vibe_matches": ["Mountain & Alpine Nature", "Beach & Tropical Coastal", "Adrenaline & Outdoor Adventure"],
        "budget_level": "Moderate",
        "daily_cost_usd": 90,
        "emergency": {"police": "10111", "ambulance": "10177", "tourist_safety": "+27 21 487 6552"},
        "clusters": [
            {"zone": "Table Mountain & Camps Bay", "theme": "Cableway Peaks & Atlantic Sunset Beaches"},
            {"zone": "V&A Waterfront & Robben Island", "theme": "Harbor Dining, Marine Life & Nelson Mandela Legacy"},
            {"zone": "Kirstenbosch & Constantia", "theme": "Botanical Canopy Walkways & Historic Vineyards"},
            {"zone": "Cape Peninsula & Boulders Beach", "theme": "African Penguin Colony & Cape of Good Hope"}
        ]
    },
    "Zurich": {
        "name": "Zurich & Lucerne, Switzerland",
        "country": "Switzerland",
        "coords": [47.3769, 8.5417],
        "currency": "CHF",
        "best_months": "June - September (Alpine Hiking) or December - March (Skiing)",
        "vibe_matches": ["Mountain & Alpine Nature", "Romantic Getaways & Sunsets", "Urban Pulse & Modern Architecture"],
        "budget_level": "Luxury",
        "daily_cost_usd": 280,
        "emergency": {"police": "117", "ambulance": "144", "swiss_rescue": "1414"},
        "clusters": [
            {"zone": "Altstadt & Lake Zurich Promenade", "theme": "Lindenhof Panoramas, Grossmünster & Lake Cruises"},
            {"zone": "Uetliberg Mountain Peak", "theme": "Panoramic Alpine Vistas & Forest Trails"},
            {"zone": "Lucerne Day Loop & Chapel Bridge", "theme": "Historic Wooden Bridges & Mount Pilatus Cogwheel"},
            {"zone": "Zurich West & Viadukt", "theme": "Industrial Design Shops, Artisan Bakeries & Urban Gardens"}
        ]
    },
    "Goa": {
        "name": "Goa (North & South), India",
        "country": "India",
        "coords": [15.2993, 74.1240],
        "currency": "INR",
        "best_months": "November - February (Sunny Beaches, Watersports & Vibrant Nightlife)",
        "vibe_matches": ["Beach & Tropical Coastal", "Nightlife & Speakeasies", "Culinary & Street Food Trail"],
        "budget_level": "Moderate",
        "daily_cost_usd": 50,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 832 242 7700"},
        "clusters": [
            {"zone": "North Goa Beaches & Sunsets", "theme": "Vagator Clifftops, Anjuna Flea Market & Chapora Fort"},
            {"zone": "Old Goa & Latin Quarter", "theme": "Fontainhas Heritage Walk, Basilica of Bom Jesus & Pastel Havelis"},
            {"zone": "South Goa Serenity & Watersports", "theme": "Palolem Crescent Beach, Agonda Sands & Dolphin Cruises"},
            {"zone": "Panaji Waterfront & Mandovi River", "theme": "Floating River Cruises, Miramar Beach & Goan Seafood Shacks"}
        ]
    },
    "Kerala": {
        "name": "Kerala (Alleppey & Munnar), India",
        "country": "India",
        "coords": [9.9312, 76.2673],
        "currency": "INR",
        "best_months": "September - March (Tranquil Backwaters & Lush Emerald Hills)",
        "vibe_matches": ["Wellness, Hot Springs & Yoga", "Beach & Tropical Coastal", "Mountain & Alpine Nature"],
        "budget_level": "Moderate",
        "daily_cost_usd": 48,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 484 222 6543"},
        "clusters": [
            {"zone": "Fort Kochi Heritage & Arts", "theme": "Chinese Fishing Nets, Jew Town, Mattancherry & Kathakali"},
            {"zone": "Alleppey (Alappuzha) Backwaters", "theme": "Private Houseboat Cruise, Vembanad Canals & Village Life"},
            {"zone": "Munnar Misty Tea Estates", "theme": "Eravikulam Nilgiri Tahr, Top Station Panoramas & Tea Factory"},
            {"zone": "Marari Beach & Ayurvedic Wellness", "theme": "Pristine Palm Sands, Coconut Groves & Traditional Ayurvedic Spas"}
        ]
    },
    "Varanasi": {
        "name": "Varanasi (Kashi), India",
        "country": "India",
        "coords": [25.3176, 82.9739],
        "currency": "INR",
        "best_months": "October - March (Pleasant River Breezes & Sacred Evening Ceremonies)",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Wellness, Hot Springs & Yoga"],
        "budget_level": "Budget",
        "daily_cost_usd": 35,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 542 250 8555"},
        "clusters": [
            {"zone": "Dashashwamedh & Assi Ghats", "theme": "Sunrise Boat Row, Grand Maha Ganga Aarti & Morning Yoga"},
            {"zone": "Kashi Vishwanath & Ancient Lanes", "theme": "Golden Temple Corridor, Silk Weavers & Malaiyyo Chaat Trail"},
            {"zone": "Sarnath Buddhist Sacred Circle", "theme": "Dhamek Stupa, Deer Park & Ashoka Lion Capital Museum"},
            {"zone": "Manikarnika & Northern Heritage Ghats", "theme": "Centuries-Old Havelis, Scindia Ghat & Riverside Reflection"}
        ]
    },
    "Ladakh": {
        "name": "Ladakh (Leh & Pangong Tso), India",
        "country": "India",
        "coords": [34.1526, 77.5771],
        "currency": "INR",
        "best_months": "May - September (Clear High Passes & Vibrant Monastic Festivals)",
        "vibe_matches": ["Mountain & Alpine Nature", "Adrenaline & Outdoor Adventure", "Cultural & Historical Heritage"],
        "budget_level": "Moderate",
        "daily_cost_usd": 65,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 1982 252 018"},
        "clusters": [
            {"zone": "Leh Old Town & Royal Palace", "theme": "Leh Palace, Shanti Stupa, Thiksey Monastery & Tibetan Market"},
            {"zone": "Nubra Valley & Khardung La Pass", "theme": "World's Highest Motorable Pass, Diskit Buddha & Double-Humped Camels"},
            {"zone": "Pangong Tso High Altitude Lake", "theme": "Color-Changing Turquoise Waters & Star-Gazing Mountain Camps"},
            {"zone": "Magnetic Hill & Indus Sangam", "theme": "Confluence of Indus-Zanskar Rivers & Gurudwara Pathar Sahib"}
        ]
    },
    "Manali": {
        "name": "Manali & Solang Valley, India",
        "country": "India",
        "coords": [32.2396, 77.1887],
        "currency": "INR",
        "best_months": "March - June (Spring Pine Valleys) or December - February (Snow Sports)",
        "vibe_matches": ["Mountain & Alpine Nature", "Adrenaline & Outdoor Adventure", "Romantic Getaways & Sunsets"],
        "budget_level": "Budget",
        "daily_cost_usd": 40,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 1902 252 322"},
        "clusters": [
            {"zone": "Old Manali & Hadimba Cedar Forest", "theme": "Deodar Groves, Hadimba Temple, Bohemian Cafes & Live Music"},
            {"zone": "Solang Valley & Atal Tunnel", "theme": "Paragliding, Snow Canyons & Lahaul Sissu Waterfall Crossing"},
            {"zone": "Jogini Falls & Vashisht Springs", "theme": "Natural Sulphur Thermal Baths & Pine Forest Waterfall Hikes"},
            {"zone": "Naggar Castle Heritage Loop", "theme": "Nicholas Roerich Art Gallery & Wooden Himalayan Architecture"}
        ]
    },
    "Udaipur": {
        "name": "Udaipur (City of Lakes), India",
        "country": "India",
        "coords": [24.5854, 73.7125],
        "currency": "INR",
        "best_months": "October - March (Cool Lake Breezes & Romantic Royal Sunsets)",
        "vibe_matches": ["Romantic Getaways & Sunsets", "Cultural & Historical Heritage", "Culinary & Street Food Trail"],
        "budget_level": "Moderate",
        "daily_cost_usd": 55,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 294 241 1500"},
        "clusters": [
            {"zone": "Lake Pichola & City Palace", "theme": "Grand Mewar Palace, Boat Cruise to Jag Mandir & Ambrai Sunset"},
            {"zone": "Fateh Sagar & Saheliyon-ki-Bari", "theme": "Royal Fountains, Lakeside Coffee Promenades & Island Parks"},
            {"zone": "Monsoon Palace (Sajjangarh)", "theme": "Hilltop Fortress Panoramas over the Aravalli Valley"},
            {"zone": "Bagore Ki Haveli & Old Bazaar", "theme": "Dharohar Folk Dances, Gangaur Ghat & Heritage Miniature Art"}
        ]
    },
    "Amritsar": {
        "name": "Amritsar (Golden Temple), India",
        "country": "India",
        "coords": [31.6340, 74.8723],
        "currency": "INR",
        "best_months": "October - March (Crisp Winters & Legendary Punjabi Hospitality)",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Wellness, Hot Springs & Yoga"],
        "budget_level": "Budget",
        "daily_cost_usd": 35,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 183 222 5555"},
        "clusters": [
            {"zone": "Golden Temple & Heritage Street", "theme": "Harmandir Sahib Langar, Amrit Sarovar & Jallianwala Bagh"},
            {"zone": "Wagah Border Grand Trunk Road", "theme": "Beating Retreat Military Parade & Patriotic Spectacle"},
            {"zone": "Old City Kulcha & Lassi Trail", "theme": "World-Famous Butter Amritsari Kulcha & Kesar Da Dhaba"},
            {"zone": "Gobindgarh Fort & Partition Museum", "theme": "Sikh Martial History & Historic Town Hall Exhibits"}
        ]
    },
    "Rishikesh": {
        "name": "Rishikesh & Haridwar, India",
        "country": "India",
        "coords": [30.0869, 78.2676],
        "currency": "INR",
        "best_months": "September - November & February - May (Clean Himalayan Ganga, Rafting & Yoga)",
        "vibe_matches": ["Wellness, Hot Springs & Yoga", "Adrenaline & Outdoor Adventure", "Mountain & Alpine Nature"],
        "budget_level": "Budget",
        "daily_cost_usd": 38,
        "emergency": {"police": "100 / 112", "ambulance": "108", "tourist_police": "+91 135 243 0005"},
        "clusters": [
            {"zone": "Tapovan & Lakshman Jhula", "theme": "Himalayan Yoga Ashrams, Organic Cafes & Beatles Ashram Murals"},
            {"zone": "Ganga White Water & Shivpuri", "theme": "Grade III/IV River Rafting, Cliff Jumping & Eco-Camps"},
            {"zone": "Triveni Ghat & Parmarth Niketan", "theme": "Sunset Vedic Ganga Aarti & Riverbank Music"},
            {"zone": "Neelkanth & Forest Waterfalls", "theme": "Patna Hidden Waterfall Hike & Himalayan Valley Vistas"}
        ]
    },
    "Agra": {
        "name": "Agra, India",
        "country": "India",
        "coords": [27.1767, 78.0081],
        "currency": "INR",
        "best_months": "October - March (Cooler Weather for Monument Visits)",
        "vibe_matches": ["Cultural & Historical Heritage", "Romantic Getaways & Sunsets", "Photography Hotspots"],
        "budget_level": "Budget",
        "daily_cost_usd": 45,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Taj Mahal & Mehtab Bagh", "theme": "Marble Mausoleum, Yamuna River Views & Sunrise Photography"},
            {"zone": "Agra Fort & Old City", "theme": "Mughal Fortifications, Historic Gates & Traditional Bazaars"},
            {"zone": "Fatehpur Sikri", "theme": "Mughal Palace Courtyards, Buland Darwaza & Heritage Architecture"},
            {"zone": "Sadar Bazaar & Cantonment", "theme": "Local Sweets, Handicrafts & Market Walks"}
        ]
    },
    "Jodhpur": {
        "name": "Jodhpur, India",
        "country": "India",
        "coords": [26.2389, 73.0243],
        "currency": "INR",
        "best_months": "October - March (Dry, Pleasant Days)",
        "vibe_matches": ["Cultural & Historical Heritage", "Photography Hotspots", "Culinary & Street Food Trail"],
        "budget_level": "Budget",
        "daily_cost_usd": 42,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Mehrangarh Fort & Blue City", "theme": "Hilltop Fort, Indigo Lanes & Panoramic Rooftops"},
            {"zone": "Jaswant Thada & Rao Jodha Park", "theme": "Marble Cenotaphs, Desert Ecology & Rocky Trails"},
            {"zone": "Clock Tower & Sardar Market", "theme": "Spice Stalls, Handicrafts & Local Street Food"},
            {"zone": "Umaid Bhawan & Palace District", "theme": "Art Deco Palace, Royal Collections & Gardens"}
        ]
    },
    "Jaisalmer": {
        "name": "Jaisalmer, India",
        "country": "India",
        "coords": [26.9157, 70.9083],
        "currency": "INR",
        "best_months": "November - February (Cool Desert Days and Nights)",
        "vibe_matches": ["Cultural & Historical Heritage", "Adrenaline & Outdoor Adventure", "Romantic Getaways & Sunsets"],
        "budget_level": "Budget",
        "daily_cost_usd": 45,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Jaisalmer Fort & Havelis", "theme": "Living Sandstone Fort, Patwon Ki Haveli & Jain Temples"},
            {"zone": "Gadisar Lake & Royal Cenotaphs", "theme": "Historic Reservoir, Chhatris & Sunset Reflections"},
            {"zone": "Sam Sand Dunes", "theme": "Thar Desert Camel Rides, Dune Walks & Stargazing"},
            {"zone": "Kuldhara & Desert National Park", "theme": "Abandoned Village Heritage & Desert Wildlife"}
        ]
    },
    "Pushkar": {
        "name": "Pushkar, India",
        "country": "India",
        "coords": [26.4899, 74.6399],
        "currency": "INR",
        "best_months": "October - March (Mild Weather and Fair Season)",
        "vibe_matches": ["Cultural & Historical Heritage", "Wellness, Hot Springs & Yoga", "Culinary & Street Food Trail"],
        "budget_level": "Budget",
        "daily_cost_usd": 35,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Pushkar Lake & Ghats", "theme": "Sacred Lake, Historic Ghats & Sunset Walks"},
            {"zone": "Brahma Temple & Old Bazaar", "theme": "Pilgrimage Heritage, Rose Market & Vegetarian Cafes"},
            {"zone": "Savitri Mata Hill", "theme": "Ropeway Ride, Aravalli Views & Hilltop Sunset"},
            {"zone": "Camel Fair Grounds & Countryside", "theme": "Rural Trails, Camel Country & Seasonal Fairgrounds"}
        ]
    },
    "Bikaner": {
        "name": "Bikaner, India",
        "country": "India",
        "coords": [28.0229, 73.3119],
        "currency": "INR",
        "best_months": "November - February (Cool Desert Weather)",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Photography Hotspots"],
        "budget_level": "Budget",
        "daily_cost_usd": 38,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Junagarh Fort & Old City", "theme": "Ornate Palace Rooms, Courtyards & Walled-City Lanes"},
            {"zone": "Rampuria Havelis & Kote Gate", "theme": "Carved Red-Sandstone Facades & Traditional Markets"},
            {"zone": "National Research Centre on Camel", "theme": "Desert Camel Breeds, Museum & Farm Visits"},
            {"zone": "Lalgarh Palace & Gajner", "theme": "Royal Architecture, Museum Collections & Lakeside Nature"}
        ]
    },
    "Mount Abu": {
        "name": "Mount Abu, India",
        "country": "India",
        "coords": [24.5926, 72.7156],
        "currency": "INR",
        "best_months": "October - March (Cool Hill-Station Weather)",
        "vibe_matches": ["Mountain & Alpine Nature", "Romantic Getaways & Sunsets", "Cultural & Historical Heritage"],
        "budget_level": "Moderate",
        "daily_cost_usd": 48,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Dilwara Temples & Achalgarh", "theme": "Intricate Marble Carving, Jain Heritage & Hill Fort"},
            {"zone": "Nakki Lake & Town Center", "theme": "Boating, Lakeside Walks & Local Markets"},
            {"zone": "Guru Shikhar & Arbuda Hills", "theme": "Highest Aravalli Peak, Temple Views & Mountain Roads"},
            {"zone": "Sunset Point & Mount Abu Wildlife Sanctuary", "theme": "Rocky Viewpoints, Forest Trails & Native Wildlife"}
        ]
    },
    "Shimla": {
        "name": "Shimla, India",
        "country": "India",
        "coords": [31.1048, 77.1734],
        "currency": "INR",
        "best_months": "March - June (Mild Summers) and October - February (Winter Scenery)",
        "vibe_matches": ["Mountain & Alpine Nature", "Romantic Getaways & Sunsets", "Cultural & Historical Heritage"],
        "budget_level": "Moderate",
        "daily_cost_usd": 55,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "The Ridge & Mall Road", "theme": "Colonial-Era Buildings, Mountain Views & Cafe Walks"},
            {"zone": "Jakhu Hill & Temple", "theme": "Forest Ascent, Hilltop Shrine & Himalayan Vistas"},
            {"zone": "Viceregal Lodge & Summer Hill", "theme": "Historic Estate, Botanical Grounds & Quiet Trails"},
            {"zone": "Kufri & Mashobra", "theme": "Pine Forests, Open Meadows & Scenic Day Trips"}
        ]
    },
    "Dharamshala": {
        "name": "Dharamshala & McLeod Ganj, India",
        "country": "India",
        "coords": [32.2190, 76.3234],
        "currency": "INR",
        "best_months": "March - June and September - November (Clear Mountain Views)",
        "vibe_matches": ["Mountain & Alpine Nature", "Wellness, Hot Springs & Yoga", "Cultural & Historical Heritage"],
        "budget_level": "Moderate",
        "daily_cost_usd": 48,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "McLeod Ganj & Tsuglagkhang", "theme": "Tibetan Culture, Monastery Visits & Mountain Cafes"},
            {"zone": "Bhagsu & Dharamkot", "theme": "Waterfall Trails, Village Walks & Dhauladhar Views"},
            {"zone": "Dharamshala Stadium & Lower Town", "theme": "Himalayan Cricket Ground, Markets & Local Food"},
            {"zone": "Naddi & Dal Lake", "theme": "Forest Paths, Quiet Lake Shore & Sunset Mountain Panoramas"}
        ]
    },
    "Dalhousie": {
        "name": "Dalhousie, India",
        "country": "India",
        "coords": [32.5387, 75.9701],
        "currency": "INR",
        "best_months": "March - June and September - November (Pleasant Hill Weather)",
        "vibe_matches": ["Mountain & Alpine Nature", "Romantic Getaways & Sunsets", "Outdoor Hiking & Scenic Nature"],
        "budget_level": "Moderate",
        "daily_cost_usd": 45,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Gandhi Chowk & Subhash Baoli", "theme": "Colonial Walkways, Deodar Groves & Mountain Lookouts"},
            {"zone": "Panchpula & Bakrota Hills", "theme": "Forest Trails, Springs & Dhauladhar Views"},
            {"zone": "Khajjiar Meadows", "theme": "Open Alpine Meadow, Cedar Forest & Lake Walks"},
            {"zone": "Chamba Heritage Quarter", "theme": "Historic Temples, Riverfront & Regional Museum"}
        ]
    },
    "Spiti Valley": {
        "name": "Spiti Valley, India",
        "country": "India",
        "coords": [32.2461, 78.0349],
        "currency": "INR",
        "best_months": "June - September (Accessible High-Altitude Roads)",
        "vibe_matches": ["Mountain & Alpine Nature", "Adrenaline & Outdoor Adventure", "Cultural & Historical Heritage"],
        "budget_level": "Moderate",
        "daily_cost_usd": 60,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Kaza & Key Monastery", "theme": "High-Altitude Monastery, Valley Views & Local Market"},
            {"zone": "Kibber & Chicham Bridge", "theme": "Mountain Village, Deep Gorge Crossing & Wildlife Country"},
            {"zone": "Tabo & Dhankar", "theme": "Ancient Monastery Murals, Cliffside Gompa & Spiti River Views"},
            {"zone": "Langza, Hikkim & Komic", "theme": "High-Altitude Villages, Fossil Landscapes & Himalayan Roads"}
        ]
    },
    "Srinagar": {
        "name": "Srinagar, India",
        "country": "India",
        "coords": [34.0837, 74.7973],
        "currency": "INR",
        "best_months": "April - October (Gardens, Lakes and Alpine Scenery)",
        "vibe_matches": ["Mountain & Alpine Nature", "Romantic Getaways & Sunsets", "Cultural & Historical Heritage"],
        "budget_level": "Moderate",
        "daily_cost_usd": 60,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Dal Lake & Boulevard Road", "theme": "Shikara Rides, Houseboats & Floating Market"},
            {"zone": "Mughal Gardens", "theme": "Shalimar Bagh, Nishat Bagh & Terraced Flower Walks"},
            {"zone": "Old Srinagar & Jamia Masjid", "theme": "Wooden Architecture, Historic Lanes & Artisan Bazaars"},
            {"zone": "Pari Mahal & Shankaracharya Hill", "theme": "Hilltop Gardens, City Views & Lake Panoramas"}
        ]
    },
    "Gulmarg": {
        "name": "Gulmarg, India",
        "country": "India",
        "coords": [34.0484, 74.3805],
        "currency": "INR",
        "best_months": "December - March (Snow Sports) and May - September (Alpine Meadows)",
        "vibe_matches": ["Mountain & Alpine Nature", "Adrenaline & Outdoor Adventure", "Romantic Getaways & Sunsets"],
        "budget_level": "Moderate",
        "daily_cost_usd": 70,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Gulmarg Gondola & Apharwat", "theme": "Mountain Cable Car, Snow Views & High-Altitude Trails"},
            {"zone": "Gulmarg Golf Course & Meadows", "theme": "Alpine Grasslands, Pine Forests & Open-Air Walks"},
            {"zone": "St Mary's Church & Heritage Loop", "theme": "Historic Stone Church, Gulmarg Shrine & Meadow Paths"},
            {"zone": "Khilanmarg Viewpoints", "theme": "Wildflower Meadows, Valley Lookouts & Himalayan Peaks"}
        ]
    },
    "Pahalgam": {
        "name": "Pahalgam, India",
        "country": "India",
        "coords": [34.0161, 75.3144],
        "currency": "INR",
        "best_months": "April - October (Green Valleys and Clear River Walks)",
        "vibe_matches": ["Mountain & Alpine Nature", "Outdoor Hiking & Scenic Nature", "Romantic Getaways & Sunsets"],
        "budget_level": "Moderate",
        "daily_cost_usd": 58,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Lidder River & Pahalgam Center", "theme": "Riverside Walks, Pine Forests & Mountain Cafes"},
            {"zone": "Betaab Valley", "theme": "Meadow Trails, River Views & Snow-Capped Peaks"},
            {"zone": "Aru Valley", "theme": "Quiet Village, Alpine Scenery & Day Hikes"},
            {"zone": "Baisaran Meadow", "theme": "Open Grassland, Forested Slopes & Valley Panoramas"}
        ]
    },
    "Gangtok": {
        "name": "Gangtok, India",
        "country": "India",
        "coords": [27.3389, 88.6065],
        "currency": "INR",
        "best_months": "March - May and October - December (Clear Mountain Views)",
        "vibe_matches": ["Mountain & Alpine Nature", "Cultural & Historical Heritage", "Culinary & Street Food Trail"],
        "budget_level": "Moderate",
        "daily_cost_usd": 55,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "MG Marg & Central Gangtok", "theme": "Pedestrian Boulevard, Cafes & Himalayan Town Life"},
            {"zone": "Enchey Monastery & Ganesh Tok", "theme": "Buddhist Heritage, Forest Paths & Kanchenjunga Views"},
            {"zone": "Rumtek Monastery & Ranka", "theme": "Monastic Architecture, Prayer Halls & Mountain Roads"},
            {"zone": "Tsomgo Lake & Nathula Route", "theme": "High-Altitude Lake, Alpine Scenery & Borderland Landscapes"}
        ]
    },
    "Darjeeling": {
        "name": "Darjeeling, India",
        "country": "India",
        "coords": [27.0410, 88.2663],
        "currency": "INR",
        "best_months": "March - May and October - December (Views of the Himalayas)",
        "vibe_matches": ["Mountain & Alpine Nature", "Cultural & Historical Heritage", "Romantic Getaways & Sunsets"],
        "budget_level": "Moderate",
        "daily_cost_usd": 52,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Chowrasta & Mall Road", "theme": "Hilltop Promenade, Colonial Architecture & Mountain Air"},
            {"zone": "Tiger Hill & Ghoom", "theme": "Sunrise Mountain Lookout, Monastery & Heritage Railway"},
            {"zone": "Tea Estates & Happy Valley", "theme": "Tea Gardens, Factory Visits & Estate Walks"},
            {"zone": "Himalayan Mountaineering Institute", "theme": "Climbing Museum, Padmaja Naidu Zoo & Botanical Gardens"}
        ]
    },
    "Shillong": {
        "name": "Shillong, India",
        "country": "India",
        "coords": [25.5788, 91.8933],
        "currency": "INR",
        "best_months": "October - April (Cool Weather and Clearer Skies)",
        "vibe_matches": ["Mountain & Alpine Nature", "Culinary & Street Food Trail", "Outdoor Hiking & Scenic Nature"],
        "budget_level": "Budget",
        "daily_cost_usd": 42,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Police Bazaar & Ward's Lake", "theme": "City Markets, Garden Paths & Local Cafes"},
            {"zone": "Shillong Peak & Elephant Falls", "theme": "Forest Viewpoints, Waterfall Steps & Khasi Hills"},
            {"zone": "Laitlum Canyons", "theme": "Ridge Walks, Deep Valley Views & Open Highland Landscapes"},
            {"zone": "Don Bosco Museum & Mawphlang", "theme": "Northeast Heritage, Sacred Grove & Khasi Culture"}
        ]
    },
    "Cherrapunji": {
        "name": "Cherrapunji (Sohra), India",
        "country": "India",
        "coords": [25.2702, 91.7323],
        "currency": "INR",
        "best_months": "October - May (Waterfalls and Trails; Monsoon Is Very Wet)",
        "vibe_matches": ["Mountain & Alpine Nature", "Adrenaline & Outdoor Adventure", "Photography Hotspots"],
        "budget_level": "Budget",
        "daily_cost_usd": 42,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Nohkalikai Falls & Sohra Plateau", "theme": "High Waterfall Viewpoints, Cliffs & Monsoon Landscapes"},
            {"zone": "Mawsmai Cave & Eco Park", "theme": "Limestone Cave Walk, Forest Paths & Valley Lookouts"},
            {"zone": "Nongriat Living Root Bridges", "theme": "Village Trek, Living Root Bridge & Natural Pools"},
            {"zone": "Seven Sisters Falls & Arwah Cave", "theme": "Layered Waterfalls, Limestone Formations & Scenic Trails"}
        ]
    },
    "Kaziranga": {
        "name": "Kaziranga National Park, India",
        "country": "India",
        "coords": [26.5775, 93.1711],
        "currency": "INR",
        "best_months": "November - April (Park Open and Wildlife Viewing Season)",
        "vibe_matches": ["Outdoor Hiking & Scenic Nature", "Adrenaline & Outdoor Adventure", "Photography Hotspots"],
        "budget_level": "Moderate",
        "daily_cost_usd": 65,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Central Range & Kohora", "theme": "Grassland Safaris, Rhino Habitat & Wetland Birds"},
            {"zone": "Western Range & Bagori", "theme": "Wildlife Viewing, Riverine Grasslands & Forest Edges"},
            {"zone": "Eastern Range & Agoratoli", "theme": "Waterbird Wetlands, Floodplain Forests & Boatland Views"},
            {"zone": "Tea Gardens & Kaziranga Villages", "theme": "Assam Tea Country, Local Crafts & Rural Landscapes"}
        ]
    },
    "Guwahati": {
        "name": "Guwahati, India",
        "country": "India",
        "coords": [26.1445, 91.7362],
        "currency": "INR",
        "best_months": "October - April (Comfortable Weather and River Excursions)",
        "vibe_matches": ["Cultural & Historical Heritage", "Culinary & Street Food Trail", "Outdoor Hiking & Scenic Nature"],
        "budget_level": "Budget",
        "daily_cost_usd": 40,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Kamakhya Hill & Nilachal", "theme": "Hilltop Temple, Pilgrimage Heritage & Brahmaputra Views"},
            {"zone": "Brahmaputra Riverfront & Umananda", "theme": "River Ferry, Peacock Island & Sunset Boat Ride"},
            {"zone": "Assam State Museum & Pan Bazaar", "theme": "Regional History, Handloom Shops & Old-City Walks"},
            {"zone": "Deepor Beel & Sualkuchi", "theme": "Wetland Birdlife, Assamese Silk & Craft Traditions"}
        ]
    },
    "Tawang": {
        "name": "Tawang, India",
        "country": "India",
        "coords": [27.5861, 91.8594],
        "currency": "INR",
        "best_months": "March - May and September - November (Road and Weather Conditions Vary)",
        "vibe_matches": ["Mountain & Alpine Nature", "Cultural & Historical Heritage", "Outdoor Hiking & Scenic Nature"],
        "budget_level": "Moderate",
        "daily_cost_usd": 58,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Tawang Monastery & Old Town", "theme": "Major Buddhist Monastery, Prayer Halls & Mountain Town"},
            {"zone": "Sela Pass & Jaswant Garh", "theme": "High Mountain Pass, Alpine Lake & Memorial"},
            {"zone": "Bum La Route & Sangestar Tso", "theme": "High-Altitude Lakes, Himalayan Landscapes & Border Route"},
            {"zone": "Nuranang Falls & Jang", "theme": "Forest Waterfall, River Valley & Scenic Mountain Road"}
        ]
    },
    "Bhubaneswar": {
        "name": "Bhubaneswar, India",
        "country": "India",
        "coords": [20.2961, 85.8245],
        "currency": "INR",
        "best_months": "October - March (Milder Weather for Temple Visits)",
        "vibe_matches": ["Cultural & Historical Heritage", "Art & Architecture", "Culinary & Street Food Trail"],
        "budget_level": "Budget",
        "daily_cost_usd": 38,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Old Town & Lingaraj Temple", "theme": "Kalinga Temple Architecture, Sacred Tanks & Heritage Lanes"},
            {"zone": "Udayagiri & Khandagiri Caves", "theme": "Ancient Jain Caves, Rock Inscriptions & City Views"},
            {"zone": "Dhauli & Daya River", "theme": "Peace Pagoda, Ashokan History & Riverside Landscapes"},
            {"zone": "Ekamra Haat & Museum District", "theme": "Odisha Crafts, Textiles, Food Stalls & Regional History"}
        ]
    },
    "Puri": {
        "name": "Puri, India",
        "country": "India",
        "coords": [19.8135, 85.8312],
        "currency": "INR",
        "best_months": "October - February (Pleasant Beach Weather)",
        "vibe_matches": ["Beach & Tropical Coastal", "Cultural & Historical Heritage", "Culinary & Street Food Trail"],
        "budget_level": "Budget",
        "daily_cost_usd": 38,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Puri Beach & Marine Drive", "theme": "Bay of Bengal Shoreline, Sunrise Walks & Local Snacks"},
            {"zone": "Jagannath Temple & Grand Road", "theme": "Pilgrimage Heritage, Market Streets & Traditional Crafts"},
            {"zone": "Chilika Lake & Satapada", "theme": "Lagoon Boat Trips, Birdlife & Coastal Landscapes"},
            {"zone": "Raghurajpur Craft Village", "theme": "Pattachitra Art, Palm-Leaf Painting & Artisan Homes"}
        ]
    },
    "Konark": {
        "name": "Konark, India",
        "country": "India",
        "coords": [19.8876, 86.0945],
        "currency": "INR",
        "best_months": "October - February (Comfortable Heritage Walks)",
        "vibe_matches": ["Cultural & Historical Heritage", "Art & Architecture", "Photography Hotspots"],
        "budget_level": "Budget",
        "daily_cost_usd": 35,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Sun Temple & Archaeological Park", "theme": "UNESCO Stone Chariot, Carved Wheels & Temple Sculptures"},
            {"zone": "Chandrabhaga Beach", "theme": "Coastal Sunrise, Fishing Boats & Quiet Shoreline"},
            {"zone": "Konark Museum & Heritage Walk", "theme": "Sculpture Conservation, Temple History & Local Crafts"},
            {"zone": "Pipili & Raghurajpur Excursion", "theme": "Applique Textiles, Pattachitra Art & Village Workshops"}
        ]
    },
    "Chennai": {
        "name": "Chennai, India",
        "country": "India",
        "coords": [13.0827, 80.2707],
        "currency": "INR",
        "best_months": "November - February (Cooler Weather for City Exploring)",
        "vibe_matches": ["Cultural & Historical Heritage", "Beach & Tropical Coastal", "Culinary & Street Food Trail"],
        "budget_level": "Moderate",
        "daily_cost_usd": 55,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Marina Beach & Mylapore", "theme": "Coastal Promenade, Kapaleeshwarar Temple & South Indian Food"},
            {"zone": "Fort St George & George Town", "theme": "Colonial History, Museum Collections & Bazaars"},
            {"zone": "Government Museum & Egmore", "theme": "Archaeology, Bronze Galleries & Public Gardens"},
            {"zone": "Besant Nagar & Adyar", "theme": "Elliot's Beach, Theosophical Gardens & Cafe Culture"}
        ]
    },
    "Bengaluru": {
        "name": "Bengaluru, India",
        "country": "India",
        "coords": [12.9716, 77.5946],
        "currency": "INR",
        "best_months": "October - February (Mild Weather and Outdoor Events)",
        "vibe_matches": ["Urban Pulse & Modern Architecture", "Culinary & Street Food Trail", "Outdoor Hiking & Scenic Nature"],
        "budget_level": "Moderate",
        "daily_cost_usd": 60,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Cubbon Park & Vidhana Soudha", "theme": "Green City Park, State Architecture & Central Galleries"},
            {"zone": "Bengaluru Palace & Malleshwaram", "theme": "Royal Interiors, Traditional Markets & Local Eateries"},
            {"zone": "Lalbagh & Basavanagudi", "theme": "Botanical Glasshouse, Bull Temple & South Indian Food"},
            {"zone": "Indiranagar & Church Street", "theme": "Independent Cafes, Bookshops & Contemporary City Life"}
        ]
    },
    "Ooty": {
        "name": "Ooty, India",
        "country": "India",
        "coords": [11.4102, 76.6950],
        "currency": "INR",
        "best_months": "October - June (Cool Hill-Station Climate)",
        "vibe_matches": ["Mountain & Alpine Nature", "Romantic Getaways & Sunsets", "Outdoor Hiking & Scenic Nature"],
        "budget_level": "Moderate",
        "daily_cost_usd": 50,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Ooty Lake & Town Center", "theme": "Boating, Botanical Gardens & Heritage Streets"},
            {"zone": "Doddabetta Peak & Tea Museum", "theme": "Nilgiri Viewpoints, Tea Tasting & Mountain Air"},
            {"zone": "Coonoor & Sim's Park", "theme": "Toy Train Scenery, Botanical Paths & Tea Estates"},
            {"zone": "Pykara Falls & Pine Forest", "theme": "Forest Walks, Waterfalls & Lakeside Landscapes"}
        ]
    },
    "Coorg": {
        "name": "Coorg (Kodagu), India",
        "country": "India",
        "coords": [12.3375, 75.8069],
        "currency": "INR",
        "best_months": "October - March (Coffee Harvest and Clearer Weather)",
        "vibe_matches": ["Mountain & Alpine Nature", "Outdoor Hiking & Scenic Nature", "Wellness, Hot Springs & Yoga"],
        "budget_level": "Moderate",
        "daily_cost_usd": 52,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Madikeri Fort & Raja's Seat", "theme": "Hilltop Gardens, Historic Fort & Sunset Valley Views"},
            {"zone": "Abbey Falls & Coffee Estates", "theme": "Forest Waterfall, Plantation Walks & Coffee Tasting"},
            {"zone": "Dubare & Kaveri Riverside", "theme": "Riverbank Nature, Forest Trails & Wildlife Country"},
            {"zone": "Talacauvery & Bhagamandala", "theme": "Sacred River Source, Mountain Roads & Temple Heritage"}
        ]
    },
    "Puducherry": {
        "name": "Puducherry, India",
        "country": "India",
        "coords": [11.9416, 79.8083],
        "currency": "INR",
        "best_months": "November - February (Mild Coastal Weather)",
        "vibe_matches": ["Beach & Tropical Coastal", "Romantic Getaways & Sunsets", "Cultural & Historical Heritage"],
        "budget_level": "Moderate",
        "daily_cost_usd": 50,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "White Town & Promenade", "theme": "Colonial Streets, Seafront Walks & Heritage Cafes"},
            {"zone": "Auroville & Matrimandir", "theme": "International Community, Meditation Spaces & Green Design"},
            {"zone": "Heritage Quarter & Tamil Town", "theme": "Temples, Local Markets & Indo-French Architecture"},
            {"zone": "Paradise Beach & Chunnambar", "theme": "Ferry Ride, Sandy Shore & Coastal Views"}
        ]
    },
    "Andaman Islands": {
        "name": "Andaman Islands, India",
        "country": "India",
        "coords": [11.6234, 92.7265],
        "currency": "INR",
        "best_months": "October - May (Calmer Seas and Island Activities)",
        "vibe_matches": ["Beach & Tropical Coastal", "Adrenaline & Outdoor Adventure", "Romantic Getaways & Sunsets"],
        "budget_level": "Moderate",
        "daily_cost_usd": 75,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Port Blair & Cellular Jail", "theme": "Island History, Museum Galleries & Evening Light Show"},
            {"zone": "Swaraj Dweep (Havelock)", "theme": "Radhanagar Beach, Coral Reefs & Snorkeling"},
            {"zone": "Shaheed Dweep (Neil)", "theme": "Natural Rock Bridge, Quiet Beaches & Reef Life"},
            {"zone": "Baratang Island", "theme": "Mangrove Boat Ride, Limestone Caves & Forest Landscapes"}
        ]
    },
    "Lakshadweep": {
        "name": "Lakshadweep, India",
        "country": "India",
        "coords": [10.5667, 72.6417],
        "currency": "INR",
        "best_months": "October - May (Dry Season and Better Sea Conditions)",
        "vibe_matches": ["Beach & Tropical Coastal", "Adrenaline & Outdoor Adventure", "Wellness, Hot Springs & Yoga"],
        "budget_level": "Luxury",
        "daily_cost_usd": 100,
        "emergency": {"police": "112", "ambulance": "112"},
        "clusters": [
            {"zone": "Agatti Island & Lagoon", "theme": "Turquoise Lagoon, Reef Snorkeling & Island Airstrip"},
            {"zone": "Bangaram Island", "theme": "Coral Atoll, Clear Water & Beach Walks"},
            {"zone": "Kavaratti Island", "theme": "Island Capital, Marine Aquarium & Lagoon Activities"},
            {"zone": "Kadmat Island", "theme": "Long Sandy Beach, Scuba Diving & Reef Exploration"}
        ]
    }
}
