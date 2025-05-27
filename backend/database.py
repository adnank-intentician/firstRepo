import sqlite3

DATABASE="fruits.db"
def init_db():
    connection = sqlite3.connect(DATABASE)

    c = connection.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS fruit_clicks(
            fruit TEXT PRIMARY KEY,
            count INTEGER DEFAULT 0)
    ''')

    for fruit in ['apple','banana','orange','mango']:
        c.execute("INSERT OR IGNORE INTO fruit_clicks (fruit, count) VALUES (?,0)",(fruit,))
    connection.commit()
    connection.close()

    