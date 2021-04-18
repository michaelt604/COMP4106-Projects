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
    #global qvalues # nested dictionary

    def __init__(self, trajectory_filepath):    # trajectory_filepath is the path to a file containing a trajectory through state space
        global qvalues # nested dictionary
        qvalues = {}
        alpha = 0.1
        gamma = 0.5
        allActions= ["C","U","R","L", "D"]
        # SUDO CODE 
        '''
        Create a series, index= state, values = actions
        
        Loop through  trajetories :
            If state exists in states 
                if action extists actions & action is possible in that square 
                    call q function ( state and ation ) and add q value to list( state-action pair)
                if action doesnt exist
                    Add action too action state pair
            else: # state doesn't exsit in dictionary
                qvalues['state']= {}
                if action is possible in state
                    qvalues['state'][action]= q value calculation
        '''
        self.csvInput = np.genfromtxt(trajectory_filepath, delimiter=",", dtype="str")  #Input as string so string operations can be performed
        self.prevValue = 0
        self.nextPair = {}
        
        for i in range(len(self.csvInput)): # loop through trajectories
            state = self.csvInput[i][0]
           # location = self.csvInput[i][0][:1]
           # states = self.csvInput[i][0][1:]
            action = self.csvInput[i][1]
            print(qvalues)
           # qv = qvalue(state,action) + alpha*(rewardAt(state) + gamma*maxAllActions(csvInput[i+1][0]) - qvalue(state,action))
            qv=0.0
            if i < (len(self.csvInput) - 1):
                if state in  qvalues.keys():
                    if action in qvalues[state].keys() and self.actionPossible(state, action): # if state and actions already exsists 
                            qv = self.qvalue(state,action) + alpha*(self.rewardAt(state) + gamma*self.maxAllActions(self.csvInput[i+1][0]) - self.qvalue(state,action))  # calculate Q value
                            self.qValueSetter(state,action,qv)  # add them to exsiting list
                            
                    elif self.actionPossible(state, action):  # state exsits but action doesn't 
                            qv = self.qvalue(state,action) + alpha*(self.rewardAt(state) + gamma*self.maxAllActions(self.csvInput[i+1][0]) - self.qvalue(state,action))  # calculate Q value
                            qvalues[state][action] = [qv]
                else: # state not in exist already
                    qvalues[state] = {}
                    for acts in allActions:             
                        if self.actionPossible(state,acts):     # make all relevant actions that is possible in that squre
                            qvalues[state][acts] = [0.0]
                        if acts == action:   
                            qv = self.qvalue(state,action) + alpha*(self.rewardAt(state) + gamma*self.maxAllActions(self.csvInput[i+1][0]) - self.qvalue(state,action))  # calculate Q value
                            qvalues[state][action] = [qv]
        
        p= self.policy("201011")
        print(p)
        g = self.qvalue("300000", "C")
        print(g)
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




       # notes
    ''' 
       # calculate q function here 
        # hold double list holdinig state- action pairs and their Q values

        #Add to begining of loop    when adding to a nested_dictionary     
        # Conditions for allowing movement to certain squres ( recommended to do it in a function to check if its valid)
            # only allowed  to move  up down left and right
        # when declairing the list variables, if it doesnt exist just returns 0.

        # if state and action doesnt exits, add it to the q values and add value at the end
        

        # need to take into 

        #Steps 
        # Check if state exists 
        # Then were adding it to our nested ductionary using Q function 
        # copy and paste the state and aciton from trajectory and compute Q value
        # NOT ADDING FUTURE States When checking next state

        # make another function returns max values for a state
        # use a setter function ( state ,action )


        # use a libary that formats everything when looping
    '''
    
    
    
    # OLD CODE
        

    def qvalue(self, state, action):     #this is a getter
        if state in qvalues.keys() and action in qvalues[state].keys():
            return max(qvalues[state][action])
        else:
            return 0
        


        
        
    def policy(self, state):    # state is a string representation of a state
        # Examines all the actions for that state, returns maxmim Q value for a the state action pair ( dependent on Q value)
        a = ""
        hq=-999  # highest Q value
        for actionss in qvalues[state]:  # for actions in  in this states qvalues 
            highestAct= max(qvalues[state][actionss])
            
            if highestAct > hq :
                hq = highestAct
                a = actionss  
        # Return the optimal action under the learned policy
        return a
        
    def rewardAt(self, state):  #Returns the reward at a given state
        reward = 0
        for s in state[1:]:
            reward += int(s)        
        return -reward
    
    def qValueSetter(self, state, action, qval):  #add new q value to list for that action. not sure if implementation right
        qvalues[state][action].append(qval)
        return 

    def maxAllActions(self, state):
        highest= 0.0
        if state in qvalues.keys(): 
            for actionss in qvalues[state]:  # for actions in  in this states qvalues 
                highestAct= max(qvalues[state][actionss])  # get the max vaalue
                if highestAct > highest:
                    highest = highestAct
        
                
        return highest


    def actionPossible(self,state, action):
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

    
    def maxFuture(self, state): #Returns the maximum of potential future options
        location = int(state[:1])
        states = state[1:]
        m1 = self.rewardAt(states)   #Move and don't clean
        m2 = self.rewardAt(f"{states[:location-1]}0{states[location:]}")   #Replace character at location with cleaned state 0

        return max(m1, m2)


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