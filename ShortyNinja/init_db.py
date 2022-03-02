import sqlite3

# connects to the database file
conn = sqlite3.connect('database.db')

# initialises the database with the schema in schema.sql
with open('schema.sql') as schema:
    conn.executescript(schema.read())

# commits the changes to the database
conn.commit()
# closes the connection to the database
conn.close()
