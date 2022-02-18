from consoleClearner import cleanConsole

# Numero x es potencia de 2 (Ejercicio 4)
def powerNumber(): 
    numberList = []
    while True: 
        cleanConsole()
        print(f"Ejercicio 4 (Numero x es potencia de 2): \n")
        number = input("Digite un numero => ")
        if number.isdigit():
            number = int(number)
            startingPoint = 1
            while True:
                newNumber = 2 ** startingPoint
                if newNumber <= number:
                    numberList.append(newNumber)
                    startingPoint += 1
                else:
                    break
            print("\n* Verdadero" if number in numberList else "\n* Falso")
            input("\n\nPresiona enter para continuar...")
            break
        
# Si el ejercicio es ejecutado independientemente
powerNumber()
