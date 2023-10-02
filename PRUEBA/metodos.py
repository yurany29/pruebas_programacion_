import numpy as np
import random

class Metodos:

	# Metodo para convertir texto a código Morse
	def texto_codigo_morse(self, mensaje):
		lista = []
		codigo_morse = {
    	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    	'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    	'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', # Espacio
		}
		#Convierte el mensaje en mayusculas para su lectura
		mensaje = mensaje.upper() #or lower
		#Se recorre cada caracter contenido
		for i in mensaje:
			#encuentra el caracter en el diccionario
			if i in codigo_morse:
				#Almacena en la lista cada que haya coincidencia
				lista.append(codigo_morse[i])
		#Une los elementos de la lista y retorna
		return ' '.join(lista)


	#Metodo para convertir codigo morse a texto
	def codigo_morse_texto(self, mensaje):
		lista = []
		codigo_morse = {
		'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
		'-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
		'..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', # Espacio
		}
		
		#Separa todos los caracteres ingresados
		mensaje = mensaje.split(' ')
		lista = []
		#Se recorre cada caracter contenido
		for i in mensaje:
			#encuentra el caracter en el diccionario
			if i in codigo_morse:
				#Almacena en la lista cada que haya coincidencia
				lista.append(codigo_morse[i])
		#Une los elementos de la lista y retorna
		return ''.join(lista)

	#Metodo para crear la matriz
	def matriz(self):
		matriz = []
		fila = 10#int(input("Ingrese la cantidad de filas (10): "))
		columna = 5#int(input("Ingrese la cantidad de columnas (5): "))

		for i in range(fila):
			lista = []
			for k in range(columna):
				#Almacceno las filas
				lista.append([])
			#Almacena toda la matriz
			matriz.append(lista)
		
		return matriz


		#Metodo para seleccionar el campo
	def deshabilitar_campos(self, fila, columna, crear_matriz):
		#cuando encuentra e campo le asigna el valor -1
		if crear_matriz[fila][columna] != -1:
			crear_matriz[fila][columna] = -1
			return True
		return False

	#Metodo para mostrar la matriz completa
	def mostrar_matriz(self, crear_matriz):
		#Recorre cada fila y columna de la matriz
		for i in crear_matriz:
			for k in i:
				#Compara los campos y cuando haya coincidencia imprime XX
				if k == -1:
					print("XX", end=" ") 
				else:
					#Genera nnumeros al azar en el rango
					k = random.randint(1,50)
					print(k, end=" ")
			print() 