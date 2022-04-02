import imghdr
import tkinter as tk
from tkinter import ttk
from cProfile import label
from tkinter import *
from tkinter import messagebox
import math

raiz = tk.Tk()
raiz.title("Conversion de bases")
raiz.geometry("400x200")
raiz.resizable(False,False)
raiz.config(background="#F0F8FF")
raiz.iconbitmap("piton.ico")


miFrame = Frame(raiz)
miFrame.pack(fill= "y", expand="True")
miFrame.config(width="350" , height="100",background="#F0F8FF")



labelTop = tk.Label(miFrame,
                    text = "Ingrese el numero y lo que deseas hacer con el",background="#F0F8FF",font = ("Helvetica",9))
labelTop.place(x = "40", y = "30")

cuadroTexto = Entry(miFrame)
cuadroTexto.place(x= "105", y = "70")
cuadroTexto.config(justify="center")

comboBases = ttk.Combobox(miFrame, state= 'readonly')
comboBases.place(x = "95", y = "100")

opciones = ["Base 6", "Base 7", "Base 8", "Base 9","Numeros primos","fibonacci","permutacion"] 

comboBases['values'] = opciones



def base6(n):
    final = []
    resultado = []
    while n != 0:
        final.append(n % 6)
        n = n // 6
    for i in reversed(final):
        resultado.append(i)
    messagebox.showinfo(message= "El numero en base 6 es: "+ ''.join(map(str, resultado)))

def base7(n):
    final = []
    resultado = []
    while n != 0:
        final.append(n % 7)
        n = n // 7
    for i in reversed(final):
        resultado.append(i)
    messagebox.showinfo(message= "El numero en base 7 es: "+ ''.join(map(str, resultado)))

def base8(n):
    final = []
    resultado = []
    while n != 0:
        final.append(n % 8)
        n = n // 8
    for i in reversed(final):
        resultado.append(i)
    messagebox.showinfo(message= "El numero en base 8 es: "+ ''.join(map(str, resultado)))

def base9(n):
    final = []
    resultado = []
    while n != 0:
        final.append(n % 9)
        n = n // 9
    for i in reversed(final):
        resultado.append(i)
    messagebox.showinfo(message= "El numero en base 9 es: "+ ''.join(map(str, resultado)))
    resultado.clear()

def Primo(n):
    if n == 2 or n==3:
        return messagebox.showinfo(message= "El numero es primo: ")
    if n <= 1 or n % 2 ==0:
        return messagebox.showinfo(message= "El numero no es primo: ")
    for a in range(3,n-1,2):
        if a**(n-1) % n != 1:
            return messagebox.showinfo(message= "El numero no es primo: ")
    return messagebox.showinfo(message= "El numero es primo: ")

def Fibonacci(n):
    arr=[0,1]
    if n==1:
        return messagebox.showinfo(message= "0")
    elif n==2:
        return messagebox.showinfo(message= "'[0,','1]' ")
    else:
        while(len(arr)<n):  
            arr.append(0)
        if(n==0 or n==1):
            return  messagebox.showinfo(message= "1")
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,n):   
                arr[i]=arr[i-1]+arr[i-2]      
            return messagebox.showinfo(message= arr)

def permutations(start, end=[]):
    if len(start) == 0:
        print(end)
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i+1:], end + start[i:i+1])

def converir(n): 
    n.split(' ')
    n_int = [int(x) for x in  n]
    r = permutations(n_int)
    return Listbox(message= r)

def cambioBase():
    if comboBases.get() == "Base 6":
        base6(int(cuadroTexto.get()))
    elif comboBases.get() == "Base 7":
        base7(int(cuadroTexto.get()))
    elif comboBases.get() == "Base 8":
        base8(int(cuadroTexto.get()))
    elif comboBases.get() == "Base 9":
        base9(int(cuadroTexto.get()))
    elif comboBases.get() == "Numeros primos":
        Primo(int(cuadroTexto.get()))
    elif comboBases.get() == "fibonacci":
        Fibonacci(int(cuadroTexto.get()))
    elif comboBases.get() == "permutacion":
        converir(cuadroTexto.get())

botonConvertir = Button(miFrame, text = "Convertir", command= cambioBase)
botonConvertir.place(x = 130, y = 140)


raiz.mainloop()