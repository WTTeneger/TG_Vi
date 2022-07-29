from cmath import log
import time
from pathlib import Path
from weakref import ref
import db
import telebot
from text import *
import os
from threading import Thread
_db = db.dbmethods()

bot_users = []

# портировать всне из button как bt
from button import * # Импортируем все клавиатуры
users_data = {}
bot = telebot.TeleBot('5411180764:AAGfShatpU8JcQSrpdaick8WiZy2D8VHEgo')
admin = [569452912]


def send_from(tgid, message, timeout=30):
    time.sleep(timeout)
    bot.send_messge(tgid, message)


def send_for_admin(message):
    for el in admin:
        print(message)
        if message.content_type == 'photo': 
            bot.send_photo(el, message.photo[-1].file_id, 
                           text_bottom_image.format(tgid=message.from_user.id, tgnick=message.from_user.username), 
                           reply_markup=key_board_admin_access(message.from_user.id))
        elif message.content_type == 'text':
            bot.send_message(el, f'Отправил {message.text}\n'+ text_bottom_image.format(tgid=message.from_user.id, tgnick=message.from_user.username), 
                             reply_markup=key_board_admin_access(message.from_user.id))
            
            
        

def payable(message):
    bot.send_message(message.chat.id, payable_1, reply_markup=key_board_user_payable())
    
def access_payable(message):
    bot.send_message(message.chat.id, 'Отправь нам чек после оплаты, или имя фамилию', reply_markup=keyboard_disabled())
    bot.register_next_step_handler(message, sended_payable)

def sended_payable(message):
    if message.content_type == 'text' and message.text == keyboard_disabled_1:
        bot.send_message(message.chat.id, f'Отменил')
        bot.send_message(message.chat.id, 'menu', reply_markup=keyboard_menu())   
    elif message.content_type == 'photo': 
        # bot.send_photo(message.chat.id, message.photo[-1].file_id)
        bot.send_message(message.chat.id, text_end_payment, reply_markup = keyboard_menu()) # удаляем кнопки у последнего сообщения
        send_for_admin(message)

    elif message.content_type == 'text':
        bot.send_message(message.chat.id, text_end_payment, reply_markup = keyboard_menu()) # удаляем кнопки у последнего сообщения
        send_for_admin(message)
        
    else:
        bot.send_message(message.chat.id, f'Не верный формат сообщения, отправь либо фото, либо текст')
        access_payable(message)
        



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print('call_data', call.data)
    if call.data == 'user_yes':
        message = call.message
        print(message)
        print(message.text)
        bot.edit_message_reply_markup(message.chat.id, message_id = message.message_id, reply_markup = '') # удаляем кнопки у последнего сообщения
        access_payable(message)

    if 'admin_access_yes-' in call.data:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        message = call.message
        user_id = int(call.data.split('-')[1])
        bot.send_message(user_id, text_compile_payment_yes, reply_markup = keyboard_menu())
        Thread(target=send_from(user_id, [
            {
            
            }
        ])).start()
        _db.set_payabled(user_id)
    if 'admin_access_no-' in call.data:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        message = call.message
        user_id = int(call.data.split('-')[1])
        bot.send_message(user_id, text_compile_payment_no, reply_markup = keyboard_menu())
        # print(data)
        # print(mes)
        # for el in admin:    
            # bot.send_message(el, 'оплатила', reply_markup=key_board_admin_access())


@bot.message_handler(commands=['start', 'helps'])
def get_text_messages(message):
    print(message.chat.id)
    print(message)
    if message.chat.id not in bot_users:
        if '/start' in message.text:
            ref_code = 0
            if 'ref' in message.text:
                ref_code = message.text.split(' ')[1].replace('ref', '')
                print(ref_code)
            data_created = _db.create_user(message.from_user.id, message.from_user.first_name, ref_code)
            _db.add_ref_for_user(ref_code)
            text = new_user_1 if data_created else last_user_1
            bot.send_message(message.chat.id, text)
    # bot.send_message(message.chat.id, 'menu', reply_markup=key_board_share_for_frends(message.chat.id))
    bot.send_message(message.chat.id, 'menu', reply_markup=keyboard_menu())
    # bot.reply_to(message, 'menu', reply_markup=keyboard_menu())

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    
    if message.text == keyboard_disabled_1:
        bot.send_message(message.chat.id, 'menu', reply_markup=keyboard_menu())
    
    if message.text == keyboard_menu_1:
        payable(message)
    
    if message.text == keyboard_menu_3:
        user =_db.get_all_info(message.chat.id)
        total_sup = 100
        bot.send_message(message.chat.id, 
                         referal_info.format(
                            tgid = message.chat.id, 
                            count_ref= user['count_refferal'], 
                            count_ref_pay =  user['count_payable_refferal'],
                            balance = user['count_refferal']*total_sup), 
                         reply_markup=key_board_share_for_frends(message.chat.id))

def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
   webAppTest = types.WebAppInfo("https://telegram.mihailgok.ru") #создаем webappinfo - формат хранения url
   one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest) #создаем кнопку типа webapp
   keyboard.add(one_butt) #добавляем кнопки в клавиатуру

   return keyboard #возвращаем клавиатуру

def start():
    print('Бот запущен')
    while True:
        bot.polling(none_stop=True, interval=0, timeout=2)


start()
