from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import sqlalchemy

#Functionality Part

def connect_database():
    def connect():
        try:
            con=sqlalchemy.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
            messagebox.showinfo('Success', 'Database Connection is successful')
        except:
           messagebox.showerror('Error', 'Invalid Details')     
        
        
    connectWindow=Toplevel()
    connectWindow.geometry('440x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)
    
    hostnameLabel=Label(connectWindow, text='Host Name', font=('arial',15,'bold'))
    hostnameLabel.grid(row=0, column=0, pady=20)
    
    hostEntry=Entry(connectWindow, font=('roman',15,'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=45, pady=20)
    
    usernameLabel=Label(connectWindow, text='User Name', font=('arial',15,'bold'))
    usernameLabel.grid(row=1, column=0, pady=20)
    
    usernameEntry=Entry(connectWindow, font=('roman',15,'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=45, pady=20)
    
    passwordLabel=Label(connectWindow, text='Password', font=('arial',15,'bold'))
    passwordLabel.grid(row=2, column=0, pady=20)
    
    passwordEntry=Entry(connectWindow, font=('roman',15,'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=45, pady=20)
    
    connectButton=ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, columnspan=2)


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

datetimeLabel=Label(root,font=('times new roman', 15, 'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel=Label(root, font=('arial',20,'italic bold'), width=50)
sliderLabel.place(x=200,y=0)
slider()

# ---------------- Connect database Button ----------------
connectButton=ttk.Button(root,text='Connect database', command=connect_database)
connectButton.place(x=980,y=0)

# ---------------- Left side color red ----------------
leftFrame=Frame(root)
leftFrame.place(x=25, y=60, width=300, height=600)

# ---------------- Logo Image ----------------
logo_image=PhotoImage(file='students.png')
logo_Label=Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0)

# ---------------- Add Student Button ----------------
addstudentButton=ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED)
addstudentButton.grid(row=1, column=0, pady=18)

# ---------------- Search Student Button ----------------
searchstudentButton=ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED)
searchstudentButton.grid(row=2, column=0, pady=18)

# ---------------- Delete Student Button ----------------
deletestudentButton=ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED)
deletestudentButton.grid(row=3, column=0, pady=18)

# ---------------- Update Student Button ----------------
updatestudentButton=ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED)
updatestudentButton.grid(row=4, column=0, pady=18)

# ---------------- show Student Button ----------------
showstudentButton=ttk.Button(leftFrame, text='Show Student', width=25, state=DISABLED)
showstudentButton.grid(row=5, column=0, pady=18)

# ---------------- Export Data ----------------
showstudentButton=ttk.Button(leftFrame, text='Export data', width=25, state=DISABLED)
showstudentButton.grid(row=6, column=0, pady=18)

# ---------------- Exit ----------------
showstudentButton=ttk.Button(leftFrame, text='Exit', width=25)
showstudentButton.grid(row=7, column=0, pady=18)

# ---------------- Right Frame ----------------
rightFrame=Frame(root)
rightFrame.place(x=300, y=60, width=820, height=600)

scrollBarX=Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame, orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame, columns=('Id','Name','Mobile','Email', 'Address','Gender','D.O.B','Added Date', 'Added Time'),
                          xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studentTable.xview)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile', text='Mobile No')
studentTable.heading('Email', text='Email Address')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')

studentTable.config(show='headings')

root.mainloop()