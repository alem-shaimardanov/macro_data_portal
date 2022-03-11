import pandas
import json
import math
# Read excel document
excel_data_df = pandas.read_excel('Отчет НФ на 1.02.2022г.xlsx', sheet_name='01.02.2022')

######################### SOLUTION 1 #############################
# # Convert excel to string 
# # (define orientation of document in this case from up to down)
# thisisjson = excel_data_df.to_json(orient='records')

# # Print out the result
# print('Excel Sheet to JSON:\n')

# # Make the string into a list to be able to input in to a JSON-file
# thisisjson_dict = json.loads(thisisjson)

# # Define file to write to and 'w' for write option -> json.dump() 
# # defining the list to write from and file to write to
# # with open('minfin.json', 'w') as json_file:
# #     json.dump(thisisjson_dict, json_file)


# # Read loaded json file
# json_file = open('minfin.json')

# # Return json object as a dictionary
# json_object = json.load(json_file)

# print("Size of json: ", len(json_object))
# print(json_object)
##################################################################

######################### SOLUTION 2 #############################
excel_data_df = pandas.read_excel('Отчет НФ на 1.02.2022г.xlsx', sheet_name='01.02.2022')

v_tom_chisle = 'в том числе:'
column1 = 'ОТЧЕТ О ПОСТУПЛЕНИЯХ И ИСПОЛЬЗОВАНИИ НАЦИОНАЛЬНОГО ФОНДА РЕСПУБЛИКИ КАЗАХСТАН НА 1 ФЕВРАЛЯ 2022 ГОДА '
column2 = 'Unnamed: 1'
column3 = 'Unnamed: 2'

excel_json_gen0 = {}
excel_json_gen1 = {}
excel_json_gen2 = {}
prev_key = 'Средства Национального фонда (далее-Фонд) на начало отчетного периода (кассовое исполнение), всего:*'
prev_v_tom_chisle_key_gen1 = ''
prev_v_tom_chisle_key_gen2 = ''

# Use variables below to navigate between inner and outer dictionaries
v_tom_chisle_gen1 = False
v_tom_chisle_gen2 = False

# This is the function to check whether string contains '-' in front of it
def isDashString(string):
    string_no_spaces = "".join(string.split())
    has_dash = False

    if string_no_spaces[0] == '-':
        has_dash = True
    return has_dash


# This is the function to check if value is float or not
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False




# Loop through the rows of dataframe
for ind in excel_data_df.index:
    current_col1_val = excel_data_df[column1][ind]
    current_col2_val = excel_data_df[column2][ind]
    current_col3_val = excel_data_df[column3][ind]
    
    
    # 1. Check if this is the main key
    if isinstance(current_col1_val, str) and len(current_col1_val) < 3:
        # Set v_tom_chisle_gen1 and v_tom_chisle_gen2 to False
        v_tom_chisle_gen1 = False
        v_tom_chisle_gen2 = False

        # Add main key to the excel_json
        print("TYPE of current_col3_val: ", type(current_col3_val), " ; VALUE: ",current_col3_val)
        # excel_json_gen0[current_col2_val] = -1 if not isfloat(current_col3_val) else current_col3_val
        excel_json_gen0[current_col2_val] = current_col3_val if (isfloat(current_col3_val)) and not math.isnan(current_col3_val) else "nan"
        # res = num if (isfloat(num) and not math.isnan(num)) else -1
        print(" 1 TYPE of current_col3_val: ", " ; KEY: ",current_col2_val)

    # 2. Check if cur value is key_v_tom_chisle of gen1
    elif current_col2_val == v_tom_chisle and v_tom_chisle_gen1 == False and v_tom_chisle_gen2 == False:
        # Set v_tom_chisle_gen1 to True
        v_tom_chisle_gen1 = True
        
        # Create a dict_gen1
        excel_json_gen1 = {}
        key_gen1 = prev_key + v_tom_chisle
        
        # Add it to the excel_json
        excel_json_gen0[key_gen1] = excel_json_gen1
        
        # Update prev_v_tom_chisle_key
        prev_v_tom_chisle_key_gen1 = key_gen1
        print(" 2 TYPE of current_col3_val: ", " ; KEY: ",current_col2_val)
        
    # 3. Check if cur value is key_v_tom_chisle of gen2
    elif current_col2_val == v_tom_chisle and v_tom_chisle_gen1 == True and v_tom_chisle_gen2 == False:
        # Set v_tom_chisle_gen2 to True
        v_tom_chisle_gen2 = True
        
        # Create a dict_gen2
        excel_json_gen2 = {}
        key_gen2 = prev_key + v_tom_chisle
        
        # Add it to the excel_json_gen1
        excel_json_gen0[prev_v_tom_chisle_key_gen1][key_gen2] = excel_json_gen2
        
        # Update prev_v_tom_chisle_key
        prev_v_tom_chisle_key_gen2 = key_gen2
        print(" 3 TYPE of current_col3_val: ", " ; KEY: ",current_col2_val)
    

    # 5. Check if cur value belongs to dict_gen1 and is a dash_str and you just finished filling the dict_gen_2 
    elif isinstance(current_col2_val, str) and isDashString(current_col2_val) and v_tom_chisle_gen2 and v_tom_chisle_gen1:
        v_tom_chisle_gen2 = False # This means you're done with filling the dict_gen2. Work with dict_gen1
        
        # Add dash_str to dict_gen1
        print(" 5 TYPE of current_col3_val: ", " ; KEY: ",current_col2_val)
        excel_json_gen0[prev_v_tom_chisle_key_gen1][current_col2_val] = current_col3_val if (isfloat(current_col3_val)) and not math.isnan(current_col3_val) else "nan"
    
    # 6. Check if cur value is a dash_str and you've previously added other dash_str
    elif isinstance(current_col2_val, str) and isDashString(current_col2_val) and v_tom_chisle_gen2 == False and v_tom_chisle_gen1:
        # Add dash_str to dict_gen1
        print(" 6 TYPE of current_col3_val: ", " ; KEY: ",current_col2_val)
        excel_json_gen0[prev_v_tom_chisle_key_gen1][current_col2_val] = current_col3_val if (isfloat(current_col3_val)) and not math.isnan(current_col3_val) else "nan"
    
    # 4. Check if cur value belongs to dict_gen2
    elif v_tom_chisle_gen1 and v_tom_chisle_gen2:
        print(" 4 TYPE of current_col3_val: ", " ; KEY: ",current_col2_val)
        excel_json_gen0[prev_v_tom_chisle_key_gen1][prev_v_tom_chisle_key_gen2][current_col2_val] = current_col3_val if (isfloat(current_col3_val)) and not math.isnan(current_col3_val) else "nan"
        
    
       
    # Update prev_key
    prev_key = current_col2_val


print("Final JSON:")
print(excel_json_gen0)

# Save dict in json
# indicator_name = "ОТЧЕТ О ПОСТУПЛЕНИЯХ И ИСПОЛЬЗОВАНИИ НАЦИОНАЛЬНОГО ФОНДА РЕСПУБЛИКИ КАЗАХСТАН"
# json_file_name = indicator_name + ".json"
# with open(json_file_name, 'w') as json_file:
#     json.dump(excel_json_gen0, json_file)


