
import random

print("Welcome to The Rock,Paper and Scissor Game !!! ")

play = input("Do you want to play : ").lower()

if play != "yes":
    print("Ok Then Good Bye ## ")
    quit()
else:
    print("Ok Then Lets Get Started ")
    print()


usr_input = 0
comp_input = 0 
round = 0

options = ["rock", "paper", "scissor"]

 
while True:
    usr_option = input("What do you Choose : Rock/Paper/Scissor (press 'q' to quit ) : ").lower()
    round = round + 1
    if usr_option == "q":
        print("Nice Playing With You :) ")
        print("The Scores Are ")
        print("You : ",usr_input)
        print("Machine : ",comp_input)
        print("Rounds : ",round)
        quit()

    if usr_option not in options:
        print("Choose a Valid Option ")
        continue

    rand = random.randint(0,2)
    comp_option = options[rand]
    print('The Computer Choose : ',comp_option)

    if usr_option == "rock" and comp_option == "scissor":
        print("congrats you won")
        print("Time For Round ", round)
        usr_input = usr_input + 1
        print()
    elif usr_option == "rock" and comp_option == "rock":
        print("Draw, Lets go Again ")
        print()
    elif usr_option == 'paper' and comp_option == 'paper':
        print("Draw, Lets fo Again")
        print()
    elif usr_option == 'scissor' and comp_option =='scissor':
        print("Draw, Lets fo Again")
        print()
    elif usr_option == "paper" and comp_option == "rock":
        print("congrats you won")
        print("Time for round", round)
        usr_input = usr_input + 1
        print()
    elif usr_option == "scissor" and comp_option == "paper":
        print("congrats you won")
        print("Time for Round", round)
        usr_input = usr_input + 1 
        print()
    else:
        print("You Lost :( ")
        print("Lets Play Again ")
        comp_input = comp_input + 1
        print()
















