
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
        self.oriCost = 0        #Original cost to calculate total cost at the end
        self.heuri = 0          #Heuristic Estimate
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
        self.G = []

        self.createGraph(self.xCount, self.yCount, grid)  #Create our graph
    
    def getWeight(self, n):
        if (n.id == "X"):    #Empty node
            return -1
        if (n.id == "S"):   #Check node start 
            self.S = n
            dummyNode = Node((-1, -1), "dummy")
            dummyNode.heuri = 0 #Helps with the first node calculations
            n.prev = dummyNode
            return 0
        if (n.id == "G"):   #Check node end
            self.G.append(n)
            return 0
        else:   #If a normal weighted node
            return int(n.id)    
    
    def createGraph(self, xCount, yCount, grid):
        for i in range(xCount): #Create all our nodes
            for j in range(yCount):
                newNode = Node((i, j), grid[i, j])          #Create new node
                newNode.oriCost = self.getWeight(newNode)   #Original Node Cost
                self.nodes[i, j] = newNode
        
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
                
        for i in range(xCount): #Set heuristic estimate for all nodes, chooses best heuristic based on closest goal
            for j in range(yCount):                
                bestHuri = 0
                for goal in self.G: #For all goals
                    heuristic = (abs(self.nodes[j, i].xy[0] - goal.xy[0]) + abs(self.nodes[j, i].xy[1] - goal.xy[1])) * 1    #Manhattan distance estimate * average edge weight
                    bestHuri = min(bestHuri, heuristic) #Picks best current heuristic

                self.nodes[j, i].heuri = bestHuri
        self.G = set(self.G)    #Removes goal duplicates

# inputFileName contains a CSV file with the input grid
# optimalPathFilename is the name of the file the optimal path should be written to
# exploredListFilename is the name of the file the list of explored nodes should be written to
def pathfinding(inputFileName, optimalPathFilename, exploredListFilename):
    csv = np.genfromtxt(inputFileName, delimiter=",", dtype="str")      #Import CSV
    csv = np.char.strip(csv)    #Clean csv

    g = Graph(csv)  #Create Graph and Link nodes
    pq = PriorityQueue()    #Our priority queue

    g.nodes[g.S.xy[0], g.S.xy[1]].nCost = 0  #Start node cost at 0
    sNode = g.nodes[g.S.xy[0], g.S.xy[1]] #Physical start node
    pq.put((0, sNode))   #Priority queue start node

    goalXYs = []
    for goals in g.G:
        goalXYs.append(goals.xy)

    #gNode = g.nodes[g.G[0].xy[0], g.G[0].xy[1]] #Physical goal node
    gNode = 0
    checked = []  

    #Pathfind
    while (not pq.empty()):   
        lowest = pq.get()   #Get lowest code node

        #Explore node
        lowestCost = lowest[0]
        lowest = lowest[1]    #Lowest node
        checked.append(lowest.xy)   #Add to our checked list
        #print("Explore: " + str(lowest.xy))
        neighbours = lowest.edges  #Nearby edges

        #if (lowest.xy == gNode.xy):   
        if (lowest.xy in goalXYs):  #Reached end node       
            gNode = lowest
            break

        for i in range(len(neighbours)):    #neighbours[i].n2 is the current node we're checking         
            if (lowest.prev.xy == neighbours[i].n2.xy): #Prevents checking the node that this node came from
                continue

            edgeCost = neighbours[i].cost   #Edge cost to next nude
            prevNodeCost = (lowestCost - lowest.heuri)  #True cost before next node
            nextNodeHeuristic = neighbours[i].n2.heuri  #Heuristic cost of next node
            nodeCost = prevNodeCost + edgeCost + nextNodeHeuristic     #Total node cost
            neighbours[i].n2.checked = True

            #Update node based on search
            if (neighbours[i].n2.nCost > nodeCost):  #If nodes cost is larger than calculated, update node, add node to queue
                #print(f"\tUpdating {neighbours[i].n2.xy} Cost From {neighbours[i].n2.nCost} to {nodeCost}")
                neighbours[i].n2.nCost = nodeCost    #Update node cost
                neighbours[i].n2.prev = lowest      #Set new route node (lowest cost to node)

                pq.put((nodeCost, neighbours[i].n2))    #Add node to queue    
    

    finishedList = [gNode.xy]
    cost = 0

    curNode = g.nodes[gNode.xy[0], gNode.xy[1]]
    while(curNode.xy != sNode.xy):
        curNode = curNode.prev
        finishedList.append(curNode.xy)
        cost += curNode.oriCost

    finishedList.reverse()


    #Write to files
    optimalPath = open(optimalPathFilename, "w")
    optimalPath.truncate()  #Cleans file before writing
    for n in finishedList:
        optimalPath.write(str(n) + "\n")
    optimalPath.close()

    exploredList = open(exploredListFilename, "w")
    exploredList.truncate()  #Cleans file before writing
    for n in checked:
        exploredList.write(str(n) + "\n")
    exploredList.close()

    fileCost = open("optimalPathCost.txt", "w")
    fileCost.truncate()  #Cleans file before writing
    fileCost.write(str(cost))
    fileCost.close()

    return cost


def main():
    cost = pathfinding("Assignment1/Example3/input.txt", "optimalpath.txt", "exploredList.txt")

    return

if (__name__ == "__main__"):
    main()