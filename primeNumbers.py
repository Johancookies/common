from consoleClearner import clearConsole

# Lista de numeros primos (Ejercicio 2)
def primeNumbers():
    startingNumber = 1
    while True:
        clearConsole() 
        print("Ejercicio 2 (Numeros primos):\n")
        primeAmount = input("Digite la cantidad de numeros primos que quiere => ")
        if primeAmount.isdigit(): # Verifica que la entrada sea numerica
            primeAmount = int(primeAmount) # Cambia el tipo de dato a numerico
            numberCollection = []
            while primeAmount > len(numberCollection):
                operationsCount = 0 # Guarda el numero de operaciones que tienen resultado entero
                for currentNumber in range(startingNumber):
                    currentOperation = startingNumber / (currentNumber + 1)
                    if currentOperation.is_integer(): # Verifica que el resultado de la divison sea entero
                        operationsCount += 1
                if operationsCount == 2: # Verifica si el numero es primo, contanso sus dos posible divisones
                    numberCollection.append(startingNumber)        
                startingNumber += 1
            break
    print(f"Su lista de numeros es: \n{numberCollection}")
    input("\n\nPresiona enter para continuar...")

primeNumbers()