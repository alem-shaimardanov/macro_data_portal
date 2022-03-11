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

        '''
        Before:
        1. Insert 'otchet o post...' to 'posts' table. Return its post_id.
        2. Insert 'feb 2022' to 'comments_data' table. Return its comment_id.
        3. Insert into 'comments_tree' (idAncestor, idDescendant, idNearestAncestor, commentLevel, post_id)
            values (comment_id, comment_id, 0, 0, post_id).
        
        Logic:
        1. if main key found (v_tom_chisle not in item_name and v_tom_chisle_gen1 == False and v_tom_chisle_gen2 == False):
            
        2. elif 
        '''


        
except:
    con.rollback()
# -----------------------------------------------





# Save (commit) the changes
con.commit()

# Close the connection
con.close()
