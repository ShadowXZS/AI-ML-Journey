import random
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Options and Player
options_rps =[Rock, Paper, Scissors]
#List Items Can Be Variables. 
player_one = int(input("Type Your Option \n 1. Type (0) for Rock. \n 2. Type (1) for Paper. \n 3. Type (2) for Scissors.\n : "))
if player_one <= 2:
#Computer and Choices
    computer_s = random.randint(0,2)
    computer_choice = options_rps[computer_s]
    player_choice = (options_rps[player_one])
    #Display
    print("You choose " + player_choice)
    print("Computer choose " + computer_choice)
    #Game Logic
    if player_choice == computer_choice:
        print("Its a Draw")
    elif player_choice == Rock and computer_choice == Paper:
        print("You Loose")
    elif player_choice == Paper and computer_choice == Scissors:
        print("You Loose")
    elif player_choice == Scissors and computer_choice == Rock:
        print("You Loose")
    else:
        print("You Win")
else:
    print("Please Check Your Option.")
#Added the Error Management After Inspection Parameters Were Shared. 