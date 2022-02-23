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

#### Table 2: source_names
| source_id | source_name |
|-----------|-------------|
|    1      | "Taldau"    |

#### Table 3: periods
| period_id | period_name |
|-----------|-------------|
|     1     | "Год" |
|     2     | "Квартал" |

#### Table 4: indicator_period_combo
| indic_period_id | indicator_id | period_id |
|-----------------|--------------|-----------|
|        1        |       2      |     1     |
|        2        |       1      |     1     |

#### Table 5: termNames
| termName_id | termName |
|-------------|----------|
|      1      | "КЫЗЫЛОРДИНСКАЯ ОБЛАСТЬ" |
|      2      | "ЮЖНО-КАЗАХСТАНСКАЯ ОБЛАСТЬ" |
|      3      | "Скот крупный рогатый" |

#### Table 6: termNames_combo
| termName_combo_id | termName_term_id | termName_id | indic_period_id |
|-------------------|------------------|-------------|-----------------|
|         1         |         1        |      1      |         2       |
|         2         |         2        |      2      |         1       |
|         3         |         2        |      3      |         1       |

#### Table 7: values
| value_id | termName_term_id | name | date | value_string | value_long | date_created |
|----------|------------------|------|------|--------------|------------|--------------|
|     1    |         2        |"2004 год" | "31.12.2004" | "115.5" | 115.5 | 21.02.2021 |







