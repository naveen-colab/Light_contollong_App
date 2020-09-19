#!pip install adafruit-io
#!pip install python-telegram-bot

from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Feed,Data
import os 

def adafruit_auth(n):
    x = os.getenv("ADAFRUIT_IO_USERNAME")  #ADAFRUIT_IO_USERNAME
    y = os.getenv("ADAFRUIT_IO_KEY")    #ADAFRUIT_IO_KEY
    aio = Client(x,y)
    if n==1:            #light on condtion 
      test = aio.feeds('lightstatus')
      aio.send_data(test.key, 10)
    else:               #light off condition
      test = aio.feeds('lightstatus')
      aio.send_data(test.key, 0)
def light_on(bot,update):   #light on function
    str = "light on"
    print(str)
    adafruit_auth(1)
    chat_id=update.effective_chat.id
    bot.send_message(chat_id,text=str)
    bot.send_photo(chat_id,photo="https://static.scientificamerican.com/sciam/cache/file/2B38DE31-C1D3-4339-8808D61972976EE4.jpg")

def light_off(bot,update):      #light off function
      str = "light off"
      print(str)
      adafruit_auth(0)
      chat_id=update.effective_chat.id
      bot.send_message(chat_id,text=str)
      bot.send_photo(chat_id,photo="https://ak.picdn.net/shutterstock/videos/2860753/thumb/1.jpg")

#tele_api = os.getenv("telegram_api")
updater = Updater("1116113868:AAGpjuLnhS19HgkJ1W8R5zZahtghy8augV4")
print("crossed the updater")
dispatch = updater.dispatcher
commandhandler1 = CommandHandler("lightoff",light_off)
commandhandler2 = CommandHandler("lighton",light_on)
dispatch.add_handler(commandhandler1)
dispatch.add_handler(commandhandler2)
updater.start_polling()
updater.idle()
