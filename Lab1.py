# # Fibonacci 
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# def fib2(n):   
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result

# from datetime import datetime, date, timedelta
# import calendar

# date = datetime.now()
# print(date)
# print(date.year)
# print(date.strftime("%Y"))

# print(date.strftime("%B"))

# print(date.strftime("%A"))

# date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
# print(date_object)

# date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
# print(date_object)

# date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
# new_date = date_object + timedelta(days=5)
# print(new_date)

# print(date-timedelta(weeks=2))

# new_year = datetime.strptime("2023-Jan-1", "%Y-%b-%d")
# print((date - new_year).days)

# new_year = calendar.isleap(2024)
# print(new_year)

# print(date.strftime("%U"))


# rfc_date = datetime.strptime('2023-11-15 00:00:00', "%Y-%m-%d %H:%M:%S").strftime("%a, %d %b %Y %H:%M:%S %z")
# print(rfc_date)

# p_date = datetime(date.year, 7, 4)
# print(p_date.strftime("%A"))


# poczatek_roku=datetime(date.year,1,1)
# czas_uplyniety=(date - poczatek_roku).total_seconds()
# print(czas_uplyniety)

# this_date=datetime(2023, 11, 15)
# now_date=datetime.now()
# if this_date < now_date:
#     print("True")
# else:
#     print("False")

# rfc_date = datetime.strptime('2023-11-15 14:30:00', "%Y-%m-%d %H:%M:%S").strftime("%d  %Y %H:%M:%S %z")
# print(rfc_date)
