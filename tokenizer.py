import spacy
from cedict_utils.cedict import CedictParser


class SentenceTokenizer():
    def __init__(self):
        # sentence tokenizer
        self._nlp = spacy.load("zh_core_web_lg")

        # for pinyin and meaning
        parser = CedictParser()
        parser.read_file(file_path='data/cedict_ts.u8')
        entries = parser.parse()
        self._lookup = dict(zip([e.simplified for e in entries], [{'pinyin': e.pinyin, 'meanings': e.meanings} for e in entries]))

    def tokenize(self, sentence):
        doc = self._nlp(sentence)
        tokens = []
        for token in doc:
            current_token = [token.text, self.get_pinyin(token.text), token.pos_, token.tag_, token.dep_]
            tokens.append(current_token)
        return tokens

    def get_pinyin(self, word):
        if word in self._lookup:
            return self._lookup[word]['pinyin']

        pinyins = []
        for c in word:
            pinyin = self._lookup[c]['pinyin'] if c in self._lookup else '(???)'
            pinyins.append(pinyin)
        return ''.join(pinyins)

    def get_meanings(self, word):
        return '\n'.join(self._lookup[word]['meanings']) if word in self._lookup else '[??????]'

    def get_graph(self, sentence):
        doc = self._nlp(sentence)
        return spacy.displacy.render(doc)
