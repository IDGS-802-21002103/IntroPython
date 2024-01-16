'''
 * Una lista es una secuencia de elementos
 [1,2,3,4,5,6,7,8,9,10]
'''

lista=["Mario",33,29.5,True,'German',20,9]

print(lista)
print(lista[:])
print(lista[2])
print(lista[-1])
print(lista[0:3])
print(lista[3:])
lista.append("Vargas")
print(lista)

lista.insert(2,"Nadia")
print(lista)

lista.extend(["uno",1.1, False])
print(lista)

lista.remove(9)
print(lista)

lista.pop()
print(lista)

lista2=["tres","cuatro"]
lista3=lista+lista2
print(lista3)

print(lista2*4)

lista4=[2,1,5,4,3]
print(lista4)

lista4.sort()
print(lista4)

del lista4[0]
print(lista4)
