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

#Write your code below this line 👇
import random
human = int (input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if human == 0:
  print(rock)
elif human == 1:
  print(paper)
else:
  print(scissors)
set = [rock, paper, scissors]
cpu = random.randint(0,2)

print("Computer chose:")
print(set[cpu])

if cpu == human:
  print("It's a tie!")
elif (human == 0 and cpu == 2) or (human == 1 and cpu == 0) or (human == 2 and cpu == 1):
    print("You win!")
else:
    print("You lose.")

