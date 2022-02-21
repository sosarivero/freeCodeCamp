def add_time(start, duration, weekday=None):
    # Handles edge case of user inputting no time
    if duration == '0:00':
        return start
    # Splits the starting time into three strings.
    # Then convert the numbers into integers.
    start = start.replace(':', ' ').split()
    start_hours = int(start[0])
    start_minutes = int(start[1])
    # Convert the time to 24h format for easier calculations.
    if start[2] == 'PM':
        start_hours += 12

    # Splits the duration time and then converts into integers.
    duration = duration.split(':')
    add_hours = int(duration[0])
    add_minutes = int(duration[1])

    # Sums the hours
    hours_sum = start_hours + add_hours
    # Sums the minutes
    minutes_sum = start_minutes + add_minutes
    # Overflow of minutes
    rest_minutes = minutes_sum % 60

    if rest_minutes != minutes_sum:
        # Adds hours according to the overflow of minutes
        hours_sum += int(minutes_sum / 60)

    # Sets a next day counter according to the overflow of hours
    day_counter = int(hours_sum / 24)

    # Sets a default value of meridem. Changes to PM if the hour is after 11AM.
    meridem = 'AM'
    if hours_sum % 24 > 11:
        meridem = 'PM'

    # Calculate the final hour mark
    final_hour = 0
    if int(hours_sum / 12) > 0:
        final_hour = hours_sum % 12
        # I personally think this is wrong, but test wants midnight and noon to show 12 rather than 00.
        if final_hour == 0:
            final_hour = 12

    # Sets the hour and minute mark into strings to concatenate
    final_hour = str(final_hour)
    rest_minutes = str(rest_minutes)
    # If the minute is only one digit, adds 0 for formatting.
    if len(rest_minutes) == 1:
        rest_minutes = '0' + rest_minutes

    # Concatenates everything
    new_time = final_hour + ':' + rest_minutes + ' ' + meridem

    # Checks if user input optional weekday argument
    if not weekday is None:
        # Sets weekday to capitalize
        weekday = weekday.capitalize()
        # List of weekdays
        weekdays = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
        # Checks which will be the final day using the day_counter
        newday_index = (weekdays.index(weekday) + day_counter) % 7
        newday = weekdays[newday_index]
        # Adds final day info to the output
        new_time += f', {newday}'

    # Adds day_counter information to the output
    if day_counter == 1:
        new_time += ' (next day)'
    elif day_counter > 1:
        new_time += f' ({day_counter} days later)'

    return new_time
