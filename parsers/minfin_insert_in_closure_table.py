from calendar import month
import sqlite3
import json
import insert_in_closure_table

indicator_name = "ОТЧЕТ О ПОСТУПЛЕНИЯХ И ИСПОЛЬЗОВАНИИ НАЦИОНАЛЬНОГО ФОНДА РЕСПУБЛИКИ КАЗАХСТАН"
month_name = "1 ФЕВРАЛЯ 2022 ГОДА "

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
v_tom_chisle = "в том числе"


try:
    ####### Pre-work ##########
    # Insert month into 'posts' table and retrieve the post_id
    post_id = insert_in_closure_table.create_post(indicator_name)
    
    # Insert month into 'comments_data' table and 'comments_tree' table. Retreive comment_id.
    comment_id = insert_in_closure_table.add_comment(str(post_id), month_name)

    # Retrieve idAncestor, idNearestAncestor, commentLevel of a newly added row from the 'comments_tree' table
    cur.execute("SELECT idAncestor, idNearestAncestor, commentLevel FROM comments_tree WHERE idDescendant = '" + str(comment_id) + "'")
    records = cur.fetchall()
    idAncestor = records[0][0]
    idNearestAncestor = records[0][1]
    commentLevel = records[0][1]
    ############################

    v_tom_chisle_gen1 = False
    v_tom_chisle_gen2 = False

    # Create variables to store lastly visited comments for every level in comments_tree
    recent_level0_comment_id = comment_id
    recent_level1_comment_id = 0
    recent_level2_comment_id = 0
    recent_level3_comment_id = 0

    print("Entering for loop ...")
    # Iterate through the json list:
    for item in json_object:

        # Check if the current item is a main category and not a dict
        if v_tom_chisle not in item and v_tom_chisle_gen1 == False and v_tom_chisle_gen2 == False:
            content = item
            comment_sum = json_object[item]

            # commentLevel = 1
            print("Main category: ", content, " ; Value: ", comment_sum, " ; Type of value: ", type(comment_sum))
            print("---+++---+++---+++---+++---")

            # Insert subcomment under "1 february" comment. Insert row into 'comments_data' table and relevant rows into 'comments_tree' table.
            subcomment_lvl1_id = insert_in_closure_table.reply_to_comment(str(post_id), content, str(recent_level0_comment_id), str(comment_sum))
            print("Subcomment level 1 id: ", subcomment_lvl1_id)
            recent_level1_comment_id = subcomment_lvl1_id

        
        # Check if the current item is a dict of main category
        elif v_tom_chisle in item and v_tom_chisle_gen1 == False and v_tom_chisle_gen2 == False:
            v_tom_chisle_gen1 = True
            print("Inside dashed strings")
            for elem in json_object[item]:
                if v_tom_chisle not in elem:
                    print("Dashed string: ", elem, " ; Value: ", json_object[item][elem], " ; Type of value: ", type(json_object[item][elem]))
                    content = elem
                    comment_sum = json_object[item][elem]

                    # Insert subcomment under main category comment. Insert row into 'comments_data' table and relevant rows into 'comments_tree' table.
                    subcomment_lvl2_id = insert_in_closure_table.reply_to_comment(str(post_id), content, str(recent_level1_comment_id), str(comment_sum))
                    
                    recent_level2_comment_id = subcomment_lvl2_id
                    
                
                elif v_tom_chisle in elem:
                    print("Found v_tom_chisle_gen2: ", elem)
                    v_tom_chisle_gen2 = True
                    for sub_elem in json_object[item][elem]:
                        print("subcom 2: ", sub_elem, " ; Value: ", json_object[item][elem][sub_elem])
                        content = sub_elem
                        comment_sum = json_object[item][elem][sub_elem]

                        # Insert subcomment under main category comment. Insert row into 'comments_data' table and relevant rows into 'comments_tree' table.
                        subcomment_lvl3_id = insert_in_closure_table.reply_to_comment(str(post_id), content, str(recent_level2_comment_id), str(comment_sum))
                        print("Subcomment level 3 id: ", subcomment_lvl3_id)
                        recent_level3_comment_id = subcomment_lvl3_id
            
        
            v_tom_chisle_gen1 = False
            v_tom_chisle_gen2 = False


        
except:
    print("ERROR")
    con.rollback()
# -----------------------------------------------



# Save (commit) the changes
con.commit()

# Close the connection
con.close()
