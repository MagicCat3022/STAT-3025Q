import sys
curr_path = sys.path[0]
sys.path.insert(1, f'{curr_path}/..')
import STAT3025_Tools.Prob_Tools as PT


p = 0.5
r = 3
def PartB():
    EX = r / p
    VX = r * (1 - p) / (p ** 2)
    print(f"E(X) = {EX}")
    print(f"Var(X) = {VX}")

PartB()