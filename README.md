# zhongwen-bot
Telegram bot to help me learn Chinese grammar.

This bot is a thin layer on top of [spacy](https://spacy.io/) to tokenize sentences and show grammar relationships. Just send a sentence and you will get back:

* a tokenization of the sentence using the `zh_core_web_lg` model.
* the meaning of the individual tokens (using CEDICT).
* a pretty graph with the grammar relationships between the tokens (using the `displacy` tool shipped with spacy).

![zhongwen-bot-1](https://user-images.githubusercontent.com/27380/187194126-223fcdeb-c702-4ce1-8950-90c4031207e2.png)
![zhongwen-bot-2](https://user-images.githubusercontent.com/27380/187194130-82d81ff3-21ee-435b-9b2a-fe6ad3b2c5e6.png)
![zhongwen-bot-3](https://user-images.githubusercontent.com/27380/187194133-25f7f217-1bc6-4730-8049-3a3e8a42f084.jpg)
