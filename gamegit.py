import datetime 
import random
import time
import sys
import os # this will be used to clear screen when moving room to room
import xlwt # this is what will add the best score to the excel spreadsheet
import xlrd # this module will get info from the excel spreadsheet as to the best score

from roomsgit import rooms
from player import *
from gameparser import *
from Bars import *


workbook = xlrd.open_workbook('example.xls')
worksheet = workbook.sheet_by_name('A Test Sheet') # these commands find the spreadsheet with the best score

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet') # this setup spreadsheet for inputting the score if it is better than the one in the spreadsheet currently

global player_score
player_score = 0 # start player with 0 score

start_time = datetime.datetime.now()

global difficulty_multiplier
difficulty_multiplier = 1.0 # this multiplier will change dependant on user input for difficulty in game's menu

def cls():
            os.system('cls' if os.name=='nt' else 'clear') # this is the function for clearing screen

cls()

def slow_type(statement, typing_speed):
    for letter in statement:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed) # this function allows use of slow_type which prints strings with a typing effect

def screen_menu():
    """First menu when the game is executed. Appears once."""
    slow_type("\n" + "\n" + "RAPPING GAME (title in progress)" + "\n" + "\n" + "\n" + "Your goal is to become the best rapper, and beat Eminem at the Rap Concert." + "\n", 400)
    input("")
    slow_type("The less rappers you have to destroy, the better your overall score will be. The lower your score - the better!" + "\n" + "\n", 400)
    input("")
    global username
    slow_type("What is your name?:" + "\n", 400)
    username = input("> ")
    slow_type("Chose your difficulty - harder difficulty means better score! EASY / MEDIUM / HARD: " + "\n", 400)
    difficulty = input("> ")
    
    global difficulty_multiplier # now uses the user input to edit difficulty_multiplier, which will change time given in rooms AND difficulty of rap given to user to input
    if difficulty.lower() == "easy":
        difficulty_multiplier = 1.5 
    elif difficulty.lower() == "medium":
        difficulty_multiplier = 1.0
    elif difficulty.lower() == "hard":
        difficulty_multiplier = 0.8
    elif difficulty.lower() == "legendary":
        difficulty_multiplier = 0.750
    else:
        slow_type("That's not an option", 400)
        difficulty = input("easy/medium/hard: ")

    cls()



def calculate_reputation(inventory):
    """Calculate reputation and returns it via players inventory."""
    reputation = 0
    for item in inventory:  # iterates through every item in the players inventory (see player.py)
        reputation = reputation + item["reputation"]  # Reputation is added to by each item
    return reputation  # The total rep is returned to the function that called it (probs the battle one.)


def produce_bar():
    """Return a random bar depending on the difficulty for the battle."""
    global difficulty_multiplier
    a = float(difficulty_multiplier)
    length = len(difficulty_dict[a])
    choice = random.randrange(0, length)
    return difficulty_dict[a][choice]


def battle():
    """Function that completes battle, takes a timed input, gives player item etc."""
    global difficulty_multiplier
    global player_score
    players_rap = produce_bar()
    print("")
    
    slow_type("You're in the heat of the battle! You have " + str(round(int(current_room["room_difficulty"]) * difficulty_multiplier + int(calculate_reputation(inventory)))) + " seconds to show your talent and rap " + "\n" + "'" + players_rap + "'" +"\n", 400)
    input("")
    slow_type("You must type word for word, letter for letter." + "\n", 400)
    input("")
    yes_or_no = input("Ready? y / n: " + "\n" + "> ")
    if yes_or_no == "y":
        z = datetime.datetime.now()  # gets the exact time that the user begins inputting the rap
        print("")
        rap_input = normalise_in(input("> "))

        if rap_input == normalise_in(players_rap):  # if the user input is exactly what the room's rap is
            b = datetime.datetime.now()  # record the time that the user entered their input
            c = b - z  # work out how long it took the user to input by subtracting the start time from the end time
            divmod(c.days * 86400 + c.seconds, 60)  # this formats the time into something that can be used in an if statement
            d = current_room["room_difficulty"] * difficulty_multiplier
            total_time = d + int(calculate_reputation(inventory))
            
            if c.seconds > total_time:  # if the user time is larger than what the room's allocated time is
                slow_type("You didn't rap fast enough!", 400)
                input("")
                slow_type("\n" + "That took you " + str(c.seconds) + " seconds, which is " + str(c.seconds - total_time) + " seconds more than it should have." + "\n", 400)
                input("")
                slow_type("You don't have to type in punctuation - that's not the rappers way" + "\n", 400)
                global player_score
                player_score += 10
                input("[ENTER]")
            
            else:
                slow_type("\n" + "\n" + "You showed your rapping skills and won the rap battle!" + "\n", 400)
                current_room["rapperbeat"] = True
                input("")
                slow_type("That took you " + str(c.seconds) + " seconds." + "\n", 400)
                inventory.append(current_room["award"]) # adds an item to inventory which gives the user more time to rap in the next rooms
                input("")
                slow_type("\n" + "Winning the rap battle got you a " + current_room["award"]["name"] + "." + "\n", 400)
                input("")
                slow_type(current_room["award"]["description"] + "\n" + "\n", 400)
                input("")
                slow_type("The " + current_room["award"]["id"] + " gives you an extra " + str(current_room["award"]["reputation"]) + " reputation." + "\n", 400)
                input("")
                slow_type("This now makes your total reputation " + str(calculate_reputation(inventory)) + ".", 400)
                player_score += c.seconds
                print("")
                input("\n" + "[ENTER]")
        else:
            slow_type("You didn't rap the right words, and flopped in the battle." + "\n" + "\n", 400)
            player_score += 10 
            input("[ENTER]")
    
    else:
        slow_type("You pussied out of the fight and got thrown out of the club", 400)
        player_score += 5
        input("")


def print_inventory_items(players_items):
    """Prints a list of inventory items."""
    if len(players_items) == 0:
        slow_type("You currently have no items", 400)
    else:
        slow_type("You have" + list_of_items(players_items) + ".", 400)


def list_of_items(items):
    """Returns a string with all the players items in a list."""
    full_list = ""
    i = 0
    for item in items:
        if i == 0:
            full_list = full_list + item["name"]
            i =+ 1
        else:
            full_list = full_list + ", " + item["name"]
    return full_list


def print_room(current_room):
    """Prints the description of the current room."""
    print("")
    slow_type(current_room["name"].upper() + "\n", 400)
    print("")
    slow_type(current_room["description"], 400)
    print("")


def exit_leads_to(exits, direction):
    """Returns exits of a room."""
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads):
    """Tells the user about an exit."""
    slow_type("\n""GO " + direction.upper() + " to " + leads + ".", 400)


def print_menu(exits):
    """Prints the list of options for the user to choose."""
    print_inventory_items(inventory)
    print("")
    input("")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    if current_room["rapperbeat"] == False:
        if len(current_room["rapper"]) != 0:
            slow_type("\n"+"Battle " + current_room["rapper"], 400)
    else:
        print("")
        print("")


def execute_command(command):
    """Sends the program to the current execute function."""
    if command.split(' ', 1)[0] == "battle":

        if current_room["rapperbeat"] == False: # if the rapper in the current room has not been beaten

            if len(current_room["rapper"]) != 0: # if the room has a rapper in it

                if current_room["rapper"] == "Eminem": 

                    if calculate_reputation(inventory) < 10: # player needs reputation of above 10 to face Eminem
                        
                        print("You need to have a street cred of above 10")
                        input("")
                        print("Your current street credit is at " + str(calculate_reputation(inventory)))
                        input("")

                    else:
                        battle()

                else:
                    battle()

    elif command.split(' ', 1)[0] == "go":
        execute_go(command.split(' ', 1)[1])

    else:
        print("I don't understand that command")


def execute_go(direction):
    """Sends the user to a new room."""
    global current_room
    if direction in current_room["exits"]:
        a = (current_room["exits"])

        b = a[direction]

        current_room = rooms[b] # changes room using direction and current room's exits

    else:
        print("You need to pick a valid direction")



def menu(exits):
    """Produces the menu via print_menu and takes the user's input."""
    print_menu(current_room["exits"])
    print("")
    user_input = input("\n" + "> ")
    if user_input == "q": # this is mainly for ease of developing the game
        raise SystemExit()

    else:
        return user_input


def main():
    """The main program that controls the flow of the program."""
    screen_menu()
    while True:

        print_room(current_room)
        input("")
        command = menu(current_room["exits"])
        execute_command(command) # execute either GO or BATTLE
        calculate_reputation(inventory)
        
        cls()
        if rooms["Concert"]["rapperbeat"] == True:
            end_time = datetime.datetime.now() # ends the timer that has ran throughout the game
            total_game_time = end_time - start_time
            divmod(total_game_time.days * 86400 + total_game_time.seconds, 60) # formats time game has been played into seconds
            scr = total_game_time.seconds
            global player_score
            player_score += scr
            player_score = player_score * difficulty_multiplier

            if difficulty_multiplier == 0.750: # if the game has been played on legendary mode
                player_score = player_score / 4

            slow_type("\n" + "You have beaten one of the greatest rappers ever and performed for thousands," + "\n", 400)
            slow_type("\n" + "Your score for the game was " + str(player_score) + " points!" + "\n", 400)
            
            best_score = worksheet.row(0)[0].value # takes value of score from excel spreadsheet
            if float(player_score) < best_score: # if the users score is lower (better) than the score on the spreadsheet (current best score)
                print("You have the best score of the day - so far!")
                ws.write(0, 0, player_score) # adds the player's score to the spreadsheet, in place of the previous best score
                ws.write(1, 0, username) # adds the user's name in place of the current user's name on the spreadsheet
                wb.save('example.xls') # saves the excel document

            break



main()
