
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes 
now = datetime.now()

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print("Year (2-digit):", now.strftime("%y"))
print("Year (4-digit):", now.strftime("%Y"))
print("Weekday (abbreviated):", now.strftime("%a"))
print("Weekday (full):", now.strftime("%A"))
print("Month (abbreviated):", now.strftime("%b"))
print("Month (full):", now.strftime("%B"))
print("Day of month:", now.strftime("%d"))
print(now.strftime("%a, %B %d, %Y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
print("Locale's date and time:", now.strftime("%c"))
print("Locale's date:", now.strftime("%x"))
print("Locale's time:", now.strftime("%X"))


#### Time Formatting ####
print(now.strftime("%I:%M:%S %p"))
# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("%H:%M:%S"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%H:%M"))
print(now.strftime("%I %p"))
print(now.strftime("%H"))
