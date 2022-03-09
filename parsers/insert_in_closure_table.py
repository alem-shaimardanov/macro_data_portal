import sqlite3

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# Function to Create a post
def create_post(post_content):
    try:
        # Insert a post
        cur.execute("INSERT INTO posts (content) VALUES ('" + post_content + "')")

        # Retrieve the post id of a newly created post
        cur.execute("SELECT postid from posts WHERE content='" + post_content + "'")
        records = cur.fetchone()
        print("Post_id: ", records[0])
        print("--------------------------------")

        # # Save (commit) the changes
        con.commit()
        
        # Return post id
        return records[0]

    except:
        cur.rollback()
        return -1

# Function to Add a comment to the main post
def add_comment(post_id, comment_content):
    try:
        # Insert a comment into 'comments_data' table
        cur.execute("INSERT INTO comments_data (content) VALUES ('" + comment_content + "')")

        # Retrieve the comment id of a newly created comment
        cur.execute("SELECT idEntry from comments_data WHERE content='" + comment_content + "'")
        records = cur.fetchone()
        print("Comment_id: ", records[0])
        comment_id = records[0]

        # Insert post_id, comment_id into 'comments_tree' table
        cur.execute("INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (" +
        str(comment_id) + "," + str(comment_id) + "," + "0," + "0," + post_id + ")")

        # # Save (commit) the changes
        con.commit()
        
        # Return comment id
        # 2
        #print("Comment_id: ", comment_id)
        print("--------------------------------")
        return comment_id
    except:
        con.rollback()
        return -1


# Function to Reply to a comment
def reply_to_comment(post_id, comment_content, root_comment_id):
    try:
        # Retrieve commentLevel of the comment to which user replies
        cur.execute("SELECT idAncestor, commentLevel from comments_tree WHERE idAncestor='" + root_comment_id + "'and idDescendant='" + root_comment_id + "'")
        
        records = cur.fetchall()
        print("Comment Level: ", records[0][1])
        print("idAncestor: ", records[0][0])
        comment_level = records[0][1]
        idAncestor = records[0][0]
        # Increment comment_level of comment_reply_level
        comment_reply_level = comment_level + 1

        # Insert comment_text into 'comments_data' table
        cur.execute("INSERT INTO comments_data (content) VALUES ('" + comment_content + "')")

        # Retrieve the comment id of a newly created comment
        cur.execute("SELECT idEntry from comments_data WHERE content='" + comment_content + "'")
        records = cur.fetchone()
        print("Comment_id: ", records[0])
        comment_id = records[0]

        # # Set idNearAncestor = idDescendant of root_comment
        # idNearestAncestor = root_comment_id

        # Retrive all ancestors ids of root_comment
        cur.execute("SELECT idAncestor FROM comments_tree WHERE idDescendant=" + root_comment_id)
        records = cur.fetchall()

        for ancestor in records:
            print("idAncestor: ", ancestor[0])
            idAncestor = ancestor[0]

            # Insert into 'comments_tree' table
            cur.execute("INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (" +
            str(idAncestor) + "," + str(comment_id) + "," + root_comment_id + "," + str(comment_reply_level) + "," + post_id + ")")

        # Insert a row with same idAncestor and idDescendant
        cur.execute("INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (" +
            str(comment_id) + "," + str(comment_id) + "," + root_comment_id + "," + str(comment_reply_level) + "," + post_id + ")")

        # # Save (commit) the changes
        con.commit()

        return comment_id
    except:
        con.rollback()
        return -1



def print_tree(ancestor_id):
    try:
        cur.execute('''
        SELECT tableData.idEntry, 
        tableData.content, 
        tableTree.idAncestor, 
        tableTree.idDescendant, 
        tableTree.idNearestAncestor, 
        tableTree.commentLevel, 
        tableTree.idSubject 
        FROM comments_data AS tableData 
        JOIN comments_tree AS tableTree 
        ON tableData.idEntry = tableTree.idDescendant 
        WHERE tableTree.idAncestor = ''' + ancestor_id)
        records = cur.fetchall()

        print("Type of records: ", type(records))
        print("Values: ",records)
        return 1
    except:
        con.rollback()
        return -1

    

def delete_comment_branch(post_id, root_comment_id):
    try:
        # DELETE FROM comments_data where idEntry = root_comment_id;
        # Fetch tree of comments
        cur.execute('''
        SELECT tableData.idEntry, 
        tableData.content, 
        tableTree.idAncestor, 
        tableTree.idDescendant, 
        tableTree.idNearestAncestor, 
        tableTree.commentLevel, 
        tableTree.idSubject 
        FROM comments_data AS tableData 
        JOIN comments_tree AS tableTree 
        ON tableData.idEntry = tableTree.idDescendant 
        WHERE tableTree.idAncestor = ''' + root_comment_id)
        records = cur.fetchall()
        idEntry_list = []
        for record in records:
            idEntry_list.append(record[0])
        print("idEntry list: ", idEntry_list)

        # Loop through idEntry list:
        for idEntry in idEntry_list:

            # Delete rows from comments_data 
            cur.execute("DELETE FROM comments_data where idEntry = " + str(idEntry))
            
            # Delete rows from comments_tree
            cur.execute("DELETE FROM comments_tree where idAncestor = " + str(idEntry) + " and idSubject = " + post_id)

        # # Save (commit) the changes
        con.commit()

        return 1
    except:
        con.rollback()
        return -1


stop = False
while not stop:
    print("Operations:")
    print("0 : Exit")
    print("1 : Create a post")
    print("2 : Write a comment to the main post")
    print("3 : Reply to a comment")
    print("4 : Print comments in tree format")
    print("5 : Delete comment and its branch")
    print("6 : Delete post and all its comments")
    operation = input("Type number to choose an operation:")
    if operation == '1':
        post_content = input("Type text of post: ")
        res = create_post(post_content)
        print("Res of function: ",res)
        print("++++++++++++++++++++++++++++")

    elif operation == '2':
        post_id = input("Enter post_id: ")
        comment_text = input("Enter text of comment: ")
        res = add_comment(post_id, comment_text)
        print("Res of function: ", res)
        print("++++++++++++++++++++++++++++")
    
    elif operation == '3':
        post_id = input("Enter post_id: ")
        root_comment_id = input("Enter id of comment to which you want to reply: ")
        comment_text = input("Enter text of comment: ")
        res = reply_to_comment(post_id, comment_text, root_comment_id)
        print("Res of function: ", res)
        print("++++++++++++++++++++++++++++")

    elif operation == '4':
        ancestor_id = input("Enter root_comment_id of branch to be printed: ")
        res = print_tree(ancestor_id)
        print("Res of function: ", res)
        print("++++++++++++++++++++++++++++")
    
    elif operation == '5':
        post_id = input("Enter post_id: ")
        root_comment_id = input("Enter comment_id to be deleted:")
        res = delete_comment_branch(post_id, root_comment_id)
        print("Res of function: ", res)
        print("++++++++++++++++++++++++++++")

    elif operation == '6':
        stop = True

    elif operation == '0':
        stop = True
    
    else:
        print("Enter a valid number")
        pass
