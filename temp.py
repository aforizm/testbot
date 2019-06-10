from datetime import datetime
import sqlite3
'''
Список переменных которе нужны
count       - счетчик дней, с момента последнего обнуления
lastDateRes - дата последнего сброса
today		- сегодняшняя дата
maxCount 	- Рекорд дней без сборса счетчика

потом надо бужет сделать переменную  ID пользователя

Подключить БД и работа с ней.
'''
frm = '%Y,%m,%d'
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

c.execute("select lastDateRes from counts where user=1 ")
lastDateRes = c.fetchone()
lastDateRes = datetime.strptime(str(lastDateRes).strip('"(), \''),frm)
print(lastDateRes)

c.execute("DELETE from counts where user=45")

conn.commit()
for r in c.execute("SELECT * from counts"):
	print(r)
conn.close()

today = datetime.today()

def check():
	'''Проверка счетчика'''
	global lastDateRes
	if lastDateRes!= today:
		count = today - lastDateRes
		count = count.days
		if count > data['maxCount']:
			data['maxCount'] = count
			print('Идешь на рекорд\n')

		print('Прошло %i дней\nРекорд: %i\nДата последнего сброса %s\n' % (count,data['maxCount'] ,lastDateRes))
	else:
		print('Прошло меньше 24 часов с последнего сброса\n')


def reset():
	'''Сброс счетчика'''
	global lastDateRes
	check()
	lastDateRes = today
	print(lastDateRes)
	print('Счетскик обнулен\n')


if __name__ == '__main__':	
	'''check()
				reset()
				check()'''