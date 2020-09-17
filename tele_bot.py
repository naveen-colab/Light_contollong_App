from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Feed,Data

def adafruit_auth(n):
    x = "Naveen_bot"   #ADAFRUIT_IO_USERNAME
    y = "aio_hQRr84atT81tRI8reNF4Uo95qVmU"    #ADAFRUIT_IO_KEY
    aio = Client(x,y)
    if n==1:
      test = aio.feeds('foo')
      aio.send_data(test.key, 10)
    else:
      test = aio.feeds('foo')
      aio.send_data(test.key, 0)
def light_on(context,update):
    str = "light on"
    adafruit_auth(1)
    context.send_message(chat_id=update.effective_chat.id,text=str)

def light_off(context,update):
      str = "light off"
      adafruit_auth(0)
      context.send_message(chat_id=update.effective_chat.id,text=str)

updater = Updater("1116113868:AAGpjuLnhS19HgkJ1W8R5zZahtghy8augV4")
dispatch = updater.dispatcher
commandhandler1 = CommandHandler("off",light_off)
commandhandler2 = CommandHandler("on",light_on)
dispatch.add_handler(commandhandler1)
dispatch.add_handler(commandhandler2)
updater.start_polling()
updater.idle()
