import json
from urllib.request import urlopen
# import requests
from time import *
from random import randint

base_url_1 = "https://api.stlouisfed.org/fred/series/observations?series_id=GNPCA&api_key=7d1fa8e45a6f8b1fa966454d53fb91dd&file_type=json"

urls_list = [base_url_1]

indicator_name_1 = "GNPCA"


indicator_names_list = [indicator_name_1]

############## CODE TO LOAD JSON FROM TALDAU #################
for i in range(len(urls_list)):
    indicator_name = indicator_names_list[i]
    print("Indicator: ", indicator_name)

    # Set up a random timer to wait before parsing a new page
    x = randint(2,5)
    print(x)
    sleep(x)
    print(f'I waited {x} seconds')

    with urlopen(urls_list[i]) as response:
        source = response.read()
    

    data = json.loads(source)
    # print(json.dumps(data, indent = 2, ensure_ascii=False)) # ascii is False in order to print Russian chars
    

    ## Use the code below to save json into a file
    file_name = indicator_name + ".json"
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)
    

###############################################################