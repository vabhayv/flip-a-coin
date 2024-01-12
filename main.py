import random
input("Want to flip a coin?\nTap enter")
luck = random.randint(0,1)
if luck==0:
    print("It's Heads")
else:
    print("It's Tails")