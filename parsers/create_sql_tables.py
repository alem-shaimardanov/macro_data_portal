import sqlite3

# current_dir = "/Users/alemshaimardanov/Desktop/nat_bank/macro_data_portal_code/parsers"
db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

# Create 'indicators_main' table
cur.execute('''
    create table indicators_main (
    indicator_id integer primary key autoincrement,
    indicator_name text,
    source_id int)''')


# Create 'source_names' table
cur.execute('''create table source_names (
    source_id integer primary key autoincrement,
    source_name text
)''')


# Create 'periods' table
cur.execute('''create table periods (
    period_id integer primary key autoincrement,
    period_name text
)''')


# Create 'indicator_period_combo' table
cur.execute('''create table indicator_period_combo (
    indic_period_id integer primary key autoincrement,
    indicator_id int,
    period_id int
)''')


# Create 'term_item_names' table
cur.execute('''create table term_item_names (
    term_item_name_id integer primary key autoincrement,
    term_item_name text
)''')


# Create 'term_category_groups' table
cur.execute('''create table term_category_groups (
    id integer primary key autoincrement,
    term_category_group_id int,
    term_category_id int
)''')


# Create 'term_category_names' table
cur.execute('''create table term_category_names (
    term_category_id integer primary key autoincrement,
    term_category_name text
)''')



# Create 'term_item_groups' table
cur.execute('''create table term_item_groups(
    id integer primary key autoincrement,
    term_category_group_id int,
    term_item_group_id int, 
    term_item_id int
)''')



# Create 'term_item_group_indic_periods' table
cur.execute('''create table term_item_group_indic_periods (
    id integer primary key autoincrement,
    term_item_group_id int,
    indic_period_id int
)''')


# Create 'taldau_values' table
cur.execute('''create table taldau_values (
    value_id integer primary key autoincrement,
    term_item_group_id int,
    name text,
    date text,
    value_string text,
    value_long real,
    date_created smalldatetime
)''')




# Save (commit) the changes
con.commit()

# Close the connection
con.close()