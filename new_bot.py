from cmath import log
from threading import Thread
import time
from pathlib import Path
from weakref import ref
import db
import telebot
from telebot import types
from text import *
import os

_db = db.dbmethods()

bot_users = []


# AgACAgIAAxkBAAIDgWLjqV27QMZTSNiZUh-OmWJLRqwiAALHvzEbWGUgS-u_DrhP6Kc-AQADAgADcwADKQQ -- 1000rub

#  -- Бизнес нутая

# AgACAgIAAxkBAAIE1GLj2JA-lcZIgPkEHdYOeXMwy_TMAAL6vjEbhSUgS9-LeZqbyDPRAQADAgADbQADKQQ -- найти себя

# AgACAgIAAxkBAAIE32Lj2LiQ66lVuFYWUeVbjPhkVmaQAAL7vjEbhSUgS9AJ6k8sbxA4AQADAgADbQADKQQ -- маркетинг

# AgACAgIAAxkBAAIE62Lj2OoEs06Xl3yNGb5SgUqpvAQEAAL8vjEbhSUgSwxchSQu442zAQADAgADcwADKQQ -- личностный рост

# AgACAgIAAxkBAAIE8mLj2RShbHBj12JcQK1e3iWiWqT5AAL9vjEbhSUgS1WPmmmCnaEHAQADAgADcwADKQQ -- женская энергия

# AgACAgIAAxkBAAIEymLj2FOwkPAM1FpMQj-TOKmLoj_lAAL4vjEbhSUgS9ldOEbMsRWqAQADAgADcwADKQQ -- фин грам

# AgACAgIAAxkBAAIE-WLj2TcXR1BfMjZEkG9oGbDJb9K7AAL-vjEbhSUgS2i5MgHrc_sfAQADAgADbQADKQQ -- доп

# AgACAgIAAxkBAAIFCWLj2W4Nr8xM42ILYO1dNRJUKZA_AAO_MRuFJSBLpTh-D6_2AAG7AQADAgADbQADKQQ -- макс - мин

abouts = [
    'AgACAgIAAxkBAAIE1GLj2JA-lcZIgPkEHdYOeXMwy_TMAAL6vjEbhSUgS9-LeZqbyDPRAQADAgADbQADKQQ', # -- найти себя
    'AgACAgIAAxkBAAIE32Lj2LiQ66lVuFYWUeVbjPhkVmaQAAL7vjEbhSUgS9AJ6k8sbxA4AQADAgADbQADKQQ', # -- маркетинг
    'AgACAgIAAxkBAAIE62Lj2OoEs06Xl3yNGb5SgUqpvAQEAAL8vjEbhSUgSwxchSQu442zAQADAgADcwADKQQ', # -- личностный рост
    'AgACAgIAAxkBAAIE8mLj2RShbHBj12JcQK1e3iWiWqT5AAL9vjEbhSUgS1WPmmmCnaEHAQADAgADcwADKQQ', # -- женская энергия
    'AgACAgIAAxkBAAIEymLj2FOwkPAM1FpMQj-TOKmLoj_lAAL4vjEbhSUgS9ldOEbMsRWqAQADAgADcwADKQQ', # - фин грам
]

# 

# 

# портировать всне из button как bt
from button import * # Импортируем все клавиатуры
users_data = {}
bot = telebot.TeleBot('5411180764:AAGfShatpU8JcQSrpdaick8WiZy2D8VHEgo')
admin = [714118879]

users_local_data = {}

def send_from(tgid, message = [], timeout=30):
    time.sleep(timeout)
    for el in message:
        if 'keyboard' in el and el['keyboard'] != '':
            if el['keyboard'] != 'none':
                bot.send_message(tgid, el['message'], reply_markup=el['keyboard'])
        else:
            bot.send_message(tgid, el['message'], reply_markup=types.ReplyKeyboardRemove())


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
  

def __payabled(message):
    # bot.send_message(message.chat.id, text_select_sphere, reply_markup=keyboard_sphere())
    if message.content_type == 'photo': 
        bot.send_message(message.chat.id, text_after_payments, reply_markup=keyboard_menu())
        send_for_admin(message)
        
    elif message.content_type == 'text':
        if message.text == keyboard_disabled_1:
            bot.send_message(message.chat.id, 'С возвращением в меню', reply_markup=keyboard_menu())
        else:
            bot.send_message(message.chat.id, text_after_payments, reply_markup=keyboard_menu())
            send_for_admin(message)
    
    else:
        bot.send_message(message.chat.id, f'Не верный формат сообщения, отправь либо фото, либо текст')
        bot.register_next_step_handler(message, __payabled)


def payable(message):
    bot.send_message(message.chat.id, payable_1, reply_markup=key_board_user_payable())


def access_payable(message):
    bot.send_message(message.chat.id, 'Отправь нам чек после оплаты, или имя фамилию', reply_markup=keyboard_disabled())
    bot.register_next_step_handler(message, sended_payable)


def sended_payable(message) :
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


def make_ref_link_data(message):
    _db.set_payable_data(message.chat.id, message.text)
    bot.send_message(message.chat.id, link_s, reply_markup=keyboard_menu())
    bot.send_message(message.chat.id, link, reply_markup=key_board_share_for_frends_and_help(message.chat.id))
    bot.delete_message(message.chat.id, message_id = message.message_id-1) # удаляем кнопки у последнего сообщения


def make_ref_link_data_start(message):
    bot.send_message(message.chat.id, text_take_ref_link, reply_markup=go_back_in_menu())
    bot.register_next_step_handler(message, make_ref_link_data)
    

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print('call_data', call.data)
    
    if 'sphere-' in call.data:
        id_sphere = call.data.split('-')[1]
        bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения
        if call.message.chat.id not in users_local_data:
            users_local_data[call.message.chat.id] = {}
        users_local_data[call.message.chat.id]['sphere'] = id_sphere
        bot.send_message(call.message.chat.id, text_select_payments, reply_markup = keyboard_payable())
        
    if "button-payments-" in call.data:
        id_pay = call.data.split('-')[2]
        print(id_pay)
        # bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '') # удаляем кнопки у последнего сообщения
        bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения
        if int(id_pay) == 1:
            print('ss')
            bot.send_message(call.message.chat.id, text_date_sberbank, reply_markup = keyboard_disabled())
            bot.register_next_step_handler(call.message, __payabled)
        elif int(id_pay) == 2:
            bot.send_message(call.message.chat.id, text_date_tinkoff, reply_markup = keyboard_disabled())
            bot.register_next_step_handler(call.message, __payabled)

    if 'admin_access-' in call.data:
        data = call.data.split('-')
        type = data[1]
        tgid = data[2]
        if data[1] == 'yes':
            try:
                _db.set_payabled(tgid, users_local_data[tgid]['sphere'])
            except:
                _db.set_payabled(tgid, 1)
                
            bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '') # удаляем кнопки у последнего сообщения
            bot.send_message(tgid, succcess_payments)
            
            Thread(target=send_from(tgid, [
            {
                'message': text_after_sucs1,
                # 'keyboard': ''
            }], 10)).start()
            Thread(target=send_from(tgid, [{
                'message': text_after_sucs2, 
                'keyboard': keyboard_yes_ref_add()
            }], 15)).start()
            
        else:
            bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '') # удаляем кнопки у последнего сообщения
            bot.send_message(tgid, unsucccess_payments)
    
    if call.data == 'yes-go-stage-ref':
        print('ss')
        bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id, reply_markup = '') # удаляем кнопки у последнего сообщения
        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIDgWLjqV27QMZTSNiZUh-OmWJLRqwiAALHvzEbWGUgS-u_DrhP6Kc-AQADAgADcwADKQQ',
                       ref_text, reply_markup=keyboard_yes_no_make_ref())
    
    if 'go-stage-create-ref_' in call.data:
        answer = call.data.split('_')[1]
        bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения

        print('answer', answer)
        if answer == 'yes':
            # bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения
            make_ref_link_data_start(call.message)
        if answer == 'no':
            # bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения
            bot.send_message(call.message.chat.id, text_no_ref, reply_markup=but_access_ref())
        
    if call.data == 'go_back_in_menu':
        bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения
        bot.send_message(call.message.chat.id, 'С возвращением в меню', reply_markup=keyboard_menu())
    
    if 'but-access-ref_' in call.data:
        answer = call.data.split('_')[1]
        bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения
        if answer == 'yes':
            make_ref_link_data_start(call.message)
        if answer == 'no':
            bot.send_message(call.message.chat.id, but_access_ref_no_click, reply_markup=keyboard_menu())
            Thread(target=send_from(call.message.chat.id, [
            {
                'message': text_after_20_hours,
            },
            {
                'message': button_after_20_hours,
                'keyboard': keyboard_yes_no_make_ref_20TH()
            },
            
            ], 20*60*60)).start()
    
    if 'go-stage-create-ref-20TH_' in call.data:
        answer = call.data.split('_')[1]
        
        bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения
        if answer == 'yes':
            make_ref_link_data_start(call.message)
        if answer == 'no':
            # bot.delete_message(call.message.chat.id, message_id = call.message.message_id) # удаляем кнопки у последнего сообщения
            bot.send_message(call.message.chat.id, button_after_20_hours_no, reply_markup=keyboard_menu())
            Thread(target=send_from(call.message.chat.id, [
            {
                'message': text_after_23_hours,
            },
            {
                'message': button_after_20_hours,
                'keyboard': keyboard_yes_no_make_ref_23TH()
            },
            ],  23*60*60)).start()
    
    if 'go-stage-create-ref-23TH_' in call.data:
        answer = call.data.split('_')[1]
        
        if answer == 'yes':
            make_ref_link_data_start(call.message)
        if answer == 'no':
            bot.send_message(call.message.chat.id, 'С возвращением в меню', reply_markup=keyboard_menu())

    if "abount-" in call.data:
        answer = int(call.data.split('-')[1]) - 1
        bot.send_photo(call.message.chat.id, abouts[answer], reply_markup=keyboard_yes_go_buy(int(call.data.split('-')[1])))
        
        
        
           
@bot.message_handler(commands=['start'])
def get_text_messages(message):
    print(message.chat.id)
    print(message)
    if message.chat.id not in bot_users:
        if '/start' in message.text:
            ref_code = 0
            if 'ref' in message.text:
                ref_code = message.text.split(' ')[1].replace('ref', '')
                print(ref_code)
            data_created = _db.create_user(message.from_user.id, message.from_user.username, ref_code)
            _db.add_ref_for_user(ref_code)
            text = new_user_1 if data_created else last_user_1
            bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, 'С возвращением в меню', reply_markup=keyboard_menu())

 
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == keyboard_menu_1:
        bot.send_message(message.chat.id, text_about, reply_markup=keyboard_sphere())
        # bot.register_next_step_handler(message, __sphere)
    
    if message.text == keyboard_menu_2:
        bot.send_message(message.chat.id, text_about, reply_markup=keyboard_abount())
    
    if message.text == keyboard_menu_3:
        user =_db.get_all_info(message.chat.id)
        print(user)
        if bool(user['payabled']):
            total_sup = 1000
            bot.send_message(message.chat.id, 
                            referal_info.format(
                                tgid = message.chat.id, 
                                count_ref= user['count_refferal'], 
                                count_ref_pay =  user['count_payable_refferal'],
                                balance = user['count_payable_refferal']*total_sup), 
                            reply_markup=key_board_share_for_frends(message.chat.id))
        else:
            bot.send_message(message.chat.id, text_take_money)
            

def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
   webAppTest = types.WebAppInfo("https://telegram.mihailgok.ru") #создаем webappinfo - формат хранения url
   one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest) #создаем кнопку типа webapp
   keyboard.add(one_butt) #добавляем кнопки в клавиатуру

   return keyboard #возвращаем клавиатуру





def start():

    print('Бот запущен')
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except:
            pass
start()
