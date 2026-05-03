from tkinter import *
from PIL import ImageTk

window = Tk()
window.geometry('1280x700+0+0')
window.resizable(False, False)

# ---------------- BACKGROUND ----------------
backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

# ---------------- LOGIN FRAME ----------------
loginFrame=Frame(window, bg='white')
loginFrame.place(x=500, y=150)

# ---------------- LOGO ----------------
logoImage = PhotoImage(file='')
logoLabel = Label(loginFrame,image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

# ---------------- USERNAME ----------------
usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame,image=usernameImage, text='Username', compound=LEFT,font=('times new roman',20,'bold'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

# ---------------- INPUT ----------------
usernameEntry = Entry(loginFrame, font=('times new_roman',20,'bold'), bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20) 

# ---------------- password ----------------
passwordImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame,image=passwordImage, text='Password', compound=LEFT,font=('times new roman',20,'bold'), bg='white')
usernameLabel.grid(row=2, column=0, pady=10, padx=20)

# ---------------- INPUT ----------------
usernameEntry = Entry(loginFrame, font=('times new_roman',20,'bold'), bd=5, fg='royalblue')
usernameEntry.grid(row=2, column=1, pady=10, padx=20) 

window.mainloop()

