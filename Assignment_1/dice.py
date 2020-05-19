import random

print("Roll-a-Dice")
while 1:
    choice = input("Roll ? (y/n)")
    if choice == 'y':
        a = random.randint(1, 6)
        print(a)
    elif choice == 'n':
        break

