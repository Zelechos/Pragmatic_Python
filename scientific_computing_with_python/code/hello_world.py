# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:18:13 2024

@author: Alex T.H.
"""

print("Hello Scientific Computing Course")

name = "Alex T.H."
print(name)

character = name[0]
print(character)

#Para obtener el Ultimo caracter de un String el indice es -1
last_character = name[-1]
print(last_character)

#Y para obtener el anteultimo caracter el indice es -2
before_last_character = name[-2]
print(before_last_character)

#Asi suscesivamente con los indices negativos en un String

#Para saber la longitud o cantidad de caracteres de un String
print(name , " -> " ,len(name))

#Funcion para saber el tipo de dato
number = 99
is_ai_model = True
print("The datatype of <",name,"> is",type(name))
print("The datatype of <",number,"> is",type(number))
print("The datatype of <",is_ai_model,"> is",type(is_ai_model))

#INVESTIGACION
#Que Ocurriria si quisieramos obtener el indice de un int
#number_of_int = number[0]
#print(number_of_int)
#last_number_of_int = number[-1]
#print(last_number_of_int)
#RESPUESTA => no se puede obtener el mediante indice de un int

#Funcion find() para encontrar la posicion mediante indice de un caracter
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print("cantidad de caracteres de ",alphabet,"->",len(alphabet))
print("posicion del caracter z ->",alphabet.find('z'))
print("posicion del caracter c ->",alphabet.find('c'))
print("posicion del caracter a ->",alphabet.find('a'))


