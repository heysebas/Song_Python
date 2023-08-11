# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:11:11 2023

@author: sebas
"""

# =============================================================================
# Dada la siguiente letra, obtenga la misma pero sustituyendo la palabra voices por sounds:
# =============================================================================

song = '''You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness'''


# =============================================================================
# # Definir las palabras antigua y nueva
# palabra_antigua = 'voices'
# palabra_nueva = 'sounds'
# 
# 
# # Dividir la cadena en una lista de palabras
# palabras = song.split()
# 
# # Recorrer la lista de palabras y reemplazar la palabra antigua por la nueva
# palabras_modificadas = [palabra_nueva if palabra == palabra_antigua else palabra for palabra in palabras]
# 
# # Unir las palabras modificadas para formar la cadena final
# song_modificada = " ".join(palabras_modificadas)
# 
# # Imprimir la cadena original y la cadena modificada
# print('Canción original:', song)
# print('Canción modificada:', song_modificada)
# =============================================================================


# Encuentra la posición del texto 'voices' en la cadena 'song'
inicio_voces = song.find('voices')

# Crea una nueva cadena llamada 'song_modificada' que combina tres partes:
# 1. El contenido de 'song' desde el inicio hasta la posición de 'voices'
# 2. La palabra 'sounds'
# 3. El contenido de 'song' desde después de 'voices' hasta el final
song_modificada = song[:inicio_voces] + 'sounds' + song[inicio_voces + 6:]

# Imprime la canción original y la canción modificada
print('Canción original:', song)
print('Canción modificada:', song_modificada)
