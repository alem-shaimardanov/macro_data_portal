import json
import sqlite3
import csv

# Save the name of the database
db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# Save name of period
month_names_list = ["1 МАЯ 2019 ГОДА", "1 ФЕВРАЛЯ 2022 ГОДА", "1 АВГУСТА 2021 ГОДА"]

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
        WHERE tableTree.idAncestor = tableTree.idDescendant and tableData.period_id = 3''')
records = cur.fetchall()

# print("Type of records: ", type(records))
# # print("Values: ",records)

# Create a CSV file where data will be stored
csv_file_name = month_names_list[2] + '.csv'

# Create variable to store head row of CSV
fields = ["Индикатор", "Сумма"]

# writing to csv file 
with open(csv_file_name, 'w') as csvfile:
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 

        # writing the fields 
        csvwriter.writerow(fields)
        
#     # writing the data rows 
#     csvwriter.writerows(rows)

        for record in records:
                current_row_list = [record[1], record[7]]
                csvwriter.writerow(current_row_list) 

# for record in records:
#         line_indent = 4*record[5]
#         print(line_indent*" ", record[1], " - ", record[7])
#         # print("comLevel: ", record[5], " ; comSum: ", record[7])
