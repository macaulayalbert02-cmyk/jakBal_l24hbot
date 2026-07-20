import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your bot.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands: /start, /help")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

if __name__ == '__main__':
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("❌ No bot token found!")
        exit(1)
    
    logger.info("✅ Starting bot...")
    
    try:
        # Using Application directly (not ApplicationBuilder)
        app = Application.builder().token(token).build()
        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        logger.info("✅ Bot is running!")
        app.run_polling()
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        exit(1)
