from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from Bots_command import *

updater = Updater('6145377833:AAGR3C2ZtPowkD5kkMXOqbmpj0ZbiSI_74A')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', summ_command))


print('server start')
updater.start_polling()
updater.idle()