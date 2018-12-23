if __name__ == '__main__':
    lines = sorted(tuple(open('input', 'r')))
    shifts = dict()
    currentGuard = ''
    start = 0
    for line in lines:
        parts = line[1:-1].split(' ')
        parts[1] = parts[1][:-1]
        if len(parts) == 6:
            currentGuard = parts[3]
            continue
        if parts[2] == 'falls':
            start = int(parts[1].split(':')[1])
            continue

        currentShift = shifts[currentGuard] if currentGuard in shifts else [0] * 61

        end = int(parts[1].split(':')[1])
        for daysAsleep in range(start, end):
            currentShift[daysAsleep] += 1

        currentShift[60] += (end - start)
        shifts[currentGuard] = currentShift

    for key in shifts.keys():
        print(key, shifts[key])

    targetGuard = ''
    maxHoursAsleep = 0
    for guard in shifts.keys():
        if shifts[guard][60] > maxHoursAsleep:
            targetGuard = guard
            maxHoursAsleep = shifts[guard][60]

    maxDaysAsleep = 0
    targetMinute = 0
    for i in range(len(shifts[targetGuard])-1):
        daysAsleep = shifts[targetGuard][i]
        if daysAsleep > maxDaysAsleep:
            maxDaysAsleep = daysAsleep
            targetMinute = i

    print(targetMinute, targetGuard, targetMinute * int(targetGuard[1:]))
