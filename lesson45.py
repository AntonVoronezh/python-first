# https://sqlitestudio.pl/
import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXIST users (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# email TEXT NOT NULL UNIQUE
# )
# ''')

# cursor.execute("INSERT INTO users (name, email) VALUES ('Иванов', 'grhy@jyu')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Петров', 'kvhilgul@jyu')")

# cursor.executescript('''
# INSERT INTO users (name, email) VALUES ('khi', 'ukh@jyu');
# INSERT INTO users (name, email) VALUES ('ukgiul', 'uiyiugiy@jyu');
# ''')
users = [('us1', 'usfkfl@lh;h;'), ('us2', 'yutudt@kkk')]
cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

db.commit()


db.close()