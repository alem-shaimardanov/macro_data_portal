import sqlite3

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

# Drop 'indicators_main' table
cur.execute('''drop table indicators_main''')

# Drop 'source_names' table
cur.execute('''drop table source_names''')

# Drop 'termNames_combo' table
cur.execute('''drop table termNames_combo''')

# Drop 'termNames' table
cur.execute('''drop table termNames''')

# Drop 'taldau_values' table
cur.execute('''drop table taldau_values''')

# Drop 'indicator_period_combo' table
cur.execute('''drop table indicator_period_combo''')

# Drop 'periods' table
cur.execute('''drop table periods''')


# Save (commit) the changes
con.commit()

# Close the connection
con.close()