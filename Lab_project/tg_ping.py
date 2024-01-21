import telebot

bot_token = '6938914611:AAEG8jHiyGYYIwTGeEG723057WD4JEgo-ck'
bot = telebot.TeleBot(bot_token)

def ping_door_trouble(x):
    if x > 0 and x < 9:
       bot.send_message(338756016, 'Door was unlocked!!!!!')
       
@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.username
    bot.send_message(message.chat.id, 'Thanks for connect to Lab_monitoring system!')

 
bot.polling()