import time


time.localtime()


# retuns time as a tuple in this format (2026, 2, 16, 12, 33, 55, 0, 47)
# (year, month, day, hour, minute, second, weekday, yearday)



# +- RTC Config +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
 
# has to be redone when system is turned poweroff
# ideally this require 24/7 connected to keep track
# otherwise requires re-config everythime

from machine import RTC


# Initialize the RTC
rtc = RTC()

#  Set the date and time to this format
# Format: (year, month, day, weekday, hour, minute, second, subsecond)
# Weekday: Monday=0, Sunday=6

rtc.datetime((2026, 2, 16, 0, 12, 30, 5, 0))

#  Read the current time
current_time = time.localtime()

print(current_time)

