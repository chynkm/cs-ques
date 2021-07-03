#!/bin/python3

# Hikes always start and end at sea level, and each step up or down
# represents a  unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level,
# starting with a step up from sea level and ending with a step down
# to sea level.
# A valley is a sequence of consecutive steps below sea level, starting
# with a step down from sea level and ending with a step up to sea level.

# The hiker first enters a valley  units deep. Then they climb out
# and up onto a mountain  units high. Finally, the hiker returns to
# sea level and ends the hike.


def countingValleys(steps, path):
    v = vc = 0
    for i in list(path):
        if i == 'D':
            if v == 0:
                vc += 1
            v -= 1
        else:
            v += 1

    print(vc)


steps = 8
path = 'DDUUUUDD'
path = 'UDUDUD'

countingValleys(steps, path)
