import sqlite3
import json

import json
import sqlite3
import insert_in_closure_table

indicator_name_1 = "GDP"
indicator_name_2 = "Inflation"
indicator_name_3 = "Currency"

path="/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers/trading_economics/"

indicator_names_list = [indicator_name_1, indicator_name_2, indicator_name_3]
file_names_list = ['world_gdp', "world_inflation", "currency"]
db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# -----------------------------------------------
# Read loaded json file
json_file = open(path + file_names_list[0] + '.json')

# Return json object as a dictionary
json_object = json.load(json_file)

# print("JSON: ")
# print(json_object)
# print("Type of object: ", type(json_object))
# observations = json_object["observations"]

try:
    ####### Pre-work ##########
    # Insert indicator_name into 'posts' table and retrieve the post_id
    post_id = insert_in_closure_table.create_post(indicator_name_1)


    for observation in json_object:
        # ////////////////////////////////
        country_name = observation["country_name"]
        last_value = observation["last_value"]
        reference = observation["reference"]
        units = observation["units"]

        print("Country_name: ", country_name, ". Value: ", last_value, " ; Type of last_value: ", type(last_value), ". Reference: ", reference, " ; Units: ", units)
        # ////////////////////////////////
        
        # Insert month into 'comments_data' table and 'comments_tree' table. Retreive comment_id.
        comment_id = insert_in_closure_table.add_comment(post_id=str(post_id), content=local_date, comment_sum=local_value)

    

except:
    print("ERROR")
    con.rollback()
# -----------------------------------------------



# # Save (commit) the changes
# con.commit()

# # Close the connection
# con.close()