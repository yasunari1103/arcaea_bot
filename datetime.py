import datetime
now = datetime.datetime.now()
print(now)
late = now + datetime.timedelta(minutes=30)
print(late)
now_str = now.strftime('%Y/%m/%d %H:%M:%S')
print(type(now_str))
format = '%Y/%m/%d %H:%M:%S'
now_str_datetime = datetime.datetime.strptime(now_str,format)
print(type(now_str_datetime))