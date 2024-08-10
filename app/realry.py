import sqlite3
import requests
from config import token, chat_id


def format_text(offer):
    text = f"<a href='{offer['url']}'>{offer['price']} руб</a>"
    return text

def send_telegram(offer):
    text = format_text(offer)
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    
    respons = requests.post(url=url, data={'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'})
    print(respons)


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


def main():
    offer = {'price': 123, 'url': 'https://translate.yandex.ru/'}
    send_telegram(offer)


if __name__ == '__main__':
    main()