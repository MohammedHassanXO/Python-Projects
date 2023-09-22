"""
Build a countdown calculator. Write some code that can take two dates as input, and then calculate the amount of time between them
"""

from datetime import datetime


def countdown(start_date, end_date):
    time_left = start_date - end_date
    return time_left

date_str1 = input("Enter the first date in YYYY-MM-DD format: ")
date_obj1 = datetime.strptime(date_str1, '%Y-%m-%d')

date_str2 = input("Enter the second date in YYYY-MM-DD format: ")
date_obj2 = datetime.strptime(date_str2, '%Y-%m-%d')

print(countdown(date_obj1, date_obj2))