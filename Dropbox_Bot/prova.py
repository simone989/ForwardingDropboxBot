def readFile(message):
	responseFile = open("bot.txt","r")
	with responseFile as f:
		lines = f.read().splitlines()
	return lines

readFile("prova")