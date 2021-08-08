from statistics import median


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


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
expenditure = [1, 2, 3, 4, 4]
d = 5
expenditure = [10, 20, 30, 40, 50]
d = 3
print(activityNotifications(expenditure, d))
