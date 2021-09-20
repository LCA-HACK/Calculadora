import pyfiglet
import os
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[39m'
os.system("clear")
b= pyfiglet.figlet_format("Calculadora")
s= pyfiglet.figlet_format("Adios:)")
print(GREEN+b)
while True:
    print("Que vas a hacer?")
    print(RESET+"[1] Suma\n[2] Resta\n[3] Multiplicacion\n[4] Division\n[5] Salir")
    opcion=int(input(RED+">> "))
    if opcion==1:
        num1=int(input(RESET+"Primer número: "))
        num2=int(input("Segundo número: "))
        suma= num1 + num2
        print(YELLOW+"El resultado de la suma es: " ,suma)
    if opcion==2:
        num1=int(input(RESET+"Primer número: "))
        num2=int(input("Segundo número: "))
        resta= num1 - num2
        print(YELLOW+"El resultado de la resta es: " ,resta)
    if opcion==3:
        num1=int(input(RESET+"Primer número: "))
        num2=int(input("Segundo número: "))
        mult= num1 * num2
        print(YELLOW+"El resultado de la multiplicacion es: " ,mult)
    if opcion==4:
        num1=int(input(RESET+"Primer número: "))
        num2=int(input("Segundo número: "))
        div= num1 / num2
        print(YELLOW+"El resultado de la division es: " ,div)
    if opcion==5:
        print(GREEN+s)
        break
