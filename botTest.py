from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import CallbackContext
from telegram import Update

from telegram import KeyboardButton, ReplyKeyboardMarkup

TOKEN=""
updater = Updater(TOKEN, use_context=True)

t_1 = "/team1"
t_2 = "/team2"
t_3 = "/ranking"

PT1 = 0
PT2 = 0

def start(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(t_1)], [KeyboardButton(t_2)], [KeyboardButton(t_3)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hey, welcome to the unofficial La Vuelta bot.", reply_markup=ReplyKeyboardMarkup(buttons))
    

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :
    /team1      - t1
    /team2      - t2
    /ranking- ranking""")

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()