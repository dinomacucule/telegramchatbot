import telebot
from telebot import custom_filters
import time
from requests import get
import json
from datetime import datetime
from configparser import ConfigParser
import csv
import os
import ast

#credentials
path = os.path.dirname(__file__)
config = ConfigParser()

config.read(os.path.join(path, "config.ini"))
tg_token = config["credentials"]["TELEGRAM_TOKEN"]
API_KEY = "AF4b9R9XUsa8zOH6v9m0YuTkJOpqcLUr27f8OFoSvNu2RcsaiEN7NiqkitPR8OkZ"

#connectios
bot = telebot.TeleBot(tg_token)

#helpers
started = 0

'''
def create_table():
    try:
        with open(os.path.join(path, "cadastrados.csv"), "w", encoding="utf-8") as chat:
            fields = ["usuario", "nivel"]
            writer = csv.DictWriter(chat, fieldnames = fields)
            writer.writeheader()

def insert_user(usuario)
    exist = False
    with open(os.path.join(path, "cadastrados.csv"), "r", encoding="utf-8") as users:
        old_table = csv.DictReader(users)
        
        for row in old_table:
            if usuario["usuario"] == row["usuario"]:
                exist = True
    with open(os.path.join(path, "cadastrados.csv"), "a", encoding="utf-8") as users:
        if not exist:
            writer = csv.DictWriter(users, fieldnames = usuario)
            writer.writerow(usuario)
    if exist == True:
        old = []
        with open(os.path.join(path, "cadastrados.csv"), "r", encoding="utf-8") as users:
            old_table = csv.DictReader(users)
            create_table()
            
            for row in old_table:
                old.append(row)
'''

@bot.message_handler(commands=['start']) #first command
def admin_reply(message):
    global started
    
    welcome_msg = """
    Olá, 👋 Meus parabéns🎉

Você está muito perto de ter acesso totalmente grátis a todos meus robôs de sinais VIP’s totalmente de graça e ainda concorrer a um sorteio de um Iphone 📲

Para ter acesso aos Robôs é necessário fazer o cadastro na plataforma através desse link que vou deixar aqui abaixo👇

faz o cadastro e mande “ok” 👇
    """
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Cadastrar', url ='https://18kbet.online/player-from-agent/agent/167j6'))
    bot.send_message(message.chat.id, welcome_msg, reply_markup = keyboard, parse_mode = "HTML")
    started = 1
    
@bot.callback_query_handler(func=lambda call: True) #add  token command
def callback_query(call):
    if (call.data.startswith("https://18kbet")):
        bot.answer_callback_query(call.id, "https://18kbet.online/player-from-agent/agent/167j6", show_alert=True)

@bot.message_handler(content_types = ["text"])
def final_add(message):

    try:
        global started

        msg = """
        Maravilha👏 

    🚨 LEIA COM ATENÇÃO AGORA 🚨

    Agora eu preciso que você deposite pelo menos o mínimo que é R$50 reais para poder pegar os sinais do robô 🤖 

    Assim que depositar me envia aqui algum print ou algo do tipo, que após isso eu vou liberar o robô gratuito 

    Observação 👇

    👉 1°PASSO: Mande a FOTO que comprovante do seu depósito 

    👉 2ºPASSO: E mande uma mensagem abaixo com a palavra "PRONTO"
        """
        if (message.text.lower() == "pronto" or message.text.lower() == "ok") and started == 1:
            bot.send_message(message.chat.id, msg, parse_mode = "HTML")
            started = 2
        elif (message.text.lower() == "pronto" or message.text.lower() == "ok") and started == 2:
            msg = """
            Tudo pronto ✅

    Agora clique nesse botão abaixo para acessar o Robô do Spaceman 🤖 👇🏻

    Após acessar envie um Ok para liberar as demais salas de sinais

            """
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton('SPACEMAN', url ='https://t.me/+0qv1_7Xc-XlmMTA5'))
            bot.send_message(message.chat.id, msg, parse_mode = "HTML", reply_markup = keyboard)
            started = 3
        elif (message.text.lower() == "pronto" or message.text.lower() == "ok") and started == 3:
            msg = """
            Agora que você já tem acesso a 1 ROBÔ 
      Que tal ter acesso a vários robôs de sinais secretos?

      Para conseguir é muito simples 
      Copia este link abaixo e envie para 10 amigos 👇🏻 

      Com esse link seus amigos também terão acesso aos robôs e vocês poderão pegar os sinais juntos 💸💸💸
      https://t.me/nathanbarbosa_bots

      Feito isso me envia “PRONTO”
            """
            bot.send_message(message.chat.id, msg, parse_mode = "HTML")
            started = 4
        elif (message.text.lower() == "pronto" or message.text.lower() == "ok") and started == 4:
            
            msg = """
            Tudo pronto ✅

    Agora clique nesse botão abaixo para acessar o Robô 🤖 👇🏻
    Após acessar os 2 envie um Ok

            """
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton('Robo Roleta', url ='https://t.me/+zyO3yWGxXhRkNDgx'))
            keyboard.add(telebot.types.InlineKeyboardButton('Sala Secreta', url ='https://t.me/+c6Nrwdqu3_Q5YTBh'))
            bot.send_message(message.chat.id, msg, parse_mode = "HTML", reply_markup = keyboard)
            
            started = 5
        elif (message.text.lower() == "pronto" or message.text.lower() == "ok") and started == 5:
            video = open(os.path.join(path,'video.mp4'), 'rb')
            msg = """
            Agora voce precisa ficar atento no Canal para nao perder as lives e a unica coisa que te peco em troca e me enviar print dos seus resultados no meu instagram<a href = 'https://instagram.com/nathan.bf9'>@nathan.bf9 🙏</a>
            """
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton('Cadastrar', url ='https://18kbet.online/player-from-agent/agent/167j6'))

            bot.send_message(message.chat.id, msg, parse_mode = "HTML", reply_markup = keyboard)
            #bot.send_video(message.chat.id, video, supports_streaming = True)
            started = 0
        else:
            bot.send_message(message.chat.id, "Erro de entrada. Recomece o procedimento, por favor! /start", parse_mode = "HTML")
    except:
        bot.send_message(message.chat.id, "Erro de entrada. Recomece o procedimento, por favor! /start", parse_mode = "HTML")
bot.add_custom_filter(custom_filters.ChatFilter())
bot.polling(none_stop=True)