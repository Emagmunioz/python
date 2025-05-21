#Importar las bibliotecas necesarias
import matplotlib.pyplot as plt


#Crea las variables de cada parcela
x1 = [1,1.23,1.512,2,2.1321]
x2 = [-1,-2,-3,-5,2]
y1 = x1
y2 = x2
#crea la figura con 1 fila y dos columnas
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x1, y1,'b') 
axes[1].plot(x2, y2,'r')


#Muestra los gráficos
plt.show()