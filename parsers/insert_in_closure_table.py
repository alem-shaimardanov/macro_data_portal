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


stop = False
while not stop:
    print("Operations:")
    print("1 : Create a post")
    print("2 : Write a comment to the main post")
    print("3 : Reply to a comment")
    print("4 : Print comments in tree format")
    print("5 : Exit")
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
        pass
    
    elif operation == '5':
        stop = True
    
    else:
        print("Enter a valid number")
        pass
    