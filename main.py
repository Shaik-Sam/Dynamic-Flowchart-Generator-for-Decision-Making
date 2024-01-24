from fpdf import FPDF
from PIL import Image
import os
print("Current Working Directory:", os.getcwd())

def main():
    flowchart = input(" **SELECT YOUR TOPIC**\n"
    "1. WhatNext After Graduation\n"
    "2. WhatNext After Intermediate\n"
    "3. WhatNext After 10 th class\n"
    "4. Gradution courses\n"
    "5. Talent tests (from school to intermediate)\n"
    "6. Fashion Design\n"
    "7. Agriculture & Hotel Management\n"
    "8. Law\n"
    "9. Marine, Navy, Defence\n"
    "10. Medical\n"
    "11. Engineering Exams\n"
    "12. EXAMS (cets)- after Intermediate:  ")
    name = input("Type your name: ")

    text_img = flowchart + ".png"

    pdf_name = str(name + "_" + flowchart + ".pdf")

    create_pdf(text_img, pdf_name)
    print("PDF", pdf_name, "created successfully")

def create_pdf(img_path, output):
    pdf = FPDF(unit='mm', format=(420, 297))
    pdf.add_page()
    pdf.set_line_width(0.4)
    pdf.set_draw_color(0)
    pdf.set_fill_color(r=255, g=255, b=255)

    # Import and display the image in the PDF
    x, y, w, h = 30, 30, 150, 150  # Adjust position and size as needed
    pdf.image(img_path, x=x, y=y, w=w, h=h)

    pdf.set_font("Helvetica", size=11)
    pdf.cell(0, 30, "Flowchart", ln=True, align='C')  # Modify the text as needed
    pdf.set_font("Helvetica", size=30)
    pdf.set_line_width(0.3)
    pdf.set_draw_color(0)
    pdf.line(x1=0, y1=250, x2=420, y2=250)
    pdf.output(output)

if __name__ == "__main__":
    main()
