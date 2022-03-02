import re
import json
import sqlite3
from datetime import date

# Indicator name
indicator_name = "индекс реальных денежных доходов"

current_source_name = "Taldau"
current_source_name_id = "1"
current_term_category_name = "Регионы"
current_term_category_group_id = "1"
current_term_category_id = "1"
term_item_group_ids_list = [0]
current_indicator_id = "1"
current_period_id = "1"
current_period_name = "Год"

value_id = '1'
termName_term_id = '1'


# Save today's date
date_today = date.today()

# Regular Expression to check if value is of type double
'''
-23.456
1. check if there is either a dot or comma
2. check if there is a negative sign in front of number
'''
regnumber = re.compile(r'^([-])?\d+(?:[,.]\d*)?$')


############# CODE TO WRITE INTO SQLITE TABLE #################
# current_dir = "/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers"
db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)



# Create a cursor
cur = con.cursor()

# # Use term_name to get termName_id from 'termNames' table
# cur.execute("SELECT termName_id FROM termNames WHERE termName = '" + current_term_category_name + "'")

# # Fetch the result of the above query
# records = cur.fetchall()

# print("Retrieved termName_id: ")
# print(records[0][0])
# print("Type: ", type(records[0][0]))

# termName_id = records[0][0]


# Use indicator_name to get indicator_id from 'indicators_main' table
cur.execute("SELECT indicator_id FROM indicators_main WHERE indicator_name = '" + indicator_name + "'")
records = cur.fetchall()

indicator_id = records[0][0]


# Use period_name to get period_id from 'periods' table
cur.execute("SELECT period_id FROM periods WHERE period_name = '" + current_period_name + "'")
records = cur.fetchall()

# ORM - object relational mapping like SQL Alchemy
# #periods
#     .filter(period_name=123)
#     .select(period_id)

period_id = records[0][0]

# Use indicator_id and period_id to get 'indic_period_id' from 'indicator_period_combo' table
cur.execute("SELECT indic_period_id FROM indicator_period_combo WHERE indicator_id = " + str(indicator_id) \
    + " AND period_id = " + str(period_id))
records = cur.fetchall()

print("Retrieved indic_period_id: ")
print(records[0][0])
print("Type: ", type(records[0][0]))

indic_period_id = records[0][0]


# # Use indic_period_id and termName_id to get termName_term_id from 'termNames_combo' table
# cur.execute("SELECT termName_term_id FROM termNames_combo WHERE indic_period_id = " + str(indic_period_id) \
#     + " AND termName_id = " + str(termName_id))
# records = cur.fetchall()

# print("Retrieved termName_term_id: ")
# print(records[0][0])
# print("Type: ", type(records[0][0]))

# termName_term_id = records[0][0]



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
        if i < 1:
            cur_term_items_list = item['termNames']
            term_item_group_id = "0"
            ### CHECK IF term_item_group_id EXISTS. if exists, save it; if not, then set term_item_group_id = "1"
            cur.execute("SELECT * FROM term_item_groups ORDER BY term_item_group_id DESC LIMIT 1")
            records = cur.fetchall()
            if len(records) == 0:
                # term_item_group_id = "1"
                pass
            else:
                term_item_group_id = str(records[0][2])
            
            term_item_group_id_iterator = 0

            for term_item_name in cur_term_items_list:
                # Check if term_item_name is already in the table 'term_item_names'
                cur.execute("SELECT COUNT(1) FROM term_item_names WHERE term_item_name='" + term_item_name + "')")
                records = cur.fetchall()
                term_group_id = "0"

                # If term_item_name is not in the table
                if records[0][0] == 0:

                    # Insert term_item_name into 'term_item_names' table
                    cur.execute("INSERT INTO term_item_names (term_item_name) VALUES ('" + term_item_name + "')")
                
                if term_item_group_id_iterator % 2 == 0:
                    term_item_group_id_integer = int(term_item_group_id)
                    term_item_group_id_integer += 1
                    term_item_group_id = str(term_item_group_id_integer)
                else:
                    pass
                
                # Fetch 'term_item_name_id' from 'term_item_names' table
                cur.execute("SELECT term_item_name_id FROM term_item_names where term_item_name='" + term_item_name + "')")
                records = cur.fetchall()
                term_item_id = records[0][0]
                
            
            # Insert 'term_category_group_id', 'term_item_group_id', 'term_item_id' into 'term_item_groups' table
            cur.execute("INSERT INTO term_item_groups (term_category_group_id, term_item_group_id, term_item_id) VALUES ('" +
            "','" +  current_term_category_group_id + "','"  + term_item_group_id + "','" + term_item_id + "')")
            
            # Insert 'term_item_group_id', 'indic_period_id' into 'term_item_group_indic_periods' table

            
            cur_period_list = item['periods']
            for elem in cur_period_list:
                elem_name = elem["name"]
                elem_date = elem["date"]
                elem_value_string = elem["value"].replace(',','.') # replace all commas with dots
                elem_value_long = 0.0
                if elem_value_string == "" or not regnumber.match(elem_value_string): # use regular expressions
                    elem_value_string = "NULL"
                    elem_value_long = "NULL"
                else:
                    elem_value_long = float(elem_value_string)
                    
                print("Name: ", elem_name, ", Date: ", elem_date, ", Value: ", elem_value_string)

                # Insert 'value_id', 'termName_term_id', 'name', 'date', 'value_string', 'value_long', 'date_created'
                cur.execute("INSERT INTO taldau_values (termName_term_id, name, date, value_string, value_long, date_created) VALUES('" + str(termName_term_id) + "','" + elem_name + \
                "','" + elem_date +  "','" + elem_value_string + "','" + str(elem_value_long) + "','" + str(date_today) + "')")
                
                

        i += 1
except:
    con.rollback()
# -----------------------------------------------

# # Save (commit) the changes
con.commit()



# try:
# 
#   con.commit()
# except:
#   con.rollback()

# Close the cursor
con.close()