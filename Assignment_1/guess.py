import random
a = random.randint(0,100)
chances = 50
def guess(a) :
	global chances 
	b = input("Guess Number : ")
	if(b == a) :
		print("correct guess")
		return
	elif(a > b) :
		print("Number is greater")
		chances = chances - 1
		guess(a)
	elif(a < b) :
		print("Number is smaller")
		chances =  chances - 1
		guess(a)
print("LET'S GUESS IT...")
print("You have 50 chances!")
guess(a)
