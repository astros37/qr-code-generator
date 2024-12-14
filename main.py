import qrcode

def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(output_file)
    print(f"QR-код збережено як {output_file}")

if __name__ == "__main__":
    data = input("Введіть текст або URL для QR-коду: ")
    output_file = "qr_code.png"
    generate_qr_code(data, output_file)
