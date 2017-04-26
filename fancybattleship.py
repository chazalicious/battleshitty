from random import randint

# This sets the number of turns in the game. 
game_length = int(raw_input("How many turns do you want to play?"))

# This sets the size of the board. 
# It gets funky if it's over 10. 
board_size = int(raw_input("How many rows/columns do you want?"))

board = []

for x in range(board_size):
    board.append(["O"] * board_size)

def print_board(board):
    print '__' + '_'.join(str(x) for x in xrange(1,board_size + 1))
    row_number = 1
    for row in board:
        print str(row_number) + "|" + " ".join(row)
        row_number += 1


print "Let's play Battleship!"
print "You have %s turns to find me. Bet you can't, sucker!" % game_length
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(game_length):
	print "Turn", turn + 1, "of", str(game_length)
	try:
		guess_row = int(raw_input("Guess Row:")) - 1
		guess_col = int(raw_input("Guess Col:")) - 1
	
	except ValueError:
		print "Hey, that's not a row OR column. Stop breaking my stuff! Now you lose a turn!"
		print_board(board)
		continue

	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations! You sunk my battleship!"
		break
	else:
   		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
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