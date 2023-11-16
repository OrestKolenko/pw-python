from datetime import datetime
from datetime import timedelta
now = datetime.now()
date_first = datetime(2005, 8, 27) # <--- Tutaj wprowadź swoją datę urodzenia
day = now - date_first
print(day.days)

def numbers():
    return '01-11-2023'
def set_numbers(date:str):
    return '01-11-2023'

from datetime import datetime

roznica = (datetime.now())-(datetime.strptime("01/01/1900 00:00", "%d/%m/%Y %H:%M"))
print (roznica)

# from datetime import datetime
# import calendar
# now = datetime.now()
# print(now.strftime("%U"))

from datetime import datetime
import calendar
date_object = datetime.strptime("2023-11-15","%Y-%m-%d")
print(date_object.strftime("%U"))

