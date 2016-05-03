# -*- coding: utf-8 -*-
import telegram
from classes.botresponse import *


TOKEN  = '179093943:AAFaUKS559e-SnAoja-4iUnXfA_M0CJZUiw'
#chat_id log
logs = 1 #disable/enable chatid logs (1 enabled, 0 disabled)

news = "News"
msgManager = Response()
bot = telegram.Bot(TOKEN)

#debugging
#bot.sendMessage(chat_id=26349488, text="BOT ON")
try:
    update_id = bot.getUpdates()[0].update_id
except IndexError:
    update_id = None

LAST_UPDATE_ID = update_id
last_text = ""
NOFOUND_MESSAGE="Comando non riconosciuto"
waitingToken = False
try:
	while True:
		messageText = ""
		for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=20):
			text = update.message.text
			chat_id = update.message.chat.id
			update_id = update.update_id
			print(update.message.from_user.username+" Ha scritto: "+text)
			messageText = msgManager.responseText(text)
			if(waitingToken == True):
				print ("WaitingTOKEN OPEN")
				dropboxToken = text.split(" ")	
				
				if(dropboxToken[0] == "/token"):
					print ("Dropbox token: "+dropboxToken[0])			
					sessionDropbox = NewSession(dropboxToken[1])
					if(sessionDropbox.startAuth() == True):
						messageText = "Sessione valida. Sei autenticato"
						waitingToken = False
			if(text == "/reload"):
				if(msgManager.reloadFile()):
					messageText = "Reload effettuato correttamente."
				else:
					messageText = "Errore nel reload"
			elif(text == "/startservice"):
				messageText = "Inserisci ora il token - /token <authentication token> (senza parentesi angolari)"
				waitingToken = True
			elif(messageText == False):
				messageText = NOFOUND_MESSAGE
			print ("Risposta: "+messageText)
			bot.sendMessage(chat_id=chat_id, text=messageText)
			LAST_UPDATE_ID = update_id + 1
			text = ""

except Exception as error:
	print (str(error))
	open("errors.txt", "a+").write(str(error)+"\n")

