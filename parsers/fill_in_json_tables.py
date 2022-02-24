# from asyncio.windows_events import NULL
import json
import sqlite3
from datetime import date

# Indicator name
indicator_name = "индекс реальных денежных доходов"

# Create a dict to match source names to their source ids
source_names = {"Taldau": 1, "MinFin": 2, "FRED": 3} # use SQL query !!!
current_source_name = "Taldau"
current_term_name = "Регионы"
value_id = '1'
termName_term_id = '1'

# Save today's date
date_today = date.today()

# This function is used to update primary key of taldau_values table
def increment_id(value_id_str): # NO NEED for the func, use automatic ids insertion !!!
    value_id_int = int(value_id_str)
    value_id_int += 1
    value_id_str = str(value_id_int)
    return value_id_str

############# CODE TO WRITE INTO SQLITE TABLE #################
current_dir = "/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers"
db_file = current_dir + '/taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# Read loaded json file
json_file = open(indicator_name + '.json')

# Return json object as a dictionary
json_object = json.load(json_file)

print("Size of json: ", len(json_object))
# Iterate through the json list:
i = 0
for item in json_object:
    if i < 1:
        cur_period_list = item['periods']
        for elem in cur_period_list:
            elem_name = elem["name"]
            elem_date = elem["date"]
            elem_value_string = elem["value"]
            elem_value_long = 0.0
            if elem_value_string == "": # use regular expressions
                elem_value_string = None
                elem_value_long = None
            else:
                elem_value_long = float(elem_value_string)
                
            print("Name: ", elem_name, ", Date: ", elem_date, ", Value: ", elem_value_string)

            # Insert 'value_id', 'termName_term_id', 'name', 'date', 'value_string', 'value_long', 'date_created'
            cur.execute("INSERT INTO taldau_values (termName_term_id, name, date, value_string, value_long, date_created) VALUES('" + termName_term_id + "','" + elem_name + \
            "','" + elem_date +  "','" + elem_value_string + "','" + str(elem_value_long) + "','" + str(date_today) + "')")
            
            # Increment value_id
            value_id = increment_id(value_id)

    i += 1


# # Save (commit) the changes
con.commit()

# try:
# 
#   con.commit()
# except:
#   con.rollback()

# Close the cursor
con.close()