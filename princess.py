# tutorial
from sys import stdin, stdout

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    used = [False for i in range(n)]
    v = -1
    for i in range(n):
        l = [int(x) - 1 for x in stdin.readline().split()][1:]
        for j in l:
            if not used[j]:
                used[j] = True
                break
        else:
            v = i
    if v == -1:
        stdout.write("OPTIMAL\n")
    else:
        u = used.index(False)
        stdout.write("IMPROVE\n" + str(v + 1) + " " + str(u + 1) + "\n")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# my code

# import numpy as np 

# for _ in range(int(input())):
#     count=0
#     p=int(input())
#     p_c=np.zeros((p,p))
#     pr=np.arange(1,p+1)
#     # print(p_c,pr) 

#     for i in range(p):
#         x=list(map(int,input().split()))[:p+1]
#         # print(x)
#         y=x[1:]
#         while len(y)!=p:
#             y.append(None)
#         # print(y)
#         p_c[:,i]=y
#         # print(p_c)

#     for i in range(p):
#         for j in range(p):
#             if(p_c[j][i] in pr and not 0):
#                 temp=np.where(pr==p_c[j][i])
#                 pr[temp]=0
#                 p_c[:,i]=0
#                 # print(pr)
#                 break
#     # print("#",p_c)
#     for q in range(p):
#         if(pr[q]!=0):
#             for i in range(p):
#                 for j in range(p):
#                     if (p_c[j][i]!=pr[q] and p_c[j][i]!=0 and count!=1) :
#                         print('IMPROVE')
#                         # print(pr)
#                         print(i+1,pr[q])
#                         pr[q]=0
#                         count=1
#                         break
#     if(count==0):
#         print('OPTIMAL')