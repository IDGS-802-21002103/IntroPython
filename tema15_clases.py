import os

class OperaBas:
  #declaracion de propiedades
    num1=0
    num2=0
    res=0

#declaracion de constructor
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es: ", self.res)

def main():
    os.system("cls")
    obj=OperaBas(3,4)
    obj.suma()


if __name__ == "__main__":
    main()