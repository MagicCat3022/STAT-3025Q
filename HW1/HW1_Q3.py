import sys
curr_path = sys.path[0]
sys.path.insert(1, f'{curr_path}/..')
import STAT3025_Tools.Stat_Tools as ST

data = '''
16 18 18 26 33 41 54 56 66 68 87 91 95 98 106 109 111 118 127 127 135 145 147 149 151 168 172 183 189 190 200 210 220 229 230 233 238 244 259 294 329 403
'''
data = data.strip().split(' ')
data = [int(x) for x in data]
data.sort()
print(data)


ST.print_statistical_values(data)
ST.construct_boxplot(data)