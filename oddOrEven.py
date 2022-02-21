from consoleClearner import clearConsole

# Numero par o impar (Ejercicio 1)
def oddOrEven(): 
    while True:
        clearConsole()
        print("Ejercicio 1 (Numero par o impar):\n")
        number = input("Digita un numero => ")
        if number.isdigit(): # Verifica que la entrada sea numerica
            number = int(number) # Cambia el tipo de dato a entero
            if number % 2 == 0: # Verifica si es par o impar con el reciduo de la division
                print(f'Tu numero es par. \nSu suma es => {number + number}')
            else:
                print(f'Tu numero es impar. \nSu doble es => {number * number}')
            input("\n\nPresiona enter para continuar...")
            break

oddOrEven()