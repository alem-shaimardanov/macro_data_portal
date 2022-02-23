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
    indicator_id int primary key,
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
    source_id int primary key,
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
    period_id int primary key,
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
    indic_period_id int primary key,
    indicator_id int,
    period_id int
);
```

#### Table 5: termNames
| termName_id | termName |
|-------------|----------|
|      1      | "КЫЗЫЛОРДИНСКАЯ ОБЛАСТЬ" |
|      2      | "ЮЖНО-КАЗАХСТАНСКАЯ ОБЛАСТЬ" |
|      3      | "Скот крупный рогатый" |

SQL code:
```SQL
create table termNames (
    termName_id int primary key,
    termName text
);
```

#### Table 6: termNames_combo
| termName_combo_id | termName_term_id | termName_id | indic_period_id |
|-------------------|------------------|-------------|-----------------|
|         1         |         1        |      1      |         2       |
|         2         |         2        |      2      |         1       |
|         3         |         2        |      3      |         1       |

SQL code:
```SQL
create table termNames_combo (
    termName_combo_id int primary key,
    termName_term_id int,
    termName_id int,
    indic_period_id int
);
```

#### Table 7: values
| value_id | termName_term_id | name | date | value_string | value_long | date_created |
|----------|------------------|------|------|--------------|------------|--------------|
|     1    |         2        |"2004 год" | "31.12.2004" | "115.5" | 115.5 | 21.02.2021 |

SQL code:
```SQL
create table values (
    value_id int primary key,
    termName_term_id int,
    name text,
    date text,
    value_string text,
    value_long real,
    date_created smalldatetime
);
```





