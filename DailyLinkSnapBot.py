# Get the bot token from the environment variable

TOKEN = BOT_TOKEN = "6811190192:AAFLx7NrkQMmWRVzgBZBRSny2AMo0Iw5Leo"

# from datetime import datetime, timedelta
#
# from telegram.ext import CommandHandler, Updater
#
# updater = Updater dsf(token=BOT_TOKEN, use_context=True)
#
# # Get the dispatcher object from the updater
# dispatcher = updater.dispatcher
#
#asfd
# # Import telegram APIs
# from telegram import Bot
#
#
# # Fetch messages
#
#
#
# def start(update, context):
#     # Send a welcome message to the user
#     context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text="Hello, I am a Telegram bot created using Python. I can echo your text messages.",
#     )
#
#
# # Define a function to handle the /today command
# def today_message(update, context):
#     # Get the channel username from the command argument
#     def get_todays_messages(channel_username):
#         bot = Bot(token=BOT_TOKEN)
#
#         # Get chat id from channel username
#         chat_id = bot.get_chat(channel_username).id
#
#         # Fetch messages from yesterday till today
#         yesterday = datetime.utcnow() - timedelta(days=1)
#         messages = bot.get_updates(offset=yesterday.timestamp(), timeout=10)[0]
#
#         # Filter messages that are from this channel
#         todays_messages = []
#         for m in messages:
#             if m.message and m.message.chat.id == chat_id:
#                 todays_messages.append(m)
#
#         return todays_messages
#     if not context.args:
#         context.bot.send_message(
#             chat_id=update.effective_chat.id,
#             text="Please provide the channel username."
#             " Usage: /today <channel_username>",
#         )
#         return
#
#     channel_username = context.args[0]
#     printx(channel_username, context, update)
#
#     try:
#         # Get the chat_id of the channel
#         chat = context.bot.get_chat(channel_username)
#         chat_id = chat.id
#
#         # Fetch today's messages from the channel
#         today = datetime.now()
#         yesterday = today - timedelta(days=1)
#         messages = get_todays_messages(channel_username)
#         if messages:
#             latest_message = messages[0].message.text
#             printx(latest_message, context, update)
#         # if messages:
#         #     latest_message = messages[0].text
#         #     update.message.reply_text(
#         #         f"Today's message from {channel_username}: {latest_message}"
#         #     )
#         else:
#             update.message.reply_text(
#                 f"No messages found for {channel_username} today."
#             )
#
#     except Exception as e:
#         update.message.reply_text(f"An error occurred: {str(e)}")
#     printx("done", context, update)


def printx(message, context, update):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"m:{message}",
    )


import logging
import datetime
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Channel username
CHANNEL = "@channelusername"

def start(update, context):
    update.message.reply_text("Hi! I can fetch today's message from a channel. Use /today")

def today(update, context):
    """ Fetch today's message from channel """

    bot = Bot(token=BOT_TOKEN)

    try:
        # Get channel chat id
        channel_id = bot.get_chat(CHANNEL).id

        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days=1)

        # Fetch messages
        messages = bot.get_updates(offset=yesterday.timestamp())[0]

        # Filter for channel messages
        todays_message = ""
        for m in messages:
            if m.message and m.message.chat.id == channel_id:
                todays_message = m.message.text
                break

        update.message.reply_text(f"Today's message from {CHANNEL}: \n{todays_message}")

    except Exception as e:
        update.message.reply_text(f"Sorry, error fetching message - {str(e)}")


if __name__ == '__main__':
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("today", today))

    updater.start_polling()
    updater.idle()