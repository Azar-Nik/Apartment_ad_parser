import sqlite3


def main():
    conn = sqlite3.connect('db\\realty.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE chat_id (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER
        )
    ''')
    conn.close()


if __name__ == '__main__':
    main()