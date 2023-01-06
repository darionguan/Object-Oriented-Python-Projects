def add_time(start, duration, day = NULL):
    new_time = to_army(start)
    new_time = add_min(new_time, duration)
    new_time = add_hour(new

    return new_time

def to_army(start):
    am_or_pm = start[-2:]
    hour = 0
    start = start[:-3]
    start = start.split(':')
    hour = start[0]
    hour = int(hour)
    if am_or_pm == 'PM':
        hour += 12
    army_time = str(hour) + ':' + start[1]
    return army_time

def add_min(start, duration):
    days = 0
    start = start.split(':')
    start[0] = int(start[0])
    start[1] = int(start[1])
    duration = duration.split(':')
    duration[0] = int(duration[0])
    duration[1] = int(duration[1])
    while duration[1] > 0:
        duration[1] -= 1
        start[1] += 1
        if start[1] == 60:
            start[1] = 0
            start[0] += 1
        if start[0] == 24:
            start[0] = 0
            days += 1
    start[0] = str(start[0])
    start[1] = str(start[1])
    army_time = str(start[0]) + ':' + str(start[1])
    return [army_time, days]

def add_hour(start, duration):
    days = start[1]
    start = start[0]
    start = start.split(':')
    start[0] = int(start[0])
    duration = duration.split(':')
    duration[0] = int(duration[0])
    while duration[0] > 0:
        duration[0] -= 1
        start[0] += 1
        if start[0] == 24:
            start[0] = 0
            days += 1
    start[0] = str(start[0])
    if len(start[1]) < 2:
        start[1] = '1' + start[1]
    army_time = str(start[0]) + ':' + str(start[1])
    return [army_time, days]

def am_or_pm(new_time):
    time_of_day = 'AM'
    new_time[0].split(':')
    new_time[0][0] = int(new_time[0][0])
    if new_time[0][0] == 0:
        new_time[0][0] += 12
    if new_time[0][0] >= 12:
        new_time[0][0] -= 12
        time_of_day = 'PM'
    not_army = str(new_time[0][0]) + ':' + new_time[0][1] + time_of_day
    return [not_army, new_time[1]]

def day_to_num(day):
    day = day.lower()
    if day == 'monday':
        return 1
    elif day == 'tuesday':
        return 2
    elif day == 'wednesday':
        return 3
    elif day == 'thursday':
        return 4
    elif day == 'friday':
        return 5
    elif day == 'saturday':
        return 6
    else:
        return 7

def num_to_day(day):
    if day == 1:
        return 'Monday'
    elif day == 2:
        return 'Tuesday'
    elif day == 3:
        return 'Wednesday'
    elif day == 4:
        return 'Thursday'
    elif day == 5:
        return 'Friday'
    elif day == 6:
        return 'Saturday'
    else:
        return 'Sunday'
    
def day_modifier(new_time, day):
    if new_time[1] == 0:
        return [new_time[0], 'same day']
    elif new_time[1] == 1:
        return [new_time[0], 'next day']
    else:
        days_added = new_time[1]
        days_later = new_time[1]
        while days_added > 0:
            days_added -= 1
            day += 1
            if day == 8:
                day = 1
        return [new_time[0], num_to_day(day), str(days_later)]

def show_time(new_time):
    if new_time[1] == 'same day':
        return new_time[0]
    elif new_time []