def main():
	width = 8
	height = 8
	board = [[0 for i in range(0, width)] for j in range(0, height)]
	gameOver = False
	numPlayers = 2
	playerId = 1

	while not gameOver:
		DrawBoard(board, width, height)
		colNum = Prompt()
		insert(board, colNum, height, playerId)
		playerId = playerId % numPlayers + 1

def Prompt():
	print "It is player 2's turn"
	colNum = input("Insert into which column?")
	return colNum

def DrawBoard(board, width, height):
	for i in range(0, width):
			print str(width - i) + " " + " ".join(map(str, board[i]))
	print " ".join(map(str, range(0, width)))

def checkBoard():
	return 0

main()