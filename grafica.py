import matplotlib.pyplot as plt
import numpy as np
import math
nombreArchivo=input('Dame el nombre de tu archivo entre comillas. ')
f=open(nombreArchivo,'r')
l=f.readlines()
x=[]
y=[]
if l[1]==',':
    for i in l:
        k=i.split(',')
        x.append(k[0])
        y.append(k[1])
        plt.plot(x,y,'*',color='r')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(nombreArchivo)
        plt.savefig("grafica.png")
else:
    for i in l:
        k=i.split(' ')
        x.append(k[0])
        y.append(k[1])
        plt.plot(x,y,'*',color='r')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(nombreArchivo)
        plt.savefig("grafica.png")
