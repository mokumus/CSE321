#--------QUESTION 1
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
#------------------ 
#------------------
#------------------    
#--------QUESTION 3
# Find the first occurance of index = arr[index] with binary search
def binarySearch(arr, left, right):
    if right >= left : 
        mid = (left + right)//2

    if mid is arr[mid] : #Check if index == array[index]  
        return mid 
      
    if mid > arr[mid] : 
        return binarySearch(arr, (mid + 1), right)


    if mid == 0 and arr[mid] == mid :
        return 0;    

    if mid == 0 and arr[mid] != mid :
        return -1

    if mid != 0 : 
        return binarySearch(arr, left, (mid - 1)) 
      
    return -1
#------------------ 
#------------------
#------------------    
#--------QUESTION 5
# Return if a given key is in list of pairs.
# Pre: List constructed with sublists of size 2
#      which first element is a key and second element is a value.
#      And a key in type of string.
# Post: No side effects.
# Return: True if value exists for a key, false otherwise.
def isToken (mapOfTokens, value) :
    for x in mapOfTokens :
        temp = stringToList(x[1])
        if temp == value :
            return True
    return False

# Converts a string literal to list of chars
# Pre: None
# Post: No side effects
def stringToList(string) : 
    chars = []
    for c in string :
        chars.append(c.lower())
    return chars

# Wrapper function for pattern validation
# Checks if the given string is constructed by the provided pattern
def isPatternValid(pattern, string) :
    token = []
    stringAsChars = stringToList(string)
    stringAsChars.reverse()
    return validation(pattern, stringAsChars, token)

# This function should be called via the wrapper, do not call this on its own
# Pre: A dictionary of posible tokens 
#      A string construtcted as list of characters
#      An empty list for temporary tokens 
# Post: Provided list of characters will be deleted
def validation(pattern, string, token) :
    if len(string) == 0 and len(token) > 0 and isToken(pattern,token):
        return True

    if isToken(pattern, token) and len(string) >= 1 :
        token = []
        return validation(pattern, string, token)

    if len(string) >= 1:
        token.append(string.pop())
        return validation(pattern, string, token)

    else :
        return False




