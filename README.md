# zhongwen-bot
Telegram bot to help me learn Chinese grammar.

This bot is a thin layer on top of [spacy](https://spacy.io/) to tokenize sentences and show grammar relationships. Just send a sentence and you will get back:

* a tokenization of the sentence using the `zh_core_web_lg` model.
* the meaning of the individual tokens (using CEDICT).
* a pretty graph with the grammar relationships between the tokens (using the `displacy` tool shipped with spacy).

![image](https://user-images.githubusercontent.com/27380/197734066-cc92b8f7-ba52-4181-b490-1f5179dd329b.png)


![image](https://user-images.githubusercontent.com/27380/197734136-d873e00a-1ab8-42c2-b66e-57d72733a61c.png)


![image](https://user-images.githubusercontent.com/27380/197734154-6e1f1317-8bc4-4167-afb0-39e9ebdd00d3.png)
