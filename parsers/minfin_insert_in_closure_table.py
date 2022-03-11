from calendar import month
import sqlite3
import json
indicator_name = "ОТЧЕТ О ПОСТУПЛЕНИЯХ И ИСПОЛЬЗОВАНИИ НАЦИОНАЛЬНОГО ФОНДА РЕСПУБЛИКИ КАЗАХСТАН"
post_id = '1'
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
    ######### Pre-work ##########
    # # Insert month into 'posts' table
    # cur.execute("INSERT INTO posts (content) VALUES ('" + indicator_name + "')")
    
    # # Retrieve post_id of a newly added post from the 'posts' table
    # cur.execute("SELECT postid FROM posts WHERE content = '" + indicator_name + "'")
    # records = cur.fetchone()
    # post_id = records[0]
    # print("Post_id: ",post_id)

    # # ////////
    # # Insert month into 'comments_data' table
    # cur.execute("INSERT INTO comments_data (content, post_id) VALUES ('" + month_name + "','" + str(post_id) + "')")
    
    # # Retrieve idEntry of a newly added comment from the 'comments_data' table
    # cur.execute("SELECT idEntry FROM comments_data WHERE content = '" + month_name + "'")
    # records = cur.fetchone()
    # comment_id = records[0]
    # print("Comment_id: ",post_id)

    # # Insert comment_id into 'comments_tree' table
    # cur.execute("INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (" + str(comment_id) + "," + str(comment_id) + "," +"0,0," + str(post_id) + ")")
    

    # # Retrieve idAncestor, idNearestAncestor, commentLevel of a newly added row from the 'comments_tree' table
    # cur.execute("SELECT idAncestor, idNearestAncestor, commentLevel FROM comments_tree WHERE idDescendant = '" + str(comment_id) + "'")
    # records = cur.fetchall()
    # idAncestor = records[0][0]
    # idNearestAncestor = records[0][1]
    # commentLevel = records[0][1]
    # print("idAncestor: ",idAncestor)
    # print("idNearestAncestor: ",idNearestAncestor)
    # print("commentLevel: ",commentLevel)


    v_tom_chisle_gen1 = False
    v_tom_chisle_gen2 = False

    print("Entering for loop ...")
    # Iterate through the json list:
    for item in json_object:

        # print("Type of item: ", type(item))
        # print("ITEM: ", item, " ; VALUE: ", json_object[item])

        # Check if the current item is a main category
        if v_tom_chisle not in item and v_tom_chisle_gen1 == False and v_tom_chisle_gen2 == False:
            print("V_tom_chisle: ", json_object[item])
            # Insert subcom to 'month' main comment

        # Check if the current item is a dict of main category
        elif v_tom_chisle in item and v_tom_chisle_gen1 == False and v_tom_chisle_gen2 == False:
            v_tom_chisle_gen1 = True
            print("Inside dashed strings")
            for elem in json_object[item]:
                print("Dashed string: ", elem)
                if v_tom_chisle in elem:
                    print("Found v_tom_chisle_gen2: ", elem)
                    v_tom_chisle_gen2 = True
                    for sub_elem in json_object[item][elem]:
                        print("subcom 2: ", sub_elem)
            
        
            v_tom_chisle_gen1 = False


        # Check if the current item is a dashed string
        

        # if isinstance(item, dict):
        #     for k, v in item.items():
        #         print ("SUBDICT. Key: ", k, " ; Value: ", v)
        

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
    print("ERROR")
    con.rollback()
# -----------------------------------------------





# Save (commit) the changes
con.commit()

# Close the connection
con.close()
