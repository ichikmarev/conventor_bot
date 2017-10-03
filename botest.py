import telebot
import requests
import time
import os

T0KEN = '432988684:AAEY6eHEu6qEQeSKvqwU1i9-IBYaR5lIaqw'

bot = telebot.TeleBot(T0KEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Taken')
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('new_file.mp4', 'wb') as new_file:
        new_file.write(downloaded_file)
    videonote = open('new_file.mp4', 'rb')
    #bot.send_video_note(chat_id, videonote)
    #bot.send_video_note('@shlyakov', videonote)
    bot.send_video_note('@PRO16_channel', videonote)

@bot.message_handler(func=lambda message:'21')
def send_qustion(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'JUST SEND ME VIDEO')

bot.polling()
