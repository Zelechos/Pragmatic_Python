# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:13:04 2024
El primer tipo de cifrado que va a construir se llama 
cifrado César. Específicamente, tomará cada letra 
de su mensaje, encontrará su posición en el alfabeto, 
tomará la letra ubicada después de 3 posiciones 
en el alfabeto y reemplazará la letra original 
con la nueva letra.

@author: Alex T.H.
"""

#Cesar Cipher -> Cifrado Cesar

message_to_cipher = "El submarino a recibido el mensaje Heil Hitler"
second_message = "Heil Hitler"

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def cesar_cipher(message, alphabet):
    message_cipher = ""
    for letter in message.lower():
        if letter != " ":
            message_cipher = message_cipher + alphabet[alphabet.find(letter) + 3]
        else :
            message_cipher = message_cipher + "@"
    return message_cipher

def cesar_decipher(message, alphabet):
    message_decipher = ""
    for letter in message:
        if letter != "@":
            message_decipher = message_decipher + alphabet[alphabet.find(letter) - 3]
        else : 
            message_decipher = message_decipher + " "
    return message_decipher
    
print(message_to_cipher)
message_cipher = cesar_cipher(message_to_cipher, alphabet)
print(message_cipher)
print(cesar_decipher(message_cipher, alphabet))
print(cesar_cipher(second_message, alphabet))
