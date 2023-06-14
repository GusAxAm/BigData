# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:38:27 2022

@author: maxam
"""

#Funciones
# def saludo():
#     print("Hola desde la funcion")
# ##Programa principal 
# saludo()

# print()

# def suma(primero, segundo):
#     '''Despliegue la suma de dos objetos'''
#     """Despliegaa"""
#     print(primero+segundo)
# suma(5,10)

# def promedio(*muestras):
#     '''calcula el promedio de la muestra
#     correspondiente a todos los parametros ingresados de la tupla.'''
#     print(type(muestras))
#     promedio=sum(muestras)/len(muestras)
#     print("El promedio de la muestra de %d elementos es %.3f"
#           %(len(muestras),promedio))
    
# promedio(1,3,5,8,11,24,90,29)
# promedio(14,38,1)

# def promedio(titulo,*muestras):
#     '''calcula el promedio de la muestra
#     correspondiente a todos los parametros ingresados de la tupla.'''
    
#     promedio=sum(muestras)/len(muestras)
#     print(titulo)
#     print("El promedio de la muestra de %d elementos es %.3f" %(len(muestras),promedio))
    

# promedio("conteo de las abejas en campo",34,45,61,23,47,41,52)

# def superficie(**dato):
#     superficie = 0
    
#     if dato["tipo"] == "Rectangulo":
#         superficie = dato["base"] * dato["altura"]
#     elif dato["tipo"] == "Triangulo":
#         superficie = float(dato["base"]) * float(dato["altura"]) / 2
#     elif dato["tipo"] == "circulo":
#         superficie = float(dato["radio"]) ** 2 * 3.1416
#     else:
#         print("nio puedo calcular las superficie")
#     if superficie != 0:
#         print("la superficie del %s es de %.2f" %(dato["tipo"].lower(), superficie))
        
# superficie(base = 20, altura = 30, tipo = "Rectangulo")  

# def promedio(*muestras):
#     return(len(muestras), sum(muestras) / len(muestras))

# media = promedio(1, 3, 5, 8, 11, 24, 90, 29)
# print(media)
# print('El promedio de la muestra de %d elementos es %.3f' %(media))      

# Funciones lamba o anonimas
##### Sintaxis: lambda <argumentos>:<codigo>#####

# saluda = lambda texto = "mundo" , ancho = 50 : print ("Hola, {}".format(texto).center(ancho))
# saluda ()
# saluda ( "mundi" ,20)

#Lambda con concidional
#lambda <argumento>: <expresion_1> if <condicion> else <expresion_2>

es_par = lambda numero : True if numero % 2 == 0 else False
print (es_par(3))
factorial = lambda numero : numero*factorial(numero - 1) if numero >1 else 1
print (factorial(5))




#
#
#
#
#
#



 
    