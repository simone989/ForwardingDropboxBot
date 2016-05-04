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
	def __init__(self):
		self.errorMessage = "Comando non riconosciuto"
		self.sessionOpen = False
	def executeCommand(self,command,fromuser = None):
		command = self.parseCommand(command)
		
		if(self.sessionOpen):
			if(self.dropboxSession.waitingToken == True and command.split(" ")[0] == "/token"):
				self.dropboxSession.token = command.split(" ")[1]
				
				return self.dropboxSession.startAuth()
		else:
			if(command.startswith("/token")):
				return "Iniziare una sessione con /startsession prima di continuare."

		if(command == "/start"):
			print ("Debug metodo. Per evitare il loop")
			return "Started"
		elif (command == "/info"):
			return "Bot creato da @xVinz e @simone989"
		elif (command == "/startsession"):
			self.startSession(fromuser.username)
			self.dropboxSession.waitingToken = True
			return "Digita /token <token di autenticazione> per procedere."
			#self.startSession(fromuser.username)

		else:
			return self.errorMessage
	def parseCommand(self,command):
		if(command.startswith("/")):
			return command 
		else:
			return "/"+command.lower()

	def startSession(self,user):
		self.sessionOpen = True
		self.dropboxSession = NewSession()

	def DEBUGlog(self,fromuser,command):
		print("Utente: "+ fromuser +" ha digitato: "+command)

class NewSession(object):
	def __init__(self):
		self.isAuthenticated = False
		self.waitingToken = False
		self.token = None
		print ("DEBUG Inizializzazione classe NewSession")

	def startAuth(self):
		client = dropbox.client.DropboxClient(self.token)
		try:
			client.account_info()
			self.isAuthenticated = True
			self.waitingToken = False
			return "Autenticazione eseguita"
		except Exception as error:
			self.waitingToken = True
			return "Errore nell'inserimento del token"