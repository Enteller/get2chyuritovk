import requests # для работы с пост гет запросами
import json     # для работы с выводами гет запросов
import random   # для гет запроса 
import time     # для таймаута



token = 'токен_группы_вк'
ver = 5.92                 # можно не трогать               
domain = 'ваш_id'
timeo = 55                 # таймаут перед отправкой 

get_2ch_thread = requests.get('https://2ch.hk/aa/res/56163.json') # получение треда
ddd = json.loads(get_2ch_thread.text)

for i in range(0,500): # обход всего треда
	try:
		mes = 'https://2ch.hk'+ddd['threads'][0]['posts'][i]['files'][0]['path']
		print(mes)
		get_message_post = requests.get('https://api.vk.com/method/messages.send',  # get запрос на сообщение ВК
			params = {
				'access_token': token,
				'v': ver,
				'user_id': domain,
				'random_id': random.randrange(0,9999999,1), # рандомное число, чтобы не отправить mes > 1 раза
				'message': mes
				})
		time.sleep(timeo)
	except:
		i = i + 1  # если нет картинки в посте, то едем дальше

#data = json.loads(get_message_post.text) 
