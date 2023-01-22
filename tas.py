import random

start=input("aya amade shoro bazi hasti ? ")
if start=="yes":
    while start=="yes":
        print(random.randint(1,6))
        game_again=input("Do you want to play the game again ? ")
        if game_again=="no":
            break
    print("I'm waiting for you again")
else:
    end=input("I'm waiting for you again")