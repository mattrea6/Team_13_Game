import datetime
from roomsgit import rooms

global current_room
current_room = rooms["Studio"]
rap = current_room["rap"] # finds the relative rap from the room that you're in
n = current_room["n"] # this is the time limit you get for rapping in the current room


def battle(n, room):
	print("You're in the heat of the battle! You have " + str(n) + " seconds to show your talent and rap " + "'" + rap + "'")
	print("You must type word for word, letter for letter." + "\n")
	yes_or_no = input("Ready? y / n: ")
	if yes_or_no == "y":
		a = datetime.datetime.now() # gets the exact time that the user begins inputting the rap
		rap_input = input("")
		if rap_input == rap: # if the user input is exactly what the room's rap is
			b = datetime.datetime.now() # record the time that the user entered their input
			c = b - a # work out how long it took the user to input by subtracting the start time from the end time
			divmod(c.days * 86400 + c.seconds, 60) # this formats the time into something that can be used in an if statement
			if c.seconds > n: # if the user time is larger than what the room's allocated time is
				print("You didn't rap fast enough!")
			else:
				print("You showed your rapping skills and won the rap battle!")
		else:
			print("You're not rapping the right words")
	else:
		print("You pussied out of the fight and got thrown out of the club")


def print_room(current_room):
	print("")
	print(current_room["name"].upper())
	print("")
	print(current_room["description"])
	print("")


def main():
	while True:

		print_room(current_room)
		battle(n, current_room)
		break

main()
