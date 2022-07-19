import sqlite3

connect = sqlite3.connect('items.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS items(
    item_code INTEGER PRIMARY KEY,
    item_name TEXT,
    item_price REAL
)
""")
connect.commit()

def items_add(code, name, price):
    items_list = [code, name, price]
    cursor.execute("INSERT INTO items VALUES(?, ?, ?);", items_list)
    connect.commit()


options = [
    {
        'code':0,
        'name':'Buy',
    },
    {
        'code':1,
        'name':'Add Items',
    },
]

print('Welcome to Python Venting Machine!')

print('-' * 34)

print('Select the option:')

for i in options:
    print(f"Option Name: {i['name']} - Code: {i['code']}")

print('-' * 34)

query = int(input("Enter the code number of the option you want to get: "))

for i in options:
    if query == i['code']:
        option = i
        print(f"Great, you select: {i['name']}")
        print('-' * 34)
    pass

