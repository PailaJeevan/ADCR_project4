# Report Generator Module
""" Generates a styled PDF report summarizing document details. """
# Note: Large PDFs (>50 pages) may take 10-20 seconds
# Consider adding progress indicator for production use

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import datetime

def generating_pdf(file_path, report_data):# Generate a styled PDF report
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4
    
    # Colors
    header_color = colors.HexColor("#2C3E50")
    accent_color = colors.HexColor("#3498DB")
    section_bg = colors.HexColor("#ECF0F1")
    text_color = colors.HexColor("#34495E")
    
    # Header Section with Background
    c.setFillColor(header_color)
    c.rect(0, height - 80, width, 80, fill=True, stroke=False)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(40, height - 45, "Document Processing Report")
    
    c.setFont("Helvetica", 10)
    c.drawString(40, height - 65, f"Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
    
    y = height - 110
    
    # Document Name Section
    c.setFillColor(section_bg)
    c.rect(30, y - 35, width - 60, 45, fill=True, stroke=False)
    
    c.setFillColor(header_color)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y - 15, report_data.get("Document Name", "Unknown"))
    
    c.setFillColor(accent_color)
    c.setFont("Helvetica-Bold", 11)
    category = report_data.get("Category", "Uncategorized")
    c.drawString(40, y - 30, f"Category: {category}")
    
    y -= 65
    
    # Summary Section
    c.setFillColor(header_color)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40, y, "Summary")
    c.setStrokeColor(accent_color)
    c.setLineWidth(2)
    c.line(40, y - 5, 150, y - 5)
    
    y -= 25
    c.setFillColor(text_color)
    c.setFont("Helvetica", 10)
    
    summary = report_data.get("Summary", "No summary available")
    # Word wrap summary
    max_width = width - 100
    words = summary.split()
    line = ""
    for word in words:
        test_line = line + word + " "
        if c.stringWidth(test_line, "Helvetica", 10) < max_width:
            line = test_line
        else:
            c.drawString(50, y, line.strip())
            y -= 15
            line = word + " "
            if y < 100:
                c.showPage()
                y = height - 40
                c.setFillColor(text_color)
                c.setFont("Helvetica", 10)
    if line:
        c.drawString(50, y, line.strip())
    
    y -= 35
    
    # Details Section
    if y < 250:
        c.showPage()
        y = height - 40
    
    c.setFillColor(header_color)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40, y, "Document Details")
    c.setStrokeColor(accent_color)
    c.setLineWidth(2)
    c.line(40, y - 5, 180, y - 5)
    
    y -= 25
    
    # Create two-column layout for details
    details = [
        ("Word Count", report_data.get("Word Count", "N/A")),
        ("Character Count", report_data.get("Character Count", "N/A")),
        ("Dates Found", len(report_data.get("Dates Found", []))),
        ("Amounts Found", len(report_data.get("Amounts Found", []))),
    ]
    
    c.setFillColor(section_bg)
    for i, (label, value) in enumerate(details):
        box_y = y - (i * 35)
        c.rect(40, box_y - 25, 220, 30, fill=True, stroke=False)
        
        c.setFillColor(header_color)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, box_y - 8, label)
        
        c.setFillColor(accent_color)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, box_y - 20, str(value))
    
    y -= len(details) * 35 + 20
    
    # Keywords Section
    if y < 150:
        c.showPage()
        y = height - 40
    
    c.setFillColor(header_color)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40, y, "Top Keywords")
    c.setStrokeColor(accent_color)
    c.setLineWidth(2)
    c.line(40, y - 5, 150, y - 5)
    
    y -= 25
    
    keywords = report_data.get("Keywords", [])
    if keywords:
        c.setFont("Helvetica", 10)
        for i, keyword in enumerate(keywords[:5], 1):
            c.setFillColor(section_bg)
            c.roundRect(50, y - 18, c.stringWidth(f" {i}. {keyword} ", "Helvetica", 10) + 10, 20, 5, fill=True, stroke=False)
            
            c.setFillColor(text_color)
            c.drawString(55, y - 12, f"{i}. {keyword}")
            y -= 28
    else:
        c.setFillColor(text_color)
        c.drawString(50, y, "No keywords extracted")
        y -= 25
    
    # Footer
    c.setStrokeColor(accent_color)
    c.setLineWidth(1)
    c.line(40, 50, width - 40, 50)
    
    c.setFillColor(colors.grey)
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(40, 35, "Automated Document Processing System")
    c.drawRightString(width - 40, 35, "Confidential")
    
    c.save()

