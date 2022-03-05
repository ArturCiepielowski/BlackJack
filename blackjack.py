import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_first_card=cards[random.randint(0,12)]
my_second_card=cards[random.randint(0,12)]
myScore= my_first_card + my_second_card

comp_first_card=cards[random.randint(0,12)]
comp_second_card=cards[random.randint(0,12)]
compScore = comp_first_card + comp_second_card

Game= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if Game == "y":
  print(f"Your cards :[{my_first_card}, {my_second_card}],   current score: {myScore}")
  print(f"Computer first card : {comp_first_card}")

  if compScore == 21 and myScore < 21:
    print("The Computer is the winner")
  elif myScore == 21 and compScore <21:
    print("The Player is the winner")
  elif  compScore == 21 and  myScore == 21:
    print("The Computer is the winner")
  
  gameContinue= input(" Type 'y' to get another card, type'n' to pass: ")
  loop = True

  while loop:
    if gameContinue == "y":
        