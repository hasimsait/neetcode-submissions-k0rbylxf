class Path:
    def __init__(self,weight,target):
        self.weight=weight
        self.target=target
class Node:
    def __init__(self,value,neighbors):
        self.value=value
        self.neighbors=neighbors
    def rint(self):
        a=""
        for neighbor in self.neighbors:
            a+=str(neighbor.target)+" "+str(neighbor.weight)+","
        return str(self.value) + ": "+a
class Solution:
    shortest = Dict[int,int]
    

    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        nodes = {}
        costs = {}
        for i in range(n):
            nodes[i] = Node(i,[])
        for edge in edges: # infinite loop when edge negative
            nodes[edge[0]].neighbors.append(Path(edge[2],edge[1]))
        
        def visit(node,existing_cost):
            if node.value not in costs:
                costs[node.value]=existing_cost
            else:
                costs[node.value]=min(existing_cost,costs[node.value])
            for neighbor in node.neighbors:
                cost = existing_cost + neighbor.weight
                tnode = nodes[neighbor.target]
                if neighbor.target not in costs or costs[neighbor.target]>cost:
                    visit(tnode,cost)
        visit(nodes[src],0)
        for node in nodes:
            if node not in costs:
                costs[node]=-1
        return costs

