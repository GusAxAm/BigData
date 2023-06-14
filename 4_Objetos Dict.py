# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 12:36:30 2022

@author: maxam
"""
#forma 1 Parejas llave:valor
# persona = {"Nombre":"José","Apellido_Paterno":"Perez","Apellido_Materno":"Juarez"}
# print(persona)
# print(persona["Apellido_Materno"])
# persona[ "Nombre" ]="Luis"
# print(persona)
# otra = dict(Nombre = "Armando",Escolaridad_Maxima="Licenciatura")
# print(otra)
# print()
# del otra["Nombre"]
# print(otra)
persona = {"nombre":"Jose","Apellido_Paterno":"Ambriz","Apellido_Materno":"Zamarripa"}
print (persona.get("nombre"))
print()
persona.update({"nombre":"Pedro","Codigo_postal":"27294"})
print(persona)
print()
persona.update({"profesion":"ISC"})
print(persona)
print()
persona.setdefault("email","Correo_isc@itlalaguna.edu.mx")
print(persona)
print()
persona.setdefault("certificacion")
print(persona)
print()
elementos=persona.items()
print(elementos)
print()
for elementos in elementos:
    print(elementos)

print()
print()
print()
##    
llaves = persona.keys()
print(llaves)
for clave in llaves:
    print(clave)
    
print()    
print()    
##  
valores = persona.values()#objeto iterable
print(valores)
for val in valores:
    print(val)




