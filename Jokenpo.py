from random import choice
print("-=-" * 20)
print("Jogue Jokenpo")
print("-=-" * 20)

escolhas = ["PEDRA","PAPEL","TESOURA"]
computador = choice(escolhas)
jokenpo = str(input("Digite qual é sua escolha (Pedra,Papel ou Tisora): ")).upper()

#PEDRA
if jokenpo == "PEDRA" and computador == "PEDRA":
    print("Empatou")
    print("Voce escolheu {} e o computador {}".format(jokenpo,computador))
elif jokenpo == "PEDRA" and computador == "TESOURA" or computador == "PEDRA" and jokenpo == "TESOURA":
    print("Pedra ganha de Tesoura, quem jogou Pedra ganhou")
    print("Voce escolheu {} e o computador {}".format(jokenpo,computador))
elif jokenpo == "PEDRA" and computador == "PAPEL" or computador == "PEDRA" and jokenpo == "PAPEL":
    print("Papel ganha de Pedra, quem jogou Papel ganhou")
    print("Voce escolheu {} e o computador {}".format(jokenpo,computador))

#PAPEL
elif jokenpo == "PAPEL" and computador == "PAPEL":
    print("Empatou")
    print("Voce escolheu {} e o computador {}".format(jokenpo,computador))
elif jokenpo == "PAPEL" and computador == "TESOURA" or computador == "PAPEL" and jokenpo == "TESOURA":
    print("Tesoura ganha de Papel, quem jogou Tesoura ganhou")
    print("Voce escolheu {} e o computador {}".format(jokenpo,computador))

#TESOURA
elif jokenpo == "TESOURA" and computador == "TESOURA":
    print("Empatou")
    print("Voce escolheu {} e o computador {}".format(jokenpo,computador))


