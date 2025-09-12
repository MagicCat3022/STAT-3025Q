import sys
sys.path.insert(1, 'C:\\Users\\AHMET\\Documents\\GitHub\\CS-Stuff\\STAT 3025Q')
import STAT3025_Tools.Prob_Tools as PT

a = PT.nCr(19,4)
b = PT.nPr(6,1)
c = PT.nCr(19,5)
T = PT.nCr(25,5)
print(a,b,c,T)

P = ((a*b)+c)/T
print(P)