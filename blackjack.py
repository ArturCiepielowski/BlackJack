import random
from tkinter import Y

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

myScore = 0
compScore = 0
my_cards = []
comp_cards = []


def cardShuffle():

    my_cards = []
    comp_cards = []

    my_cards.append(cards[random.randint(0, 12)])
    my_cards.append(cards[random.randint(0, 12)])
    myScore = 0
    for x in my_cards:
        myScore = myScore + x

    comp_cards.append(cards[random.randint(0, 12)])
    comp_cards.append(cards[random.randint(0, 12)])
    compScore = 0
    for y in comp_cards:
        compScore = compScore + y


def firstWinCondition():
    if compScore == 21 and myScore < 21:
        print(
            f"The Computer is the winner. \n Computer score: {compScore} \n Player score: {myScore}"
        )
        blackJack = False
    elif myScore == 21 and compScore < 21:
        print(
            f"The Player is the winner. \n Computer score: {compScore} \n Player score: {myScore}"
        )
        blackJack = False
    elif compScore == 21 and myScore == 21:
        print(
            f"The Computer is the winner. \n Computer score: {compScore} \n Player score: {myScore}"
        )
        blackJack = False


def winCondition():
    if compScore == 21 and myScore < 21:
        print(
            f"The Computer is the winner. \n Computer score: {compScore} \n Player score: {myScore}"
        )
        blackJack = False
    elif myScore == 21 and compScore < 21:
        print(
            f"The Player is the winner. \n Computer score: {compScore} \n Player score: {myScore}"
        )
        blackJack = False
    elif compScore == 21 and myScore == 21:
        print(
            f"The Computer is the winner. \n Computer score: {compScore} \n Player score: {myScore}"
        )
        blackJack = False
    elif compScore > myScore:
        print(
            f"The Computer is the winner. \n Computer score: {compScore} \n Player score: {myScore}"
        )
        blackJack = False
    elif myScore > compScore:
        print(
            f"The Player is the winner. \n Computer score: {compScore} \n Player score: {myScore}"
        )
        blackJack = False


def looseCondition():
    if myScore > 21:
        print(
            f"The Player lost. \n Computer score: {compScore} \n Player score: {myScore}"
        )
    elif compScore > 21:
        print(
            f"The Computer lost. \n Computer score: {compScore} \n Player score: {myScore}"
        )


cardShuffle()
blackJack = True
while blackJack:

    Game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if Game == "y":
        print(f"Your cards :{my_cards},   current score: {myScore}")
        print(f"Computer first card : {comp_cards[0]}")

        firstWinCondition()

        loop = True

        if blackJack == True:

            while loop:
                gameContinue = input(" Type 'y' to get another card, type'n' to pass: ")

                if gameContinue == "y":
                    my_cards.append(cards[random.randint(0, 12)])
                    myScore = 0
                    for x in my_cards:
                        myScore = myScore + x
                    print(f"Your cards :{my_cards},   current score: {myScore}")
                    print(f"Computer first card : {comp_cards[0]}")
                    looseCondition()
                elif gameContinue == "n":
                    loop = False
                    winCondition()
                    my_cards = []
                    comp_cards = []
    elif Game == "n":
        blackJack = False
