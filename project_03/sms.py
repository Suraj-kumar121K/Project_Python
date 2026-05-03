from tkinter import *
import time
import ttkthemes
from tkinter import ttk

#Functionality Part
count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(1000,slider)
    
def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)

#GUI part
root = ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')

root.geometry('1200x635+0+0')
root.resizable(0,0)
root.title("Student Management System")

datetimeLabel=Label(root,font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel=Label(root, font=('arial',20,'italic bold'), width=50)
sliderLabel.place(x=200,y=0)
slider()

# ---------------- Connect database Button ----------------
connectButton=ttk.Button(root,text='Connect database')
connectButton.place(x=980,y=0)

# ---------------- Left side color red ----------------
leftFrame=Frame(root, bg='red')
leftFrame.place(x=25, y=60, width=180, height=565)

# ---------------- Logo Image ----------------
root_image=PhotoImage

root.mainloop()