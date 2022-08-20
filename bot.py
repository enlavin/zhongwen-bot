from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from tabulate import tabulate

import tokenizer


sentence_tokenizer = tokenizer.SentenceTokenizer()


def get_tabulated_tokens(tokens):
    token_headers = ['Text', 'Pinyin', 'POS', 'Tag', 'DEP']
    tabulated_tokens = tabulate(tokens, headers=token_headers)
    return tabulated_tokens


def on_new_message(update: Update, context: CallbackContext):
    tokens = sentence_tokenizer.tokenize(update.message.text)
    response = f'```\n{get_tabulated_tokens(tokens)}\n```'
    update.message.reply_markdown(response)


if __name__ == '__main__':
    with open('secret.txt', encoding='UTF-8') as f:
        api_key = f.read().strip()

    updater = Updater(api_key, use_context=True)

    updater.dispatcher.add_handler(MessageHandler(Filters.text, on_new_message))

    updater.start_polling()
