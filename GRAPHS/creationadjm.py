# adj matrix

n,m=map(int,input().split())
adj=[]
for i in range(n+1):
    eachrow=[0]*(n+1)
    adj.append(eachrow)

for i in range(m):
    u,v=map(int,input().split())
    adj[u][v]=1
    adj[v][u]=1

print(adj)

# adj list representation

n,m=map(int,input().split())
adj=[]
for i in range(n+1):
    adj.append([])

for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

print(adj)