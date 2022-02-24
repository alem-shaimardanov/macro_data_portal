import re
import json
import sqlite3
from datetime import date

# Indicator name
indicator_name = "индекс реальных денежных доходов"

# Create a dict to match source names to their source ids
source_names = {"Taldau": 1, "MinFin": 2, "FRED": 3} # use SQL query !!!
current_source_name = "Taldau"
current_term_name = "Регионы"
current_period_name = "Год"

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

# Regular Expression to check if value is of type double
'''
-23.456
1. check if there is either a dot or comma
2. check if there is a negative sign in front of number
'''
regnumber = re.compile(r'^([-])?\d+(?:[,.]\d*)?$')


############# CODE TO WRITE INTO SQLITE TABLE #################
current_dir = "/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers"
db_file = current_dir + '/taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

try:

    # Create a cursor
    cur = con.cursor()

    # Use term_name to get termName_id from 'termNames' table
    cur.execute("SELECT termName_id FROM termNames WHERE termName = '" + current_term_name + "'")

    # Fetch the result of the above query
    records = cur.fetchall()

    print("Retrieved termName_id: ")
    print(records[0][0])
    print("Type: ", type(records[0][0]))

    termName_id = records[0][0]


    # Use indicator_name to get indicator_id from 'indicators_main' table
    cur.execute("SELECT indicator_id FROM indicators_main WHERE indicator_name = '" + indicator_name + "'")
    records = cur.fetchall()

    indicator_id = records[0][0]


    # Use period_name to get period_id from 'periods' table
    cur.execute("SELECT period_id FROM periods WHERE period_name = '" + current_period_name + "'")
    records = cur.fetchall()

    period_id = records[0][0]

    # Use indicator_id and period_id to get 'indic_period_id' from 'indicator_period_combo' table
    cur.execute("SELECT indic_period_id FROM indicator_period_combo WHERE indicator_id = " + str(indicator_id) \
        + " AND period_id = " + str(period_id))
    records = cur.fetchall()

    print("Retrieved indic_period_id: ")
    print(records[0][0])
    print("Type: ", type(records[0][0]))

    indic_period_id = records[0][0]


    # Use indic_period_id and termName_id to get termName_term_id from 'termNames_combo' table
    cur.execute("SELECT termName_term_id FROM termNames_combo WHERE indic_period_id = " + str(indic_period_id) \
        + " AND termName_id = " + str(termName_id))
    records = cur.fetchall()

    print("Retrieved termName_term_id: ")
    print(records[0][0])
    print("Type: ", type(records[0][0]))

    termName_term_id = records[0][0]

    # -----------------------------------------------
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
                
                # Increment value_id
                value_id = increment_id(value_id)

        i += 1
    # -----------------------------------------------

    # # Save (commit) the changes
    con.commit()

except:
    con.rollback()

# try:
# 
#   con.commit()
# except:
#   con.rollback()

# Close the cursor
con.close()