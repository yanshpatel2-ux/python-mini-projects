import random
player_input = input("Enter rock, paper or scissor?: ")
player_input1 = player_input.lower()
elements = random.choice(["rock", "scissor", "paper"])
print("Computer's choice: ", elements)

if player_input1 == elements:
    print("It's a tie")
else:
    if player_input1 == "rock":
        if elements == "paper":
            print("You lost")
        else:
            print("You won!!!")
    
    elif player_input1 == "paper":
        if elements == "scissor":
            print("You lost!!!")
        else:
            print("You won!!!")
    
    elif player_input1 == "scissor":
        if elements == "paper":
            print("You won!!!")
        else:
            print("You lost")
            
    else:
        print("Invalid input! Check your spelling.")