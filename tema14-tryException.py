num = 30
num2 = 0

try:
    resultado=num/num2
except ZeroDivisionError:
    print("No se puede dividir por cero")
    print("Error en el programa")
finally:
    print("Yo siempre aparezco")