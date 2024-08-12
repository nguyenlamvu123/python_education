# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot.py
import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
# InlineKeyboardButton & InlineKeyboardMarkup: Nút và bàn phím tương tác của chatbot ( ví dụ click tùy chọn )

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
# CommandHandler: Được sử dụng để xử lý các lệnh được gửi đến bot từ người dùng trên Telegram.
# MessageHandler: Được sử dụng để xử lý các tin nhắn văn bản từ người dùng trên Telegram.
# filters: Cung cấp các bộ lọc để kiểm tra và lọc các loại tin nhắn, cho phép bạn chỉ xử lý các tin nhắn thỏa mãn các điều kiện nhất định.

import os  # Tương tác với hệ điều hành, đường dẫn file, biến môi trường.
from dotenv import load_dotenv  # Được sử dụng để tải các biến môi trường từ tệp tin .env, cho phép bạn lưu trữ thông tin nhạy cảm như API token một cách bảo mật.
import threading  # Cung cấp các phương thức để tạo và quản lý các luồng (threads), cho phép ứng dụng của bạn thực hiện các tác vụ đồng thời.
from datetime import datetime  # Làm việc với ngày và giờ.


env_path = r'C:\Users\Admin\.venv'  # Đường dẫn đến file .venv chứa thông tin kết nối

load_dotenv(dotenv_path=env_path)  # https://pypi.org/project/python-dotenv/
BOT_TOKEN = os.getenv('BOT_TOKEN').strip()

# Thiết lập logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO = range(4)


# Hàm xử lý command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [["Boy", "Girl", "Other"]]

    context.user_data.clear()
    await update.message.reply_text(
        "Hi! My name is Professor Bot. I will hold a conversation with you. "
        "Send /cancel to stop talking to me.\n\n"
        "Are you a boy or a girl?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Boy or Girl?"
        ),
    )

    return GENDER


async def gender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "I see! Please send me a photo of yourself, "
        "so I know what you look like, or send /skip if you don't want to.",
        reply_markup=ReplyKeyboardRemove(),
    )

    return PHOTO


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("user_photo.jpg")
    logger.info("Photo of %s: %s", user.first_name, "user_photo.jpg")
    await update.message.reply_text(
        "Gorgeous! Now, send me your location please, or send /skip if you don't want to."
    )

    return LOCATION


async def skip_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the photo and asks for a location."""
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    await update.message.reply_text(
        "I bet you look great! Now, send me your location please, or send /skip."
    )

    return LOCATION


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    await update.message.reply_text(
        "Maybe I can visit you sometime! At last, tell me something about yourself."
    )

    return BIO


async def skip_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the location and asks for info about the user."""
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    await update.message.reply_text(
        "You seem a bit paranoid! At last, tell me something about yourself."
    )

    return BIO


async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Thank you! I hope we can talk again some day.")

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start)
        ],
        states={
            GENDER: [
                MessageHandler(
                    filters.Regex("^(Boy|Girl|Other)$"),
                    gender
                )
            ],
            PHOTO: [
                MessageHandler(
                    filters.PHOTO,
                    photo
                ),
                CommandHandler("skip", skip_photo)
            ],
            LOCATION: [
                MessageHandler(filters.LOCATION, location),
                CommandHandler("skip", skip_location),
            ],
            BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
        },
        fallbacks=[
            CommandHandler("cancel", cancel)
        ],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
