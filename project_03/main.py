import tkinter as tk
import time
import qrcode
from PIL import Image, ImageTk

# ---------------- WINDOW ----------------
clk = tk.Tk()
clk.title("QR + Clock System")
clk.geometry("900x600+200+50")
clk.config(bg="#0C1E28")

# ---------------- LINKS ----------------
links = [
    "https://github.com/Suraj-kumar121K",
    "https://linkedin.com",
    "https://google.com",
    "https://youtube.com",
    "https://facebook.com",
    "https://instagram.com",
    "https://twitter.com",
    "https://stackoverflow.com",
    "https://kaggle.com",
    "https://openai.com"
]

last_qr_min = -1
link_index = 0

# ---------------- TITLE ----------------
title = tk.Label(clk, text="Data Analyst",
                 font=("Times", 30, "bold"),
                 bg="#0C1E28", fg="#00FFAA")
title.pack(pady=20)

name = tk.Label(clk, text="Name: Suraj Kumar",
                font=("Times", 16),
                bg="#0C1E28", fg="white")
name.pack()

skills = tk.Label(clk,
                  text="Visualization: Excel | SQL | Power BI\nPython: NumPy | Pandas | Matplotlib",
                  font=("Times", 14),
                  bg="#0C1E28", fg="#00BFFF")
skills.pack(pady=10)

# ---------------- QR ----------------
qr_label = tk.Label(clk, bg="#0C1E28")
qr_label.pack(pady=20)

# ---------------- TIMER ----------------
timer_label = tk.Label(clk,
                       text="Next QR in: 300 sec",
                       font=("Times", 16, "bold"),
                       bg="#0C1E28", fg="#FFD700")
timer_label.pack()

# ---------------- FOOTER ----------------
footer = tk.Label(clk,
                  text="Scan QR to visit profile 🚀",
                  font=("Times", 12),
                  bg="#0C1E28", fg="gray")
footer.pack(pady=10)

# ---------------- FUNCTION ----------------
def update():
    global last_qr_min, link_index

    current_time = time.localtime()
    mn = current_time.tm_min
    sc = current_time.tm_sec

    # ⏳ Countdown (5 min = 300 sec)
    remaining = 300 - ((mn % 5) * 60 + sc)
    timer_label.config(text=f"Next QR in: {remaining} sec")

    # 🔥 QR Update every 5 minutes
    if mn % 5 == 0 and mn != last_qr_min:
        data = links[link_index]

        qr = qrcode.make(data)
        qr = qr.resize((250, 250))

        qr_img = ImageTk.PhotoImage(qr)
        qr_label.config(image=qr_img)
        qr_label.image = qr_img

        link_index = (link_index + 1) % len(links)
        last_qr_min = mn

    clk.after(1000, update)

# ---------------- EXIT BUTTON ----------------
exit_btn = tk.Button(clk, text="Exit", command=clk.destroy,
                     font=("Times", 14, "bold"),
                     bg="red", fg="white")
exit_btn.pack(pady=20)

# ---------------- START ----------------
update()
clk.mainloop()
