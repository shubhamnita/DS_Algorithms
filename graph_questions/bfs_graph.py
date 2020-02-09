from collections import defaultdict
import queue

def bfs(g,N):
    # code here
    visited = set()
    for i in range(N):
        if i not in visited:
            bfs_int(g,i,visited)

def bfs_int(g,v,visited):
    q = queue.Queue()
    q.put(v)
    visited.add(v)
    while not q.empty():
        fi = q.get()
        print(fi,end=' ')
        for i in g[fi]:
            if i not in visited:
                q.put(i)
                visited.add(i)


if __name__ == '__main__':
    # n : number of nodes
    # e: number of edges
    # edges: list of edges between two nodes of directed graph 
    n,e = map(int,input.strip().split())
    edges = list(map(int,input().strip().split()))
    g = defaultdict(list)
    for i range(o,len(e),2)
        u,v = edges[i],edges[i+1]
        g[u].append(v)
    #g[1].append(2)
    #g[1].append(4)
    #g[0].append(1)
    #g[2].append(3)
    bfs(g,n)



################################# Second approach which print graph only from vertex 0
def bfs(g,N):

visited=[False]*N
queue=[]
queue.append(0)
visited[0]=True
while queue:
    s=queue.pop(0)
    print(s,end=" ")
    for i in g[s]:
        if visited[i]==False:
            queue.append(i)
            visited[i]=True


