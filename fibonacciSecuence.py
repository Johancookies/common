from consoleClearner import cleanConsole

# Serie Fibonacci (Ejercicio 7)
def fibonacciSecuence(): 
    while True:
        cleanConsole()
        print("Ejercicio 7 (Serie Fibonacci):\n")
        number = input("Digita limite de la serie => ")
        numberCollection = [0, 0, 1]
        currentPosition = 2
        if number.isdigit(): 
            number = int(number)
            for x in range(number):
                numberCollection.append(numberCollection[currentPosition] + numberCollection[currentPosition - 1] + numberCollection[currentPosition - 2])
                currentPosition += 1
        break
    print(f"\nLa serie Fibonacci es: \n{showList(numberCollection)}")
    input("\n\nPresiona enter para continuar...") 

def showList(numberCollection):
    newCollection = []
    currentPosition = 2
    for x in range(len(numberCollection) - 2):
        newCollection.append(numberCollection[currentPosition])
        currentPosition += 1
    return newCollection[:-1]
    
# Si se ejecuta de forma independiente
fibonacciSecuence() 