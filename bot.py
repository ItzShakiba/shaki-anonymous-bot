import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = 8736169059


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "پیامت رو بفرست 🩵🌙\n"
        "پیامت به صورت ناشناس برای صاحب بات ارسال میشه."
    )


async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == OWNER_ID:
        return

    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"📩 پیام ناشناس:\n\n{update.message.text}"
    )

    await update.message.reply_text("پیامت ارسال شد 🩵")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_message))

print("ShakiBot is running...")
app.run_polling()