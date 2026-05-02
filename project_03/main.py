from tkinter import *
from PIL import ImageTk

window = Tk()

window.geometry('1280x700+0+0')

window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file='Background_image.jpg')

bgLabel = Label(window, image=backgroundImage)
# bgLabel.place(x=0,y=0)

loginFrame = Frame(window)
loginFrame.place(x=500, y=150)

logoImage = PhotoImage(file='graduated.png')

logoLabel = Label(loginFrame, image=logoImage)
usernameImage = logoLabel.grid(row=0, column=0)
PhotoImage(file='user.png')
usernameLabel=Label(loginFrame, image=usernameImage, text='Username', compound=LEFT, font=('times new roman', 20, 'bold'))
usernameLabel.grid(row=1, column=0)

window.mainloop()
