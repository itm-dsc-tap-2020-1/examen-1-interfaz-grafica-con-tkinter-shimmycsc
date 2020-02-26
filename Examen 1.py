import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox

def calif():
    calif= 0
    if(uno.get=="Bill Gates"):
        calif+=20
    if(dos.get=="Python"):
        calif+=20
    if(op03.get==2):
        calif+=20
    if(op04.get==3):
        calif+=20     
    if(op2.get==1 or op4.get==1 or op5.get==1):
        print("")
    else:
        calif+=20
    mBox.showinfo("Calificación","Tu calificación es " + str(calif))

ventana=tk.Tk()
ventana.title("Examen de Computación")
ventana.tk_setPalette('light gray')

ttk.Label(ventana,text="1.- ¿Quién es el fundador de Microsoft?").grid(column=0,row=1)
ttk.Label(ventana,text="2.- ¿Qué lenguaje de programación es el más usado?").grid(column=0,row=2)
ttk.Label(ventana,text="3.- Selecciona un dispositivo de entrada").grid(column=0,row=3)
ttk.Label(ventana,text="4.- Selecciona un dispositivo de salida").grid(column=0,row=4)
ttk.Label(ventana,text="5.- Seleccione sistemas operativos").grid(column=0,row=5)

uno= tk.StringVar()
dos= tk.StringVar()

ttk.Entry(ventana, width=20,textvariable=uno).grid(column=1,row=1)
ttk.Entry(ventana, width=20,textvariable=dos).grid(column=1,row=2)

op03= tk.IntVar()
op04= tk.IntVar()
op1= tk.IntVar()
op2= tk.IntVar()
op3= tk.IntVar()
op4= tk.IntVar()
op5= tk.IntVar()

rad13= ttk.Radiobutton(ventana,text="Monitor",variable=op03,value=1)
rad13.grid(column=1,row=3, sticky=tk.W)
rad23= ttk.Radiobutton(ventana,text="Teclado",variable=op03,value=2)
rad23.grid(column=2,row=3, sticky=tk.W)
rad33= ttk.Radiobutton(ventana,text="Procesador",variable=op03,value=3)
rad33.grid(column=3,row=3, sticky=tk.W)

rad14= ttk.Radiobutton(ventana,text="Teclado",variable=op04,value=1)
rad14.grid(column=1,row=4, sticky=tk.W)
rad24= ttk.Radiobutton(ventana,text="Mouse",variable=op04,value=2)
rad24.grid(column=2,row=4, sticky=tk.W)
rad34= ttk.Radiobutton(ventana,text="Monitor",variable=op04,value=3)
rad34.grid(column=3,row=4, sticky=tk.W)

chb1= ttk.Checkbutton(ventana,text="Ubuntu",variable=op1)
chb1.grid(column=1,row=5,sticky=tk.W)
chb2= ttk.Checkbutton(ventana,text="Intel",variable=op2)
chb2.grid(column=2,row=5,sticky=tk.W)
chb3= ttk.Checkbutton(ventana,text="Windows",variable=op3)
chb3.grid(column=3,row=5,sticky=tk.W)
chb4= ttk.Checkbutton(ventana,text="IBM",variable=op4)
chb4.grid(column=4,row=5,sticky=tk.W)
chb5= ttk.Checkbutton(ventana,text="Keyboard",variable=op5)
chb5.grid(column=5,row=5,sticky=tk.W)

bot= ttk.Button(ventana, text="Ver Calificación", command=calif)
bot.grid(column=10,row=7)

ventana.mainloop()
