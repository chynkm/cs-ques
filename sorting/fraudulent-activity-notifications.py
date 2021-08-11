# https://stackoverflow.com/a/58271130
# Counting sort will not work for negative and floating point values
# unless modified

from statistics import median
from bisect import bisect_left, insort


def activityNotifications1(expenditure, d):
    notifications = 0
    if len(expenditure) <= d:
        return notifications

    i = 0
    for x in range(d, len(expenditure)):
        computed_median = median(expenditure[i:x])
        if expenditure[d] >= computed_median * 2:
            notifications += 1

        i += 1

    return notifications


def computed_median(sorted_expenditure, d):
    m = d//2
    # even median
    if d % 2 == 0:
        return sum(sorted_expenditure[m-1:m+1])/2

    return sorted_expenditure[m]


def findMedian(cntarr, d):
    cnt = 0
    rslt = 0

    if d % 2 != 0:
        for i in range(len(cntarr)):
            cnt += cntarr[i]

            if cnt > d//2:
                rslt = i
                break
    else:
        first = 0
        second = 0

        for i, _ in enumerate(cntarr):
            cnt += cntarr[i]
            if first == 0 and cnt >= d//2:
                first = i
            if second == 0 and cnt >= d//2 + 1:
                second = i
                break
        rslt = (first+second) / 2
    return rslt


def activityNotifications(expenditure, d):
    notifications = 0
    count_arr = [0 for _ in range(201)]

    for i in range(d):
        count_arr[expenditure[i]] += 1

    print(count_arr)

    for i in range(d, len(expenditure)):
        my_median = findMedian(count_arr, d)
        # my_median = computed_median(count_arr, d)
        if expenditure[d] >= my_median * 2:
            notifications += 1

        count_arr[expenditure[i-d]] -= 1
        count_arr[expenditure[i]] += 1

    return notifications


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
# expenditure = [1, 2, 3, 4, 4]
# d = 5
# expenditure = [10, 20, 30, 40, 50]
# d = 3
print(activityNotifications(expenditure, d))
