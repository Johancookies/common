from consoleClearner import clearConsole

def polydivisibleNumber():
    while True:
        clearConsole()
        numbersApproved = 0 # Cuenta la cantidad de divisones posibles para el numero
        print(f"Ejercicio 6 (Numero polidivisible): \n")
        number = input("Digite un numero => ")
        if number.isdigit():
            startingLen = len(number) 
            number = int(number)
            while True:
                currentOperation = number / (len(str(number))) # Guarda el resultado de la operacion actial
                if currentOperation.is_integer(): #Verifica si es entero
                    numbersApproved += 1 # Cuenta una divion con resultado entero
                    if len(str(number)) == 1: #Termina el proceso si solo es de una cifra el numero
                        break
                    else: 
                        number = int(str(number)[:-1]) # Eetira la ultima cifra del numero
                else: 
                    break
        print("\n* Verdadero" if numbersApproved == startingLen else "\n* Falso") 
        input("\n\nPresiona enter para continuar...")
        break

polydivisibleNumber()