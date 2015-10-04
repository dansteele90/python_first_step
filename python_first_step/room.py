# this game is called the room

from sys import exit
import random

def door2_room1():
	print "You enter through door #2 and find yourself in a room with two doors"
	print "Above door #1 is a riddle with a combination to unlock the door"
	print "Door #2 has no riddle and is unlocked, but a horrid stench seeps through the cracks"
	print "Which door do you take?"
	
	choice = raw_input("-> ")
	
	if "1" in choice:
		while True:
			print "Above Door #1 reads:"
			print "\nWhat has four legs and 1 foot?"
			choice = raw_input("-> ")
		
			if "bed" in choice:
				print "Correct Answer"
				door2_room2()
			else:
				print "incorrect try again"
	elif "2" in choice:
		print "Above Door #2 reads:"
		print "Enter at your own peril!"
		print "You walk through the door"
		door2_room3()
	else:
		end("You make no choice and hope for rescue. It never comes and you slip away from memory, never to be found.")

def door2_room2():
	print "You proceed through the door as you enter you are blinded by bright lights"
	print "A soft voice calls \" Is this heaven?\" You take a cautious step forward"
	print "The voice hardens \" Or is this hell?!\" The lights turn blood red and screams start to fill the room"
	print "You feel yourself slipping away and notice two doors"
	print "You have no time to think so you jump through a door."
	print "Is it Door A or Door B?"
	
	choice = raw_input("-> ").lower() # adding lower() converts the string into lowercase characters
	
	if "a" in choice:
		print "You step blindly through Door A"
		end("The door slams behind you and you feel all the air fleeing your body. You slip into unconsciousness, never to return.")
	elif "b" in choice:
		print "You jump through Door B"
		door2_room4()
	else:
		end("Wrong Answer. The room collapses you on and you are now trapped in limbo... forever.")

def door2_room3():
	print "You step into the room and a repugnant stench fills your lungs causing you to gag"
	print "In the corner you spot a fallen knight with a sign slung over his lifeless body"
	print "The sign reads \" Don't let the same fate befall you as it has me!\""
	print "You realise that the floor is a maze of pressure pads"
	print "There are 3 pads you can start on: A, B and C"
	print "Which one do you choose?"
	
	while True:
	
		choice = raw_input("-> ").lower()
	
		if "a" in choice:
			print "You step onto pad A, and the pad sinks under your weight"
			print "The room is silent, all you can hear is the sound of your baited breathe"
			print "A minute goes by and all seems fine, you breathe a sigh of relief"
			print "You notice a feint sound, almost like a whistle, you turn around"
			print "WHAM! A sharpened log impales you against the wall"
			end("Your adventure comes to an end as the life drains out of you.")
		elif "b" in choice:
			print "You step onto pad B, and you feel some resistance to the pad"
			print "A light shines on the pads in front of you, there are two choices"
			print "Do you pick the left pad or the right pad?"
			
			choice = raw_input ("-> ").lower()
			
			if "left" in choice:
				end("You step to the left and the pad crumbles beneath our feet, and you plumment to your untimely demise.")
			elif "right" in choice:
				print "You step to the right, and the next pads are illuminated, you made the right choice"
				print "There are now 3 pads in front of you and the door to the next room"
				print "Which pad do you choose 1, 2 or 3?"
				
				choice = raw_input("-> ").lower()
				
				if "1" in choice:
					end("You step onto pad number 1. The floor starts to rise, you run for the door to find it is locked.\nYou realise your fate is sealed. Crush!")
				elif "2" in choice:
					end("You step onto pad number 2. A mist starts to appear in the room, you start to breathe it in and begin coughing uncontrolably.\n YOu realise it's poison, your vision begins to blur and then everything turns black.")
				elif "3" in choice:
					print "The pad sinks and the door flies open, you run towards it and enter the next room."
					door2_room6()
				else:
					end("You can't follow simple instructions and roam aimlessly around the room until the darkness swallows you.")
			else:
				end("You can't follow simple instructions and roam aimlessly around the room until the darkness swallows you.")
		elif "c" in choice:
			end("You step onto C and the floor in front of you opens up. Two Komodo Dragons emerge and attack you. You die slowly as their poison takes effect and they wait for you to pass before eating you.")
		else:
			end("You can't follow simple instructions and roam aimlessly around the room until the darkness swallows you.")
		
def door2_room4():
	print "On the otherside of the door are three objects on pedestals. A circle, a square and a triangle."
	print "Behind them are two doors but a shutter blocks you off."
	print "A sign reads \"To open the shutter, you must solve the puzzle\""
	print "If the circle weighs 200g, and the weight of the square is equal to 4 times of the triangle and the triangle has a weight of the circle squared."
	print "What is the weight of the square?"
	
	choice = raw_input("-> ").lower()
	
	if choice == "160000":
		print "The shutter begins to open and you are presented with the option of two doors."
		print "Do you take the left door or the door on the right?"
		
		choice = raw_input("-> ").lower()
		
		if "left" in choice:
			print "You step through the door on the left"
			door2_room5()
		elif "right" in choice:
			print "You step through the door on the right"
			door2_room3()
		else:
			end("This is not the time to be dilly dallying you fool! A swarm of rats run into the room and devour you alive.")
	else:
		end("I'm afraid that was the wrong answer. And thus you are trapped forever, mwahaha!")
		
def door2_room5():
	print "There is a lion in the room, prowling looking for his next meal. Will you be it?"
	print "To your left is a sword, to your right is a hunk of gazelle"
	print "Which one do you pick?"
	
	choice = raw_input("-> ").lower()
	
	if "sword" in choice:
		print "You pick up the sword and the lion snarls at you"
		print "The lion darts from side to side, inching ever closer to you"
		print "You raise the sword and swing..."
		print "You miss!"
		end("The lion pounces on you and finds his next meal.")
	elif "gazelle" in choice:
		print "You grab the hunk of gazelle and the lion stares longingly at it"
		print "The lion bares his teeth and licks his lips"
		print "You throw the gazelle across the otherside of the room and the lion darts for it"
		print "Whilst the lion is distracted you make your away across the room and go through the door"
		door2_room6()
	else:
		end("The lion gets bored waiting for you to make a decision and pounces you, tearing chunks of flesh away from your body.")
	
def door2_room6():
	print "Inside the room is a safe and a door."
	print "You try the door but it's locked, the key must be in the safe."
	print "Taped to the safe is a letter, you open it."
	print "Inside the letter reads, \" Find the combination to the safe by answering these riddles three. \""
	print "The first riddle reads: \"How many degrees(in whole numbers, if any) are there between the hands of a clock when the time half past three?\"" # answer is 75 degrees
	print "The second riddle reads: \"A merchant can place 8 large boxes or 10 small boxes into a carton for shipping. \nIn one shipment, he sent a total of 96 boxes. If there are more large boxes than small boxes, how many cartons did he ship? \"" #answer is 11 cartons
	print "The third and final reads: \" As I was going to St. Ives,\nI met a man with seven wives,\nEach wife had seven sacks,\nEach sack had seven cats,\nEach cat had seven kits:\nKits, cats, sacks, and wives,\nHow many were there going to St. Ives?\"" # answer is 1
	print "Now enter your answers yo see if the combination of the safe opens."
	safe_cnt = 0
	
	while safe_cnt < 3:
		choice = raw_input("-> ")
		if choice == "75111":
			print "The safe clicks open and inside is a key. You take the key, open the door and step through"
			final_door()
		else:
			print"The safe remians locked, your combination is incorrect. Try again."
			safe_cnt = safe_cnt + 1
	else:
		end("After your third failed attempt the safe crumbles into dust along with the contents. You are trapped in the room forever.")
	
def door3_room1():
	print "You enter the room. Opposite you is knight with a stern expression on his face"
	print "He yells \"If you want to enter the next room, you must best me in a game of rock, paper, scissors\" He shows you his hand"
	print "What do hand do you play? rock, scissors or paper?"
	
	while True:
		knights_choices = ["rock", "paper", "scissors"]
		knights_hand = random.choice(knights_choices)
		choice = raw_input("-> ").lower()
		
		print "input: " , choice, "knights hand: ", knights_hand 
		if choice == knights_hand:
			print "You both show",choice,"Prepare to battle again"
		else:
			if choice == "rock" and knights_hand == "scissors":
				print "You are victorious! Proceed to the next room"
				door2_room3()
			elif choice == "rock" and knights_hand == "paper":
				print "You have been defeated! Try again!"
			elif choice == "paper" and knights_hand == "scissors":
				print "You have been defeated! Try again!"
			elif choice == "paper" and knights_hand == "rock":
				print "You are victorious! Proceed to the next room"
				door2_room3()
			elif choice == "scissors" and knights_hand == "paper":
				print "You are victorious! Proceed to the next room"
				door2_room3()
			elif choice == "scissors" and knights_hand == "rock":
				print "You have been defeated! Try again!"
			
def final_door():
	print "You have made it to the final room!"
	print "Congratulations! The game has been completed. Feel free to play again"
	exit(0)
			
def start():
	print "You wake up in a dark room, there are three doors"
	print "Which door do you take door #1, door #2 or door #3?"
	
	choice = raw_input("-> ")
	
	if choice == "1":
		end("You walk blindly through the door and fall into oblivion. Unlucky")
	elif choice == "2":
		door2_room1()
	elif choice == "3":
		door3_room1()
	else:
		print "That's not a valid choice, please enter a door number!"
		start()
		
def end(why):
	print why, "GAME OVER!"
	exit(0)

start()