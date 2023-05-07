import yadisk

token = ...

y = yadisk.YaDisk(token=token)
file_path = '/Netology/Sample_hokku.txt'
y.upload("Sample_hokku.txt", file_path)
