from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات که از BotFather دریافت کرده‌اید
BOT_TOKEN = "7670138616:AAF7bwoSj5czVLKmWiqcVtBG1pARrxdVd6k"

# فایل برای ذخیره پیام‌ها
LOG_FILE = "messages_log.txt"

# پیام خوشامدگویی
WELCOME_MESSAGE = "سلام! من منشی شما هستم. لطفاً پیام خود را بگذارید. 😊"

# پیام پاسخ به پیام کاربر
REPLY_MESSAGE = "پیام شما دریافت شد. در اسرع وقت پاسخ داده خواهد شد."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دستور /start برای خوشامدگویی به کاربران."""
    await update.message.reply_text(WELCOME_MESSAGE)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ذخیره پیام کاربر و ارسال پاسخ."""
    user_message = update.message.text
    user_info = f"کاربر: {update.effective_user.username or 'نامشخص'}\nپیام: {user_message}\n\n"

    # ذخیره پیام در فایل
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(user_info)

    # پاسخ به کاربر
    await update.message.reply_text(REPLY_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """نمایش دستورالعمل‌ها با /help."""
    help_text = "من اینجا هستم تا پیام‌های شما را ذخیره کنم و به مدیر ارسال کنم. لطفاً سوالات خود را ارسال کنید."
    await update.message.reply_text(help_text)

if __name__ == "__main__":
    # ایجاد اپلیکیشن تلگرام
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # اضافه کردن هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات منشی در حال اجرا است...")
    app.run_polling()
