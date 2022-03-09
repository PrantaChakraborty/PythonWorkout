import random
number = random.randint(10, 100)
while True:
	user_input = int(input("Enter number"))
	if user_input < number:
		print("Guess is greater than number")
	elif user_input > number:
		print("Guess is less than number")
	elif number == user_input:
		print("Match")
		break
	
		
