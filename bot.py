# -*- coding: utf-8 -*-
import telegram
from classes.botresponse import Response


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
try:
	while True:
		messageText = ""
		for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=2):

			text = update.message.text
			chat_id = update.message.chat.id
			update_id = update.update_id
			messageText = msgManager.responseText(text)
			if(text == "/reload"):
				if(msgManager.reloadFile()):
					messageText = "Reload effettuato correttamente."
				else:
					messageText = "Errore nel reload"
			if(messageText == False):
				messageText = NOFOUND_MESSAGE
			else:
				bot.sendMessage(chat_id=chat_id, text=messageText)
			LAST_UPDATE_ID = update_id + 1
			text = ""

except Exception as error:
	print (str(error))
	open("errors.txt", "a+").write(str(error)+"\n")

