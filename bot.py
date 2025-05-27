import os
from assignments.data import assignment_data
import logging
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

load_dotenv()
# print(os.getenv("OPENROUTER_API_KEY"))
import requests



BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

logging.basicConfig(level=logging.INFO)

def get_openrouter_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourdomain.com",  # optional
        "X-Title": "MyTelegramBot"
    }
    payload = {
        # "model": "mistralai/mistral-7b-instruct",  
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "system", "content": (
                "You are a smart and friendly assistant who automatically replies in the same language as the user. "
                "If the user speaks in English, reply in English. If the user writes in Hindi (Devanagari script), reply in Hindi. "
                "If the user types in Hinglish (Hindi written in Roman script), reply in Hinglish. "
                "Always match the tone and script of the user. Keep your replies natural, helpful, and short. "
                "Do not invent stories, metaphors, or irrelevant examples. Stay focused and reply in a real, human style."
                "NEVER talk about laddoos, dreams, cooking, or boss — unless user actually mentions it. "
                "Your tone should always be chill, funny, and helpful — like a close Indian friend. "
            )},
            {"role": "user", "content": prompt}
        ]
        
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip().lower()

    # Check if user asked for a specific assignment like "assignment 18.1"
    if "assignment" in user_message:
        for key in assignment_data:
            if key in user_message:
                data = assignment_data[key]
                reply = (
                    f"📄 HTML CODE:\nhtml\n{data['html']}\n\n"
                    f"🎨 CSS CODE:\ncss\n{data['css']}\n\n"
                    f"🧠 JS CODE:\njs\n{data['js']}"
                )
                await update.message.reply_text(reply, parse_mode='Markdown')
                return
        await update.message.reply_text("❌ Sorry, assignment code not found.")
    else:
        # fallback to your chatbot response
        try:
            bot_reply = get_openrouter_response(user_message)
            await update.message.reply_text(bot_reply)
        except Exception as e:
            await update.message.reply_text("⚠ API error: " + str(e))


if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("🤖 Bot is running with OpenRouter API...")
    app.run_polling()