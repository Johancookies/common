from consoleClearner import cleanConsole

# Numero par o impar (Ejercicio 1)
def oddOrEvenNumber(): 
    while True:
        cleanConsole()
        print("Ejercicio 1 (Numero par o impar):\n")
        number = input("Digita un numero => ")
        if number.isdigit(): 
            number = int(number)
            if number % 2 == 0:
                print(f'Tu numero es par. \nSu suma es => {number + number}')
            else:
                print(f'Tu numero es impar. \nSu doble es => {number * number}')
            input("\n\nPresiona enter para continuar...")
            break

# Si se ejecuta de forma independiente
oddOrEvenNumber()