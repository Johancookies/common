from consoleClearner import cleanConsole

# Organizador de arreglos (Ejercicio 5)
def arrayOrganizer():
    while True: 
        cleanConsole()
        print(f"Ejercicio 5 (Organizador de arreglos): \n")
        number = input("Digite un numero de campos para su arreglo => ")
        if number.isdigit():
            dataCollection = []
            number = int(number)
            for currentValue in range(number):
                while True:
                    value = input(f"Digite valor {currentValue + 1} => ")
                    if len(value) > 0:
                        break
                dataCollection.append(value)
            newDataCollection = organizeByAsciiCode(dataCollection)
            print(f'\nSu arreglo organizado es: \n\n {newDataCollection}')
            input("\n\nPresiona enter para continuar...")
            break

# Organiaza por el valor ascii del primer caracter
def organizeByAsciiCode(dataCollection):
    dataCollection.append(" ")
    littleBuddy = ""
    maxIndex = len(dataCollection) - 1
    for x in range(maxIndex):
        for index in range(maxIndex):
            if index < maxIndex:
                if ord(dataCollection[index][0]) > ord(dataCollection[index + 1][0]):
                    littleBuddy = dataCollection[index + 1]
                    dataCollection[index + 1] = dataCollection[index]
                    dataCollection[index] = littleBuddy
                    
        
    del dataCollection[0]
    return dataCollection

# Si se ejecuta de forma independiente
arrayOrganizer()