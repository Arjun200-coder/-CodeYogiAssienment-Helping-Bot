from telegram.ext import MessageHandler, filters
from ocr_utils import extract_text_from_image
import os

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    image_path = f"downloads/{update.message.from_user.id}.jpg"

    await file.download_to_drive(image_path)

    text = extract_text_from_image(image_path)

    await update.message.reply_text(f"📄 Extracted Text:\n\n{text}")

    os.remove(image_path)

app.add_handler(MessageHandler(filters.PHOTO, handle_image))
