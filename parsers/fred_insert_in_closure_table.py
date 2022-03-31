import json
import sqlite3
import insert_in_closure_table

indicator_name_1 = "GNPCA"
indicator_name_2 = "CPIFABSL"

indicator_names_list = [indicator_name_1, indicator_name_2]

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# -----------------------------------------------
# Read loaded json file
json_file = open(indicator_name_2 + '.json')

# Return json object as a dictionary
json_object = json.load(json_file)

observations = json_object["observations"]

try:
    ####### Pre-work ##########
    # Insert indicator_name into 'posts' table and retrieve the post_id
    post_id = insert_in_closure_table.create_post(indicator_name_2)


    for observation in observations:
        # print("Observation: ", observation, " ; Type: ", type(observation))
        local_date = observation["date"]
        local_value = observation["value"]
        print("Date: ", local_date, " ; Type of date: ", type(local_date), " . Value: ", local_value, " ; Type of value: ", type(local_value))

        # Insert month into 'comments_data' table and 'comments_tree' table. Retreive comment_id.
        comment_id = insert_in_closure_table.add_comment(post_id=str(post_id), content=local_date, comment_sum=local_value)

    

except:
    print("ERROR")
    con.rollback()
# -----------------------------------------------



# Save (commit) the changes
con.commit()

# Close the connection
con.close()