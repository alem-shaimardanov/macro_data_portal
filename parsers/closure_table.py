import sqlite3

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()


# Create 'sources' table
cur.execute('''
    create table sources (
        source_id integer primary key autoincrement,
        name text
    )
''')


# Create 'posts' table
cur.execute('''
    create table posts (
    post_id integer primary key autoincrement,
    content text,
    source_id int,
    dateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')


# Create 'periods' table
cur.execute('''create table periods (
    period_id integer primary key autoincrement,
    period_name text,
    dateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')


# Create 'comments_data' table
cur.execute('''
    create table comments_data (
    idEntry integer primary key autoincrement,
    content text,
    country_name_id int,
    post_id int,
    period_id int,
    comment_sum int,
    reference,
    reference_date,
    dateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')


# Create 'comments_tree' table
cur.execute('''
    create table comments_tree (
    idAncestor int,
    idDescendant int,
    idNearestAncestor int,
    commentLevel int, 
    idSubject int,
    dateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (idAncestor, idDescendant)
)''')


# Save (commit) the changes
con.commit()

# Close the connection
con.close()