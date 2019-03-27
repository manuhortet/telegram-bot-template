import telegram
import logging
from telegram.ext import CommandHandler, Updater
from telegram.ext.dispatcher import run_async
from credentials.credentials import token

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# 'Logging in' the bot with its token
bot = telegram.Bot(token=token)


# Function for the /start command
@run_async
def start(bot, update):
    user_first_name = update.effective_user.first_name
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello {}!".format(user_first_name))


def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    # Linking a command for the bot to our function
    dispatcher.add_handler(CommandHandler('start', start))

    # Starting the bot
    logging.info("Bot running at @<BOT_NAME>")
    updater.start_polling()
    updater.idle()
