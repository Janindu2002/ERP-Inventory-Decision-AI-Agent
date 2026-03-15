from reportlab.pdfgen import canvas


def generate_invoice(product, quantity, supplier, cost):

    filename = f"invoice_{product}.pdf"

    c = canvas.Canvas(filename)

    c.drawString(100, 800, "Reorder Invoice")
    c.drawString(100, 760, f"Product: {product}")
    c.drawString(100, 740, f"Quantity: {quantity}")
    c.drawString(100, 720, f"Supplier: {supplier}")
    c.drawString(100, 700, f"Unit Cost: ${cost}")
    c.drawString(100, 680, f"Total Cost: ${quantity * cost}")

    c.save()

    print("Invoice created:", filename)