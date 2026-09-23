#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
print(c.formatmonth(2024, 6))

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
print(hc.formatmonth(2024, 6))

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for day in c.itermonthdays(2024, 6):
    print(day)
# loop over the days of a month with their weekday
for day, weekday in c.itermonthdays2(2024, 6):
    print(day, weekday)

# display the names of the days of the week
print("Day names:", list(calendar.day_name))
print("Abbreviated day names:", list(calendar.day_abbr))

# display the names of the months
print("Month names:", list(calendar.month_name))
print("Abbreviated month names:", list(calendar.month_abbr))
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for day_name in calendar.day_name:
    print(day_name)

for month_name in calendar.month_name:
    print(month_name)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for month in range(1, 13):
    # find the first Friday of the month
    month_calendar = c.monthdayscalendar(2024, month)
    first_friday = [day for day in month_calendar[0] if day != 0 and calendar.weekday(2024, month, day) == calendar.FRIDAY]
    if not first_friday:
        first_friday = [day for day in month_calendar[1] if day != 0 and calendar.weekday(2024, month, day) == calendar.FRIDAY]
    print(f"First Friday of {calendar.month_name[month]} 2024 is on day {first_friday[0]}")