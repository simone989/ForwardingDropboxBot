def textResponse(message):
	responseFile = open("bot.txt","r")
	responseFile.read()
	
	print (responseFile.read())


textResponse("ciao")