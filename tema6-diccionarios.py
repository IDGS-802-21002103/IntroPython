miDiccionario={"Matricula":1234,"Nombre":"German","Apellidos":"Vargas"}
print(miDiccionario["Nombre"])
print(miDiccionario["Apellidos"])
print(miDiccionario["Matricula"])
print(miDiccionario)
print(type(miDiccionario))
print(miDiccionario.keys())
print(miDiccionario.values())
print(len(miDiccionario))
print(miDiccionario.items())
print(miDiccionario.get("Nombre"))

miDiccionario["Nombre"]="Juan"
print(miDiccionario)

miDiccionario["correo"]="damian@gmail.com"
print(miDiccionario)