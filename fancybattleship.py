from random import randint

""" Shit to add:
multiple ships = hardcoded as 2, want to make this dynamic (but never exceeding board size)
bigger ships
error handling on setup steps
"""

# This sets the number of turns in the game. 
game_length = int(raw_input("How many turns do you want to play?"))

# This sets the size of the board. 
# It gets funky if it's over 10. 
board_size = int(raw_input("How many rows/columns do you want?"))

# Number of ships
global ship_count
ship_count = 2

board = []

for x in range(board_size):
    board.append(["O"] * board_size)

def print_board(board):
    print "============================="
    print '__' + '_'.join(str(x) for x in xrange(1,board_size + 1))
    row_number = 1
    for row in board:
        print str(row_number) + "|" + " ".join(row)
        row_number += 1
    print "============================="

print "Let's play Battleship!"
print "You have %s turns to find me. Bet you can't, sucker!" % game_length
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
    
def ship_sunk(row, column):
	print "Congratulations! You sunk my battleship!"
	board[row][column] = "*"
	print_board(board)
	global ship_count
	ship_count = ship_count - 1
	if ship_count == 0:
		print "You got both of them! Goddamit!"
		exit()

ship1_row = random_row(board)
ship1_col = random_col(board)
ship2_row = random_row(board)
ship2_col = random_col(board)

# Turn these on for debugging, they'll print out the ship positions.
print "Ship 1: " + str(ship1_row + 1) + str(ship1_col + 1)
print "Ship 2: " + str(ship2_row + 1) + str(ship2_col + 1)

for turn in range(game_length):
	print "Turn", turn + 1, "of", str(game_length)
	try:
		guess_row = int(raw_input("Guess Row:")) - 1
		guess_col = int(raw_input("Guess Col:")) - 1
	
	except ValueError:
		print "Hey, that's not a row OR column. Stop breaking my stuff! Now you lose a turn!"
		print_board(board)
		continue

	if guess_row == ship1_row and guess_col == ship1_col or \
		guess_row == ship2_row and guess_col == ship2_col:
		ship_sunk(row = guess_row, column = guess_col)

	else:
   		if (guess_row < 0 or guess_row > board_size - 1) or \
   			(guess_col < 0 or guess_col > board_size -1):
			print "You have left the combat area. Lose a turn."
			print_board(board)
		elif(board[guess_row][guess_col] == "X"):
			print "You guessed that one already. Can't you read the board?"
			print_board(board)
   		else:
			print "Swing and a miss!"
			board[guess_row][guess_col] = "X"
			print_board(board)
if turn == game_length - 1:
	print "Ha ha ha! I got away! Now I'm going to spend all my money on hookers and blackjack!"
	print "See, I was at %s, %s and %s, %s" % (ship1_row + 1, ship1_col + 1, \
	ship2_row, ship2_col)
	board[ship1_row][ship1_col] = "*"
	board[ship2_row][ship2_col] = "*"
	print_board(board)