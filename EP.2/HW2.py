from tkinter import *
from tkinter import ttk   #theme of tk\]
from tkinter import messagebox

GUI = Tk()   # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('ร้านข้าวจุกๆ')   #นี่คือชื่อโปรแกรม
GUI.geometry('500x400')     #นี่คือขนาดโปรแกรม


L1 = Label(GUI,text='รายการอาหาร',font=('sukhumvit',30),fg='green')
L1.place(x=50,y=20)

###########
def Button2():
    text = 'ธรรมดา 35 บาท, พิเศษเพิ่มไข่ดาว 40 บาท'
    messagebox.showinfo('ราคาข้าวกะเพรา',text)


FB1 = Frame(GUI)  #คล้ายกระดาน
FB1.place(x=50,y=80)
B2 = ttk.Button(FB1,text='ข้าวผัดกะเพรา',command=Button2)
B2.pack(ipadx=20,ipady=20)
#################

def Button3():
    text = 'ไก่ 30 บาท, หมู 35 บาท'
    messagebox.showinfo('ราคาสุกี้',text)


FB2 = Frame(GUI)  #คล้ายกระดาน
FB2.place(x=50,y=155)
B3 = ttk.Button(FB2,text='สุกี้',command=Button3)
B3.pack(ipadx=20,ipady=20)
#################

def Button4():
    text = 'น้ำใส, น้ำขึ้น'
    messagebox.showinfo('ราคาก๋วยเตี๋ยว',text)


FB3 = Frame(GUI)  #คล้ายกระดาน
FB3.place(x=50,y=230)
B4 = ttk.Button(FB3,text='ก๋วยเตี๋ยว',command=Button4)
B4.pack(ipadx=20,ipady=20)
#################

L2 = Label(GUI,text='รายการเครื่องดื่ม',font=('Angsana New',30),fg='blue')
L2.place(x=300,y=20)

###########
def Button5():
    text = 'ลาเต้, อเมริกาโน่, เอสเปรสโซ่'
    messagebox.showinfo('เมนูกาแฟ',text)


FB4 = Frame(GUI)  #คล้ายกระดาน
FB4.place(x=300,y=80)
B5 = ttk.Button(FB4,text='กาแฟ',command=Button5)
B5.pack(ipadx=20,ipady=20)
#################

def Button6():
    text = 'นมสด,ชาใต้หวัน,ชาไทย'
    messagebox.showinfo('เมนูไข่มุก',text)


FB5 = Frame(GUI)  #คล้ายกระดาน
FB5.place(x=300,y=155)
B4 = ttk.Button(FB5,text='เครื่องดื่นใส่ไข่มุก',command=Button6)
B4.pack(ipadx=20,ipady=20)
#################

GUI.mainloop()
