t = [
    [-8, -14, -19, -18],
    [25, 28, 26, 20],
    [11, 18, 20, 25]
]

print("Temperature on 4th day at station 2:", t[1][3])
print("Temperature on 1st day at station 3:", t[2][0])
print("Temperatures on 2nd day:", [t[i][1] for i in range(3)])
print("Average temperature at station 3:", sum(t[2]) / len(t[2]))
print("Days and stations with temperatures in the range 24-26 degrees:", [
    (day + 1, station + 1, t[station][day])
    for station in range(3)
    for day in range(4)
    if 24 <= t[station][day] <= 26
])