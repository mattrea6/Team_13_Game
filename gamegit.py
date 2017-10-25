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


""" for finding the current best score from the spreadsheet example.xls """
workbook = xlrd.open_workbook('example.xls')
worksheet = workbook.sheet_by_name('A Test Sheet') 

""" sets up example.xls to recieve a new username and score if the score from this game surpasses current best score"""
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

""" starts the player off with 0 score """
global player_score
player_score = 0 

""" begins the timer for the game """
start_time = datetime.datetime.now()

""" this multiplier will change dependant on user input for difficulty in game's menu """
global difficulty_multiplier
difficulty_multiplier = 1.0 


""" this function is for clearing screen between rooms """
def cls():

            os.system('cls' if os.name=='nt' else 'clear') 

cls()


""" this function takes a string and integer for typing speed to make a typing aesthetic """
def slow_type(statement, typing_speed):

    for letter in statement:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed) 


""" first menu when the game is executed, which appears once """
def screen_menu():

    slow_type("\n" + "\n" + "RAPPING GAME (title in progress)" + "\n" + "\n" + "\n" + "Your goal is to become the best rapper, and beat Eminem at the Rap Concert." + "\n", 400)
    input("")
    slow_type("The less rappers you have to destroy, the better your overall score will be. The lower your score - the better!" + "\n" + "\n", 400)
    input("")

    global username
    slow_type("What is your name?:" + "\n", 400)
    username = input("> ")

    slow_type("Chose your difficulty - harder difficulty means better score! EASY / MEDIUM / HARD: " + "\n", 400)
    difficulty = input("> ")
    
    """ users the user input for difficulty to edit variable difficulty_multiplier """
    global difficulty_multiplier

    if difficulty.lower() == "easy":
        difficulty_multiplier = 1.5 
    elif difficulty.lower() == "medium":
        difficulty_multiplier = 1.0
    elif difficulty.lower() == "hard":
        difficulty_multiplier = 0.8
    elif difficulty.lower() == "legendary":
        difficulty_multiplier = 0.750
        slow_type("You've found the hidden legendary mode! While this mode is very difficult, it is still possible, and will guarantee you a great score", 400)
        input("")
    else:
        slow_type("That's not an option", 400)
        difficulty = input("easy/medium/hard: ")

    cls()


""" calculate reputation and returns it via players inventory """
def calculate_reputation(inventory):

    reputation = 0
    for item in inventory:    # iterates through every item in the players inventory (see player.py)
        reputation = reputation + item["reputation"]    # Reputation is added to by each item
    return reputation    # The total reputation is returned to the function that called it


""" return a random bar depending on the difficulty for the battle """
def produce_bar():

    global difficulty_multiplier
    a = float(difficulty_multiplier)
    length = len(difficulty_dict[a])
    choice = random.randrange(0, length)
    return difficulty_dict[a][choice]


""" function that completes battle, takes a timed input, gives player item etc """
def battle():

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
        z = datetime.datetime.now()    # gets the exact time that the user begins inputting the rap
        print("")
        rap_input = normalise_in(input("> "))

        if rap_input == normalise_in(players_rap):    # if the user input is exactly what the room's rap is
            b = datetime.datetime.now()    # record the time that the user entered their input
            c = b - z    # work out how long it took the user to input by subtracting the start time from the end time
            divmod(c.days * 86400 + c.seconds, 60)    # this formats the time into something that can be used in an if statement
            d = current_room["room_difficulty"] * difficulty_multiplier
            total_time = d + int(calculate_reputation(inventory))
            
            if c.seconds > total_time:    # if the user time (c.seconds) is larger than what the room's allocated time is
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
                inventory.append(current_room["award"])   # adds an item to inventory which gives the user more time to rap in the next rooms
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


""" prints a list of inventory items """
def print_inventory_items(players_items):

    if len(players_items) == 0:
        slow_type("You currently have no items", 400)
    else:
        slow_type("You have" + list_of_items(players_items) + ".", 400)


""" returns a string with all the players items in a list """
def list_of_items(items):

    full_list = ""
    i = 0
    for item in items:
        if i == 0:
            full_list = full_list + item["name"]
            i =+ 1
        else:
            full_list = full_list + ", " + item["name"]
    return full_list


""" prints the description of the current room """
def print_room(current_room):

    print("")
    slow_type(current_room["name"].upper() + "\n", 400)
    print("")
    slow_type(current_room["description"], 400)
    print("")


""" returns exits of a room """
def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]


""" tells the user about an exit """
def print_exit(direction, leads):

    slow_type("\n""GO " + direction.upper() + " to " + leads + ".", 400)


""" prints the list of options for the user to choose """
def print_menu(exits):

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


""" sends the program to the current execute function """
def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "battle":
        if current_room["rapperbeat"] == False:
            if len(current_room["rapper"]) != 0:
                battle()

    elif command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    else:
        print("I don't understand that command")
        input("")


""" sends the user to a new room """
def execute_go(direction):

    global current_room
    if direction in current_room["exits"]:
        a = (current_room["exits"])    # a is the dictionary of exits for the current room

        b = a[direction]    # b is the relevant room given using the key of direction

        current_room = rooms[b]    # changes the current room to the value of the direction key

    else:
        print("You need to pick a valid direction")


""" produces the menu via print_menu and takes the user's input """
def menu(exits):

    print_menu(current_room["exits"])
    print("")
    user_input = input("\n" + "> ")

    normalised_user_input = normalise_input(user_input, False)    # normalises the user's input

    
    if user_input == "q":    # this is mainly for ease of developing the game
        raise SystemExit()

    else:
        return normalised_user_input


""" the main program that controls the flow of the program """
def main():

    screen_menu()
    while True:

        print_room(current_room)
        input("")

        command = menu(current_room["exits"])

        execute_command(command)    # execute either GO or BATTLE

        calculate_reputation(inventory)

        cls()

        if rooms["Concert"]["rapperbeat"] == True:
            end_time = datetime.datetime.now()    # ends the timer that has ran throughout the game
            total_game_time = end_time - start_time
            divmod(total_game_time.days * 86400 + total_game_time.seconds, 60)    # formats time game has been played into seconds
            scr = total_game_time.seconds


            global player_score
            player_score += scr
            player_score = player_score * difficulty_multiplier


            if difficulty_multiplier == 0.750:    # if the game has been played on legendary mode
                player_score = player_score / 4

            if difficulty_multiplier == 1.5:    # if the game has been played on easy mode
                player_score = player_score + 200

            if difficulty_multiplier == 1.0:    # if the game has been played on medium mode
                player_score = player_score + 100


            slow_type("\n" + "You have beaten one of the greatest rappers ever and performed for thousands," + "\n", 400)
            slow_type("\n" + "Your score for the game was " + str(player_score) + " points!" + "\n", 400)

            
            best_score = worksheet.row(0)[0].value    # takes value of score from excel spreadsheet
            if float(player_score) < best_score:    # if the users score is lower (better) than the score on the spreadsheet (current best score)
                print("You have the best score of the day - so far!")
                ws.write(0, 0, player_score)    # adds the player's score to the spreadsheet, in place of the previous best score
                ws.write(1, 0, username)    # adds the user's name in place of the current user's name on the spreadsheet
                wb.save('example.xls')    # saves the excel document
            else:
                slow_type("The best score of the day so far is " + str(best_score) + ".", 400)
                slow_type("\n" + "Playing on a harder difficulty will make it easier to get a better score!", 400)
                slow_type("\n" + "Rumour has it the devs left a 'legendary' mode in the code, it might be worth checking out?", 400)

            break



main()
