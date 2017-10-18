import datetime
from roomsgit import rooms
from player import *

global current_room
current_room = rooms["Studio"]
rap = current_room["rap"] # finds the relative rap from the room that you're in 
n = current_room["n"] # this is the time limit you get for rapping in the current room
#repuation = 0

def calculate_reputation(inventory):
    #reputation = 0 #resets reputation of the player
    reputation = 0
    for item in inventory:  #iterates through every item in the players inventory (see player.py)
        reputation = reputation + item["reputation"] #Reputation is added to by each item
    return reputation #The total rep is returned to the function that called it (probs the battle one.)

def battle(n, room):
	print("")
	print("You're in the heat of the battle! You have " + str(n) + " seconds to show your talent and rap " + "'" + current_room["rap"] + "'")
	print("You must type word for word, letter for letter." + "\n")
	yes_or_no = input("Ready? y / n: ")
	if yes_or_no == "y":
		a = datetime.datetime.now() # gets the exact time that the user begins inputting the rap
		rap_input = input("")
		if rap_input == current_room["rap"]: # if the user input is exactly what the room's rap is
			b = datetime.datetime.now() # record the time that the user entered their input
			c = b - a # work out how long it took the user to input by subtracting the start time from the end time
			divmod(c.days * 86400 + c.seconds, 60) # this formats the time into something that can be used in an if statement
			total_time = n + int(calculate_reputation(inventory))
			if c.seconds > total_time: # if the user time is larger than what the room's allocated time is
				print("You didn't rap fast enough!")
			else:
				print("You showed your rapping skills and won the rap battle!")
				current_room["rapperbeat"] = True
				print(total_time)
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


def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]



def print_exit(direction, leads):
	print("GO " + direction.upper() + " to " + leads + ".")


def print_menu(exits):
	for direction in exits:
		print_exit(direction, exit_leads_to(exits, direction))
		if current_room["rapperbeat"] == False:
			print("Battle " + current_room["rapper"])
		else:
			print("")
		print("")


def execute_command(command):
    
    #if 0 == len(command):
     #   return

    #if command[0] == "b":
    #	print("hello world")

    if command.split(' ', 1)[0] == "battle":
    	if current_room["rapperbeat"] == False:
    		
    		battle(n, current_room)
    elif command.split(' ', 1)[0] == "go":
    	execute_go(command.split(' ',1)[1])
    else:
    	print("I don't understand that command")

def execute_go(direction):

	global current_room
	if direction in current_room["exits"]:
		a = (current_room["exits"])
		
		b = a[direction]
		
		current_room = rooms[b]
		
		
	else:
		print("You need to pick a valid direction")



def menu(exits):
	print_menu(current_room["exits"])
	user_input = input("> ")
	if user_input == "q":
		raise SystemExit()
	else:
		return user_input


def main():
	while True:
		
		print_room(current_room)
		command = menu(current_room["exits"])
		#print_menu(current_room["exits"])
		execute_command(command)
		#battle(n, current_room)
		calculate_reputation(inventory)
		
		

main()