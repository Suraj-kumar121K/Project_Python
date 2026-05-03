from tkinter import *
from PIL import ImageTk

window = Tk()
window.geometry('1280x700+0+0')
window.resizable(False, False)

# ---------------- BACKGROUND ----------------
backgroundImage = ImageTk.PhotoImage(file='bg.png')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

# ---------------- LOGIN FRAME ----------------
loginFrame=Frame(window)
loginFrame.place(x=500, y=150)

# ---------------- LOGO ----------------
logoImage = PhotoImage(file='logo.jpg')
logoLabel = Label(loginFrame,image=logoImage)
logoLabel.grid(row=0, column=0)

# ---------------- USERNAME ----------------
usernameImage = PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage, text='Username', compound=LEFT,
                    font=('times new roman'20,'bold'))
usernameLabel.grid(row=1, column=0)

window.mainloop()
