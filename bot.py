import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["TELEGRAM_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🐻 Имперский бот на связи. Приказывай, Император.")

async def prognoz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📡 СВОДКА ИМПЕРИИ НА СЕГОДНЯ:\n\n"
        "⚽️ Ювентус – Верона: П1 с форой (-1.5)\n"
        "🏀 Баскония – Бреоган: П1\n"
        "🏀 Барселона – Гран-Канария: П1\n"
        "⚽️ Астон Вилла – Тоттенхэм: Фора 0\n\n"
        "💰 Банк: 500 ₽. Цель: 2000 ₽.\n"
        "⚠️ Дисциплина: Одинар > Экспресс!"
    )
    await update.message.reply_text(text)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prognoz", prognoz))
    print("🛡️ Имперский бот запущен...")
    app.run_polling()
