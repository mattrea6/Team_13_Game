import datetime

'''currently this will allow the user to input for as long as they want, and then tell them
   after the fight whether they did it in time or not. will try and find a way of stopping the 
   timer as soon as 10 seconds is up'''


n = 10    # this is the number of seconds allowed for the rap battle
rap_1 = "words"    # this is the rap the user has to input

def countdown():

	a = datetime.datetime.now()    # a is the variable of the current time

	print("You're in the heat of the battle! You have " + str(n) + " seconds to type " + "'" + rap_1 + "'")

	inp = input("")


	if inp == rap_1:    # if the user writes exactly what they've been told to

		b = datetime.datetime.now()    # make a variable 'b' of the time once they have input they're writing

		c = b - a    # c is the time difference between when they started writing and when they stopped

		divmod(c.days * 86400 + c.seconds, 60)    # this turns the datetime.now() into a format you can use in an if statement


		if c.seconds > 10:    # if they took longer than 10 seconds to write in the input

			print("You didn't do it in time!")

		else:

			print("Well done, you did it in time")

	else:

		print("You didn't rap the right words!")


countdown()

