import sqlite3
import math
# db_file = 'taldau_indicator1.db'

# # Create SQL connection to the database
# con = sqlite3.connect(db_file)

# # Create a cursor
# cur = con.cursor()

# cur.execute("select idAncestor, commentLevel from comments_tree where idDescendant=1")
# records = cur.fetchall()

# print("Print result of SELECT:")
# print(records)
# print("------------------------")
# print(type(records))

# print("Printing loop:")
# for elem in records:
#     print("idAncestor: ", elem[0], "; CommentLevel: ", elem[1])
    
# con.close()
# This is the function to check if value is float or not
def isfloat(num):
    try:
        print(float(num))
        return True
    except ValueError:
        return False

def isFloatNan(num):
    try:
        # float(num)
        print("THIS IS nan ...")
        return num == float('nan')
    except:
        print("this is NOT nan")
        return False


num = float('nan')
print("Is float: ",isfloat(num))

res = ''
res = num if (isfloat(num) and not math.isnan(num)) else -1

# if (isfloat(num) and not math.isnan(num)):
#     res = num
# else:
#     res = "NAN!"
# res = num if (isfloat(num) and isFloatNan(num) == False) else "NAN"
print("RES: ", res)