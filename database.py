import sqlite3

# Connect to database or create it if it doesn't exist
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_coins (
        user_id INTEGER PRIMARY KEY,
        coins TEXT
        )
    ''')

# Command to add cryptocoin
def addUserList(user_id, name):
    cursor.execute('SELECT coins FROM user_coins WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    if result is None:
        coins = []
    else:
        coins = result[0].split(',') # Convert string to list
    
    if len(coins) < 5:
        coins.append(name)
        cursor.execute('REPLACE INTO user_coins (user_id, coins) VALUES (?, ?)',
                       (user_id, ','.join(coins))) # Convert list back to string
        conn.commit()
        return f"Name '{name}' added."
    else:
        return "You can only store up to 5 coins at once"
    
# Command to retrieve list of coins
def getUserList(user_id):
    cursor.execute('SELECT coins FROM user_coins WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    
    if result is None: 
        return []
    return result[0].split(',')