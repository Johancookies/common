from consoleClearner import clearConsole

# Frases palindromas (Ejercicio 3)
def palindromePhrase():
    invertedPhrase = "" 
    while True: # Invierte la palabra
        clearConsole()
        print("Frase palindroma (Ejercicio 3)\n")
        phrase = input("Digite una frase => ")
        if len(phrase) > 0:
            currentPosition = len(phrase) - 1 
            for character in range(len(phrase)): 
                character = phrase[currentPosition]
                invertedPhrase += character
                currentPosition -= 1
            if phrase == invertedPhrase: # Verifica que la palabra nueva sea igual a la inicial
                print("Su frase es palindroma!")
            else:
                print("Su frase no es palindroma")
            print(f"Su frase => {phrase}")
            print(f"Frase invertida => {invertedPhrase}")
            input("\n\nPresiona enter para continuar...")
            break

palindromePhrase()