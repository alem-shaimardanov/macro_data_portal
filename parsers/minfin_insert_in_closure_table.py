import sqlite3
import json
indicator_name = "ОТЧЕТ О ПОСТУПЛЕНИЯХ И ИСПОЛЬЗОВАНИИ НАЦИОНАЛЬНОГО ФОНДА РЕСПУБЛИКИ КАЗАХСТАН"
post_id = '1'

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# -----------------------------------------------
# Read loaded json file
json_file = open(indicator_name + '.json')

# Return json object as a dictionary
json_object = json.load(json_file)

print("Size of json: ", len(json_object))
# Iterate through the json list:

try:
    i = 0
    for item in json_object:
        print("Type of item: ", type(item))
        print("ITEM: ", item)

        print("------------------------------------------------------")
        # if i < 1:
        #     cur_term_items_list = item['termNames']
        #     term_item_group_id = "0"
        #     ### CHECK IF term_item_group_id EXISTS. if exists, save it; if not, then set term_item_group_id = "1"
        #     cur.execute("SELECT * FROM term_item_groups ORDER BY term_item_group_id DESC LIMIT 1")
        #     records = cur.fetchall()
        #     if len(records) == 0:
        #         # term_item_group_id = "1"
        #         pass
        #     else:
        #         term_item_group_id = str(records[0][2])
            
        #     term_item_group_id_iterator = 0

        #     for term_item_name in cur_term_items_list:
        #         # Check if term_item_name is already in the table 'term_item_names'
        #         cur.execute("SELECT COUNT(1) FROM term_item_names WHERE term_item_name='" + term_item_name + "')")
        #         records = cur.fetchall()
        #         term_group_id = "0"

        #         # If term_item_name is not in the table
        #         if records[0][0] == 0:

        #             # Insert term_item_name into 'term_item_names' table
        #             cur.execute("INSERT INTO term_item_names (term_item_name) VALUES ('" + term_item_name + "')")
                
        #         if term_item_group_id_iterator % 2 == 0:
        #             term_item_group_id_integer = int(term_item_group_id)
        #             term_item_group_id_integer += 1
        #             term_item_group_id = str(term_item_group_id_integer)
        #         else:
        #             pass
                
        #         # Fetch 'term_item_name_id' from 'term_item_names' table
        #         cur.execute("SELECT term_item_name_id FROM term_item_names where term_item_name='" + term_item_name + "')")
        #         records = cur.fetchall()
        #         term_item_id = records[0][0]
                
            
        #     # Insert 'term_category_group_id', 'term_item_group_id', 'term_item_id' into 'term_item_groups' table
        #     cur.execute("INSERT INTO term_item_groups (term_category_group_id, term_item_group_id, term_item_id) VALUES ('" +
        #     "','" +  current_term_category_group_id + "','"  + term_item_group_id + "','" + term_item_id + "')")
            
        #     # Insert 'term_item_group_id', 'indic_period_id' into 'term_item_group_indic_periods' table

            
        #     cur_period_list = item['periods']
        #     for elem in cur_period_list:
        #         elem_name = elem["name"]
        #         elem_date = elem["date"]
        #         elem_value_string = elem["value"].replace(',','.') # replace all commas with dots
        #         elem_value_long = 0.0
        #         if elem_value_string == "" or not regnumber.match(elem_value_string): # use regular expressions
        #             elem_value_string = "NULL"
        #             elem_value_long = "NULL"
        #         else:
        #             elem_value_long = float(elem_value_string)
                    
        #         print("Name: ", elem_name, ", Date: ", elem_date, ", Value: ", elem_value_string)

        #         # Insert 'value_id', 'termName_term_id', 'name', 'date', 'value_string', 'value_long', 'date_created'
        #         cur.execute("INSERT INTO taldau_values (termName_term_id, name, date, value_string, value_long, date_created) VALUES('" + str(termName_term_id) + "','" + elem_name + \
        #         "','" + elem_date +  "','" + elem_value_string + "','" + str(elem_value_long) + "','" + str(date_today) + "')")
                
                

        # i += 1
except:
    con.rollback()
# -----------------------------------------------





# Save (commit) the changes
con.commit()

# Close the connection
con.close()
