#!/usr/bin/python3
from tkinter import *
from termcolor import colored
import sys

try:
 ab = sys.argv[1]
except IndexError:
 print(colored("[!]","red"), "syntax : $ ./w.py file.txt")
else:
 root = Tk()
 root.configure(bg='black')
 root.title("- LOGGING TOOL - By m00nissmiling")
 root.geometry("600x700")
 f2 = Frame(root,bg='black')
 f2.pack()
 w1 = StringVar(root)
 Label(f2,text=' Issue Number ',bg='black',fg='red',width=30,font='Verdana 12 bold').pack(padx=3)
 en1 = Entry(f2,textvariable=w1,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='red',highlightcolor='white',width=5,insertbackground='white')
 en1.pack(pady=5)
 
 w2 = StringVar(root)
 Label(f2,text=' Title ',bg='black',fg='blue',width=30,font='Verdana 12 bold').pack(padx=5)
 en2 = Entry(f2,textvariable=w2,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='blue',highlightcolor='white',width=150,insertbackground='white')
 en2.pack(pady=5)
 
 w3 = StringVar(root)
 Label(f2,text=' Project ',bg='black',fg='red',width=30,font='Verdana 12 bold').pack(padx=5)
 en3 = Entry(f2,textvariable=w3,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='red',highlightcolor='white',width=40,insertbackground='white')
 en3.pack(pady=5)
 
 w4 = StringVar(root)
 Label(f2,text=' Vuln Url ',bg='black',fg='blue',width=30,font='Verdana 12 bold').pack(padx=5)
 en4 = Entry(f2,textvariable=w4,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='blue',highlightcolor='white',width=150,insertbackground='white')
 en4.pack(pady=5)
 
 w40= StringVar(root)
 Label(f2,text=' Rate ',bg='black',fg='red',width=30,font='Verdana 12 bold').pack(padx=5)
 en40 = Entry(f2,textvariable=w40,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='red',highlightcolor='white',width=40,insertbackground='white')
 en40.pack(pady=5)
 
 w5= StringVar(root)
 Label(f2,text=' Impact Detail ',bg='black',fg='blue',width=30,font='Verdana 12 bold').pack(padx=5)
 en5 = Entry(f2,textvariable=w5,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='blue',highlightcolor='white',width=150,insertbackground='white')
 en5.pack(pady=5)
 
 w6= StringVar(root)
 Label(f2,text=' Day ',bg='black',fg='green',width=30,font='Verdana 12 bold').pack(padx=5)
 en6 = Entry(f2,textvariable=w6,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='red',highlightcolor='white',width=5,insertbackground='white')
 en6.pack(pady=5)
 
 w7= StringVar(root)
 Label(f2,text=' SUN/MON/TUE ',bg='black',fg='green',width=30,font='Verdana 12 bold').pack(padx=5)
 en7 = Entry(f2,textvariable=w7,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='green',highlightcolor='white',width=10,insertbackground='white')
 en7.pack(pady=5)
 
 w8= StringVar(root)
 Label(f2,text=' Month ',bg='black',fg='green',width=30,font='Verdana 12 bold').pack(padx=5)
 en8 = Entry(f2,textvariable=w8,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='green',highlightcolor='white',width=5,insertbackground='white')
 en8.pack(pady=5)
 
 w9= StringVar(root)
 Label(f2,text=' Year ',bg='black',fg='green',width=30,font='Verdana 12 bold').pack(padx=5)
 en9 = Entry(f2,textvariable=w9,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='green',highlightcolor='white',width=10,insertbackground='white')
 en9.pack(pady=5)
 
 w10= StringVar(root)
 Label(f2,text=' Hour:Min [AM/PM] ',bg='black',fg='green',width=30,font='Verdana 12 bold').pack(padx=5)
 en10 = Entry(f2,textvariable=w10,bg='black',fg='lime',borderwidth=2,highlightthickness=2,highlightbackground='green',highlightcolor='white',width=30,insertbackground='white')
 en10.pack(pady=10)
 
 def log():
  inp0 = w1.get()
  inp1 = w2.get()
  inp10 = w3.get()
  inp2 = w40.get()
  inp3 = w4.get()
  inp4 = w7.get()
  inp5 = w6.get()
  inp6 = w8.get()
  inp7 = w9.get()
  inp8 = w5.get()
  inp9 = w10.get()
  textss = f"#issue{inp0}\nTitle - {inp1} < {inp10}\nVulnerable Url - {inp3}\nRate - {inp2}\nDetail - {inp8}\n[{inp4}] [{inp9}] [{inp5}/{inp6}/{inp7}]\n----------------------------\n"
  fileo = open(ab,"a")
  fileo.write(textss)
  fileo.close()
  en1.delete(0,END)
  en2.delete(0,END) 
  en4.delete(0,END)
  en40.delete(0,END)
  en5.delete(0,END)
  en10.delete(0,END)
  text1 = Text(f2,bg='black',fg='lime',borderwidth=2,width=150,height=8)
  text1.pack()
  text1.insert(0.0,textss)
 
 f3 = Frame(f2,bg='black')
 f3.pack(padx=10)
 
 Button(f3,text="ADD",fg='white',bg='red',command=log,width=25,height=4,borderwidth=2,relief="flat",activebackground="green",activeforeground="white",highlightthickness=2, highlightbackground="red",font='Verdana 10 bold').pack(side=LEFT,pady=5)
 


 root.mainloop()
