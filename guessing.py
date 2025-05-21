#Guessing game
#generate a random number between 1 and 10. keep asking the user to guess the number until they get it right.
import random
number = random.randint(1, 10)  
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations.....")
        break
    else:
        print("CWrong number, try again.")
        
  