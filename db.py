import sqlite3


def init_db():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id TEXT PRIMARY KEY,
            account_id TEXT,
            amount REAL,
            date TEXT,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_transaction(transaction):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (id, account_id, amount, date, category)
        VALUES (?, ?, ?, ?, ?)
    ''', (transaction['transaction_id'], transaction['account_id'], transaction['amount'], transaction['date'], ', '.join(transaction['category'])))
    conn.commit()
    conn.close()

def get_transactions():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    return transactions

init_db()
