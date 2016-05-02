#!/usr/bin/env python

class Response(object):
	def __init__(self):
		self.responseFile = open("commands.txt","r")
		self.textLines = []
		self.fromFileToList()

	def fromFileToList(self):  #Metodo che salve il contenuto del txt in una lista. Più semplice da gestire.
		print ("Joined")
		responseFile = open("bot.txt","r")
		print (responseFile)
		with responseFile as fileLine:
			self.textLines = fileLine.read().splitlines()
		
		responseFile.close()
	def getList(self):  #Metodo temporaneo. Per la prova della stampa della lista
		for lines in self.textLines:
			print (lines)

	def responseText(self,message):
		for lines in self.textLines:
			if(lines.split("=")[0] == message):
				return lines.split("=")[1]
		return "Comando non riconosciuto"