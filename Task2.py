import requests

TOKEN = "..."  # МОЙ ТОКЕН !!!!!
PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'  # Путь к АПИ
params = {'path': '/Netology/Sample_hokku.txt', 'overwrite': 'true'}  # Параметры запроса
headers = {'Accept': 'application/json', 'Authorization': TOKEN}  # Заголовки

file_path = 'Sample_hokku.txt'  # Название файла, если он будет в каталоге с программой, то он сразу найдется

response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
print(response.text)

put_url = response.json().get('href')
print(put_url)

files = {'file': open(file_path, 'rb')}
response = requests.put(put_url, files=files, headers=headers)
print(response)
