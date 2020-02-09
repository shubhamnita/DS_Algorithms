## Iterative Approach:

def dfs(g,N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    # code here
    visited = set()
    stack = []
    stack.append(0)
    visited.add(0)
    while len(stack)!=0:
        top = stack.pop()
        print(top,end=' ')
        for ele in g[top]:
            if ele not in visited:
                stack.append(ele)
                visited.add(ele)


# Recursive Approach:

def dfs(g,N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    # code here
    visited = set()
    dfsUtil(0,g,visited)

def dfsUtil(start,g,visited):
    visited.add(start)
    print(start,end=' ')
    for i in g[start]:
        if i not in visited:
            dfsUtil(i,g,visited)