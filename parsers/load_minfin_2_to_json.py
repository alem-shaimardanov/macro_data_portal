import json
from styleframe import StyleFrame
import pandas as pd

excel_file_name = 'на 1февраля 2022 г.xlsx'
sheet_names = ['табл 3']
post_name = 'ИСПОЛНЕНИЕ ГОСУДАРСТВЕННОГО БЮДЖЕТА'
# Load excel file
excel_data_df = pd.read_excel(excel_file_name, sheet_name=sheet_names[0])

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

# Save column names of the Excel sheet
column0 = '3-кесте'
column1 = 'Unnamed: 1'
column2 = 'Unnamed: 2'
column3 = 'Unnamed: 3'
column4 = 'Таблица 3'
column5 = 'Unnamed: 5'
column6 = 'Unnamed: 6'

# Declare dictionaries for JSON
excel_json_gen0 = {}
excel_json_gen1 = {}
excel_json_gen2 = {}

# Save names of data periods
column1_data_period = excel_data_df.at[3,'Unnamed: 1']
column2_data_period = excel_data_df.at[3,'Unnamed: 2']
column3_data_period = excel_data_df.at[3,'Unnamed: 3']
column3_data_period_year = excel_data_df.at[4,'Unnamed: 3']
column3_data_period_month = excel_data_df.at[4,'Таблица 3']
column5_data_period = excel_data_df.at[3,'Unnamed: 5']

# Save previous key
prev_key = 'Средства Национального фонда (далее-Фонд) на начало отчетного периода (кассовое исполнение), всего:*'
prev_v_tom_chisle_key_gen1 = ''
prev_v_tom_chisle_key_gen2 = ''


i = 0
columns_counter  = 0

# Loop through columns
for columns_counter in range(1,6):

    # Loop through rows for a single column, i.e. data period
    for ind, row in excel_data_df[5:].iterrows():
        current_col0_val = excel_data_df[column0][ind]
        current_col1_val = excel_data_df[column1][ind]
        current_col2_val = excel_data_df[column2][ind]
        current_col3_val = excel_data_df[column3][ind]
        current_col4_val = excel_data_df[column4][ind]
        current_col5_val = excel_data_df[column5][ind]
        current_col6_val = excel_data_df[column6][ind]


    
    # Increment columns_counter
    columns_counter += 1

