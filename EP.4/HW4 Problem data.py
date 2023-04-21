from tkinter import *
from tkinter import ttk    #theme of tk\]
from tkinter import messagebox

#############################CSV###############################

import csv
def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)   #fw = file writer
        fw.writerow(datalist)   #datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)   #fr = file reader
        data = list(fr)
    return data

    ##############################

GUI = Tk()     #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรบันทึกข้อมูล')   #นี่คือชื่อโปรแกรม
GUI.geometry('600x500')    #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='ปัญหาเครื่องจักร',font=('Angsana New',30),fg='black')
L1.place(x=250,y=15)
    ###############################

LF1 = ttk.LabelFrame(GUI,text='รายละเอียด')
LF1.place(x=40,y=40)

    ###############################

L2 = Label(GUI,text='วันที่',font=('Angsana New',20),fg='blue')
L2.place(x=60,y=100)

v_data2 = StringVar()   #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E2 = ttk.Entry(GUI,textvariable=v_data2,font=('Ansna New',20))
E2.place(x=200,y=100)
           
    ###############################

L3 = Label(GUI,text='Machine name',font=('Angsana New',20),fg='blue')
L3.place(x=60,y=150)

v_data3 = StringVar()   #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E3 = ttk.Entry(GUI,textvariable=v_data3,font=('Angsana New',20))
E3.place(x=200,y=150)

    ###############################
           
L4 = Label(GUI,text='ประเภทปัญหา',font=('Angsana New',20),fg='blue')
L4.place(x=60,y=200)

v_data4 = StringVar()
combo4 = ttk.Combobox(value=["Chokotei","Downtime","Downcount"])
combo4.place(x=200,y=210)

    ###############################

L5 = Label(GUI,text='Problem statement',font=('Angsana New',20),fg='blue')
L5.place(x=60,y=250)

v_data5 = StringVar()   #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E5 = ttk.Entry(GUI,textvariable=v_data5,font=('Angsana New',20))
E5.place(x=200,y=250)

    ###############################

L6 = Label(GUI,text='Root cause',font=('Angsana New',20),fg='blue')
L6.place(x=60,y=300)

v_data6 = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E6 = ttk.Entry(GUI,textvariable=v_data6,font=('Angsana New',20))
E6.place(x=200,y=300)

    ###############################

L7 = Label(GUI,text='Solution',font=('Angsana New',20),fg='blue')
L7.place(x=60,y=350)

v_data7 = StringVar()   #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E7 = ttk.Entry(GUI,textvariable=v_data7,font=('Ansna New',20))
E7.place(x=200,y=350)

    ##############ปุ่มกดบันทึก#################
           
from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H:%M:%S')
    data2 = v_data2.get()   #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    data3 = v_data3.get()
    data4 = v_data4.get()
    data5 = v_data5.get()
    data6 = v_data6.get()
    data7 = v_data7.get()
    text = [t,data2,data3,data4,data5,data6,data7]   #[เวลา,ข้อมูลที่ได้จากการกรอก]
    
    writecsv(text)   #บันทึกลง csv
    v_data2.set('')   #เคลียร์ข้อมูลที่อยู่ในช่องกรอก
    v_data3.set('')
    v_data4.set('')
    v_data5.set('')
    v_data6.set('')
    v_data7.set('')

    text1 = 'บันทึกสำเร็จ'
    messagebox.showinfo('การบันทึก',text1)

B1 = ttk.Button(GUI,text='บันทึก',command=SaveData)
#B1.pack(ipadx=30,ipady=20)
B1.place(x=250,y=400)

GUI.mainloop()
               
