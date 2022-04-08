import json
import sqlite3
import insert_in_closure_table

indicator_name_1 = "GNPCA"
indicator_name_2 = "CPIFABSL"
source_name = "FRED"
indicator_names_list = [indicator_name_1, indicator_name_2]

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# -----------------------------------------------
# Read loaded json file
json_file = open(indicator_name_1 + '.json')

# Return json object as a dictionary
json_object = json.load(json_file)

observations = json_object["observations"]

try:
    ####### Pre-work ##########
    # Check whether source_name has been inserted into 'sources' table
    cur.execute("SELECT COUNT(1) FROM sources WHERE name='" + source_name + "'")
    records = cur.fetchall()
    print('SELECT query finished')

    source_id = 0
    if records[0][0] == 0:
        
        cur.execute("INSERT INTO sources (name) values ('" + source_name + "')")
        # Retrieve the source id of a newly created source
        cur.execute("SELECT source_id from sources WHERE name='" + source_name + "'")
        records = cur.fetchone()

        source_id = records[0]
        print("Source id: ", source_id)
    else:
        cur.execute("SELECT source_id from sources WHERE name='" + source_name + "'")
        records = cur.fetchone()
        source_id = records[0]
        print("source id: ", source_id)
    con.commit()

    print("Inserting post...")
    # Insert indicator_name into 'posts' table and retrieve the post_id
    post_id = insert_in_closure_table.create_post(indicator_name_1, source_id)
    print("Post id: ", post_id)

    for observation in observations:
        # print("Observation: ", observation, " ; Type: ", type(observation))
        local_date = observation["date"]
        local_value = observation["value"]
        print("Date: ", local_date, " ; Type of date: ", type(local_date), " . Value: ", local_value, " ; Type of value: ", type(local_value))

        # Insert month into 'comments_data' table and 'comments_tree' table. Retreive comment_id.
        comment_id = insert_in_closure_table.add_comment(post_id=str(post_id), comment_content=local_date, comment_sum=local_value)

    

except:
    print("ERROR")
    con.rollback()
# -----------------------------------------------



# Save (commit) the changes
con.commit()

# Close the connection
con.close()