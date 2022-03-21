import json
from styleframe import StyleFrame
import pandas as pd

excel_file_name = 'на 1февраля 2022 г.xlsx'
# Load excel file
excel_data_df = pd.read_excel(excel_file_name, sheet_name='табл 3')

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




v_tom_chisle = 'в том числе:'
column0 = '3-кесте'
column1 = 'Unnamed: 1'
column2 = 'Unnamed: 2'
column3 = 'Unnamed: 3'
column4 = 'Таблица 3'
column5 = 'Unnamed: 5'
column6 = 'Unnamed: 6'

i = 0
for ind in excel_data_df.index:
    current_col0_val = excel_data_df[column0][ind]
    current_col1_val = excel_data_df[column1][ind]
    current_col2_val = excel_data_df[column2][ind]
    current_col3_val = excel_data_df[column3][ind]
    current_col4_val = excel_data_df[column4][ind]
    current_col5_val = excel_data_df[column5][ind]
    current_col6_val = excel_data_df[column6][ind]