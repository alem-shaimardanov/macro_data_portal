import json
from urllib.request import urlopen

base_url = "https://taldau.stat.gov.kz/ru/Api/GetIndexData/704449?period=7&dics=67"
indicator_name = "индекс реальных денежных доходов"

############## CODE TO LOAD JSON FROM TALDAU #################
with urlopen(base_url) as response:
    source = response.read()

data = json.loads(source)
# print(json.dumps(data, indent = 2, ensure_ascii=False)) # ascii is False in order to print Russian chars
for item in data:
    print(item["termNames"])


## Use the code below to save json into a file
file_name = indicator_name + ".json"
with open(file_name, 'w') as json_file:
    json.dump(data, json_file)
###############################################################