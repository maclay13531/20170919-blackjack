import random
import os

print "\n"

print "---- Welcome! Let's play! ----"

print "\n"

print "What is your name?"

player_name = str(raw_input("Insert your name."))

print "\n"

print "%s, how many deck(s) do you want to play with?" % player_name

deck_num = int(raw_input("A deck has 52 cards and you can choose a deck number between 1 to 8!"))

print "Do you want to read the game rules?"

rule = raw_input("Type Y to read the rules")

print "\n"

if(rule == "Y" or rule == "y"):
	print "\($ $)/   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     \($ $)/"
	print "\n"
	print "1)	Blackjack may be played with one to eight decks of 52-card decks."
	print "\n"
	print "2)	Aces may be counted as 1 or 11 points. EX: Heart of Ace = 1 point or 11 points."
	print "\n"
	print "3)	2 to 9 are according to pip value. EX: Spade of 6 = 6 points."
	print "\n"
	print "4)	Tens and face cards count as ten points EX: Diamond of King = 10 points."
	print "\n"
	print "5)	The value of a hand is the sum of the point values of the individual cards."
	print "\n"
	print "6)	The winning condition is to have a higher hand value than the dealer without the hand value going over 21 points."
	print "\n"
	print "7)	The dealer will give two initial cards to you and two initial cards to himself."
	print "\n"
	print "8)	The first card of two initial cards is facing up visible for everyone."
	print "\n"
	print "9)	The second card of two initial cards is facing down only visible for the hand owner."
	print "\n"
	print "10)	The game begins and the player has the following choices available"
	print "		--- Stand: Player stands pat with his or her cards."
	print "		--- Hit: Player draws another card(and more if he or she wishes)."
	print "\n"
	print "NOTE: 'BLACKJACK' is the best hand, consisting of an ace and any 10-point card."
	print "NOTE: 'BLACKJACK' outranks all other 21-point hands" 
	print "\n"
	print "\($ $)/   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     \($ $)/"
print "\n"

print "Great! We are ready!"

print "\n"

print "The dealer is ready and we can start the game as soon as you are ready to make your next move!"

print "\n"

Main_deck = []

a_deck = []

for i in range(0,4):
	for j in range(1,14):
		card = j
		a_deck.append(card)

Main_deck = a_deck * deck_num

for i in range(0, len(Main_deck)):
	if(i % 13 == 0 or i == 0):
		Main_deck[i] = 11
	for i in xrange(9, len(Main_deck), 13):
		Main_deck[i] = 10
	for i in xrange(10, len(Main_deck), 13):
		Main_deck[i] = 10
	for i in xrange(11, len(Main_deck), 13):
		Main_deck[i] = 10
	for i in xrange(12, len(Main_deck), 13):
		Main_deck[i] = 10

main_game_on = True

while main_game_on == True:
	for i in range(0, 10):
		raw_input("Press ENTER to start the game!")
		print "\n"
		print "---- PLAYER INFORMATION ----"
		random_num_one = random.randint(0, (len(Main_deck) - 1))
		player_first_initial_card = Main_deck[random_num_one]
		print "%s's first card value is: %d" % (player_name, player_first_initial_card)
		random_num_two = random.randint(0, (len(Main_deck) - 1))
		player_second_initial_card = Main_deck[random_num_two]
		print "%s's second card value is: %d." % (player_name, player_second_initial_card)
		print "\n"
		total_player_value = player_first_initial_card + player_second_initial_card
		print ">>><<<-------- Your total hand value is %d. -------->>><<<" % total_player_value
		print "\n"
		print "---- DEALER INFORMATION ----"
		random_num_three = random.randint(0, (len(Main_deck) - 1))
		dealer_first_initial_card = Main_deck[random_num_three]
		print "Dealer's first card value is: %d" % dealer_first_initial_card
		random_num_four = random.randint(0, (len(Main_deck) - 1))
		dealer_second_initial_card = Main_deck[random_num_four]
		print "Dealer's second card value is: %d." % dealer_second_initial_card
		print "\n"
		total_dealer_value = dealer_first_initial_card + dealer_second_initial_card
		print ">>><<<-------- Dealer's total hand value is %d. -------->>><<<" % total_dealer_value
		print "\n"
		print "---- PLAYER   ----"
		print "----   IN     ----"
		print "---- PROGRESS ----"
		print "Choose your option!"
		print "Option 1: Stand. Press 1"
		print "Option 2: Hit.   Press 2"
		print "\n"
		game_on = True
		while game_on == True:
			if(player_first_initial_card == 11):
				ace_value = int(raw_input("Do you want the ACE value to be 1 or 11? Type 1 or 11."))
				if(ace_value == 1):
					player_first_initial_card = 1
					print "The first card value is %d!" % ace_value
					total_player_value -= 10
					print ">>><<<-------->>><<< %s's new total hand value is %d! >>><<<-------->>><<<" % (player_name, total_player_value)
				elif(ace_value == 11):
					player_first_initial_card = 11
					print "The first card value is %d!" % ace_value
			if(player_second_initial_card == 11):
				second_ace_value = int(raw_input("Do you want the ACE value to be 1 or 11? Type 1 or 11."))
				if(second_ace_value == 1):
					player_second_initial_card = 1
					print "The first card value is %d!" % second_ace_value
					total_player_value -= 10
					print ">>><<<-------->>><<< %s's new total hand value is %d! >>><<<-------->>><<<" % (player_name, total_player_value)
				elif(second_ace_value == 11):
					player_second_initial_card = 11
					print "The second card value is %d!" % second_ace_value
			user_option = raw_input("Choose to STAND or to HIT. Press 1 to STAND or Press 2 to HIT.")
			if(user_option == "2" and game_on == True):
				print "\n"
				print "%s chose to hit!" % player_name
				hit_me_card = random.randint(0, (len(Main_deck) - 1))
				hit_me_value = Main_deck[hit_me_card]
				if(hit_me_value == 11):
					third_ace_value = int(raw_input("Do you want the ACE value to be 1 or 11? Type 1 or 11."))
					if(third_ace_value == 1):
						hit_me_value = 1
						print "The ACE card value is %d!" % hit_me_value
					elif(ace_value == 11):
						hit_me_value = 11
						print "The ACE card value is %d!" % hit_me_value
				total_player_value += hit_me_value
				print "%s received a card with a value of %d!" % (player_name, hit_me_value)
				print ">>><<<-------->>><<< %s's new total hand value is %d! >>><<<-------->>><<<" % (player_name, total_player_value)
				while total_player_value < 21:
					user_option_repeat = raw_input("Do you want to hit again? Press 1 to STAND or Press 2 to HIT.")
					if(user_option_repeat == "2"):
						print "\n"
						print "%s chose to hit again!" % player_name
						print "\n"
						hit_me_card_repeat = random.randint(0, (len(Main_deck) - 1))
						hit_me_value_repeat = Main_deck[hit_me_card_repeat]
						if(hit_me_value_repeat == 11):
							fourth_ace_value = int(raw_input("Do you want the ACE value to be 1 or 11? Type 1 or 11."))
							if(fourth_ace_value == 1):
								hit_me_value = 1
								print "The ACE card value is %d!" % hit_me_value
							elif(fourth_ace_value == 11):
								hit_me_value = 11
								print "The ACE card value is %d!" % hit_me_value
						total_player_value += hit_me_value_repeat
						print "%s received a card with a value of %d!" % (player_name, hit_me_value_repeat)
						print ">>><<<-------->>><<< %s's new total hand value is %d! >>><<<-------->>><<<" % (player_name, total_player_value)
					elif(user_option_repeat == "1"):
						break
				print ">>><<<-------->>><<< %s's new total hand value is %d! >>><<<-------->>><<<" % (player_name, total_player_value)
				if(total_player_value == 21 and total_dealer_value < 21):
					print "\n"
					print "You win!!"
					print " <<<   WON   >>>"
					game_on = False
				elif(total_player_value > 21):
					print "\n"
					print "Total hand value higher than 21. Sorry you LOST..."
					print " <<<   LOST   >>>"
					game_on = False
					break
				if(total_player_value > total_dealer_value):
					difference = total_player_value - total_dealer_value
					print "\n"
					print "Your hand value is %s greater than the dealer's hand value!! You win!!!" % difference
					print " <<<   WON   >>>"
					game_on = False
					break
				elif(total_player_value < total_dealer_value):
					print "\n"
					print "Hand value lower than the dealer's hand value. Sorry you LOST..."
					print " <<<   LOST   >>>"
					game_on = False
					break
				elif(total_player_value == total_dealer_value):
					print "\n"
					print "Equal hand values! No winner on this round."
					print " <<<   TIE   >>>"
					break
			elif(user_option == "1" and game_on == True):
				print "\n"
				print "%s chose to stand." % player_name
				print ">>><<<-------->>><<< Total hand value is still %d. >>><<<-------->>><<<" % total_player_value
				if(total_player_value == 21 and total_dealer_value < 21):
					print "You win!!"
					print " <<<   WON   >>>"
					game_on = False
					break
				elif(total_player_value > 21):
					print "\n"
					print "Total hand value higher than 21. Sorry you LOST..."
					print " <<<   LOST   >>>"
					game_on = False
					break
				if(total_player_value > total_dealer_value):
					difference = total_player_value - total_dealer_value
					print "\n"
					print "Your hand value is %s greater than the dealer's hand value!! You win!!!" % difference
					print " <<<   WON   >>>"
					game_on = False
					break
				elif(total_player_value < total_dealer_value):
					print "\n"
					print "Hand value lower than the dealer's hand value. Sorry you LOST..."
					print " <<<   LOST   >>>"
					game_on = False
					break
				elif(total_player_value == total_dealer_value):
					print "\n"
					print "Equal hand values! No winner on this round."
					print " <<<   TIE   >>>"
					game_on = False
					break
		play_again = str(raw_input("Play again? Press any KEY to continue! Insert NO to quit."))
		if(play_again == "YES" or play_again == "yes"):
			pass
		elif(play_again == "NO" or play_again == "no"):
			print "Hope to see you again soon!"
			main_game_on = False
			game_on = False
			break
		else:
			pass
		os.system('clear')
		print "\n"				
		print "\($ $)/   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   \($ $)/"
		print "\n"
		print "			  $$$~~~   NEW ROUND   ~~~$$$					"





