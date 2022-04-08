import sqlite3

db_file = 'taldau_indicator1.db'

# Create SQL connection to the database
con = sqlite3.connect(db_file)

# Create a cursor
cur = con.cursor()

# Example of a search query for macro data portal
# cur.execute('''
#     select
#         tv.*
#     from
#         taldau_values tv
#     where termName_term_id in (
#         select
#             termName_term_id
#         from 
#             termNames_combo tnc
#         join termNames tn
#             on tnc.termName_term_id = tn.termName_id
#         where
#             indic_period_id in (
#                 select ipc.indic_period_id
#                 from 
#                     indicator_period_combo ipc
#                 join indicators_main im
#                     on im.indicator_id = ipc.indicator_id
#                 join periods p
#                     on p.period_id = ipc.period_id
#                 where
#                     im.indicator_name like 'индекс%'
#                     and p.period_name like 'Год%'
#             )
#     )
#     order by
#         tv.date
# ''')

# result = cur.fetchall()

###### Drop tables related to Taldau: #########
# # Drop 'indicators_main' table
# cur.execute('''drop table indicators_main''')

# # Drop 'source_names' table
# cur.execute('''drop table source_names''')

# # Drop 'indicator_period_combo' table
# cur.execute('''drop table indicator_period_combo''')

# # Drop 'term_item_names' table
# cur.execute('''drop table term_item_names''')

# # Drop 'term_category_groups' table
# cur.execute('''drop table term_category_groups''')

# # Drop 'term_category_names' table
# cur.execute('''drop table term_category_names''')

# # Drop 'term_item_groups' table
# cur.execute('''drop table term_item_groups''')

# # Drop 'term_item_group_indic_periods' table
# cur.execute('''drop table term_item_group_indic_periods''')


# # Drop 'taldau_values' table
# cur.execute('''drop table taldau_values''')

# Drop 'sources' table
cur.execute('''drop table sources''')

# Drop 'posts' table
cur.execute('''drop table posts''')

# Drop 'periods' table
cur.execute('''drop table periods''')

# Drop 'comments_data' table
cur.execute('''drop table comments_data''')

# Drop 'comments_tree' table
cur.execute('''drop table comments_tree''')

# Save (commit) the changes
con.commit()

# Close the connection
con.close()