from telegram.ext import Updater, MessageHandler, Filters
import sys
sys.path.append("..")
import cl.test as cl
# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start


def tr(update, context):
    msg = update.message.text
    msg_resp = cl.pasarText(msg)
    context.bot.send_message(chat_id=update.message.chat_id, text=msg_resp)
    img = list(msg_resp.split("\n"))
    for s in img:
        if(s.split(" ")[0] == "Created_image:"):
            context.bot.send_photo(chat_id=update.message.chat_id, photo=open(s.split(" ")[1], 'rb'))


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello World!")


# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()
# crea objecte per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
# indica que quan el bot rebi la comanda /start s'executi la funció start
updater.dispatcher.add_handler(MessageHandler(Filters.text, tr))
# engega el bot
updater.start_polling()
