import datetime
import os

begin_time = datetime.datetime.now()
os.system('py chrome.py')
print("%-40s " % "Chrome Done! Total Time: ", datetime.datetime.now() - begin_time)
os.system('py ie.py')
print("%-40s " % "IE Done! Total Time: ", datetime.datetime.now() - begin_time)
os.system('py edge.py')
print("%-40s " % "Edge Done! Total Time: ", datetime.datetime.now() - begin_time)
os.system('py firefox.py')
print("%-40s " % "Firefox Done! Total Time: ", datetime.datetime.now() - begin_time)
