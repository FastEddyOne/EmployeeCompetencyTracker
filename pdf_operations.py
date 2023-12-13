import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(file_name, data):
    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)

    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    y_position = height - 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, y_position, "User Competency Summary Report")
    y_position -= 40

    c.setFont("Helvetica", 12)

    for item in data:
        c.drawString(30, y_position, item)
        y_position -= 20

        if y_position < 40:
            c.showPage()
            y_position = height - 40

    c.save()
