# Telegram bot template

Template in Python and basic guidance on how to start a new Telegram bot.

## Pre-requisites
* Python >= 3.4
* Declare your bot on Telegram. [Learn how](https://core.telegram.org/bots).
* Familiarity with Python and access to the [python-telegram-bot docs](https://python-telegram-bot.readthedocs.io/en/stable/).

## Settings
* Add a valid bot-token in `credentials/credentials.py`. [@BotFather](https://t.me/BotFather) will give you this when creating your bot.
* Install basic requirements:
```angular2
pip install -r requirements.txt
```

## Running
At this point you should be able to execute a simple bot answering to the command `/start`. Do it using:

```angular2
python run.py
```

**Note:** you can run it using Docker and the Dockerfile of the project:
```angular2
docker build -p <SERVICE-NAME> .
docker run <SERVICE-NAME>
```

## More commands

New commands must be added to `bot/bot.py` same way as the example `/start` command: 

```python
# Defining the action in a function                                                                   
                                                                                                      
def start(bot, update):                                                                                   
        user_first_name = update.effective_user.first_name                                            
        bot.sendMessage(chat_id=update.message.chat_id, text="Hello {}!".format(user_first_name))     
                                                                                                      
                                                                                                      
# Linking the action with the bot command call, using a handler                                 

def main():                                                                                           
    [...]                                                                                             
    dispatcher.add_handler(CommandHandler('start', start))                                            
    [...]                                                                                            
```


**Notes:** 
* For [conversational commands](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html) I'd recommend to use a different file inside `bot/`.
* All comands must be linked to the bot in the main function, independently of where their definition is.
* Use the decorator `@run_async` on all functions to add multi-threading to the bot. Relevant if you're excepting some traffic. [Read more](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Performance-Optimizations).

## Where to go from here

* Both the [github wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki) and the [official docs](https://python-telegram-bot.readthedocs.io/en/stable/index.html) of python-telegram-bot are great places to learn more about all this.

* This awesome [telegram bots compilation](https://github.com/DenisIzmaylov/awesome-telegram-bots).  

* The Telegram bots subreddit, [r/TelegramBots](https://www.reddit.com/r/TelegramBots/), is pretty active and contains plenty of resources.