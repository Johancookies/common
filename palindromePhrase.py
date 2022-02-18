from consoleClearner import cleanConsole

# Frases palindromas (Ejercicio 3)
def palindromePhrase():
    invertedPhrase = "" 
    while True: 
        cleanConsole() # Limpia consola
        print("Frase palindroma (Ejercicio 3)\n")
        phrase = input("Digite una frase => ")
        if len(phrase) > 0:
            currentPosition = len(phrase) - 1 
            for character in range(len(phrase)): # Invierte la frase inicial
                character = phrase[currentPosition]
                invertedPhrase += character
                currentPosition -= 1
            if phrase == invertedPhrase:
                print("Su frase es palindroma!")
            else:
                print("Su frase no es palindroma")
            print(f"Su frase => {phrase}")
            print(f"Frase invertida => {invertedPhrase}")
            input("\n\nPresiona enter para continuar...")
            break

# Si el ejercicio es ejecutado independientemente
palindromePhrase()