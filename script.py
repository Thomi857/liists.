import sqlite3 

#define connection and cursor

connetion = sqlite3.connect('mydatabase.db')

cursor = connetion.cursor()
# create user table
command1 = '''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, password TEXT)'''

cursor.execute(command1)

#create purchase table
command2 = '''CREATE TABLE IF NOT EXISTS purchases (purchase_id INTEGER PRIMARY KEY, user_id INTEGER, item TEXT, price REAL, FOREIGN KEY(user_id) REFERENCES users(user_id))'''

cursor.execute(command2)

# insert data into user table

cursor.execute("INSERT INTO users (username, password) VALUES ('john_zenen', 'password123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('chossen_one', 'securepass456')")

# insert data into purchase table
cursor.execute("INSERT INTO purchases (user_id, item, price) VALUES (1, 'Laptop', 999.99)")
cursor.execute("INSERT INTO purchases (user_id, item, price) VALUES (1, 'Headphones', 199.99)")
cursor.execute("INSERT INTO purchases (user_id, item, price) VALUES (2, 'Smartphone', 799.99)")

# get all purchases for a specific user
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)