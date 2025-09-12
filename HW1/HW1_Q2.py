data = '''
389 356 359 363 375 424 325 394 402 373 373 370 364 366 364 325 339 393 392 369 374 359 356 403 334 397
'''
data = data.strip().split(' ')
data = [int(i) for i in data]
data.sort()
print(data)

sum = 0
for n in data:
    sum += n
print('sum:',sum)
print(f'mean: {sum / len(data)}')

dataLen = len(data)
print(f'length: {dataLen}')
print(f'len/2: {dataLen//2}')
print(f'value 12: {data[12]}')
print(f'value 13: {data[13]}')
median = (data[dataLen//2] + data[dataLen//2 - 1]) / 2

print(f'median: {median}')

data = '''
325, 334, 339, 356, 356, 359, 359, 363, 364, 364, 366, 369, 370, 373, 373, 374, 375, 389, 392, 393, 394, 397, 402, 403
'''
data = data.strip().split(', ')
data = [int(i) for i in data]
data.sort()
print(data)

sum = 0
for n in data:
    sum += n
print('sum:',sum)
print(f'mean: {sum / len(data)}')

print(f'trim %: {1/26*100}%')
print(26*0.038461538461538464)