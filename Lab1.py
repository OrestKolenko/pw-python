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

from datetime import datetime, date, timedelta
import calendar

date = datetime.now()
print(date)
print(date.year)
print(date.strftime("%Y"))