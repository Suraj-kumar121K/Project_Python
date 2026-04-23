import qrcode
from PIL import Image, ImageDraw, ImageFont

# GitHub URL
github_url = "https://github.com/Suraj-kumar121K"

# QR CODE
qr = qrcode.QRCode(
    version=6,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2
)

qr.add_data(github_url)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Logo (optional)
logo_path = "logo.png"
try:
    logo = Image.open(logo_path).convert("RGBA")
    logo_size = 80
    logo = logo.resize((logo_size, logo_size))

    qr_w, qr_h = qr_img.size
    pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)

    qr_img.paste(logo, pos, mask=logo)
except:
    print("⚠ Logo not found, skipping")

# CARD SIZE
W, H = 900, 500
card = Image.new("RGB", (W, H), (10, 15, 30))
draw = ImageDraw.Draw(card)

# Fonts (default safe fallback)
try:
    title_font = ImageFont.truetype("arial.ttf", 40)
    text_font = ImageFont.truetype("arial.ttf", 22)
except:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# CARD BORDER
draw.rectangle([(20, 20), (W-20, H-20)], outline=(0, 255, 150), width=3)

# TITLE
draw.text((40, 40), "Data Analyst", fill=(0, 255, 150), font=title_font)

# DETAILS
draw.text((40, 120), "Name: Suraj Kumar", fill="white", font=text_font)
draw.text((40, 160), "Visulazation: Excel | SQL | PowerBi", fill=(0, 200, 255), font=text_font)
draw.text((40, 200), "CODE: Python Learner(Numpy | Pandas | Matplotlib)", fill=(0,300,255), font=text_font)

# QR BORDER BOX
qr_img = qr_img.resize((260, 260))
qr_bg = Image.new("RGB", (280, 280), (255, 255, 255))
qr_bg.paste(qr_img, (10, 10))

# Paste QR
card.paste(qr_bg, (580, 110))

# FOOTER
draw.text((40, 430), "Scan QR to visit GitHub profile 🚀", fill=(180, 180, 180), font=text_font)

# SAVE
card.save("github_profile_card.png")

# SHOW
card.show()

print("✅ Stylish GitHub Profile Card Created!")