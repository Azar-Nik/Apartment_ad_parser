import sqlite3


def main():
    conn = sqlite3.connect('realty.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            offer_id INTEGER
        )
    ''')
    conn.close()


if __name__ == '__main__':
    main()