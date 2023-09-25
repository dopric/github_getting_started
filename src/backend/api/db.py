import sqlite3

db = sqlite3.connect('../mydb.sqlite')
# cursor = db.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS TODOS(id INTEGER PRIMARY KEY, title TEXT, description TEXT, done INTEGER)''')

# insert_query = '''insert into TODOS(id, title, description, done) values(1, "Testing", "This is a test", 0)'''

# cursor.execute(insert_query)
# db.commit()
# print("values inserted")

# cursor.close()