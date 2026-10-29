"""PDF Generator using ReportLab for Offline Travel Itinerary Guides (Epic 5).

Generates a publication-grade, beautifully formatted PDF travel guide with
emergency contacts, geographic clusters, packing checklists, and day-by-day itineraries.
"""

import io
from typing import Dict, Any
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.pdfgen import canvas
from modules.config import CURRENCIES, DESTINATION_CATALOG

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and print total page numbers."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        # Footer
        footer_text = f"Personalized Travel Itinerary Planner • Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 36, 24, footer_text)
        self.drawString(36, 24, "CONFIDENTIAL & TAILORED FOR TRAVELER • ZERO-BACKTRACKING ROUTE")
        self.restoreState()


def _clean_pdf_text(text: str) -> str:
    """Sanitize text to be 100% safe for standard ReportLab Helvetica font (Latin-1)."""
    if not text:
        return ""
    # Map common currency symbols and symbols to ASCII/Latin-1 safe equivalents
    replacements = {
        "₹": "INR ",
        "€": "EUR ",
        "£": "GBP ",
        "¥": "JPY ",
        "A$": "AUD ",
        "C$": "CAD ",
        "•": "*",
        "—": "-",
        "–": "-",
        '"': '"',
        '"': '"',
        ''': "'",
        ''': "'",
        "🌍": "",
        "🚨": "",
        "🎒": "",
        "🗓️": "",
        "🗓": "",
        "📍": "",
        "🚆": "",
        "🚶‍♂️": "",
        "🚶": "",
        "🍽️": "",
        "🍽": "",
        "🌅": "",
        "🏛️": "",
        "🏛": "",
        "🌙": "",
        "✨": "",
        "✈️": "",
        "✈": "",
        "💡": "",
        "📌": ""
    }
    cleaned = text
    for k, v in replacements.items():
        cleaned = cleaned.replace(k, v)
    
    # Strip any remaining characters outside latin-1
    return cleaned.encode('latin-1', 'ignore').decode('latin-1').strip()


def generate_itinerary_pdf(itinerary: Dict[str, Any], currency: str = "USD") -> io.BytesIO:
    """Generate high-quality PDF buffer from itinerary dictionary."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # Custom styles
    primary_color = colors.HexColor("#0F766E")
    secondary_color = colors.HexColor("#0D9488")
    dark_slate = colors.HexColor("#0F172A")
    light_bg = colors.HexColor("#F8FAFC")
    border_color = colors.HexColor("#E2E8F0")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#475569"),
        spaceAfter=12
    )

    section_heading = ParagraphStyle(
        'SectionHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=dark_slate
    )

    cluster_badge_style = ParagraphStyle(
        'ClusterBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#0F766E")
    )

    story = []

    # 1. Header Banner & Title
    raw_dest = itinerary.get("destination", "Destination")
    raw_title = itinerary.get('trip_title', f'Travel Itinerary: {raw_dest}')
    destination = _clean_pdf_text(raw_dest)
    trip_title = _clean_pdf_text(raw_title)

    duration = itinerary.get("duration_days", len(itinerary.get("days", [])))
    budget_tier = _clean_pdf_text(str(itinerary.get("budget_tier", "Moderate")))
    curr_label = "INR " if currency == "INR" else (CURRENCIES.get(currency, {"symbol": "$"}).get("symbol", "$"))
    if curr_label == "₹":
        curr_label = "INR "

    total_local = itinerary.get("total_cost_local", 0.0)
    total_usd = itinerary.get("total_cost_usd", 0.0)

    story.append(Paragraph(f"Travel Itinerary: {trip_title}", title_style))
    story.append(Paragraph(f"Destination: <b>{destination}</b> | Duration: <b>{duration} Days</b> | Tier: <b>{budget_tier}</b> | Curated with Intelligent Route Clustering", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=secondary_color, spaceAfter=10))

    # 2. Executive Trip Metrics Table
    summary_data = [
        [
            Paragraph(f"<b>Total Budget:</b><br/>{curr_label}{total_local:,.1f} (${total_usd:,.1f} USD)", body_style),
            Paragraph(f"<b>Daily Average:</b><br/>{curr_label}{(total_local/max(1, duration)):,.1f} (${(total_usd/max(1, duration)):,.1f} USD)", body_style),
            Paragraph(f"<b>Route Optimization:</b><br/>Zero-Backtracking Geographic Clusters", body_style),
            Paragraph(f"<b>Field Guide:</b><br/>Offline Ready Travel Document", body_style),
        ]
    ]
    summary_table = Table(summary_data, colWidths=[135, 135, 140, 130])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), light_bg),
        ('BOX', (0, 0), (-1, -1), 1, border_color),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, border_color),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 10))

    # 3. Emergency Contacts & Local Safety Checklist
    story.append(Paragraph("Emergency Contacts & Safety Protocol", section_heading))
    
    cat_match = None
    for k, v in DESTINATION_CATALOG.items():
        if k.lower() in destination.lower():
            cat_match = v
            break

    police_no = _clean_pdf_text(cat_match["emergency"]["police"]) if cat_match else "112 / 911"
    ambulance_no = _clean_pdf_text(cat_match["emergency"].get("ambulance", "112")) if cat_match else "112"
    tourist_line = _clean_pdf_text(cat_match["emergency"].get("tourist_hotline", cat_match["emergency"].get("tourist_police", "Check Local Embassy"))) if cat_match else "Local Tourist Police"

    emerg_data = [
        [
            Paragraph("<b>Emergency Service</b>", body_style),
            Paragraph("<b>Contact Number / Details</b>", body_style),
            Paragraph("<b>Action Protocol</b>", body_style)
        ],
        [
            Paragraph("Local Police", body_style),
            Paragraph(f"<b>{police_no}</b>", body_style),
            Paragraph("Keep physical and offline digital copies of passport and visa documents.", body_style)
        ],
        [
            Paragraph("Medical & Ambulance", body_style),
            Paragraph(f"<b>{ambulance_no}</b>", body_style),
            Paragraph("Verify travel health insurance policy number and international clinic network.", body_style)
        ],
        [
            Paragraph("Tourist Helpline", body_style),
            Paragraph(f"<b>{tourist_line}</b>", body_style),
            Paragraph("Multilingual assistance for lost items, consular assistance, and transit safety.", body_style)
        ]
    ]
    emerg_table = Table(emerg_data, colWidths=[120, 140, 280])
    emerg_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#FEF2F2")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#991B1B")),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor("#FCA5A5")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#FEE2E2")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(emerg_table)
    story.append(Spacer(1, 10))

    # 4. Essential Packing Checklist
    story.append(Paragraph("Smart Travel Packing Checklist", section_heading))
    pack_data = [
        [
            Paragraph("<b>Documentation & Money:</b><br/>* Passport + physical photo copies<br/>* 2x No-FTF cards + local cash reserve<br/>* Offline tickets and lodging vouchers", body_style),
            Paragraph("<b>Electronics & Navigation:</b><br/>* Universal plug adapter + power bank<br/>* Offline map areas downloaded<br/>* Local eSIM / physical SIM QR codes", body_style),
            Paragraph("<b>Health & Comfort:</b><br/>* Prescription medicines + basic first aid<br/>* Weather-tailored layers + walking shoes<br/>* Reusable water bottle + compact umbrella", body_style),
        ]
    ]
    pack_table = Table(pack_data, colWidths=[180, 180, 180])
    pack_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F0FDF4")),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor("#86EFAC")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#DCFCE7")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(pack_table)
    story.append(Spacer(1, 14))

    # 5. Day-by-Day Detailed Schedule
    story.append(Paragraph("Optimized Day-by-Day Schedule (Geographically Clustered)", section_heading))

    for day in itinerary.get("days", []):
        day_num = day.get("day_number", 1)
        cluster_name = _clean_pdf_text(day.get("cluster_name", "District Center"))
        day_total_l = day.get("day_total_local", 0.0)
        day_total_u = day.get("day_total_usd", 0.0)
        cum_total_l = day.get("cumulative_total_local", 0.0)
        transit_tip = _clean_pdf_text(day.get("daily_transit_tip", "Walkable district."))

        day_elements = []

        header_text = f"<b>DAY {day_num}: {cluster_name}</b> | Day: {curr_label}{day_total_l:,.1f} (${day_total_u:,.1f}) | Running Total: {curr_label}{cum_total_l:,.1f}"
        day_elements.append(Paragraph(header_text, cluster_badge_style))
        day_elements.append(Paragraph(f"<i>Transit Strategy: {transit_tip}</i>", body_style))
        day_elements.append(Spacer(1, 4))

        slot_rows = [
            [
                Paragraph("<b>Time / Slot</b>", body_style),
                Paragraph("<b>Activity & Experience Description</b>", body_style),
                Paragraph("<b>Location / Transit</b>", body_style),
                Paragraph("<b>Est. Cost</b>", body_style),
            ]
        ]

        for s in day.get("slots", []):
            slot_type = _clean_pdf_text(s.get("slot_type", "Sightseeing"))
            time_str = _clean_pdf_text(s.get("time", ""))
            title = _clean_pdf_text(s.get("title", ""))
            desc = _clean_pdf_text(s.get("description", ""))
            loc = _clean_pdf_text(s.get("location", ""))
            transit = _clean_pdf_text(s.get("transit_to_next", ""))
            c_l = s.get("cost_local", 0.0)
            c_u = s.get("cost_usd", 0.0)

            col1_content = f"<b>{time_str}</b><br/><font color='#0D9488'>{slot_type}</font>"
            col2_content = f"<b>{title}</b><br/>{desc}"
            col3_content = f"Location: {loc}" + (f"<br/><i>Transit: {transit}</i>" if transit else "")
            col4_content = f"<b>{curr_label}{c_l:,.1f}</b><br/><font color='#64748B'>(${c_u:,.1f})</font>"

            slot_rows.append([
                Paragraph(col1_content, body_style),
                Paragraph(col2_content, body_style),
                Paragraph(col3_content, body_style),
                Paragraph(col4_content, body_style),
            ])

        slots_table = Table(slot_rows, colWidths=[90, 240, 140, 70])
        slots_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
            ('BOX', (0, 0), (-1, -1), 0.8, border_color),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, border_color),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        day_elements.append(slots_table)
        day_elements.append(Spacer(1, 10))

        story.append(KeepTogether(day_elements))

    # Build document with NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    buffer.seek(0)
    return buffer
