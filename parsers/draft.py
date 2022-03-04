import sqlite3

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

cur.execute("select idAncestor, commentLevel from comments_tree where idDescendant=1")
records = cur.fetchall()

print("Print result of SELECT:")
print(records)
print("------------------------")
print(type(records))

print("Printing loop:")
for elem in records:
    print("idAncestor: ", elem[0], "; CommentLevel: ", elem[1])
    
con.close()
