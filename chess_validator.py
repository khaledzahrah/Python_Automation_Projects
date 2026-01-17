def chessGame(board):
	counts = {'w':0,'b':0}
	pawn_counts = {'w':0,'b':0}
	king_counts = {'w':0,'b':0}
	valid_spaces = []
	for width in range(1,9):
		for length in 'abcdefgh':
			valid_spaces.append(str(width)+length)
	for space, piece in board.items():
		if space not in valid_spaces:
			return False
		color=piece[0]
		name=piece[1:]
		if color not in ['w','b'] or name not in ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']:
			return False
		counts[color]+=1
		if name=='pawn': pawn_counts[color]+=1
		if name=='king': king_counts[color]+=1
	if king_counts['w'] != 1 or king_counts['b'] != 1: return False 
	if counts['w'] > 16 or counts['b'] > 16: return False          
	if pawn_counts['w'] > 8 or pawn_counts['b'] > 8: return False
	return True
------------------------------------------
Examples of experimentation:
board_ok = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

   
board_error = {'1a': 'wking', '1b': 'wking', '9z': 'bpawn'}
		
	