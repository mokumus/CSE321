def bfs(graph, start):
    traversed = {}
    q = []
    order = [start]
    q.append((start, 0))
    while q:
        node, dist = q.pop(0)
        traversed[node] = dist
        if node in graph : #IF NODE HAS A PARENT
            for parent in graph[node]:
                queue_members = [x[0] for x in q]
                if parent not in traversed and parent not in queue_members: # IF NOT ALREADY TRAVERSED
                    q.append( (parent, dist+1) )
                    order.append(parent)
    return order


def dfs(graph, start):
    traversed = {}
    s = []
    order = []
    s.append((start, 0))
    while len(s) > 0 :
        node, dist = s.pop()
        order.append(node)
        traversed[node] = dist
        if node in graph :
            for parent in graph[node] :
                stack_members = [x[0] for x in s]
                if parent not in traversed and parent not in stack_members :
                    s.append((parent, dist+1))
                    
    return order




