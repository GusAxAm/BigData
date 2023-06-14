"""
Created on Thu Sep 14 10:27:24 2022

@author: maxam
U1_Práctica e investigación : Problemas a resolver en Python
"""
# In[1]
#Lea una secuencia de números,cuente cuántos números son pares y cuántos son impares. 
# def contarParesImpares(listas):
#     pares, impares = 0, 0

#     for n in listas:
#         if n % 2 == 0:
#             pares += 1
#         else:
#             impares += 1
#     print("Numero de pares: %i" % pares)
#     print("La cantidad de impares es: %i" % impares)

# listas = []
# val=int(input("Ingrese Un Numero (0 Para Finalizar):"))
# while val != 0 :
#     listas.append(val)
#     contarParesImpares(listas)
#     val=int(input("Ingrese Un Numero (0 Para Finalizar):"))
# print(listas)
# In[2]
#Lea una palabra e imprima sólo las consonantes de esa palabra. 
# Por ejemplo: Python => Pythn
# def eliminarVocales(palabra):
#     vocales = "aeiou"
#     v = ""
#     c = ""
#     for x in palabra:
#         if x in vocales:
#             v += x
#         else:
#             c += x
#     print(c)  
# palabra = str(input("Ingrese la palabra: "))
# eliminarVocales(palabra)
# In[3]:
#Lea una palabra con letras repetidas. 
# Eliminar una de las letras repetidas. 
# Por ejemplo: pyxpyxpyx  => pypypy
# def removerCaracteresDup(palabra):
#     return "".join(list(dict.fromkeys(list(palabra))))
# texto = str(input("Ingresa la palabra: "))
# print(texto)
# print(removerCaracteresDup(texto))
# In[4]:
#Lea un correo electrónico. 
# Imprimir la información antes de @.  
# Por ejemplo: python@correo.com => python
# def correoElectronico (cadena) :
#     indiceArroba = cadena.index("@")
#     subc = cadena[0:indiceArroba]
#     print(subc)
# cadena = str(input("Correo electronico: "))
# correoElectronico(cadena)
# In[5]:
#Dada una cadena de números 
# reemplazar el 0 por una c 
# Por ejemplo: "02123045067680" => "X2123X45X6768X"
# def reemplazar (cadena) :
#     subc = "0"
#     nuevaCad = cadena.replace(subc,"X")
#     print(nuevaCad)
# cadena = str(input("Ingrese El Numero: "))
# reemplazar(cadena)
# In[6]:
#Considere una lista de cinco números: 1, 2, 3, 4 y 5. 
# Tu tarea es:
#Paso 1. Solicitar al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario.
#Paso 2. Elimine el último elemento de la lista.
#Paso 3. Imprima la longitud de la lista existente.
# def listaNum():
#     lista = [1,2,3,4,5]
#     print(lista)
#     val = int(input("Ingrese el valor que remplazara: "))
#     lista[2]=val
#     print(lista)
#     lista.pop()
#     print(lista)
#     print("El Tamaño de la lista es: %i" % len(lista))
# listaNum()
# In[7]:
#Considera una lista de números enteros con repeticiones en algunos de sus elementos,
#elimina todos los elementos repetidos e imprímela en pantalla.
# def eliminarRepetidos ():
#     dat = [5,4,6,4,7,3,1,1,4,9,4,5,5]
#     print(dat)
#     resultado = []
#     for item in dat:
#         if item not in resultado:
#             resultado.append(item)
#     print(resultado)
# eliminarRepetidos()
# In[8]:
#Considere una tupla de enteros con repeticiones y elimine los elementos repetidos. 
#Imprima el resultado.
# def  eliminarRepTupla():
#     dat = (4,9,9,5,3,3,3,2,1,4,1,1,2,5,6,5,5,5)
#     resultados = []
#     for item in dat:
#         if item not in resultados:
#             resultados.append(item)
#     print(dat)
#     print(resultados)
# eliminarRepTupla()
#%% In [9]:
#Considere una tupla de números enteros. Convierta la tupla a un número. 
#Por ejemplo: t=(100, 23, 45, 150) => 1002345150
# def tuplaToNumero():
#     dat = (264,48,94,8168)
#     s = ""
#     for item in dat:
#         s=s+str(item)
#     print(dat)
#     print(s)
# tuplaToNumero()
#%% In [10]:
# Considere el siguiente diccionario {1:['a', 'b'], 2: [1, 2]}, 
#realice las combinaciones de los elementos e imprima en pantalla. 
#La salida sería: a1, a2, b1, b2
# from itertools import product
# def combDic():
#     dic= {"1": ["c", "a"], "2": ["1", "2"]}
#     for c in product(*[dic[k] for k in sorted(dic.keys())]):
#         print("".join(c))
# combDic()
#%% In [11]:
#Crea una lista y concaténala  con un número dado. 
#Por ejemplo: lista = ['a','b', 'c']  número: 3
# => [ 'a1', 'b1', 'c1','a2', 'b2', 'c2', 'a3', 'b3', 'c3' ]
# def concatenarListNum(listas,num):
#     resultado =[]
#     cont = 0
#     while cont < num :
#         cont+=1
#         for item in listas:
#             if item not in resultado:
#                 resultado.append(item+str(cont))
#     print(resultado)
# v = ["a","b","c"]
# num = 3
# concatenarListNum(v,num)