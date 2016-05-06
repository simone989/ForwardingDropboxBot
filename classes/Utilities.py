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
			if(command == "/listFiles"):
				return self.dropboxSession.listOfFile()
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
		command = command.split(" ")
		if(len(command) > 1):
			command = str(command[0]).lower()+" "+str(command[1])
		else:
			command = str(command[0]).lower()

		print (str(command))
		if(command.startswith("/")):
			return str(command) 
		else:
			return "/"+str(command)

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
		self.client = dropbox.client.DropboxClient(self.token)
		self.checkAuthentication()
		if(self.isAuthenticated):
			self.waitingToken = False
			return "Autenticazione eseguita correttamente."
		else:
			self.waitingToken = True
			return "Errore nell'inserimento del token."

	def checkAuthentication(self):
		try:
			self.client.account_info()
			self.isAuthenticated = True

		except Exception as error:
			self.isAuthenticated = False

	def listOfFile(self):#Da continuare
		folderMetadata = self.client.metadata('/')
		return folderMetadata