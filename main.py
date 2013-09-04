from Engine import *
from sys import exit

#Game continues playing until the user tells it to stop
stopPlaying = False
while not stopPlaying:
	
    #User determines number of computer players to play against
	num_players = int(raw_input("How many players do you want to play against?\n> "))
	
    #Cannot deal more cards than are in the deck
	if num_players > 9:
		print "Too many players! You'll use up the whole deck."
		print "Goodbye!"
		exit(1)
	
    #Play game
	game = Engine(num_players)
	print game.play()
	
    #User determines if (s)he wants to continue playing
	next = raw_input("Keep playing?(y/n)\n> ")
	
	if 'n' in next:
		stopPlaying = True
	elif 'y' in next:
		stopPlaying = False
	else:
		print "INVALID RESPONSE. GOODBYE!"
		exit(1)	
		

