from consoleClearner import clearConsole

# Serie Fibonacci (Ejercicio 7)
def fibonacciSecuence(): 
    while True:
        clearConsole()
        print("Ejercicio 7 (Serie Fibonacci):\n")
        number = input("Digita limite de la serie => ")
        numberCollection = [0, 0, 1] # Crea la primera secuencia
        currentPosition = 2 # Posicion en donde comienza la verificacion
        if number.isdigit(): # Verifica que la entrada sea numerica 
            number = int(number) #Cambia el tipo de dato a entero
            for x in range(number): # Completa la serie de acuerdo a la cantidad de numeros
                numberCollection.append(numberCollection[currentPosition] + numberCollection[currentPosition - 1] + numberCollection[currentPosition - 2])
                currentPosition += 1
        break
    print(f"\nLa serie Fibonacci es: \n{showList(numberCollection)}")
    input("\n\nPresiona enter para continuar...") 

def showList(numberCollection): # Muestra la lista, eliminando los registros que no pertenecen a la serie
    newCollection = []
    currentPosition = 2
    for x in range(len(numberCollection) - 2):
        newCollection.append(numberCollection[currentPosition])
        currentPosition += 1
    return newCollection[:-1] 
    
fibonacciSecuence() 