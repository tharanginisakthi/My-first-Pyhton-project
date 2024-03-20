# My-first-Pyhton-project
input  ("What's your choice?") #Input from user
user_choice=("stone", "paper", "scissor")
import random
computer_choice=("stone", "paper", "scissor")
result=random.choice(computer_choice)
print(result)
if user_choice==result:
  print("It's a tie. Try again")
elif user_choice=="stone" and result=="scissor" or\
    user_choice=="stone" and result=="paper" or\
    user_choice=="scissor" and result=="paper":
  print("The user won")
else:
    print("The computer won")
