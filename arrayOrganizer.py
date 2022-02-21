from consoleClearner import clearConsole

# Organizador de arreglos (Ejercicio 5)
def arrayOrganizer():
    while True: 
        clearConsole()
        print(f"Ejercicio 5 (Organizador de arreglos): \n")
        number = input("Digite un numero de campos para su arreglo => ")
        if number.isdigit(): #Verifica que la entrada sea numerica
            dataCollection = []
            number = int(number) # Cambia el tipo de dato a entero
            for currentValue in range(number): # Recolecta la cantidad de datos
                while True:
                    value = input(f"Digite valor {currentValue + 1} => ")
                    if len(value) > 0:
                        break
                dataCollection.append(value)
            newDataCollection = organizeByAsciiCode(dataCollection)
            print(f'\nSu arreglo organizado es: \n\n {newDataCollection}')
            input("\n\nPresiona enter para continuar...")
            break

def organizeByAsciiCode(dataCollection): # Oraniza el arreglo de acuerdo a el valor assci del primer caracter
    dataCollection.append(" ") # Agreaga registro vacio, para evitar el error "Index out of range" al momento de oganizar
    littleBuddy = "" # Variable de ayuda para hacer la origanizacion
    maxIndex = len(dataCollection) - 1 # Limita la cantidad de ciclos
    for x in range(maxIndex): #Organiza el arreglo con metodo burbuja
        for index in range(maxIndex):
            if index < maxIndex:
                if ord(dataCollection[index][0]) > ord(dataCollection[index + 1][0]):
                    littleBuddy = dataCollection[index + 1]
                    dataCollection[index + 1] = dataCollection[index]
                    dataCollection[index] = littleBuddy
                    
        
    del dataCollection[0] # Elimina el registro vacio agreagdo anteriormente
    return dataCollection

arrayOrganizer()