import random
print("Welcome to rock paper scissors!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, scissors, paper]
player_choice = int(input("Enter your choice: 0 for rock, 1 for scissors, and 2 for paper. "))
if player_choice>2 or player_choice<0:
    print("Invalid number you loose")
print(images[player_choice])
computer_choice = random.randint(0, 2)
print(f"Computer choose: {computer_choice}")
print(images[computer_choice])

#rock beats scissors
#scissoprs beats paper
#and paper beats rock

if player_choice == 0 and computer_choice == 0:
    print("It's a draw")
elif player_choice == 0 and computer_choice == 1:
    print("rocks beats scissors, You won")
elif player_choice == 0 and computer_choice == 2:
    print("paper beats rock, You loose")
elif player_choice == 1 and computer_choice == 0:
    print("rock beats scissors, You loose")
elif player_choice == 1 and computer_choice == 1:
    print("It's a draw")
elif player_choice == 1 and computer_choice == 2:
    print("scissors beats paper, You won")
elif player_choice == 2 and computer_choice == 0:
    print("paper beats rock, you won")
elif player_choice == 2 and computer_choice == 1:
    print("scissors beats paper, You loose")
else:
    print("It's a draw")