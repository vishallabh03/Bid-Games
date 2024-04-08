import random
Rock = '''  

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper ='''

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors ='''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images=[Rock,Paper,Scissors]
your_choice= int(input("What do you want to choose ? Type 0 for Rock,1 for Paper,2 for Scissor\n"))
if your_choice>=3 or your_choice<0:
    print(" You enter the inavalid number")
else:   
    print(images[your_choice])
    computer_choice=random.randint(0,1)
    print("computer chosses the ")
    print(images[computer_choice])
    if computer_choice==2 and your_choice==0:
       print("You win")
    elif computer_choice==0 and your_choice==2:
       print("You Lose")    
    elif computer_choice > your_choice:
       print("You lose ")  
    elif computer_choice< your_choice:
       print("you win")      
    elif computer_choice==your_choice:
       print("it's a  Draw")
   