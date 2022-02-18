from consoleClearner import cleanConsole


def polydivisibleNumber():
    while True: 
        cleanConsole()
        numbersApproved = 0
        print(f"Ejercicio 6 (Numero polidivisible): \n")
        number = input("Digite un numero => ")
        if number.isdigit():
            startingLen = len(number)
            number = int(number)
            while True:
                currentOperation = number / (len(str(number)))
                if currentOperation.is_integer():
                    numbersApproved += 1
                    if len(str(number)) == 1:
                        break
                    else: 
                        number = int(str(number)[:-1])
                else: 
                    break
        print("\n* Verdadero" if numbersApproved == startingLen else "\n* Falso")
        input("\n\nPresiona enter para continuar...")
        break

# Si se ejecuta de forma independiente
polydivisibleNumber()