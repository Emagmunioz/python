#Importar las bibliotecas necesarias
import matplotlib.pyplot as plt


#Crea la variable independente x
x = [0,1,2,3,4,5]
#Crea la variable dependente y
y = x

# Método orientado a objetos
# Crear figura 
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])# ejes principales
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # ejes insertados
# Ejes de figuras más grandes 1
axes1.plot(x, y, 'b')
# Insertar ejes de figura 2
axes2.plot(y, x, 'r')


#Muestra los gráficos
plt.show()