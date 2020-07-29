import secrets #for the really good random generator
import sys #for exiting out

def convert_num_to_string(number): #converting the number 
	if number == 0: #looks like boulder
		return "r"
	elif number == 1: #looks like paper
		return "p"
	elif number == 2: #looks like inverted s
		return "s"

def match(player,pc): #true means that you get the point, false is pc
	if player == "r":
		if pc == "p":
			return False
		if pc == "s":
			return True
	if player == "p":
		if pc == "s":
			return False
		if pc == "r":
			return True
	if player == "s":
		if pc == "r":
			return False
		if pc == "p":
			return True

def convert_to_word(letter): #just for the fun of it
	if letter == 'r':
		return "Rock"
	elif letter == "p":
		return "Paper"
	elif letter == "s":
		return "Scissors"


def play_game():
	player_score=0
	pc_score=0
	rounds=input("Let's begin, shall we? How many rounds you want to play?\n")
	try: # check to see if someone input a string, roast them bc why not
		rounds=int(rounds) 
	except: 
		print("Invalid input. Wow, you start the game by losing :(\n")
		sys.exit(1) #can also use return
		#return

	rounds_to_win=int(rounds/2+1)
	player_choice="NU"#for null, just to initialize
	print("\nFirst to win ",rounds_to_win," rounds wins the game\n")
	while(True):
		pc_choice=convert_num_to_string(secrets.randbelow(101)%3) # generates 0 1 2 in a truly random fashion
		oplayer_choice=input("Input your move: ")
		player_choice=oplayer_choice.lower() #to make it not matter whether user puts in uppercase or lowercase
		if(player_choice == "q"):
			print("Game exited")
			break
		print("\nRock -- Paper -- Scissors -- Says -- Shoot\n")
		print("\nI played: ",convert_to_word(pc_choice),"\tYou played: ",convert_to_word(player_choice),"\n")
		if(pc_choice == player_choice):
			print("\t\tTie round\n")
		elif(pc_choice is not player_choice):
			match_score=match(player_choice,pc_choice)
			if(match_score is True):
				print("\tYou win this round")
				player_score+=1
			elif(match_score is False):
				print("\tI win this round")
				pc_score+=1

		print("MY SCORE: ",pc_score,"\tYOUR SCORE: ",player_score,"\n")
		if(player_score==rounds_to_win or pc_score==rounds_to_win):
			print("Game over")
			break
	if(pc_score>player_score):
		print("\n\aI win this game, sorry for being better than you :(\n")
	elif(player_score>pc_score):
		print("\n\aYou win this game, who do you think you are?")




print("\nTo play, simply choose: (R)ock \t(P)apper \t or (S)cissors\n")
print("Entering uppercase is optional\nPress q at anytime to exit\n")
print("Are you ready to play? (Y) (N) \t")
#choice="NU"


while(True):
	choice=input()
	fchoice=choice.lower()
	if(fchoice == "n" or fchoice =="q"):
		print("Quitting is for losers\n")
		break
	print("Get ready to lose\n")

	play_game()
	print("Do you want to play again?\t")
	choice=input()
	fchoice=choice.lower()
	if(fchoice == "n" or fchoice == "q"):
		print("Quitting is for losers\n")
		break
print("\t~~~\aGoodbye!~~~\n")


