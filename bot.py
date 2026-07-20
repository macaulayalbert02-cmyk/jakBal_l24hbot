import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Hello! I'm your bot. Use /help")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Commands: /start, /help")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"You said: {update.message.text}")

if __name__ == '__main__':
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("❌ No bot token found!")
        exit(1)
    
    logger.info("✅ Starting bot...")
    
    try:
        # Using Updater (older style that works with all versions)
        updater = Updater(token=token, use_context=True)
        dp = updater.dispatcher
        
        # Add handlers
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help_command))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        
        logger.info("✅ Bot is running!")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        exit(1)
