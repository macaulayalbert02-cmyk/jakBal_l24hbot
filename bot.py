import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I am your bot. Use /help for commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands: /start - Welcome, /help - This menu")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

if __name__ == '__main__':
    # Get token from environment
    token = os.environ.get('TELEGRAM_BOT_TOKEN') or os.environ.get('BOT_TOKEN')
    
    if not token:
        logger.error("❌ No bot token found!")
        exit(1)
    
    logger.info("✅ Bot token found! Starting bot...")
    
    try:
        # Use Application instead of ApplicationBuilder for better compatibility
        app = Application.builder().token(token).build()
        
        # Add handlers
        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        logger.info("✅ Bot started successfully! Waiting for messages...")
        
        # Start polling with error handling
        app.run_polling()
        
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")
        exit(1)
