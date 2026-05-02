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
    "https://www.youtube.com/@WorkLifeRoam",
    "https://www.kaggle.com/kagglesuraj12",
    "https://leetcode.com/u/Surajkumar852/",
    "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
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
                       text="Next QR in: 60 sec",
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
def generate_qr(data):
    qr = qrcode.make(data)
    qr = qr.resize((250, 250))
    qr_img = ImageTk.PhotoImage(qr)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img

def update():
    global last_qr_min, link_index

    current_time = time.localtime()
    mn = current_time.tm_min
    sc = current_time.tm_sec

    # ⏳ Countdown (1 min = 60 sec)
    remaining = 60 - sc
    timer_label.config(text=f"Next QR in: {remaining} sec")

    # 🔥 QR Update every 1 minute
    if mn != last_qr_min:
        data = links[link_index]
        generate_qr(data)
        link_index = (link_index + 1) % len(links)
        last_qr_min = mn

    clk.after(1000, update)

# ---------------- EXIT BUTTON ----------------
exit_btn = tk.Button(clk, text="Exit", command=clk.destroy,
                     font=("Times", 14, "bold"),
                     bg="red", fg="white")
exit_btn.pack(pady=20)

# ---------------- START ----------------
generate_qr(links[0])   # 👈 Initial QR show hoga
update()
clk.mainloop()

