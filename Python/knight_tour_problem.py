def board_verify(board):
	flag = True

	for i in board:
		if None in i:
			flag = False

	return flag


def print_board(board):
	for i in board:
		print(*i, sep='\t')


def just_for_debug(current_pos, board):
	y_pos, x_pos = current_pos

	possible_positions = [
		(y_pos + 2, x_pos + 1),
		(y_pos + 2, x_pos - 1),
		(y_pos - 2, x_pos + 1),
		(y_pos - 2, x_pos - 1),
		(y_pos + 1, x_pos + 2),
		(y_pos - 1, x_pos + 2),
		(y_pos + 1, x_pos - 2),
		(y_pos - 1, x_pos - 2),
	]

	print(possible_positions)


def calculate_knight_move(current_pos, board):
	y_pos, x_pos = current_pos

	possible_positions = [
		(y_pos + 2, x_pos + 1),
		(y_pos + 1, x_pos + 2),
		(y_pos + 2, x_pos - 1),
		(y_pos - 2, x_pos + 1),
		(y_pos - 2, x_pos - 1),
		(y_pos - 1, x_pos + 2),
		(y_pos + 1, x_pos - 2),
		(y_pos - 1, x_pos - 2),
	]

	res = []

	for y_pos, x_pos in possible_positions:
		if 0 <= x_pos < 8 and 0 <= y_pos < 8 and board[y_pos][x_pos] is None:
			res.append((y_pos, x_pos))

	return res


def knight_tour_roblem(board, current_pos, count):

	global max_count

	print('=========================================================')
	if count > max_count:
		max_count = count

	print(f'{count}--------------------{max_count}')

	if n**2 == count:
		print_board(board)
		return True

	else:
		for i in calculate_knight_move(current_pos, board):
			y_pos, x_pos = i
			board[y_pos][x_pos] = count
			count += 1
			if knight_tour_roblem(board, i, count):
				return True
			count -= 1
			board[y_pos][x_pos] = None
		return False
		


if __name__ == '__main__':
	n = 8
	print(n**2)
	board = []

	max_count = 0

	[board.append([None]*8) for i in range(8)]
	board[0][0] = 0
	knight_tour_roblem(board, (0, 0), 1)

	print(board)
