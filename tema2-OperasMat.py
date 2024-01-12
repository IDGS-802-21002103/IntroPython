num1=20
num2=4

print("Suma: ", num1+num2)
print("Resta: ", num1-num2)
print("Multiplicacion: ", num1*num2)
print("Division: ", num1/num2)
print("Division Entera: ", num1//num2)
print("Modulo: ", num1%num2)
print("Potencia: ", num1**num2)

#Concatenacion en python

texto= "Hola"
texto2="Mundo"
textoFinal=texto + " " + texto2

print(textoFinal)
print("El saludo es: %s %s" %(texto, texto2))

saludoFinal="El saludo es: {} {}".format(texto, texto2)
print(saludoFinal)

saludoFinal2="Saludo {x} {y}".format(x=texto, y=texto2)
print(saludoFinal2)
