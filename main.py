#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
from functions import crypto

 
command_choices = [['/coin'], ['/cancel']]
reply_markup=ReplyKeyboardMarkup(command_choices, one_time_keyboard=False, resize_keyboard=True)


def start(bot, update):
    """Start the bot and display initial message"""
    update.message.reply_text(
        'NOTIFICATION SYS STATUS: Started\n\n'
        'Send /cancel to abort.\n')


def send_price(bot, update, args):
    if args == []:
        coin_to_display = 5
    else:
        coin_to_display = int(args[0])

    update.message.reply_text(crypto.get_response(coin_to_display), parse_mode='Markdown')


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def main():
    # Access to the API w/ your token
    updater = Updater("YOUR TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # define commands and functions
    start_handler = CommandHandler('start', start)
    coin_handler = CommandHandler('coin', send_price, pass_args=True)
    unknown_handler = MessageHandler(Filters.command, unknown)

    # add handlers
    dp.add_handler(start_handler)
    dp.add_handler(coin_handler)
    dp.add_handler(unknown_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


# main
if __name__ == '__main__':
    main()
