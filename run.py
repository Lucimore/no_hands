import datetime
import os

begin_time = datetime.datetime.now()

os.system('py chrome.py')
print("%-40s " % "Chrome Done! Total Time: ", datetime.datetime.now() - begin_time)
os.system('py chrome_64.py')
print("%-40s " % "Chrome_64 Done! Total Time: ", datetime.datetime.now() - begin_time)
# os.system('py ie.py') - Вероятно проблема с WebDriver IE, версии IE на ноуте и вм не совпадают, обновить ие не смог
# print("%-40s " % "IE Done! Total Time: ", datetime.datetime.now() - begin_time)
os.system('py edge32.py')
print("%-40s " % "Edge32 Done! Total Time: ", datetime.datetime.now() - begin_time)
os.system('py edge64.py')
print("%-40s " % "Edge64 Done! Total Time: ", datetime.datetime.now() - begin_time)
os.system('py firefox64.py')
print("%-40s " % "Firefox64 Done! Total Time: ", datetime.datetime.now() - begin_time)

print("""
Не забудь запустить скрипт в папке Firefox32(надо перейти в папку 'cd Firefox32', 'py firefox32.py'), он допишет в отчет.
На данный момент не работает IE на вм - проверяй руками :(
""")