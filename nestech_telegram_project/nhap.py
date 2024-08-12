#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.
# https://stackoverflow.com/questions/74910268/how-can-i-make-a-telegram-bot-listen-to-messages-from-a-different-chat-with-pyth
# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot.py

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging, os

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

env_path = r'C:\Users\Admin\.venv'  # Đường dẫn đến file .venv chứa thông tin kết nối

load_dotenv(dotenv_path=env_path)  # https://pypi.org/project/python-dotenv/
BOT_TOKEN = os.getenv('BOT_TOKEN').strip()


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def message_handler(update, context):
    # https://stackoverflow.com/questions/74910268/how-can-i-make-a-telegram-bot-listen-to-messages-from-a-different-chat-with-pyth
    # Get the message from the update
    message = update.message

    # Print the message to the console
    print(message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    # application.add_handler(CommandHandler("start", start))
    # application.add_handler(CommandHandler("help", help_command))
    #
    # # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, message_handler))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()