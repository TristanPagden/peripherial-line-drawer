from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def add_vertical_lines_to_pdf(input_pdf, output_pdf, line_positions):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        # Create a temporary PDF with vertical lines
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        width, height = letter
        ##### width is 612

        # Add vertical lines at specified positions
        for x in line_positions:
            can.line(x, 0, x, height)

        can.save()
        packet.seek(0)

        # Merge the line overlay with the current page
        overlay_reader = PdfReader(packet)
        page.merge_page(overlay_reader.pages[0])
        writer.add_page(page)

    # Write the updated PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

# Example usage
input_pdf = "input.pdf"
output_pdf = "output_with_lines.pdf"
line_positions = [125, 487]  # X-coordinates for vertical lines
add_vertical_lines_to_pdf(input_pdf, output_pdf, line_positions)
