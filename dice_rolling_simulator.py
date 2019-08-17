#esse scrip simula o rolar de um dado
#importa a biblioteca random
import random

#função que retorna o número que você tirou nos dados
def roll(sides):
        num_rolled = random.randint(1,sides)
        return num_rolled


#função que simula a escolha de jogar os dados, nela você seleciona o tipo de dado
#também decide se quer ou não jogar ele 
def main():
    sides = int(input("How many sides does your dice has? "))
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? (r=roll.q=quit.c=changethedice) ")
        if roll_again == "r":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
        elif roll_again == "c":
            sides = int(input("How many sides does your dice has? "))
        else:
            rolling = False
            print("Thanks for playing")


main()