import sqlite3
import json

import insert_in_closure_table

indicator_name_0 = "GDP"
indicator_name_1 = "Inflation"
indicator_name_2 = "Currency"

path="/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers/trading_economics/"

indicator_names_list = [indicator_name_0, indicator_name_1, indicator_name_2]
file_names_list = ['world_gdp', "world_inflation", "currency"]
source_name = "Trading Economics"
db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# -----------------------------------------------


# Specify a choice of indicator that has to be loaded into closure table
choice = 2

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

    if choice == 0:
        # Insert indicator_name into 'posts' table and retrieve the post_id
        post_id = insert_in_closure_table.create_post(indicator_name_0, source_id)

        # Read loaded json file
        json_file = open(path + file_names_list[0] + '.json')

        # Return json object as a dictionary
        json_object = json.load(json_file)

        for observation in json_object:
            # ////////////////////////////////
            country_name = observation["country_name"]
            last_value = observation["last_value"]
            reference = observation["reference"]
            units = observation["units"]

            print("Country_name: ", country_name, ". Value: ", last_value, " ; Type of last_value: ", type(last_value), ". Reference: ", reference, " ; Units: ", units)

            # Insert country_name into 'countries' table
            # Check whether source_name has been inserted into 'sources' table
            cur.execute("SELECT COUNT(1) FROM countries WHERE name='" + country_name + "'")
            records = cur.fetchall()
            print('SELECT query finished')

            country_name_id = 0
            if records[0][0] == 0:
                
                cur.execute("INSERT INTO countries (name) values ('" + country_name + "')")
                # Retrieve the source id of a newly created source
                cur.execute("SELECT country_name_id from countries WHERE name='" + country_name + "'")
                records = cur.fetchone()

                country_name_id = records[0]
                print("Country name id: ", country_name_id)
            else:
                cur.execute("SELECT country_name_id from countries WHERE name='" + country_name + "'")
                records = cur.fetchone()
                country_name_id = records[0]
                print("country name id: ", country_name_id)
            con.commit()
            # ////////////////////////////////
            
            # Insert month into 'comments_data' table and 'comments_tree' table. Retreive comment_id.
            comment_id = insert_in_closure_table.add_comment(post_id=str(post_id), comment_content=reference, country_name_id=str(country_name_id), comment_sum=last_value, units=units)
    

    elif choice == 1:
        # Insert indicator_name into 'posts' table and retrieve the post_id
        post_id = insert_in_closure_table.create_post(indicator_name_1, source_id)

        # Read loaded json file
        json_file = open(path + file_names_list[1] + '.json')

        # Return json object as a dictionary
        json_object = json.load(json_file)

        for observation in json_object:
            # ////////////////////////////////
            country_name = observation["country_name"]
            last_value = observation["last_value"]
            reference = observation["reference"]
            units = observation["units"]

            print("Country_name: ", country_name, ". Value: ", last_value, " ; Type of last_value: ", type(last_value), ". Reference: ", reference, " ; Units: ", units)

            # Insert country_name into 'countries' table
            # Check whether source_name has been inserted into 'sources' table
            cur.execute("SELECT COUNT(1) FROM countries WHERE name='" + country_name + "'")
            records = cur.fetchall()
            print('SELECT query finished')

            country_name_id = 0
            if records[0][0] == 0:
                
                cur.execute("INSERT INTO countries (name) values ('" + country_name + "')")
                # Retrieve the source id of a newly created source
                cur.execute("SELECT country_name_id from countries WHERE name='" + country_name + "'")
                records = cur.fetchone()

                country_name_id = records[0]
                print("Country name id: ", country_name_id)
            else:
                cur.execute("SELECT country_name_id from countries WHERE name='" + country_name + "'")
                records = cur.fetchone()
                country_name_id = records[0]
                print("country name id: ", country_name_id)
            con.commit()
            # ////////////////////////////////
            
            # Insert month into 'comments_data' table and 'comments_tree' table. Retreive comment_id.
            comment_id = insert_in_closure_table.add_comment(post_id=str(post_id), comment_content=reference, country_name_id=str(country_name_id), comment_sum=last_value, units=units)
    
    
    elif choice == 2:
        # Insert indicator_name into 'posts' table and retrieve the post_id
        post_id = insert_in_closure_table.create_post(indicator_name_2, source_id)

        # Read loaded json file
        json_file = open(path + file_names_list[2] + '.json')

        # Return json object as a dictionary
        json_object = json.load(json_file)

        for observation in json_object:
            # ////////////////////////////////
            content = observation["symbol"]
            comment_sum = observation["price"]
            reference = observation["date"]
            

            # print("Country_name: ", country_name, ". Value: ", last_value, " ; Type of last_value: ", type(last_value), ". Reference: ", reference, " ; Units: ", units)

            # Insert country_name into 'countries' table
            # Check whether source_name has been inserted into 'sources' table
            country_name = 'Kazakhstan'
            cur.execute("SELECT COUNT(1) FROM countries WHERE name='" + country_name + "'")
            records = cur.fetchall()
            print('SELECT query finished')

            country_name_id = 0
            if records[0][0] == 0:
                
                cur.execute("INSERT INTO countries (name) values ('" + country_name + "')")
                # Retrieve the source id of a newly created source
                cur.execute("SELECT country_name_id from countries WHERE name='" + country_name + "'")
                records = cur.fetchone()

                country_name_id = records[0]
                print("Country name id: ", country_name_id)
            else:
                cur.execute("SELECT country_name_id from countries WHERE name='" + country_name + "'")
                records = cur.fetchone()
                country_name_id = records[0]
                print("country name id: ", country_name_id)
            con.commit()
            # ////////////////////////////////
            
            # Insert month into 'comments_data' table and 'comments_tree' table. Retreive comment_id.
            comment_id = insert_in_closure_table.add_comment(post_id=str(post_id), comment_content=content, country_name_id=str(country_name_id), comment_sum=comment_sum, reference = reference)
    

except:
    print("ERROR")
    con.rollback()
# -----------------------------------------------



# # Save (commit) the changes
# con.commit()

# # Close the connection
# con.close()