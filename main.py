from telegram.ext import Application, CommandHandler
import os

BOT_TOKEN = os.getenv("8613274805:AAFTtxg-qWu-bFu68EjLOXz2Q7Lo3ymqgMs")

async def start(update, context):
    await update.message.reply_text("Bot running successfully!")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BOT STARTED...")

app.run_polling()
