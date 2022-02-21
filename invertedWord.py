from consoleClearner import clearConsole

# Inverted word (Ejercicio 8)
def invertedWord(): 
    while True: # invierte la palabra
        clearConsole()
        invertedWord = "" # Guarda la nueva palabra
        print(f"Ejercicio 8 (Palabra invertida + lol): \n")
        word = input("Digite una frase => ")
        currentPosition = len(word) - 1 
        if len(word) > 0:
            for character in range(len(word)): # Crea una nueva palabra, comenzando por el ultimo caracter de la palabra anterior
                character = word[currentPosition]
                invertedWord += character # Agrega el caracter a la nueva palabra
                currentPosition -= 1 # Retrocede un caracter
            print(f"\nSu frase es => {invertedWord}lol")
            input("\n\nPresiona enter para continuar...")
            break

invertedWord()
