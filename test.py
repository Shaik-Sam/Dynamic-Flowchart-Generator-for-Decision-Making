from fpdf import FPDF
import os

print("Current Working Directory:", os.getcwd())

def main():
    print("**SELECT YOUR TOPIC**")
    print("1. Agriculture and Hotel Management Flow Chart")
    print("2. Engineering Exam Flow Chart")
    print("3. Graduation Course Flow Chart")
    print("4. Marine, Navy, Defence Flow Chart")
    print("5. Medical Flow Chart")
    print("6. WhatNext After Graduation")
    print("7. WhatNext After Intermediate")
    print("8. WhatNext After 10 th class")

    choice = int(input("Enter your choice (1-8): "))
    name = input("Type your name: ")

    topics = [
        "Agriculture and Hotel Management",
        "Engineering Exam",
        "Graduation Course",
        "Marine, Navy, Defence",
        "Medical",
        "WhatNext After Graduation",
        "WhatNext After Intermediate",
        "WhatNext After 10th class",
    ]

    flowchart = topics[choice - 1]
    text_img = f"{flowchart} Flow Chart.png"
    pdf_name = f"{name}_{flowchart} Flow Chart.pdf"

    create_pdf(text_img, pdf_name)
    print(f"PDF {pdf_name} created successfully")

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
