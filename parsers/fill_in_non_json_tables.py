import pandas as pd
import json
import os
import sqlite3
import requests
from urllib.request import urlopen
print("Start of tables being filled running ...")
# Parser for a single indicator from Taldau
indicator_name = "индекс реальных денежных доходов"

current_source_name = "Taldau"
current_source_name_id = "1"
current_term_category_name = "Регионы"
current_term_category_group_id = "1"
current_term_category_id = "1"
term_item_group_ids_list = [0]
current_indicator_id = "1"
current_period_id = "1"

############# CODE TO WRITE INTO SQLITE TABLES #################
# current_dir = "/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers"
db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

# Create a list to store table_names
table_names_list = []

# Save table_names from db into a list
for item in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'"):
    table_names_list.append(item)

print("Type of table_names:", type(table_names_list))
print(table_names_list)

# # Test printing table_names
# for t_n in table_names_list:
#     print(type(t_n[0]), t_n[0])
''' .tables
indicator_period_combo         term_category_groups         
indicators_main                term_category_names          
periods                        term_item_group_indic_periods
source_names                   term_item_groups             
taldau_values                  term_item_names 
'''

# Fill in the 'indicators_main' table
# Insert indicator_name, source_id, into indicators_main table
cur.execute("INSERT INTO indicators_main (indicator_name, source_id) VALUES ('" + indicator_name + "','" + current_source_name_id + "')")


# Fill in the 'source_names' table:
# Insert source_id, source_name into 'source_names' table
cur.execute("INSERT INTO source_names (source_name) VALUES ('" + current_source_name + "')")


# Fill in the 'periods' table:
# Insert period_id, period_name into 'periods' table
cur.execute("INSERT INTO periods (period_name) VALUES ('Год')")
cur.execute("INSERT INTO periods (period_name) VALUES ('Квартал')")
cur.execute("INSERT INTO periods (period_name) VALUES ('Месяц')")
cur.execute("INSERT INTO periods (period_name) VALUES ('Месяц с накоплением')")


# Fill in the 'indicator_period_combo' table:
# Insert 'indic_period_id', 'indicator_id', 'period_id'
cur.execute("INSERT INTO indicator_period_combo (indicator_id, period_id) VALUES ('" + current_indicator_id +
"','" + current_period_id + "')")


# Fill in the 'term_category_names' table:
# Insert 'term_category_name'
cur.execute("INSERT INTO term_category_names (term_category_name) VALUES ('" + current_term_category_name + "')")


# Fill in the 'term_category_groups' table:
# Insert 'term_category_group_id', 'term_category_id'
cur.execute("INSERT INTO term_category_groups (term_category_group_id, term_category_id) VALUES ('" +
current_term_category_group_id + "','" + current_term_category_id + "')")



# # Save (commit) the changes
con.commit()

# for row in cur.execute("SELECT * FROM stocks"):
#     print("Type of row: ",type(row), "TICKER: ", row[2])
#     print(row)
#     print("------------------------")
# Close the cursor
con.close()