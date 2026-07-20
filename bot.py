import os
import logging
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("👋 Hello! I'm your bot. Use /help")

def help_command(update, context):
    update.message.reply_text("Commands: /start, /help")

def echo(update, context):
    update.message.reply_text(f"You said: {update.message.text}")

def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("❌ No bot token found!")
        return
    
    logger.info("✅ Starting bot...")
    
    try:
        updater = Updater(token=token, use_context=True)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help_command))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        
        logger.info("✅ Bot is running!")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
