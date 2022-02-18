from consoleClearner import cleanConsole

# Inverted word (Ejercicio 8)
def invertedWord(): 
    while True: 
        cleanConsole()
        invertedWord = ""
        print(f"Ejercicio 8 (Palabra invertida + lol): \n")
        word = input("Digite una frase => ")
        currentPosition = len(word) - 1 
        if len(word) > 0:
            for character in range(len(word)):
                character = word[currentPosition]
                invertedWord += character
                currentPosition -= 1
            print(f"\nSu frase es => {invertedWord}lol")
            input("\n\nPresiona enter para continuar...")
            break

# Si el ejercicio es ejecutado independientemente
invertedWord()
