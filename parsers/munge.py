import pandas as pd
import json
import requests
from urllib.request import urlopen
print("Start of parser running ...")
# Parser for a single indicator from Taldau
indicator_name = "индекс реальных денежных доходов"
base_url = "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704449?period=7&dics=67"

with urlopen(base_url) as response:
    source = response.read()

data = json.loads(source)
# print(json.dumps(data, indent = 2, ensure_ascii=False)) # ascii is False in order to print Russian chars
# print(len(data[0]))
for item in data:
    print(item["termNames"])

file_name = indicator_name + ".json"

with open(file_name, 'w') as json_file:
    json.dump(data, json_file)