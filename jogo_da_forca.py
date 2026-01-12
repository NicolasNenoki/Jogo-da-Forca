import random
bonecos = [
    """
      +---+
      |   |
          |
          |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    ========= """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========= """
]

palavras = ["ARROZ", "FEIJAO", "ALFACE", "SALAME", "MORANGO", "BATATA", "CARNE", "FRANGO","PIMENTA", "QUEIJO", "PRESUNTO"]
palavra_sorteada = random.choice(palavras)
letras_erradas = []
letras_certas = []
tentativas = 6

palavra_oculta = ["_"] * len(palavra_sorteada)

def mostrar_jogo():
    print(bonecos[6 - tentativas])
    print("\nPalavra: ", end="")
    for letra in palavra_oculta:
        print(letra, end=" ")
    print()

    print("Letras erradas: ", end="")
    if len(letras_erradas) == 0:
        print("Nenhuma", end="")
    else:
        for i in range(len(letras_erradas)):
            print(letras_erradas[i], end="")
            if i < len(letras_erradas) - 1:
                print(" - ", end="")
    print()
    print(f"Tentativas restantes: {tentativas}\n")
#print("--------------------------------------------------")
print("•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•\n\t---Jogo da Forca---")
print("•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•")
print("DICA: Comida")
print("""
╔═════════════════════════╗
║🔥Que comecem os jogos🔥║
╚═════════════════════════╝""")

mostrar_jogo()

while tentativas > 0:
    chute = (input("Chute uma letra ou uma palavra: ")).upper()
    if len(chute) > 1:
        if chute == palavra_sorteada:
            print("Parabéns você acertou a palavra inteira!!!")
            break
        else:
            print("Errou, perdeu 2 tentativas!")
            tentativas -=2
            mostrar_jogo()
            continue
    if len(chute) != 1:
        print("Digite só uma letra por vez!")
        continue
    if chute in letras_certas or chute in letras_erradas:
        print("Essa letra já foi!!")
        continue
    if chute in palavra_sorteada:
        print("ACERTOU!!!")
        for i in range(len(palavra_sorteada)):
            if palavra_sorteada[i] == chute:
                palavra_oculta[i] = chute
        letras_certas.append(chute)
    else:
        print("ERROU!")
        letras_erradas.append(chute)
        tentativas -= 1

    mostrar_jogo()

    ganhou = True
    for letra in palavra_oculta:
        if letra == "_":
            ganhou = False
            break

    if ganhou == True:
        print("PARABENS!!! GANHOU O JOGO!!!")
        print(f"A palavra era: {palavra_sorteada}")
        break

if tentativas == 0:
    print(bonecos[6])
    print("Acabou para você, sobe na FORCA!!!")
    print(f"A palavra correta era: {palavra_sorteada}")
print("\nFIM!!! Fique a vontade para jogar novamente!")
