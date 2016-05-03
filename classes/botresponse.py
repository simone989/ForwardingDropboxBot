#!/usr/bin/env python
import dropbox
class Response(object):
	def __init__(self):
		self.responseFile = open("commands.txt","r")
		self.textLines = []
		self.fromFileToList()

	def fromFileToList(self):  #Metodo che salve il contenuto del txt in una lista. Più semplice da gestire.
		with self.responseFile as fileLine:
			self.textLines = fileLine.read().splitlines()

		self.responseFile.close()
	def getList(self):  #Metodo temporaneo. Per la prova della stampa della lista
		for lines in self.textLines:
			print (lines)


	def responseText(self,command):
		for lines in self.textLines:
			lineSplitted = lines.split("=")
			if(self.isCommand(lineSplitted[0],command) == True): 
				return lineSplitted[1]
		return False


	def isCommand(self,textCommand, fileCommand):
		if(textCommand == fileCommand):
			return True
		elif("/"+textCommand == fileCommand):
			return True
		return False
	def reloadFile(self):
		try:
			self.textLines = []
			self.fromFileToList()
			return True
		except Exception as error:
			return False

class NewSession(object):
	def __init__(self,token):
		self.token = token

	def startAuth(self):
		client = dropbox.client.DropboxClient(token)
		return client.account_info()