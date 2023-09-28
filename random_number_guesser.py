
import random

print("Welcome To The Gusseing Game !! ")

play = input("Do You Want To Play: ").lower()

#ASKING THE PLAYER IF HE WANTS TO PLAY 
if play != "yes":
    print("Ok See ya Then")
    quit()
else:
    print("Lets Get Started !! ")
    print()



top_num = input("What is the Top range of the Number you want to guess : ")


#CHECKING IF THE INPUT IS A INTEGER
if top_num.isdigit():
    top_num = int(top_num)
else:
    print("Please Enter A Number !! ")
    print()
    quit()


#CHECKING IF THE INPUT IS Guessable
if (top_num >= 300) or (top_num <= 0 ):
    print("Please Enter a number That is Bigger Than 0 and Smaller Than 300 !! ")
    print()
    quit()
else:
    print()


rand = random.randint(0,top_num)
print(rand)

guesses = 0

while True:
    guesses = guesses + 1
    usr_input = input("What do you Think The Number We got is ???  ")
    if usr_input.isdigit():
        usr_input = int(usr_input)
    else:
        print("Enter a Valid Number !!")
        print()
        continue

    if usr_input == rand:
        if guesses == 1:  
            print("****** WOW YOU GUESSED THE NUMBER ON YOUR FIRST TRY ******")
            break
        else:
            print("Good job you Guessed It ")
            print("You guessed",guesses,"times")
            break 
    elif usr_input > rand:
        print("You Were Above The Number")
    else:
        print("You Were Below The Number")
    print("Try Again !! ")








