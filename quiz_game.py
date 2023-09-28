
print("Welcome To The Easiest Quiz In The World ")
play = input("Do You Want To Play This Game : ").lower()

if play != "yes":
    print("Ok Bye Then !!!! ")
    quit()
else:
    print("Lets Begin Then Shall We")

points = 0

q1 = input(str("What is the Name of the Sea that is south of India : ")).lower()

if q1 == "indian ocean":
    print("Correct")
    points += 1 
    print("You have",points,"Points")
else: 
    print("Wrong Answer")
    print()

q2 = input(str("Who Went to the moon : "))

if q2.lower() == "neil armstrong":
    print("Correct")
    points += 1 
    print("You Have",points,"Points")
else:
    print("Wrong Answer")
    print()

q3 = input(str("What is main idealogy of the soviet union : "))

if q3.lower() == "communism":
    print("Correct")
    points += 1 
else:
    print("Wrong Answer")
    print()


if points == 3:
    print("Congrats You have the max Score of ", points)
elif points == 2:
    print("You got a Average Score of ", points)
else:
    print("Honestly Why are you Answering this Quiz ")



