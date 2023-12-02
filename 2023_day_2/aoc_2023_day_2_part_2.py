import re

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

result = 0

with open('input.txt', 'r') as file:
	game_dict = {}
	for index, line in enumerate(file):

		game_number = re.match(r'Game (\d+):', line).group(1)
		game_dict[game_number] = {}	

		games = re.split(r':', line)[1].replace(' ','').split(';')
		for idx, game in enumerate(games):
			game_data = {}
			single_game = game.split(',')
			for cubes in single_game:
				split_numbers = re.match(r'(\d+)(\D+)', cubes)
				game_data[split_numbers.group(2).replace('\n', '')] = split_numbers.group(1)
			game_dict[game_number][idx] = game_data



powers = []
for key, game in game_dict.items():
	max_red = 0
	max_green = 0
	max_blue = 0
	for idx, rnd in game.items():

		if 'red' in rnd and int(rnd['red']) > max_red:
			max_red = int(rnd['red'])
		if 'green' in rnd and int(rnd['green']) > max_green:
			max_green = int(rnd['green'])
		if 'blue' in rnd and int(rnd['blue']) > max_blue:
			max_blue = int(rnd['blue'])

	powers.append(max_red * max_green * max_blue)


print(sum(powers))	