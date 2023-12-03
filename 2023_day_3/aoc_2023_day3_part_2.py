import re


def get_star_index(idx_row, idx_col):
	# above
	if idx_row > 0:
		element = puzzle[idx_row-1][idx_col]
		if element == '*':
			return [idx_row-1, idx_col]
	
	# under:
	if idx_row < len(puzzle) - 1:
		element = puzzle[idx_row+1][idx_col]
		if element == '*':
			return[idx_row+1, idx_col]

	# left
	if idx_col > 0:
		element = puzzle[idx_row][idx_col-1]
		if element == '*':
			return [idx_row, idx_col-1]

	# right
	if idx_col < len(puzzle[0])-1:
		element = puzzle[idx_row][idx_col+1]
		if element == '*':
			return [idx_row, idx_col+1]

	# diagonal upper left
	if idx_row > 0 and idx_col > 0:
		element = puzzle[idx_row-1][idx_col-1]
		if element == '*':
			return [idx_row-1, idx_col-1]

	# diagonal upper right
	if idx_row > 0 and idx_col < len(puzzle[0])-1:
		element = puzzle[idx_row-1][idx_col+1]
		if element == '*':
			return [idx_row-1, idx_col+1]

	# diagonal under left
	if idx_row < len(puzzle) - 1 and idx_col > 0:
		element = puzzle[idx_row+1][idx_col-1]
		if element == '*':
			return [idx_row+1, idx_col-1]

	# diagonal under right
	if idx_row < len(puzzle) - 1 and idx_col < len(puzzle[0]) - 1:
		element = puzzle[idx_row+1][idx_col+1]
		if element == '*':
			return [idx_row+1, idx_col+1]
	
	return []


with open('./input.txt', 'r') as file:
	puzzle = []
	result = 0
	
	number_star_positions = []
	regex = re.compile(r'\d+')

	for idx_line, line in enumerate(file):
		line = line.replace('\n', '')
		puzzle.append(line)


for idx, line in enumerate(puzzle):
	matches = regex.finditer(line)

	for match in matches:
		number = match.group()
		start_index = match.start()
		end_index = match.end()

		for i in range(start_index, end_index):
			star_index = get_star_index(idx, i)
			if len(star_index) > 0:
				number_star_positions.append(
					{
						'number': int(number),
						'star_row': star_index[0],
						'star_col': star_index[1]
					}
				)	
				break

print(number_star_positions)
for idx, data in enumerate(number_star_positions):
	res = [d for d in number_star_positions[idx+1:] if d.get('star_row') == data['star_row'] and d.get('star_col') == data['star_col']]
	print(res)
	if len(res) > 0 and len(res) <2:
		for element in res:
			gear = data['number'] * res[0]['number']
		result = result + gear

print(result)
