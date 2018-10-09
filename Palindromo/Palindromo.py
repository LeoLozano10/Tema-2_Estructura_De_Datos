#Programa para saber si una palabra es un palindromo.

print ("Verificar si la palabra ingresada es un palindromo")
palabra= input("Ingresa el palindromo: ")

palabra_sin_espacios = palabra.replace(" ","")

def palindromo(string):
	if len(string)<=1:
		return True
	else:
		return string[0] == string[-1] and palindromo(string[1: -1])

if palindromo(palabra_sin_espacios) == True:
	print("LA FRASE: "+str(palabra)+"  Es palindromo")
else:
	print("LA FRASE: "+str(palabra)+" No es Palindromo")