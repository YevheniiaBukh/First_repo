# from datetime import datetime

# current_date = datetime.now()
# date_today = datetime.today()

# import datetime
# current_date = datetime.datetime.now()
# date_today = datetime.datetime.today()

# print(current_date)
# print(date_today)

# print(current_date.date())
# print(current_date.time())

# print(current_date.day, current_date.year, current_date.month, current_date.hour)

######################################
#timedelta

# current_date = datetime.now()
# print(current_date)

# interval = timedelta(days=45)
# day_on = current_date-interval
# day_off = current_date+interval

# print(day_on)
# print(day_off)
# count_days = day_off-day_on
# print(count_days.days)

# ###################################

# current_date = datetime.now()
# print(current_date)

# interval = timedelta(weeks=45)
# day_on = current_date-interval
# day_off = current_date+interval

# print(day_on)
# print(day_off)
# count_days = day_off-day_on
# print(count_days.days)

#########################

#timestamp

# current_date = datetime.now()
# print(current_date.timestamp())

# day_zero = datetime.fromtimestamp(0)
# print(day_zero)

# print (current_date > day_zero)


# datetime_string = '1970:01:01 January Jan 02 02 00'
# print(datetime.strptime(datetime_string, '%Y:%m:%d %B %b %H %I %M'))
# print(current_date.strftime('%Y-%m:%d'))

#################


# current_date = '2024-03-01'

# requesterd_day = datetime.strptime(current_date, '%Y-%m-%d').date()
# print(requesterd_day)

# today_date = datetime.now().date()
# print(today_date)
# diff_day = today_date - requesterd_day
# print('days', diff_day.days)

# print('weeks',round(diff_day.days // 7))


##########################


# from datetime import datetime

# day_2021 = datetime(year=2021, month=4, day=7, hour=12).date()
# print(day_2021)


######################

# from datetime import datetime, date
# days_name = {
#     0: "Monday",
#     1: "Tuesday",
#     2: "Wednesday",
#     3: "Thursday",
#     4: "Friday",
#     5: "Saturday",
#     6: "Sunday",
# }

# def day_of_year(full_date):
#     year, month, day = full_date.split('-')
#     day_of_week = datetime(year=int(year), month=int(month),day=int(day)).weekday()
#     return days_name.get(day_of_week)

# print(day_of_year('2021-02-13'))

############################

# Генерація випадкових чисел

# import random

# print(random.randint(0, 100))
# print(random.randrange(0, 100, 7))
# print(random.choice(['black', 'white', 'red']))
# print(random.choices(['black', 'white', 'red'], k=6, weights=[1, 7, 5]))

# range_list = list(range(10))
# print(range_list)
# random.shuffle(range_list)
# print(range_list)


############################


# from random import randint, sample
# min_value = -10
# max_value = 10
# length = 10


# result_array = set()

# while len(result_array) != length:
#     result_array.add(randint(min_value, max_value))
    
# print(sorted(list(result_array)))

# print(sorted(sample(range(min_value, max_value), length)))

################################

# math

# from math import sqrt, pow, pi, cos

# print(cos(sqrt(pow(pi, 5))))