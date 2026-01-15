theboard={'TOP-L':' ', 'TOP-M':' ','TOP-R':' ', 'MID-L':' ', 'MID-M':' ','MID-R':' ', 'LOW-L':' ', 'LOW-M':' ','LOW-R':' ',}
def printboard(board):
	print(board['TOP-L'] + '|' + board['TOP-M'] + '|'+ board['TOP-R'])
	print('-----')
	print(board['MID-L'] + '|' + board['MID-M'] + '|'+ board['MID-R'])
	print('-----')
	print(board['LOW-L'] + '|' + board['LOW-M'] + '|'+ board['LOW-R'])
	print('-----')
turn='X'
for i in range(9):
	while True:
		printboard(theboard)
		print('Turn for '+turn+' move on which space? ;(or type <close> to exit)')
		move=input()
		if move=='close':
			print('The Game is over')
			break
		if move in theboard :
			if theboard[move]==' ':
				break
			else:
				print('select an empty box')
		else:
			print('write in capital letters like: TOP-M ; MID-L.....')
	theboard[move]=turn
	if turn=='X':
		turn='O'
	else:
		turn='X'
printboard(theboard)
	
		
