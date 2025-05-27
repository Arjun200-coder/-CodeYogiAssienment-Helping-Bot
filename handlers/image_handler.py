from telegram import Update
from telegram.ext import ContextTypes

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Image received, but OCR is not enabled in this version.")
