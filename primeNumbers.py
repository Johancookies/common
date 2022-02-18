from distutils.command.clean import clean
from consoleClearner import cleanConsole

# Lista de numeros primos (Ejercicio 2)
def primeNumbers():
    startingNumber = 1
    while True:
        cleanConsole() 
        print("Ejercicio 2 (Numeros primos):\n")
        primeAmount = input("Digite la cantidad de numeros primos que quiere => ")
        if primeAmount.isdigit():
            primeAmount = int(primeAmount)
            numberCollection = []
            while primeAmount > len(numberCollection):
                operationsCount = 0
                for currentNumber in range(startingNumber):
                    currentOperation = startingNumber / (currentNumber + 1)
                    if currentOperation.is_integer():
                        operationsCount += 1
                if operationsCount == 2:
                    numberCollection.append(startingNumber)        
                startingNumber += 1
            break
    print(f"Su lista de numeros es: \n{numberCollection}")
    input("\n\nPresiona enter para continuar...")

# Si se ejecuta de forma independiente
primeNumbers()