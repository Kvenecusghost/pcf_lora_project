# import requests
# import json

# url = 'http://87.247.28.238:8501/api/weights'
# headers = {'Content-type': 'application/json',  # Определение типа данных
#            'Accept': 'text/plain',
#            'Content-Encoding': 'utf-8'}
# data = {"user_info" : [{"username" : "<user login>",
#                        "key" : "<api_key>"},
#                       {}]}  # Если по одному ключу находится несколько словарей, формируем список словарей
# answer = requests.post(url, data=json.dumps(data), headers=headers)
# print(answer)
# response = answer.json()
# print(response)


# AnimalNumber: "KZC154000000",
#     Date: "2019-04-16T13:15:00",
#     Weight: 300.5,
#   ScalesModel: ""

from datetime import datetime, date, time
import requests
import json

#url = 'http://87.247.28.238:8501/api/weights'
url = 'http://194.4.56.86:8501/api/weights'
headers = {'Content-type': 'application/json'}

data = {"AnimalNumber" : "AZT120000010", 
        "Date" : str(datetime.now()),
        "Weight" : "400" ,
        "ScalesModel" : "test_2"}  # Если по одному ключу находится несколько словарей, формируем список словарей

answer = requests.post(url, data=json.dumps(data), headers=headers)
print(answer) # можно ли как-то на этой строке остановиться вдебаге?
#response = answer.json()
print("_____________")
#print(response.json())
