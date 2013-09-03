from Engine import *
from sys import exit

stopPlaying = False
while not stopPlaying:
	
	num_players = int(raw_input("How many players do you want to play against?\n> "))
	
	if num_players > 9:
		print "Too many players! You'll use up the whole deck."
		print "Goodbye!"
		exit(1)
	
	game = Engine(num_players)
	print game.play()
		
	next = raw_input("Keep playing?(y/n)\n> ")
	
	if 'n' in next:
		stopPlaying = True
	elif 'y' in next:
		stopPlaying = False
	else:
		print "INVALID RESPONSE. GOODBYE!"
		exit(1)	
		

