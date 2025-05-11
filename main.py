import os
from telebot import TeleBot

TOKEN = os.getenv('TOKEN')  # Берем токен из переменных окружения
if not TOKEN:
    raise ValueError("Не задан TOKEN для бота")
    
bot = TeleBot(TOKEN)

TOKEN = '7305693655:AAFiR1KlGvIyHho-b-VMZFcqx1pgjByq7Uw'
bot = TeleBot(TOKEN)

hi_words_list = [ 'привет', 'здрасте', 'здарова', 'hi', ]
action_words_list = [ 'умеешь', 'знаешь', 'можешь', 'фнкци', 'возможност', ]

bot_actions_message = f""" Вот что я умею:
   ✈ - мировое время
   ☁ - прогноз погоды
"""

is_user_sey_hi = False

def check_hi(text):
    global is_user_sey_hi
    for hi in hi_words_list:
        if text.find(hi) > -1:
            is_user_sey_hi = True
    return is_user_sey_hi

def check_actions(text):
    for action in action_words_list:
        if text.find(action) > -1 : return True
    return False

def get_answer(message):
    text = message.text.lower().strip()
    if is_user_sey_hi == False:
        if check_hi(text) : return f'Привет {message.from_user.first_name}!'
        else : return f'{message.from_user.first_name}, ты забыл поздороваться!'

    if check_actions(text) : return bot_actions_message
    else : return 'К сожалению, я тебя не понимаю!'


    

@bot.message_handler()
def get_message(message):
    answer = get_answer(message)
    bot.send_message(message.chat.id, answer)
   
if __name__ == '__main__':
    bot.polling(none_stop=True)