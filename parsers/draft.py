import json
import sqlite3


db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

cur.execute('''
        SELECT tableData.idEntry, 
        tableData.content, 
        tableTree.idAncestor, 
        tableTree.idDescendant, 
        tableTree.idNearestAncestor, 
        tableTree.commentLevel, 
        tableTree.idSubject,
        tableData.comment_sum
        FROM comments_data AS tableData 
        JOIN comments_tree AS tableTree
        ON tableData.idEntry = tableTree.idDescendant 
        WHERE tableData.content = 'Использование, всего:' 
    ''')
records = cur.fetchall()

print("Type of records: ", type(records))
# print("Values: ",records)

for record in records:
    print(record)


# temp_str = "1abcd"
# print(temp_str)
# print(temp_str.strip())