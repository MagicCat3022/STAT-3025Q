string = '''
5.4
5.5
4.3
9.0
12.7
11.3
7.4
5.0
3.5
8.2
7.5
6.2
5.8
2.3
3.4
10.4
9.8
6.6
3.7
6.4
5.4
4.8
7.5
6.0
6.9
10.8
7.5
6.6
5.0
3.3
11.2
10.5
14.3
8.0
8.8
6.4
5.1
5.6
9.6
7.5
4.6
12.3
7.1
7.0
4.0
9.2
6.7
6.9
11.5
5.1
8.3
6.5
7.6
9.3
9.2
7.3
5.0
6.3
13.8
6.2
7.6
3.9
11.9
2.2
15.0
7.2
6.1
15.3
18.9
7.2

'''
string = string.strip().split('\n')
string = [float(i) for i in string]
string.sort()
print(string)

intervals: list[tuple[str, int]] = []
currInterval = 2
currTotal = 0
i = 0
while i < len(string):
    if string[i] < currInterval:
        currTotal += 1
        i += 1
    else:
        print(string[i], currInterval)
        intervals.append((f'{currInterval-2}-{currInterval}', currTotal))
        currInterval += 2
        currTotal = 0
intervals.append((f'{currInterval-2}-{currInterval}', currTotal))
        
print(intervals)
print(len(string))

relative_freq: list[tuple[str, float]] = []
for (a,b) in intervals:
    relative_freq.append((a, b / len(string)))
print(relative_freq)
sum_freq = 0
for (a,b) in relative_freq:
    sum_freq += b
print(sum_freq)