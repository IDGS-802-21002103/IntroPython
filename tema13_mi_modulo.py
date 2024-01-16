def tem():
    print("Hola, soy un módulo")
    print("y me llamo", __name__)
    print("y estoy en", __file__)

def main():
    print("Soy una funcion main")

def tem2():
    print("Adios, soy un módulo")

if __name__ == "__main__":
    main()