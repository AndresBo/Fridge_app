import datetime

# current date:
now = datetime.datetime.now()
day_number = (now.strftime("%d"))
day_name = (now.strftime("%A"))
month_name = (now.strftime("%B"))
year = (now.strftime("%Y"))

print(f"Today is {day_name} the {day_number} of {month_name}, {year}")
