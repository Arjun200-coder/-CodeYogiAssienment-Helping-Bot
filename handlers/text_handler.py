from telegram import Update
from telegram.ext import ContextTypes
from services.openai_api import generate_code

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    response = generate_code(prompt)
    await update.message.reply_text(response)
