
import numpy as np
import csv
import math
import sys

from queue import PriorityQueue


class Edge:
    def __init__(self, n1, n2, cost):
        self.n1 = n1
        self.n2 = n2
        self.cost = cost

class Node:
    def __init__(self, xy, id):
        self.edges = []
        self.xy = xy
        self.id = id
        self.nCost = sys.maxsize   #Start cost at infinity
        self.onPath = False     #On current path
        self.checked = False    #Node checked or not
        self.prev = self        #Set previous node to self by default

    def addEdge(self, nextNode, edgeCost):
        e = Edge(self, nextNode, edgeCost)
        self.edges.append(e)    #Add new edge to edges list
    
    def getNextPathID(self):    #loop through all edges finding the next one and returning when it finds the right one
        return 1
    
    def __lt__(self, other):    #Overload node less than
        return self.nCost < other.nCost

class Graph:
    def __init__(self, grid):
        self.grid = grid
        shape = grid.shape
        self.xCount = shape[1]
        self.yCount = shape[0]
        self.nodes = {}

        self.S = (0, 0)
        self.G = (0, 0)

        self.createGraph(self.xCount, self.yCount, grid)  #Create our graph
    
    def getWeight(self, n):
        if (n.id == "X"):    #Empty node
            return -1
        if (n.id == "S"):   #Check node start 
            self.S = n
            return 0
        if (n.id == "G"):   #Check node end
            self.G = n
            return 0
        else:   #If a normal weighted node
            return int(n.id)    
    
    def createGraph(self, xCount, yCount, grid):
        for j in range(xCount): #Create all our nodes
            for i in range(yCount):
                #print(grid[j, i])  print node at time
                newNode = Node((i, j), grid[i, j])
                self.nodes[j, i] = newNode
        
        for i in range(xCount):   #Create all our edges
            for j in range(yCount):   
                node1 = self.nodes[j, i]

                n1Weight = self.getWeight(node1)                
                if (n1Weight == -1):    #Empty node
                    continue

                if (j + 1 < yCount):    #If theres a node to the right of the current node, link them together                    
                    node2 = self.nodes[j+1, i]
                    n2Weight = self.getWeight(node2)                
                    if (not n2Weight == -1):    #Empty node
                        node1.addEdge(node2, n2Weight)    #Adds edge between nodes          
                        node2.addEdge(node1, n1Weight)    #Adds edge between nodes     

                if (i + 1 < xCount):    # if theres a node below the current node, link them together
                    node2 = self.nodes[j, i+1]
                    n2Weight = self.getWeight(node2)                
                    if (not n2Weight == -1):    #Empty node
                        node1.addEdge(node2, n2Weight)    #Adds edge between nodes          
                        node2.addEdge(node1, n1Weight)    #Adds edge between nodes     
        

# inputFileName contains a CSV file with the input grid
# optimalPathFilename is the name of the file the optimal path should be written to
# exploredListFilename is the name of the file the list of explored nodes should be written to
def pathfinding(inputFileName, optimalPathFilename, exploredListFilename):
    #Import CSV
    csv = np.genfromtxt("Example1\input.csv", delimiter=",", dtype="str")
    csv = np.char.strip(csv)

    print(csv)
    g = Graph(csv)  #Create Graph and Link nodes

    pq = PriorityQueue()

    """MIGHT NEED TO REVERSE THE xy's so 0 is first and 1 is second"""
    g.nodes[g.S.xy[1], g.S.xy[0]].nCost = 0  #Start node cost at 0
    sNode = g.nodes[g.S.xy[1], g.S.xy[0]] #Physical start node
    pq.put((0, sNode))   #Priority queue start node
    gNode = g.nodes[g.G.xy[1], g.G.xy[0]] #Physical goal node
    
    checked = []
    

    #Pathfind
    while (not pq.empty()):   
        lowest = pq.get()   #Get lowest code node

        #Explore node
        lowest = lowest[1]    #Lowest node
        checked.append(lowest.xy)   #Add to our checked list
        print("Explore: " + str(lowest.xy) + " - Explored: " + str(checked))
        neighbours = lowest.edges  #Nearby edges

        if (lowest.xy == gNode.xy):   #Reached end node     
            print("REACHED END NODE")  
            break

        for i in range(len(neighbours)):    #neighbours[i].n2 is the current node we're checking         
            if (lowest.prev.xy == neighbours[i].n2.xy): #Prevents checking the node that this node came from
                continue
            estimate = 0    #No estimate yet
            nodeCost = neighbours[i].cost + estimate     #Edge cost + heuristic estimate
            neighbours[i].n2.checked = True
            print("\tChecking: " + str(neighbours[i].n2.xy))

            #Update node based on search
            if (neighbours[i].n2.nCost > nodeCost):  #If nodes cost is larger than calculated, update node, add node to queue
                neighbours[i].n2.nCost = nodeCost    #Update node cost
                neighbours[i].n2.prev = lowest      #Set new route node (lowest cost to node)

                pq.put((nodeCost, neighbours[i].n2))    #Add node to queue    
                print("\t\tUpdating Cost From " + str(neighbours[i].n2.nCost) + " to " + str(nodeCost))
    
    print("done")

    finishedList = [gNode.xy]
    cost = 0

    curNode = g.nodes[gNode.xy[0], gNode.xy[1]]
    while(curNode.xy != sNode.xy):
        curNode = curNode.prev
        finishedList.append(curNode.xy)
        cost += curNode.nCost

    finishedList.reverse()
    print("Order = " + str(finishedList))
    print("Cost = " + str(cost))


    optimalPathCost = 0

    return optimalPathCost


def main():
    cost = pathfinding("a", "a", "a")

    return

if (__name__ == "__main__"):
    main()