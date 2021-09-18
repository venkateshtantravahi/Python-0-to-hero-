"""
Rock Paper Scissor Project without UI
"""

import random, re , os
i_count, u_count = 0,0

# Clearing the input window before appearing
os.system('cls' if os.name == 'nt' else 'clear')

while( 1 < 2):
    print("\n")
    print("Rock-Paper-Scissor--- Let's Shoot!")
    userChoice = input("Choose Your Weapon [R]ock,[P]aper, [S]cissor: ")
    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter")
        print("[R]ock, [S]cissor or [P]aper.")
        continue
    # Echo the user's choice
    print("You Choose:", userChoice)
    choices = ['R', 'P', 'S']
    opponentChoice = random.choice(choices)
    print("I Choose: ", opponentChoice)
    if opponentChoice == str.upper(userChoice):
        print("Match Tie!!")
    elif opponentChoice == 'S' and userChoice.upper() == 'R':
        print("Rock Beats Scissor, I Win!")
        continue
    elif opponentChoice == 'P' and userChoice.upper() == 'S':
        print("Scissor Beats Paper, I Win!!")
        continue
    elif opponentChoice == 'R' and userChoice.upper() == 'P':
        print("Paper Beats Rock, I Win!!!")
        continue
    else:
        print("You Won!!")