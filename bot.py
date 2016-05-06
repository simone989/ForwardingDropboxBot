# -*- coding: utf-8 -*-
import telegram
from classes.Utilities import *
#from classes.DatabaseManager import *


TOKEN  = '179093943:AAFaUKS559e-SnAoja-4iUnXfA_M0CJZUiw'
#chat_id log
logs = 1 #disable/enable chatid logs (1 enabled, 0 disabled)

news = "News"
msgManager = CommandManager()
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
		messageText = "" #Inizializzazione necessaria per evitare conflitti con messaggi vuoti (eventuali).
		for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=20):
			text = update.message.text
			chat_id = update.message.chat.id
			update_id = update.update_id
			messageText = msgManager.executeCommand(text,update.message.from_user)

			msgManager.DEBUGlog(update.message.from_user.username,text)
			bot.sendMessage(chat_id=chat_id, text=messageText)
			LAST_UPDATE_ID = update_id + 1
			text = ""

except Exception as error:
	print (str(error))
	open("errors.txt", "a+").write(str(error)+"\n")
