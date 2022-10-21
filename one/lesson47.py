# https://sqlitestudio.pl/
import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()


mai = 'grhy@jyu'
# cursor.execute("SELECT * FROM users WHERE email = ?", (mai,))
# cursor.execute("SELECT * FROM users WHERE email = ?", [mai])
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (mai, 'khi'))
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': mai, 'name': 'khi'})
# ff = cursor.fetchone()

cursor.execute("SELECT * FROM users")
ff = cursor.fetchall()


print(ff)


db.close()