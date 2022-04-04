import pandas as pd
import sqlite3

# Save the name of the database
db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

# indicator_name
indicator_name = "ОТЧЕТ О ПОСТУПЛЕНИЯХ И ИСПОЛЬЗОВАНИИ НАЦИОНАЛЬНОГО ФОНДА РЕСПУБЛИКИ КАЗАХСТАН"

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
        WHERE tableTree.idAncestor = tableTree.idDescendant and tableData.period_id = 1''')
records = cur.fetchall()

# Create an empty list which will store values of the Select query from above
fetched_indicator_values = []


# Function to set names to cells based on their level
def fill_out_entry(level, name, value):
    visited_cells = [False, False, False]
    entry = ["", "", "", ""]
    entry[level] = name
    visited_cells[level] = True
    # Cell in 3rd row contains the value
    entry[3] = value

    for i, cell in enumerate(visited_cells):
        if cell == False:
            entry[i] = ""
    
    return entry


# Loop through records that were received from the Select query from above
for record in records:
        current_row_list = [record[1], record[7]]
        # print('Name: ', record[1], ', Value: ', record[7])
        level = record[5]
        name = record[1]
        value = record[7]

        # Create a list which is filled out with names based on their level
        entry = fill_out_entry(level, name, value)

        # Append the list to the dataframe
        fetched_indicator_values.append(entry)

# print("List: ", fetched_indicator_values)

# Save the dataframe in Excel file
pd.DataFrame(fetched_indicator_values).to_excel('test_excel.xlsx', header=False, index=False)

# for record in records:
#         line_indent = 4*record[5]
#         print(line_indent*" ", record[1], " - ", record[7])
#         # print("comLevel: ", record[5], " ; comSum: ", record[7])
