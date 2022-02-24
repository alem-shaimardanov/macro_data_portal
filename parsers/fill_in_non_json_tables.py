import pandas as pd
import json
import os
import sqlite3
import requests
from urllib.request import urlopen
print("Start of tables being filled running ...")
# Parser for a single indicator from Taldau
indicator_name = "индекс реальных денежных доходов"

# Create a dict to match source names to their source ids
source_names = {"Taldau": 1, "MinFin": 2, "FRED": 3}
current_source_name = "Taldau"
current_term_name = "Регионы"


############# CODE TO WRITE INTO SQLITE TABLES #################
current_dir = "/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers"
db_file = current_dir + '/taldau_indicator1.db'

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


# Fill in the 'indicators_main' table
# Insert indicator_name, indicator_id, into indicators_main table
cur.execute("INSERT INTO indicators_main (indicator_name, source_id) VALUES ('" + indicator_name + "','" + str(source_names["Taldau"]) + "')")


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
cur.execute("INSERT INTO indicator_period_combo (indicator_id, period_id) VALUES ('1','1')")


# Fill in the 'termNames' table:
# Insert 'termName_id', 'termName'
cur.execute("INSERT INTO termNames (termName) VALUES ('" + current_term_name + "')")


# Fill in the 'termNames_combo' table:
# Insert 'termName_combo_id', 'termName_term_id', 'termName_id', 'indic_period_id'
cur.execute("INSERT INTO termNames_combo (termName_term_id, termName_id, indic_period_id) VALUES ('1', '1', '1')")


# # Save (commit) the changes
con.commit()

# for row in cur.execute("SELECT * FROM stocks"):
#     print("Type of row: ",type(row), "TICKER: ", row[2])
#     print(row)
#     print("------------------------")
# Close the cursor
con.close()