import sys
curr_path = sys.path[0]
sys.path.insert(1, f'{curr_path}/..')
import STAT3025_Tools.Prob_Tools as PT


n = 50
r = 15
section1 = 20
section2 = 30
def PartA():
    total = PT.nCr(n, r)
    sec1 = PT.nCr(section1, 5)
    sec2 = PT.nCr(section2, 10)
    print(f"Total combinations: {total}")
    print(f"Section 1 combinations: {sec1}")
    print(f"Section 2 combinations: {sec2}")
    prob = (sec1 * sec2) / total
    print(f"Probability: {prob}")
    prob2 = PT.hypergeometric_pmf(n, section2, r, 10)
    print(f"Probability using hypergeometric pmf: {prob2}")
PartA()
    
def PartB():
    sum = 0
    for i in range(0,6):
        sec1 = PT.nCr(section1, 5-i)
        sec2 = PT.nCr(section2, 10 + i)
        sum += sec1 * sec2
    total = PT.nCr(n, r)
    prob = sum / total
    print(f"Probability: {prob}")
    
PartB()