import numpy as np
#import pandas as pd
import csv
import math
import sys
from io import StringIO

'''
# Nested dictionary 
    #key is the stat ( 201101). value of that state is another value ( key is an action U,D, value is Q value with that )
'''
qvalues={}

class td_qlearning:
    alpha = 0.1
    gamma = 0.5
    global qvalues # nested dictionary

    def __init__(self, trajectory_filepath):    # trajectory_filepath is the path to a file containing a trajectory through state space
        global qvalues # nested dictionary
        qvalues = {}
        alpha = 0.1
        gamma = 0.5
        allActions= ["C","U","R","L", "D"]
        # SUDO CODE 
      
        self.csvInput = np.genfromtxt(trajectory_filepath, delimiter=",", dtype="str")  #Input as string so string operations can be performed
        
        for i in range(len(self.csvInput)): # loop through trajectories
            state = self.csvInput[i][0]
            action = self.csvInput[i][1]
            #print(qvalues)
           # qv = qvalue(state,action) + alpha*(rewardAt(state) + gamma*maxAllActions(csvInput[i+1][0]) - qvalue(state,action))
            qv=0.0
            if i < (len(self.csvInput) - 1):
                if state in qvalues.keys():
                    if action in qvalues[state].keys() and self.actionPossible(state, action): # if state and actions already exsists , replace it with more recent q value
                            qv = self.qvalue(state,action) + alpha*(self.rewardAt(state) + gamma*self.maxAllActions(self.csvInput[i+1][0]) - self.qvalue(state,action))  # calculate Q value
                            qvalues[state][action] = qv
                            #print("This runs"+str(self.qvalue(state,action)) )
                            #self.qValueSetter(state,action,qv)  # add them to exsiting list
                            #print("Q value after setting: "+ str(self.qvalue(state,action)))
                else: # state not in exist already
                    qvalues[state] = {}   
                    for acts in allActions:     #loop throough all actions        
                        if self.actionPossible(state,acts):     # add all relevant acitons to nested dictionary
                            qvalues[state][acts] = 0        
                        if acts == action:                      # if current action matches a possible action state can take, add q value to dictionary
                            qv = self.qvalue(state,action) + (alpha * (self.rewardAt(state) + (gamma * self.maxAllActions(self.csvInput[i+1][0])) - self.qvalue(state,action)))  # calculate Q value
                            qvalues[state][action] = qv
                            #print("Q value after setting: "+ str(self.qvalue(state,action)))
        
        
        p= self.policy("201011")
        print(p)
        g = self.qvalue("300000", "C")
        print("expected -0.175490 got :" + str(g))
        l = self.qvalue("300000", "R")
        print ("expected -0.048188 got :" + str(l))
        k = self.qvalue("510100", "U")
        print ("expected -2.285709 got :" + str(k))
        R = self.policy("310100")
        print ("expected 'C' got :" + str(R))
        t =self.policy("310100")
        print ("expected 'C' got :" + str(t))
        O = self.policy("410000")
        print ("expected 'C' got :" + str(O))
        J = self.policy("510100")
        print ("expected 'U' got :" + str(J))
        


        

    def qvalue(self, state, action):     #this is a q value getter
        if state in qvalues.keys() and action in qvalues[state].keys():     # if the state exists in qvalues and action is possible for square, get the q value in qvalues 
            #print("State: "+ state+" Action:"+action+" Qvalue Before setting: "+ str(qvalues[state][action]))
            return qvalues[state][action]
        else:       # else return 0
            return 0
        

    
    def policy(self, state):    # state is a string representation of a state
        # Examines all the actions for that state, returns action with highest q value for a the state action pair ( dependent on Q value)
        a = ""
        hq=-9797  # highest Q value
        for actionss in qvalues[state]:  # for actions in  in this states qvalues 
            highestAct= qvalues[state][actionss]
            if highestAct > hq  and highestAct != -9797:      # Any q value higher then current hq will be the action selected for policy
                hq = highestAct
                a = actionss  
        # Return the optimal action under the learned policy
        return a
        
    def rewardAt(self, state):  #Returns the reward at a given state
        reward = 0
        states = state[1:]
        for s in states:
            reward += int(s)        
        return -reward
    
    def qValueSetter(self, state, action, qval):  #add new q value to list for that action. not sure if implementation right
        global qvalues # nested dictionary
        qvalues[state][action] = qval
        return 

    def maxAllActions(self, state):
        highest= -979
        if state in qvalues.keys(): 
           # what if states
            for actionss in qvalues[state]:  # for actions in  in this states qvalues 
                highestAct= qvalues[state][actionss]  
                if highestAct > highest and highestAct != -979:# and highestAct != 0:  # anyvalue higher then curent highest is returned
                    highest = highestAct
        return highest


    def actionPossible(self,state, action):     # restrictions checking is an action is possible in a square and returning true if it is.
        possible = False
        square = int(state[0])
        if square == 1:
            if action == "D" or action == "C":
                possible = True
        elif square == 2:
            if action == "R" or action == "C":
                possible = True
        elif square == 4:
            if action == "L" or action == "C":
                possible = True
        elif square == 5:
            if action == "U" or action == "C":
                possible = True
        elif square == 3:
            if action == "R" or action == "C" or action == "L" or action == "D" or action == "U" :
                possible = True
        else:
            print("not valid action")
        return possible

    
   

def main():

    tdQLearn = td_qlearning("Assignment3/Example2/trajectory.csv")
    #Input parsing and santizing
    #txtInput = np.genfromtxt("/Users/margievenes/Desktop/COMP 4106/A1/COMP4106-Projects/Assignment2/Example2/input.txt", delimiter=",", dtype="str")  #Input as string so string operations can be performed
    #txtInput = np.char.strip(txtInput)              #Remove whitespace
    #txtInput = np.char.replace(txtInput, "[", "")   #Remove random extra brackets
    #txtInput = np.char.replace(txtInput, "]", "")   #Remove random extra brackets



    return

if (__name__ == "__main__"):
    main()