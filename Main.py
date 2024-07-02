import random
from os import system, name

def limpa_tela():

    if(name == 'nt'):
        _ = system('cls')
    else:
        _ = system('clear')


def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def game():

    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ['banana','abacate','uva','morango','laranja']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances > 0:

       
        print(display_hangman(chances))
        print("".join(letras_descobertas))
        print("Letras erradas: ","".join(letras_erradas))
        
        
        tentativa = input("\nDigite uma letra:").lower()

        if tentativa in palavra:
            indice = 0
            for letra in palavra:
                if letra == tentativa:
                    letras_descobertas[indice] = letra
                indice += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        
        if "_" not in letras_descobertas:
            print("\nParabéns, você venceu. A palavra era: ",palavra)
            break
   
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

if __name__ == "__main__":
    game()
    
         