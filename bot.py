import io
import cairosvg
from prettytable import PrettyTable
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import ParseMode

import tokenizer


print('Loading tokenizer...')
sentence_tokenizer = tokenizer.SentenceTokenizer()


def get_tabulated_tokens(tokens):
    token_headers = ['Text', 'Pinyin', 'POS', 'Tag', 'DEP']
    #tabulated_tokens = tabulate(tokens, headers=token_headers)
    table = PrettyTable()
    table.field_names = token_headers
    table.add_rows(tokens)

    tabulated_tokens = table.get_string()
    return tabulated_tokens


def convert_svg_to_png(svg):
    svg = svg.replace('<text ', '<text font-family="Noto Sans CJK SC" ')
    inf = io.BytesIO(svg.encode('utf-8'))
    outf = io.BytesIO()
    cairosvg.svg2png(file_obj=inf, write_to=outf, scale=2.0)
    outf.seek(0)
    return outf


def on_new_message(update: Update, context: CallbackContext):
    sentence = update.message.text.strip()

    tokens = sentence_tokenizer.tokenize(sentence)
    response = get_tabulated_tokens(tokens)
    update.message.reply_text(f'<pre>{response}</pre>', parse_mode=ParseMode.HTML)

    meanings = []
    for token in tokens:
        meanings.append(f'<b>{token[0]}</b>: [<i>{token[1]}</i>] {sentence_tokenizer.get_meanings(token[0])}')
    update.message.reply_text('\n'.join(meanings), parse_mode=ParseMode.HTML)

    dep_graph = sentence_tokenizer.get_svg_graph(sentence)
    png = convert_svg_to_png(dep_graph)
    update.message.reply_photo(png)



if __name__ == '__main__':
    with open('secret.txt', encoding='UTF-8') as f:
        api_key = f.read().strip()

    updater = Updater(api_key, use_context=True)

    updater.dispatcher.add_handler(MessageHandler(Filters.text, on_new_message))

    print('Waiting for messages...')
    updater.start_polling()
