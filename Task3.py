import requests

URL = 'https://api.stackexchange.com/docs/questions-by-ids#fromdate=2023-05-08&todate=2023-05-10&order=desc&sort=' \
      'activity&ids=Python&filter=default&site=stackoverflow'  #order=desc&sort=activity&filter=default&site=stackoverflow

response = requests.get(URL)
print(response.text)

# Задача не решена, не знаю что делать с ней