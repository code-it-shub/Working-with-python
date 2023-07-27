from collections import defaultdict

lis = [[2,1,1],[1,1,0],[0,1,1]]
adj_list=defaultdict(list)
for i,j,k in lis:
    adj_list[i].append(j)
    adj_list[j].append(i)

print(adj_list)


liss= []
liss.append(1,2)