#!/usr/bin/python3

# bot.py - the telegram bot settings themselves


from telegram.ext import Updater, CommandHandler, MessageHandler


# Define the command handlers
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Starting the notification system')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Fetch the current price of your favourite currencies")


def get_price(bot, update):
    """Echo the user message."""
    update.message.reply_text(pricez(coin_data))


def get_rank(bot, update):
    """Echo the user message."""
    update.message.reply_text(rankz)


def start_bot():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("APIKEY")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("price", get_price))
    dp.add_handler(CommandHandler("rank", get_rank))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()
