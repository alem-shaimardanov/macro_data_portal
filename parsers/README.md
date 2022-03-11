#### Taldau parser
This is the parser of json from Taldau

[Taldau indicator](https://taldau.stat.gov.kz/ru/NewIndex/GetIndex/704449?keyword=)

[Taldau json](https://taldau.stat.gov.kz/ru/Api/GetIndexData/704449?period=7&dics=67)

Indicator_name: "индекс реальных денежных доходов"
<ul>
    <li> Period: "Год" </li>
    <li> Classifiers: "Регионы" </li>
    <li> Unit of measure: "Процент" </li>
</ul>

We load json by using `munge.py` and save it to the json file.

Tables to store json file:

#### Table 1: indicators_main
| indicator_id | indicator_name | source_id |
|--------------|----------------|-----------|
|      1       |"индекс реальных денежных доходов"|"Taldau"|
|      2       |"GDP"           | "FRED"    |

SQL code:
```SQL
create table indicators_main (
    indicator_id integer primary key autoincrement,
    indicator_name text,
    source_id int
);
```

#### Table 2: source_names
| source_id | source_name |
|-----------|-------------|
|    1      | "Taldau"    |

SQL code:
```SQL
create table source_names (
    source_id integer primary key autoincrement,
    source_name text
);
```

#### Table 3: periods
| period_id | period_name |
|-----------|-------------|
|     1     | "Год" |
|     2     | "Квартал" |

SQL code:
```SQL
create table periods (
    period_id integer primary key autoincrement,
    period_name text
);
```

#### Table 4: indicator_period_combo
| indic_period_id | indicator_id | period_id |
|-----------------|--------------|-----------|
|        1        |       2      |     1     |
|        2        |       1      |     1     |

SQL code:
```SQL
create table indicator_period_combo (
    indic_period_id integer primary key autoincrement,
    indicator_id int,
    period_id int
);
```

#### Table 5: term_item_names
| term_item_name_id | term_item_name |
|-------------------|----------------|
|         1         | "КЫЗЫЛОРДИНСКАЯ ОБЛАСТЬ" |
|         2         | "ЮЖНО-КАЗАХСТАНСКАЯ ОБЛАСТЬ" |

```SQL
create table term_item_names (
    term_item_name_id integer primary key autoincrement,
    term_item_name text
);
```


#### Table 6: term_category_groups
// It stores 
| id | term_category_group_id | term_category_id |
|----|------------------------|------------------|
| 1  |           1            |         1        |
| 2  |           1            |         2        |


SQL code:
```SQL
create table term_category_groups (
    id integer primary key autoincrement,
    term_category_group_id int,
    term_category_id int
);
```


#### Table 7: term_category_names
| term_category_id | term_category_name |
|------------------|--------------------|
|         1        |      "Регионы"     |
|         2        | "Виды сельскохозяйственной продукции" |

```SQL
create table term_category_names (
    term_category_id integer primary key autoincrement,
    term_category_name text
)

```


#### Table 8: term_item_groups
| id | term_category_group_id | term_item_group_id | term_item_name_id |
|----|------------------------|--------------------|-------------------|
|  1 |           1            |             1      |             1     |
|  2 |           1            |             1      |             2     |
|  3 |           1            |             2      |             1     |
|  4 |           1            |             2      |             3     |
|  5 |           1            |             3      |             4     |
|  6 |           1            |             3      |             2     |

SQL code:
``` SQL
create table term_item_groups(
    id integer primary key autoincrement,
    term_category_group_id int,
    term_item_group_id int, 
    term_item_id int
);
```



#### Table 9: term_item_group_indic_periods
| id | term_item_group_id | indic_period_id |
|----|--------------------|-----------------|
|  1 |         1          |         1       |



SQL code:
```SQL
create table term_item_groups (
    id integer primary key autoincrement,
    term_item_group_id int,
    indic_period_id int
);
```

#### Table 10: taldau_values
| value_id | term_item_group_id | name | date | value_string | value_long | date_created |
|----------|--------------------|------|------|--------------|------------|--------------|
|     1    |          2         | "2004 год" | "31.12.2004" | "115.5" | 115.5 | 21.02.2021 |

SQL code:
```SQL
create table taldau_values (
    value_id integer primary key autoincrement,
    term_item_group_id int,
    name text,
    date text,
    value_string text,
    value_long real,
    date_created smalldatetime
);
```


Steps that need to be done once only:
1. Create tables in .db using `create_sql_tables.py` file;


Algorithm:
1. Load JSON into json object with `munge.py`;
2. Save json object in the .json file with `munge.py` file;
3. Create connection to existing tables with `munge.py` file;
4. Process json object and store relevant parts into existing tables;
5. Close the connection to .db.


### Order of running python files:
1. Run `load_json.py` to save json from Taldau;
2. Run `create_sql_tables.py` to create schema for the SQL tables;
3. Run `fill_in_non_json_tables.py` to fill in all tables except taldau_values table;
4. Run `fill_in_json_tables.py` to fill in taldau_values table with the values from Taldau.


### To-dos

- [x] set up primary key to be incremental;
- [x] write try, except blocks for fill_in_json.py
- [x] use insert into table (columns) values (vals)
- [x] use regular expression to check if string is double or not
- [x] use SQL queries to access ids of source_names
- [x] remove current_dir
- [x] set by default null when creating tables
- [x] add oblast's to tables and be able to use them to choose specific name,date,value records

- Create table to store termname_category_id, termname_ids
region | VKO
region | ZKO
region | SKO



- [ ] create a post which will mean created post_id
- [ ] add comment referring to post_id
- [ ] reply comment, mention post_id, comment_id
- [ ] show all comments in a tree format for post_id

4 methods:
1. Create a post
2. Add comment
3. Reply to comment
4. Get comments with a post

Read: https://habr.com/ru/post/263629/ 


### Closure Table combined with Adjancy List

#### Table 1: posts
| postid | content | dateCreated |
|--------|---------|-------------|
| 1      | "Post text" | "12/28/2021"|

SQL code:
```SQL
create table posts (
    postid integer primary key autoincrement,
    content text,
    dateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Table 2: comments_data

| idEntry | content | post_id | dateCreated |
|---------|---------|---------|-------------|
| 1       | Could the author name primary sources? | 1 | "12/28/2021"|
| 2       | I am certain, the author cannot share the primary sources.| 1 | "12/28/2021"|
| 3       | Similar request.| 1 | "12/28/2021"|
| 4       | No problem, will share links later tonight.| 1 | "12/28/2021"|
| 5       | Then please send them to my email.| 1 | "12/28/2021"|
| 6       | Why are so certain? | 1 | "12/28/2021"|
| 7       | I am well familiar with the style of publications of the sources.| 1 | "12/28/2021"|

INSERT INTO comments_data (content, post_id) VALUES ('Could the author name primary sources?',1);
INSERT INTO comments_data (content, post_id) VALUES ('I am certain, the author cannot share the primary sources.',1);
INSERT INTO comments_data (content, post_id) VALUES ('Similar request.',1);
INSERT INTO comments_data (content, post_id) VALUES ('No problem, will share links later tonight.',1);
INSERT INTO comments_data (content, post_id) VALUES ('Then please send them to my email.',1);
INSERT INTO comments_data (content, post_id) VALUES ('Why are so certain?',1);
INSERT INTO comments_data (content, post_id) VALUES ('I am well familiar with the style of publications of the sources.',1);

SQL code:
```SQL
create table comments_data (
    idEntry integer primary key autoincrement,
    content text,
    post_id int,
    dateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Table 3: comments_tree
| idAncestor | idDescendant | idNearestAncestor | commentLevel | idSubject | dateCreated |
|------------|--------------|-------------------|-------|-----------|-------------|
| 1          | 1            | 0                 | 0     | 160       | "12/28/2022"|
| 1          | 2            | 1                 | 1     | 160       | "12/28/2022"|
| 1          | 3            | 1                 | 1     | 160       | "12/28/2022"|
| 1          | 4            | 1                 | 1     | 160       | "12/28/2022"|
| 1          | 5            | 4                 | 2     | 160       | "12/28/2022"|
| 1          | 6            | 2                 | 2     | 160       | "12/28/2022"|
| 1          | 7            | 6                 | 3     | 160       | "12/28/2022"|
| 1          | 2            | 1                 | 1     | 160       | "12/28/2022"|
| 1          | 6            | 2                 | 2     | 160       | "12/28/2022"|
| 1          | 7            | 6                 | 3     | 160       | "12/28/2022"|
| 1          | 3            | 1                 | 1     | 160       | "12/28/2022"|
| 1          | 4            | 1                 | 1     | 160       | "12/28/2022"|
| 1          | 5            | 4                 | 2     | 160       | "12/28/2022"|
| 1          | 5            | 4                 | 2     | 160       | "12/28/2022"|
| 1          | 6            | 2                 | 2     | 160       | "12/28/2022"|
| 1          | 7            | 6                 | 3     | 160       | "12/28/2022"|
| 1          | 7            | 6                 | 3     | 160       | "12/28/2022"|

INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (1,1,0,0,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (1,2,1,1,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (1,3,1,1,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (1,4,1,1,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (1,5,4,2,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (1,6,2,2,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (1,7,6,3,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (2,2,1,1,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (2,6,2,2,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (2,7,6,3,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (3,3,1,1,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (4,4,1,1,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (4,5,4,2,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (5,5,4,2,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (6,6,2,2,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (6,7,6,3,160);
INSERT INTO comments_tree (idAncestor, idDescendant, idNearestAncestor, commentLevel, idSubject) VALUES (7,7,6,3,160);

SQL code:
```SQL
create table comments_tree (
    idAncestor int,
    idDescendant int,
    idNearestAncestor int,
    commentLevel int, 
    idSubject int,
    dateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (idAncestor, idDescendant)
);
```

Query to build a tree:
```SQL
SELECT 
tableData.idEntry,
tableData.content,
tableTree.idAncestor, 
tableTree.idDescendant, 
tableTree.idNearestAncestor, 
tableTree.commentLevel, 
tableTree.idSubject 
FROM comments_data AS tableData
JOIN comments_tree AS tableTree 
ON tableData.idEntry = tableTree.idDescendant
WHERE tableTree.idAncestor = 1;
```


Plan:
1. DONE - Finish creating all tables for closure (3 tables)
2. DONE - Write a function to create a post (INSERT), it returns post_id
3. DONE - Write a function to create a comment to main post. args = (post_id, comment_content, ). Return comment_id
4. DONE - Write a function to reply to a comment. args = (post_id, comment_id, comment_content). Return comment_id
5. DONE - Write a function to generate a sorted tree.


To-dos:
1. DONE - Fix minfin excel to JSON (bold categories are currently considered as values of other equiavalent bold categories)
2. DONE - Navigate through JSON to be able to access any item and its sum.
3.  Insert values from JSON into closure table.

Idea: retrieve id of comment to which you want to reply. Then add a reply.