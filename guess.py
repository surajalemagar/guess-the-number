import random
n=random.randint(0,20)
print("GUESS THE NUMBER!!!")
N=int(input("\nEnter the number of wrong attempt!!!:"))
while N>0:
    print("Number of attempt remaining:",N)
    guess=int(input("Guess the number between 1 and 20:"))
    if guess==n:
        print("\nCorrect Answer is :",n)
        print("Congratulations!!! You Guess the right number!!!")
        break
    else:
        N=N-1
        if N==0:
            print("\nYou lose the game.Try Again!!!")
            print("Correct Answer is :",n)
            break
        if guess>n:
            print("\nYou need to guess lower:")
        else:
            print("\nYou need to guess higher:")
    