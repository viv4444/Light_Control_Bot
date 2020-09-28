from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from Adafruit_IO import Client,Feed,Data
import os

ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
aio = Client('ADAFRUIT_IO_USERNAME','ADAFRUIT_IO_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

def start(bot, update):
    print(str( update.effective_chat.id ))
    bot.send_message(chat_id = update.effective_chat.id, text="Welcome! Type 'Turn on the Light' or /lighton to switch on the light bulb. Type 'Turn off the Light' or /lightoff to switch off the light bulb.")

def unknown(bot, update):
    bot.send_message(chat_id=update.effective_chat.id, text="Oops, I didn't understand that. Try again!")

def value_send(value):
  to_feed = aio.feeds('bot4')
  aio.send_data(to_feed.key,value)
  
def lighton(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Light has been turned ON")
  bot.send_photo(chat_id, photo='https://www.google.com/imgres?imgurl=https%3A%2F%2Fak.picdn.net%2Fshutterstock%2Fvideos%2F13048079%2Fthumb%2F12.jpg&imgrefurl=https%3A%2F%2Fwww.shutterstock.com%2Fvideo%2Fclip-13048079-hand-holding-light-bulb-dark-lamp-lights&tbnid=bsgMWvULrgg4kM&vet=12ahUKEwj7-vC6x4nsAhU85jgGHSTeDuMQMygZegUIARCFAg..i&docid=nG3FZjTR7D6A5M&w=852&h=480&q=bulb%20light%20on&hl=en&ved=2ahUKEwj7-vC6x4nsAhU85jgGHSTeDuMQMygZegUIARCFAg')
  value_send(1)
  
def lightoff(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Light has been turned OFF")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.google.com/imgres?imgurl=https%3A%2F%2Ffreeonlineflashlight.com%2Fimg%2Fbulb.png&imgrefurl=https%3A%2F%2Ffreeonlineflashlight.com%2F&tbnid=S6et7iZxQcCA-M&vet=12ahUKEwirhfHx34nsAhVD_TgGHUJcB2sQMygSegUIARD_AQ..i&docid=gxw5SzaQ0vFfNM&w=300&h=300&q=light%20off&ved=2ahUKEwirhfHx34nsAhVD_TgGHUJcB2sQMygSegUIARD_AQ')
  value_send(0)  

def given_message(bot, update):
  text = update.message.text.upper()
  text = update.message.text
  if text == 'Turn on the Light':
    lighton(bot,update)
  elif text == 'Turn off the Light':
    lightoff(bot,update) 

u = Updater('TELEGRAM_TOKEN',use_context = True)
dp = u.dispatcher
dp.add_handler(CommandHandler('lighton',lighton))
dp.add_handler(CommandHandler('lightoff',lightoff))
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.command, unknown))
dp.add_handler(MessageHandler(Filters.text, given_message))

u.start_polling()
u.idle()
        
