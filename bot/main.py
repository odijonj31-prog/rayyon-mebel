import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📚 Katalog", callback_data="catalog"),
            InlineKeyboardButton("📐 Buyurtma", callback_data="order"),
        ],
        [
            InlineKeyboardButton("📦 Buyurtmam", callback_data="orders"),
            InlineKeyboardButton("💳 To‘lovlarim", callback_data="payments"),
        ],
        [
            InlineKeyboardButton("🤖 AI maslahatchi", callback_data="ai"),
        ],
        [
            InlineKeyboardButton("👨‍💼 Menejer bilan bog‘lanish", callback_data="manager"),
        ],
    ]

    await update.message.reply_text(
        "🪑 *Rayyon Mebel* ga xush kelibsiz!\n\n"
        "Sifatli mebel — siz xohlagan o‘lcham va dizaynda.\n\n"
        "Kerakli bo‘limni tanlang:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN sozlanmagan!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Rayyon Mebel bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
