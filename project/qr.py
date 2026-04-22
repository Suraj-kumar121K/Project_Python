import qrcode
from PIL import Image
import os

data = """
Name: Anish
Phone: 7667795227
GitHub: https://github.com/Suraj-kumar121K
"""

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

logo_path = "logo.png"

if os.path.exists(logo_path):
    logo = Image.open(logo_path)

    logo_size = 80
    logo = logo.resize((logo_size, logo_size))

    qr_width, qr_height = qr_img.size
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    qr_img.paste(logo, pos)

else:
    print("⚠ logo.png not found, QR generated without logo")

qr_img.save("advanced_qr.png")
qr_img.show()

print("QR Code created successfully!")