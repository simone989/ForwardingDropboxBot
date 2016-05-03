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
			if(self.isCommand(command,lineSplitted[0]) == True): 
				return lineSplitted[1]
		return False


	def isCommand(self,textCommand, fileCommand):
		#if(textCommand == fileCommand):
			#return True
		#elif
		print ("Comando del file: /"+fileCommand)
		if(textCommand == "/"+fileCommand):
			return True
		return False

	def reloadFile(self):
		try:
			self.responseFile = open("commands.txt","r")
			self.textLines = []
			self.fromFileToList()
			return True
		except Exception as error:
			print (error) #debug
			return False

class CommandManager(object):
	def executeCommand(self,command):
		command = self.parseCommand(command)m
		if(command == "/start"):
			print ("Debug metodo. Per evitare il loop")
			return ""
		elif (command == "/info"):
			return "Bot creato da @xVinz e @simone989"

	def parseCommand(self,command):
		if(command.startswith("/")):
			return command 
		elif
			return "/"+command.lower()
	

class NewSession(object):
	def __init__(self,token):
		self.token = token
		self.isAuthenticated = False
		print ("DEBUG Inizializzazione classe NewSession")
		print ("SELF TOKEN: "+str(self.token))

	def startAuth(self):
		client = dropbox.client.DropboxClient(self.token)
		try:
			client.account_info()
			self.isAuthenticated = True
			return True
		except Exception as error:
			print (error)
			return False