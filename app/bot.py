import telebot
import time
import threading
from config import token
import cian, yandex, avito
import sqlite3


API_TOKEN = token
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.chat.id)
    with sqlite3.connect('db\\realty.db') as conn:
        cursor = conn.cursor()
        new_chat_id = message.chat.id
        cursor.execute(
                    '''SELECT chat_id
                    FROM chat_id
                    WHERE chat_id = (?)''', (new_chat_id,)
                    )
        result = cursor.fetchone()
        if result is None:
            cursor.execute("""
                        INSERT INTO  chat_id (chat_id)
                        VALUES (?)
                        """, (new_chat_id,)
                        )
            conn.commit()
            bot.send_message(message.chat.id, "Привет! Вы подписаны на обновления.")


def send_updates(data):
    with sqlite3.connect('db\\realty.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT chat_id FROM chat_id
                    """)
        user_chat_ids = cursor.fetchall()
        for chat_id in user_chat_ids:
            try:
                bot.send_message(chat_id[0], data)
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {chat_id}: {e}")


def send_telegram(offer):
    text = f"{offer['url']}\n{offer['offer_date']}"
    send_updates(text)


def check_database(offer):
    offer_id = offer["offer_id"]
    with sqlite3.connect('db\\realty.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT offer_id FROM offers WHERE offer_id = (?)
                    """, (offer_id, )
                    )
        result = cursor.fetchone()
        if result is None:
            send_telegram(offer)
            cursor.execute("""
                        INSERT INTO offers 
                        VALUES (NULL, :offer_id)
                        """, offer
                        )
            conn.commit()
            print('Добавлено')


def run_parser():
    while True:
        for line in cian.main():
            check_database(line)
        
        for line in yandex.main():
            check_database(line)
        
        #for line in avito.main():
        #    check_database(line)
        time.sleep(300)

if __name__ == '__main__':
    # Запускаем парсер в отдельном потоке
    parser_thread = threading.Thread(target=run_parser, daemon=True)
    parser_thread.start()
    
    # Запускаем бот
    bot.polling(none_stop=True)