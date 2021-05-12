import array
import random
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+`~[]{]\|;:,<.>/?'

def get_random_password(len, count):
    result = []
    for i in range(count):
        password = ''
        for c in range(len):
            password += random.choice(valid_chars)
        result.append(password)

    print(result)
    return result

# filan = get_random_password(5,10)
# for f in filan:
#     print(f)

def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!', 
        reply_markup=ForceReply(selective=True)
    )

def ramz(update: Update, _: CallbackContext) -> None:
    print(update.message.text)
    r = get_random_password(8, 10)
    msg = ''
    for i in r:
        msg += i + '\n'

    update.message.reply_text(f'Passwords generated : \n {msg}')

def main() -> None:
    updater = Updater('YourBotToken')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ramz', ramz))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

