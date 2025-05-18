import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pet_care_data import get_response

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    """Send a welcome message when the command /start is issued."""
    response = get_response("start")
    update.message.reply_text(response)

def help_command(update: Update, context: CallbackContext):
    """Send a help message when the command /help is issued."""
    response = get_response("help")
    update.message.reply_text(response)

def handle_message(update: Update, context: CallbackContext):
    """Handle user messages and provide appropriate responses."""
    response = get_response(update.message.text)
    update.message.reply_text(response)

def main():
    """Start the bot."""
    # Token do bot
    TOKEN = "8136664320:AAGY1pTx-jqaqHpv4gxEcOiiBI6CwTmhR1g"

    # Create the Updater
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    print("Bot iniciado! Pressione Ctrl+C para parar.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()