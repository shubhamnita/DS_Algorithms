def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    # code here
    visited = set()
    for i in range(n):
        if i not in visited:
            #print('true',i,g)
            
            if dfs_util(i,g,visited,-1):
                return 1
    return 0
    
def dfs_util(i,g,visited,parent):
    visited.add(i)
    #print(visited,parent)
    for j in g[i]:
        if j in visited and j!=parent:
            return 1
        elif j not in visited:
            if dfs_util(j,g,visited,i):
                return 1
    return 0

############## or ################# 
def dfs_util(i,g,visited,parent):
    visited.add(i)
    #print(visited,parent)
    for j in g[i]:
        if j not in visited:
            if dfs_util(j,g,visited,i):
                return 1
        elif j!=parent:
            return 1
    return 0