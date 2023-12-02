
numbers = []

number_strings = {
	'one' : '1',
	'two' : '2',
	'three' : '3',
	'four' : '4',
	'five' : '5',
	'six' : '6',
	'seven' : '7',
	'eight' : '8',
	'nine' : '9'
}

with open('input.txt', 'r') as file:
	for line in file:
		substring_1 = ''	
		substring_2 = ''
		left_number = ''	
		right_number = ''

		for letter in line:
			if left_number:
				break
			substring_1 = substring_1 + letter

			for word, number in number_strings.items():
				if word in substring_1:
					left_number = number
					break
			
			if letter.isdigit():
				left_number = letter
		for letter in line[::-1]:
			if right_number:
				break
			substring_2 = substring_2 + letter

			for word, number in number_strings.items():
				if word in substring_2[::-1]:
					right_number = number
					break
			
			if letter.isdigit():
				right_number = letter

		numbers.append(int(left_number + right_number))

print(sum(x for x in numbers))

