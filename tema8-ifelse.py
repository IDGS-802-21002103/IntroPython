print("Suma de Numeros")

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

if num1>num2:
    print("El numero {} es mayor que {}".format(num1, num2))
else:
    print("El numero {} es mayor que {}".format(num2, num1))

print("-------------- pedir una edad -------------------");
edad=int(input("Ingrese su edad: "))
if edad>=18:
    print("Usted es mayor de edad")
elif edad==18:
      print("Tienes 18 años")
else:
    print("Usted es menor de edad")