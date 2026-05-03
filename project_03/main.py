from tkinter import *
from PIL import ImageTk

window = Tk()
window.geometry('1280x700+0+0')
window.resizable(False, False)

# ---------------- BACKGROUND ----------------
backgroundImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

# ---------------- LOGIN FRAME ----------------
loginFrame = Frame(window, bg="white")
loginFrame.place(x=500, y=120)

# ---------------- LOGO ----------------
logoImage = PhotoImage(file='graduated.png')
logoLabel = Label(loginFrame, image=logoImage, bg="white")
logoLabel.grid(row=0, column=0, columnspan=2, pady=20)

# ---------------- AVATAR + USERNAME ----------------
avatarImage = PhotoImage(file='user.png')
avatarLabel = Label(loginFrame, image=avatarImage, bg="white")
avatarLabel.grid(row=1, column=0, padx=10, pady=10)

usernameLabel = Label(loginFrame, text="Username",
                      font=("times new roman", 14, "bold"),
                      bg="white")
usernameLabel.grid(row=1, column=1, sticky=W, padx=10)

usernameEntry = Entry(loginFrame, font=("times new roman", 14), bd=2, relief=GROOVE)
usernameEntry.grid(row=2, column=0, columnspan=2, padx=0, pady=0)

window.mainloop()
