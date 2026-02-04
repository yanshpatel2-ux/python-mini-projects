import random
difficulty = input("Enter the difficulty level: Easy[1,20],Medium[1,100] or Hard[1-500]: ")
attempts = int(input("Enter how many attempts you want: "))
difficulty_level = difficulty.lower()
limit = 0
if difficulty_level == "easy":
    limit = 20
elif difficulty_level == "medium":
    limit = 100
elif difficulty_level == "hard":
    limit = 500
else:
    print("Defaulting range to 100")
    limit = 100
com_num = random.randint(1,limit)
for i in range(1,attempts+1):
    user_number = int(input("Enter the number: "))
    if com_num == user_number:
        print(f"You gussed it correctly in {i} attempts")

        break
    elif user_number > com_num:
        print("Too high get lower")
    elif user_number < com_num:
        print("Too low get higher")
else:
    print("The number was: ",com_num)
    print("You are out of your attempts try again!!!")

