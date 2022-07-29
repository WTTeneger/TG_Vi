from typing import List
# from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from text import *


"""[Клавиатуры вариации ответов]"""

def go_back_in_menu():
    keyboard = [InlineKeyboardButton('В меню', callback_data='go_back_in_menu')],
    return InlineKeyboardMarkup(keyboard)

def keyboard_down_message():
    keyboard = [[InlineKeyboardButton('Menu 1', callback_data='m1')],
                [InlineKeyboardButton('Menu 2', callback_data='m2')],
                [InlineKeyboardButton('Menu 3', callback_data='m3')]]
    return InlineKeyboardMarkup(keyboard)


def keyboard_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text=keyboard_menu_1)
    button2 = KeyboardButton(text=keyboard_menu_2)
    button3 = KeyboardButton(text=keyboard_menu_3)
    markup.add(button)
    markup.add(button2)
    markup.add(button3)
    return markup


def keyboard_yes_go_buy(id=1):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Купить', callback_data=f'sphere-{id}'))
    markup.add(InlineKeyboardButton(' ', callback_data=f'1'))
    for vs, el in enumerate([text_about_button1, text_about_button2, text_about_button3, text_about_button4, text_about_button5]):
        # print(vs, el)
        if vs+1 != id:
            markup.add(InlineKeyboardButton(el, callback_data=f'abount-{vs+1}'))


    # if id == 2:
    #     markup.add(InlineKeyboardButton(text_about_button2, callback_data=f'abount-2'))
    # if id == 3:
    #     markup.add(InlineKeyboardButton(text_about_button3, callback_data=f'abount-3'))
    # if id == 4:
    #     markup.add(InlineKeyboardButton(text_about_button4, callback_data=f'abount-4'))
    # if id == 5:
    #     markup.add(InlineKeyboardButton(text_about_button5, callback_data=f'abount-5')) 
    
    
    return markup

def keyboard_yes_ref_add():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(yes, callback_data=f'yes-go-stage-ref'))                
    return markup

def keyboard_yes_no_make_ref():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(yes, callback_data=f'go-stage-create-ref_yes'))                
    markup.add(InlineKeyboardButton(no, callback_data=f'go-stage-create-ref_no'))                
    return markup


def keyboard_yes_no_make_ref_20TH():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(yes, callback_data=f'go-stage-create-ref-20TH_yes'), InlineKeyboardButton(no, callback_data=f'go-stage-create-ref-20TH_no'))                
    # markup.add(InlineKeyboardButton(no, callback_data=f'go-stage-create-ref-20TH_no'))                
    return markup

def keyboard_yes_no_make_ref_23TH():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(yes, callback_data=f'go-stage-create-ref-23TH_yes')) 
    markup.add(InlineKeyboardButton(later, callback_data=f'go-stage-create-ref-23TH_no'))                
    return markup

def keyboard_sphere():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text_about_button1, callback_data=f'sphere-1'))
    markup.add(InlineKeyboardButton(text_about_button2, callback_data=f'sphere-2'))
    markup.add(InlineKeyboardButton(text_about_button3, callback_data=f'sphere-3'))
    markup.add(InlineKeyboardButton(text_about_button4, callback_data=f'sphere-4'))
    markup.add(InlineKeyboardButton(text_about_button5, callback_data=f'sphere-5'))
                
    return markup

def keyboard_payable():
    keyboard = [InlineKeyboardButton(button_payments_1, callback_data=f'button-payments-1'),
                InlineKeyboardButton(button_payments_2, callback_data=f'button-payments-2'),
                ],
    return InlineKeyboardMarkup(keyboard)

def but_access_ref():
    keyboard = [InlineKeyboardButton(but_access_ref_yes, callback_data=f'but-access-ref_yes'),
                InlineKeyboardButton(but_access_ref_no, callback_data=f'but-access-ref_no'),
                ],
    return InlineKeyboardMarkup(keyboard)

def keyboard_disabled():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text=keyboard_disabled_1)
    markup.add(button)
    return markup

def key_board_admin_access(tgid):
    keyboard = [InlineKeyboardButton(key_board_admin_access_1, callback_data=f'admin_access-yes-{tgid}'),
                InlineKeyboardButton(key_board_admin_access_2, callback_data=f'admin_access-no-{tgid}')],
    return InlineKeyboardMarkup(keyboard)


def key_board_user_payable():
    keyboard = [InlineKeyboardButton('Оплатила', callback_data='user_yes')],
    return InlineKeyboardMarkup(keyboard)


def key_board_share_for_frends(id):
    _url = f'https://t.me/share/url?text=https://t.me/bisnesnytue_bot?start=ref{id}&url=😎👇'
    keyboard = [InlineKeyboardButton(key_board_share_for_frends_1, url=_url)],
    return InlineKeyboardMarkup(keyboard)

def key_board_share_for_frends_and_help(id):
    _url = f'https://t.me/share/url?text=https://t.me/bisnesnytue_bot?start=ref{id}&url=😎👇'
    _help = f'https://t.me/WT_Tini'
    markup = InlineKeyboardMarkup()
    
    markup.add(InlineKeyboardButton(key_board_share_for_frends_1, url=_url))
    markup.add(InlineKeyboardButton('Чат с поддержкой', url=_help))
    return markup

def keyboard_abount():
    markup = InlineKeyboardMarkup()
    
    markup.add(InlineKeyboardButton(text_about_button1, callback_data=f'abount-1'))
    markup.add(InlineKeyboardButton(text_about_button2, callback_data=f'abount-2'))
    markup.add(InlineKeyboardButton(text_about_button3, callback_data=f'abount-3'))
    markup.add(InlineKeyboardButton(text_about_button4, callback_data=f'abount-4'))
    markup.add(InlineKeyboardButton(text_about_button5, callback_data=f'abount-5'))                
    return markup

# def key_board_share_for_frends():
#     keyboard = [InlineKeyboardButton('key_board_share_for_frends_1')]#, pay=True, callback_data='')]# send='https://t.me/bisnesnytue_bot?start=ref1vQmP4')]
#     return InlineKeyboardMarkup(keyboard)
#Amal best of the best man in the all world