from tkinter import *
from PIL import ImageTk

window = Tk()

window.geometry('1280x700+0+0')

window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file='Background_image.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame = Frame(window)
loginFrame.place(x=400, y=150)

window.mainloop()
