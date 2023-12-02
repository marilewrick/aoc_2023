
numbers = []
with open('input.txt', 'r') as file:

	for line in file:
		# find left number:
		forward = line
		backward = line[::-1]

		for letter in forward:
			if letter.isdigit():
				left_number = letter
				break
		for letter2 in reversed(line):
			if letter2.isdigit():
				right_number = letter2
				break

		numbers.append(int(left_number + right_number))

print(sum(x for x in numbers))

