import telebot
import sys
import time
import os
import logging
from dotenv import load_dotenv
from telebot.apihelper import ApiTelegramException

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Загрузка переменных окружения из .env файла
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TARGET_CHAT_ID = int(os.getenv('TARGET_CHAT_ID', '7704451620'))

# Проверка наличия токена
if not TOKEN:
    logger.error("Не найден TELEGRAM_BOT_TOKEN в переменных окружения")
    logger.info("Пожалуйста, установите переменную окружения или создайте файл .env")
    sys.exit(1)

bot = telebot.TeleBot(TOKEN)
RESPONSE_MESSAGE = "Я пока что только для отправки сообщений в группу, я с тобой не буду общаться))\nМой создатель - @BorozdovNikita если есть вопросы пиши ему"

logger.info("Бот инициализирован")
logger.info(f"Токен загружен: {TOKEN[:10]}...")


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        logger.info(f"Получено сообщение от пользователя {message.from_user.id}: {message.text[:50]}...")
        bot.reply_to(message, RESPONSE_MESSAGE)
        logger.info("Отправлен ответ пользователю")

        user = message.from_user
        user_info = f"Новое сообщение от пользователя:\n"
        user_info += f"ID: {user.id}\n"
        user_info += f"Имя: {user.first_name}\n"
        if user.last_name:
            user_info += f"Фамилия: {user.last_name}\n"
        if user.username:
            user_info += f"Username: @{user.username}\n"
        user_info += f"Текст сообщения: {message.text}"

        bot.send_message(TARGET_CHAT_ID, user_info)
        logger.info(f"Информация о пользователе отправлена в чат {TARGET_CHAT_ID}")

    except Exception as e:
        logger.error(f"Ошибка при обработке сообщения: {e}", exc_info=True)


def check_bot_conflict():
    """Проверка конфликта запущенных экземпляров бота"""
    try:
        bot.get_updates(offset=-1)
        return False
    except ApiTelegramException as e:
        if e.error_code == 409:
            logger.error("Конфликт: бот уже запущен в другом месте")
            return True
        else:
            return False
    except Exception:
        return False


if __name__ == '__main__':
    logger.info("Попытка запуска бота...")

    if check_bot_conflict():
        logger.error("Не удалось запустить бота из-за конфликта")
        sys.exit(1)

    logger.info("Бот успешно запущен и готов к работе")

    while True:
        try:
            logger.info("Начало polling...")
            bot.polling(none_stop=True, interval=0, timeout=20)
        except ApiTelegramException as e:
            if e.error_code == 409:
                logger.error("Конфликт: бот уже запущен в другом месте.")
                time.sleep(30)
            else:
                logger.error(f"Ошибка Telegram API: {e}")
                time.sleep(15)
        except Exception as e:
            logger.error(f"Неожиданная ошибка: {e}", exc_info=True)
            time.sleep(15)