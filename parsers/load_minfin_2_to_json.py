import json
from styleframe import StyleFrame
import pandas as pd


# Load excel file
excel_data_df = pd.read_excel('на 1февраля 2022 г.xlsx', sheet_name='табл 3')

######################### SOLUTION 1 #############################
print("Head of df: ")
print(excel_data_df.head())

print("==============================")
print(excel_data_df)
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