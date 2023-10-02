from os import system
from metodos import Metodos

class Menu:

	def __init__(self):
		self.metodos = Metodos()


#----------------------METODOS-------------------------------

	def codigo_morse(self):
		system("cls")
		print("|--------------------------------|")
		print("|         CODIGO MORSE           |")
		print("|--------------------------------|")
		print("|--------------------------------|")
		print("|1) Texto a codigo morse         |")
		print("|2) Codigo morse a texto         |")
		print("|0) Menu principal               |")
		print("|--------------------------------|")
		try:
			op = int(input("Digite la opcion: "))

			if op == 1:
				mensaje = input("Ingrese un mensaje: ")
				if self.metodos.texto_codigo_morse(mensaje):
					print("EL mensaje descifrado es: ",self.metodos.texto_codigo_morse(mensaje))
					input()
				else:
					print("El mensaje no se puede descifrar")
					input()

			elif op == 2:
				mensaje = input("Ingrese un mensaje: ")
				if self.metodos.codigo_morse_texto(mensaje):
					print("EL mensaje descifrado es: ",self.metodos.codigo_morse_texto(mensaje))
					input()
				else:
					print("El mensaje no se puede descifrar")
					input()

			elif op == 0:
				self.mostrar_menu_principal()

			else:
				print("|--------------------------------|")
				print("|La opcion digitada es incorrecta|")
				print("|--------------------------------|")
				input()

		except ValueError:
			print("|-----------------------------------|")
			print("|  Error - El dato debe ser entero  |")
			print("|-----------------------------------|")
			input()



	def matriz(self):
		system("cls")
		print("|--------------------------------|")
		print("|             MATRIZ             |")
		print("|--------------------------------|")

		crear_matriz = self.metodos.matriz()
		#print(self.metodos.matriz())

		cont = 0
		while cont < 5:
			fila = int(input("Ingrese una fila a deshabilitar (0-9): "))
			columna = int(input("Ingrese columna a deshabilitar (0-4): "))

			if fila >= 0 and fila <= 9 and columna >=0 and columna <=4:
				if self.metodos.deshabilitar_campos(fila, columna, crear_matriz):
					cont += 1
					print("El campo se ha deshabilitado")
					print("-----------------------------")
					self.metodos.mostrar_matriz(crear_matriz)
					print("-----------------------------")

				else:
					print("Error - el campo ya se encuentra seleccionado")
					print("-----------------------------")
			else:
				print("Error - fuera de rango")
				print("-----------------------------")
		print("Final")
		#self.metodos.mostrar_matriz(crear_matriz)
		input()







#----------------------MENU----------------------------------

	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("|--------------------------------|")
			print("|        MENU DE OPCIONES        |")
			print("|--------------------------------|")
			print("|--------------------------------|")
			print("|1) Codigo Morse                 |")
			print("|2) Matriz                       |")
			print("|0) Finalizar                    |")
			print("|--------------------------------|")

			try:
				op = int(input("Digite su opcion: "))

				if op == 1:
					self.codigo_morse()

				elif op == 2:
					self.matriz()

				elif op == 0:
					break

				else:
					print("|--------------------------------|")
					print("|La opcion digitada es incorrecta|")
					print("|--------------------------------|")
					input()


			except ValueError:
				print("|-----------------------------------|")
				print("|  Error - El dato debe ser entero  |")
				print("|-----------------------------------|")
				input()

if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_principal()