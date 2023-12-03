import re


def check_for_symbol(idx_row, idx_col):
	# above
	if idx_row > 0:
		element = puzzle[idx_row-1][idx_col]
		if not element.isdigit() and element != '.':
			print('above')
			print(element)
			return True
	
	# under:
	if idx_row < len(puzzle) - 1:
		element = puzzle[idx_row+1][idx_col]
		if not element.isdigit() and element != '.':
			print('under')
			print(element)
			return True

	# left
	if idx_col > 0:
		element = puzzle[idx_row][idx_col-1]
		if not element.isdigit() and element != '.':
			print('left')
			print(element)
			return True

	# right
	if idx_col < len(puzzle[0])-1:
		element = puzzle[idx_row][idx_col+1]
		if not element.isdigit() and element != '.':
			print('right')
			print(element)
			return True

	# diagonal upper left
	if idx_row > 0 and idx_col > 0:
		element = puzzle[idx_row-1][idx_col-1]
		if not element.isdigit() and element != '.':
			print('upper left')
			print(element)
			return True

	# diagonal upper right
	if idx_row > 0 and idx_col < len(puzzle[0])-1:
		element = puzzle[idx_row-1][idx_col+1]
		if not element.isdigit() and element != '.':
			print('upper right')
			print(element)
			return True

	# diagonal under left
	if idx_row < len(puzzle) - 1 and idx_col > 0:
		element = puzzle[idx_row+1][idx_col-1]
		if not element.isdigit() and element != '.':
			print('under left')
			print(element)
			return True

	# diagonal under right
	if idx_row < len(puzzle) - 1 and idx_col < len(puzzle[0]) - 1:
		element = puzzle[idx_row+1][idx_col+1]
		if not element.isdigit() and element != '.':
			print('under right')
			print(element)
			return True
	
	return False




with open('./input.txt', 'r') as file:
	puzzle = []
	result = 0

	regex = re.compile(r'\d+')

	for idx_line, line in enumerate(file):
		line = line.replace('\n', '')
		puzzle.append(line)

	for idx, line in enumerate(puzzle):
		matches = regex.finditer(line)

		for match in matches:
			number = match.group()
			print(number)
			start_index = match.start()
			end_index = match.end()

			for i in range(start_index, end_index):
				print(i)
				print(idx)
				if check_for_symbol(idx, i):
					result = result + int(number)
					break



print(result)
