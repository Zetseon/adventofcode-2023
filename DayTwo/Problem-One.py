import re

def gameValid(game_number, r, g, b) -> bool:
	maxRed = 12
	maxGreen = 13
	maxBlue = 14
	if r <= maxRed and g <= maxGreen and b <= maxBlue:
		return True
	return False


def stripValues(text:str):
	game = text.split(':')
	game_number = int(game[0].strip('game'))
	game_pull = re.findall(r"\d+ green|\d+ red|\d+ blue", game[1].strip(""))
	r, g, b = 0,0,0
	for x in game_pull:
		if re.findall(r'\d+ green',x):
			g = max(g, int(x.strip('green')))
		elif re.findall(r'\d+ red',x):
			r = max(r, int(x.strip('red')))
		elif re.findall(r'\d+ blue',x):
			b = max(b, int(x.strip('blue')))
		else:
			continue
	return game_number, r,g, b

def main():
	data = open("input.txt", "r")
	gameScore = 0
	for line in data:
		game_number,r,g,b = stripValues(line.lower())
		if gameValid(game_number, r, g, b):
			print(game_number)
			gameScore += game_number
	print(gameScore)

if __name__ == "__main__":
    main()
