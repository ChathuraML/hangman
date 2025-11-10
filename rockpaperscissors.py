import random
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
---'    ____)____
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

rps = [rock, paper, scissors]

choisee = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if choisee >=0 and choisee <= 2:
    my_choice = rps[choisee]
    print(f"You choose: {my_choice}")

    random_chice = random.choice(rps)
    print(f"Coumputer choose: {random_chice}")

    if random_chice == rock and my_choice == paper:
        print("You Win!....")
    elif random_chice == rock and my_choice == scissors:
        print("You Lost!....")
    elif random_chice == scissors and my_choice == paper:
        print("You Lost!....")
    elif random_chice == scissors and my_choice == rock:
        print("You Win!....")
    elif random_chice == paper and my_choice == scissors:
        print("You Win!....")
    elif random_chice == paper and my_choice == rock:
        print("You Lost!....")
    else:
        print("It's a Tie!, Let's try again")
else:
    print("Invalied User input. You Lost!")