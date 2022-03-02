import sqlite3

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

cur.execute("select * from term_item_groups order by term_item_group_id desc limit 1")
records = cur.fetchall()

print("Print result of SELECT:")
print(records)
print("------------------------")
print(type(records))
con.close()
