import sys
curr_path = sys.path[0]
sys.path.insert(1, f'{curr_path}/..')
import STAT3025_Tools.Prob_Tools as PT


n = 25
p = 0.05

def partA():
    answer = PT.binomial_pmf(n, p, 2)
    print(f'Part A: {answer:.4f}')
    
def partB():
    a = PT.binomial_cdf(n, p, 4)
    b = 1 - PT.binomial_cdf(n, p, 1)
    answer = a - b
    print(f'Part B: {answer:.4f}')
    
def partC():
    answer = n*p
    print(f'Part C: {answer:.4f}')
    
def partD():
    answer = (n*p*(1-p))**0.5
    print(f'Part D: {answer:.4f}')
    