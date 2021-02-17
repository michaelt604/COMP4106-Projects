
import numpy as np
import csv
import math
import sys

from queue import PriorityQueue


class Edge:
    def __init__(self, n1, n2, cost1, cost2):
        self.n1 = n1
        self.n2 = n2
        self.e1Cost = cost1
        self.e2Cost = cost2

class Node:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.edges = []
        self.id = id
        self.cost = sys.maxsize()   #Start cost at infinity
        self.onPath = False     #On current path
        self.checked = False    #Node checked or not

    def addEdge(self, nextNode, edgeCost1, edgeCost2):
        e = Edge(self, nextNode, edgeCost1, edgeCost2)
        self.edges.append(e)    #Add new edge to edges list
    
    def getNextPathID(self):    #loop through all edges finding the next one and returning when it finds the right one
        return 1

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
        if (n.id == "S" or n.id == "G"):    #Check node start or end
            return 0
        else:   #If a normal weighted node
            return int(n.id)    
    
    def createGraph(self, xCount, yCount, grid):
        for j in range(xCount): #Create all our nodes
            for i in range(yCount):
                #print(grid[j, i])  print node at time
                newNode = Node(i, j, grid[i, j])
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
                        node1.addEdge(node2, n1Weight, n2Weight)    #Adds edge between nodes          
                        node2.addEdge(node1, n2Weight, n1Weight)    #Adds edge between nodes     

                if (i + 1 < xCount):    # if theres a node below the current node, link them together
                    node2 = self.nodes[j, i+1]
                    n2Weight = self.getWeight(node2)                
                    if (not n2Weight == -1):    #Empty node
                        node1.addEdge(node2, n1Weight, n2Weight)    #Adds edge between nodes          
                        node2.addEdge(node1, n2Weight, n1Weight)    #Adds edge between nodes     
        

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

    startPos = g.S  #Start node location
    startNode = g.nodes[startPos[1], startPos[0]]









    #Pathfind


    #Set all nodes to infinit 



    optimalPathCost = 0

    return optimalPathCost


def main():
    cost = pathfinding("a", "a", "a")

    return

if (__name__ == "__main__"):
    main()