# Task 0.8

def to_hrs_and_minutes(num):
    hours = num//60
    minutes = num % 60

    if hours > 1 and minutes > 1 or hours == 0 and minutes == 0:
        print (f"{hours} hours, {minutes} minutes")

    elif minutes <= 1 and hours <= 1:
        print(f"{hours} hour, {minutes} minute")

    elif hours > 1 and minutes == 1:
        print (f"{hours} hours, {minutes} minute")

    else:
        print (f"{hours} hour, {minutes} minutes")


to_hrs_and_minutes(0)
