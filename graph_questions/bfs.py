from collections import defaultdict
def bfs():
    from collections import deque
    d = deque()
    d.append(1)
    d.append(2)
    while(len(d) !=0):
        s=d.popleft()
        print(s)
    print('called')

if __name__ == '__main__':
    g = defaultdict(list)
    g[1].append(2)
    g[1].append(4)
    #for i,lis in dict(g):
    #    print(i,lis)
    print(dict(g))
    bfs()
