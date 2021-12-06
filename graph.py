d = {}
max_node = ""

class Node:
    def __init__(self,x):
        self.x = x
        self.nxt = []
        
        


def distance_of_route(arr):
    n = len(arr)
    i = 1
    route = True
    val = 0
    while i < n:
        start = arr[i-1]
        end = arr[i]
        present = 0
        for k in d[start].nxt:
            if d[end] == k[0]:
                val += k[1]
                present = 1

        if(present):
            i += 1
        else:
            route = False
            break
    if(not route):
        return "NO SUCH ROUTE"
    return val
            
def count_trips(x,y,cnt,m):
    if cnt > m:
        return 0
    
    if x == y and cnt > 1:
        return 1

    ans = 0
    for i in x.nxt:
        if(x != y):
            ans += count_trips(i[0],y,cnt+1,m)
        else:
            ans += count_trips(i[0],y,cnt,m)
    return ans
        

def shortest_path(x,y):
    
    def find_length(parent,weight,j):
        if j not in parent:
            return 0
        short_len = weight[parent[j] + j]
        
        l = find_length(parent, weight, parent[j])
        short_len += l
        
        return short_len
        
    
    
    vis = {}
    parent = {}
    weight = {}
    queue = []
    f = 0
    
    queue.append(x)
    vis[x] = True
    
    while queue:
        s = queue.pop(0)
        if s == y and len(parent):
            return find_length(parent, weight, s)

        
        for i in d[s].nxt:
            if i[0].x not in vis:
                queue.append(i[0].x)
                vis[i[0].x] = True
                parent[i[0].x] = s
                weight[ s + i[0].x ] = i[1]
                
            
    
    

l = list(map(str,input().split(', ')))
for i in l:
    if i[0] not in d:
        d[i[0]] = Node(i[0])
    if i[1] not in d:
        d[i[1]] = Node(i[1])
    max_nodes = max(i[0],i[1],max_node)
    
    d[i[0]].nxt.append( [d[i[1]], int(i[2])])


# First 1 to 5 test cases in question, to find the distance between the routes provided
route = distance_of_route("ABC")
print("1. " + str(route))
route = distance_of_route("AD")
print("2. " + str(route))
route = distance_of_route("ADC")
print("3. " + str(route))
route = distance_of_route("AEBCD")
print("4. " + str(route))
route = distance_of_route("AED")
print("5. " + str(route))

# Next 6 and 7 test cases in question, to find the
# The number of trips with given start and end node and with max of K nodes
trips = count_trips(d["C"],d["C"],1,3)
print("6. " + str(trips))
trips = count_trips(d["A"],d["C"],1,4)
print("7. " + str(trips))

# Next 8 and 9 test cases in question, to find shortest_path between source and destination
short_route = shortest_path("A","C")
print("8. " + str(short_route))
short_route = shortest_path("B","B")
print("9. " + str(short_route))


        
