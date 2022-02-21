from consoleClearner import clearConsole

# Numero x es potencia de 2 (Ejercicio 4)
def powerNumber(): 
    numberList = []
    while True: 
        clearConsole()
        print(f"Ejercicio 4 (Numero x es potencia de 2): \n")
        number = input("Digite un numero => ")
        if number.isdigit(): # Verifica que la entrada sea numerica
            number = int(number) # Cambia elvalor a tipo entero
            startingPoint = 1
            while True: # Guarda los multiplos de 2 hasta llegar al numero ingresado
                newNumber = 2 ** startingPoint 
                if newNumber <= number: # Verifica el resultado de la potencia sea menor para agregarlo 
                    numberList.append(newNumber)
                    startingPoint += 1
                else:
                    break
            print("\n* Verdadero" if number in numberList else "\n* Falso") # Verifica que el numero este dentro de la lista de multiplos de 2
            input("\n\nPresiona enter para continuar...")
            break
        
powerNumber()
