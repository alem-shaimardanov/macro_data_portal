import sqlite3

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# Create 'posts' table
cur.execute('''
    create table posts (
    postid integer primary key autoincrement,
    content text,
    dateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

# Save (commit) the changes
con.commit()

# Close the connection
con.close()
