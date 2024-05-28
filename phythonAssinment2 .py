print("Hello it's nice to meet you. What is your name?")
name = input ()
print("It is nice to meet you, " + name + ".")
print(" Welcome to The Big Giveaway!!")


validChoice = False
while validChoice == False:
	print("Please Choose A Door (1, 2, or 3) : ")
	choice = input()
	if choice == "1":
		print("You won a new house!")
		validChoice = True
	elif choice == "2":
		print("You won a million dollars!")
		validChoice = True
	elif choice == "3":
		print("You won cardboard shirt")
		validChoice = True
	else:
		print("That isn't one of the choices. Please try again.")
print("Thanks for playing!")
