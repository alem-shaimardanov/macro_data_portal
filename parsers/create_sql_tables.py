import sqlite3

current_dir = "/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers"
db_file = current_dir + '/taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

# Create 'indicators_main' table
cur.execute('''create table indicators_main (
    indicator_id int primary key,
    indicator_name text,
    source_id int)''')


# Create 'source_names' table
cur.execute('''create table source_names (
    source_id int primary key,
    source_name text
)''')


# Create 'periods' table
cur.execute('''create table periods (
    period_id int primary key,
    period_name text
)''')


# Create 'indicator_period_combo' table
cur.execute('''create table indicator_period_combo (
    indic_period_id int primary key,
    indicator_id int,
    period_id int
)''')


# Create 'termNames' table
cur.execute('''create table termNames (
    termName_id int primary key,
    termName text
)''')


# Create 'termNames_combo' table
cur.execute('''create table termNames_combo (
    termName_combo_id int primary key,
    termName_term_id int,
    termName_id int,
    indic_period_id int
)''')


# Create 'taldau_values' table
cur.execute('''create table taldau_values (
    value_id int primary key,
    termName_term_id int,
    name text,
    date text,
    value_string text,
    value_long real,
    date_created smalldatetime
)''')

# cur.execute('''CREATE TABLE stocks
#                (date text, trans text, symbol text, qty real, price real)''')

# Save (commit) the changes
con.commit()

# Close the connection
con.close()