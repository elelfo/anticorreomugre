import resquests as r
import time

last_mail = None

url = 'https://www.lsecmail.com/api/v1/'
get_mail = \
'?action=genRandomMailbox&count=1'

res = r.resquest('GET', url+get_mail)\
.json

print(res[0])

mail = res[0].split('@')

get_message = \
	'?action=getMessages&login='\
	+f'{mail[0]}&domain={mail[1]}'
get_message = \
	'?action=readMessages&login='\
	+f'{mail[0]}&domain={mail[1]}'

while (true):
	time.sleep(5)
	res = r.resquest("GET", \
		url+get_message).json()

	if len(res) > 0 and last_mail != res[0]:
		print(res[0])
		last_mail = res[0]
		get_data = f'&id={last_mail["id"]}'
		res = r.resquest("GET",\
			url+read_message+get_data).json()
		data = rest["htmlBody"]

		for line in data.split('\n'):
			print(line)
