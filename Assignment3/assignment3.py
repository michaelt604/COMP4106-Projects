import numpy as np
import pandas as pd
import csv
import math
import sys
from io import StringIO

'''
# Nested dictionary 
    #key is the stat ( 201101). value of that state is another value ( key is an action U,D, value is Q value with that )
'''
#qvalues={}

class td_qlearning:
    alpha = 0.1
    gamma = 0.5
    #global qvalues # nested dictionary

    def __init__(self, trajectory_filepath):    # trajectory_filepath is the path to a file containing a trajectory through state space
        #global qvalues # nested dictionary
        
        # SUDO CODE 
        '''
        Create a series, index= state, values = actions
        
        Loop through series ( trajetories )
            If state exists in qvalues 
                

        '''

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
        '''
        self.csvInput = np.genfromtxt(trajectory_filepath, delimiter=",", dtype="str")  #Input as string so string operations can be performed
        self.prevValue = 0
        self.nextPair = {}
        prevValue = 0
        for i in range(len(self.csvInput)):
            state = self.csvInput[i][0]
            location = self.csvInput[i][0][:1]
            states = self.csvInput[i][0][1:]
            action = self.csvInput[i][1]

            pair1 = (state, action) #First pair is our current number

            pair2 = ()  #Second pair is the next move that would be made
            if (i+1 >= len(self.csvInput)):   
                pair2 = (self.csvInput[0][0], self.csvInput[0][1])
            else:
                pair2 = (self.csvInput[i+1][0], self.csvInput[i+1][1])
            self.nextPair[pair] = pair2

            # trajecoties update in init
'''
        return

    def qvalue(self, state, action):     #this is a getter
        #Sudo code
        # if action in state action pair, get max, 
        # else return 0( default)
        '''
        if action in qvalues[state]:
            return max(qvalues[state][action])
        else:
            return 0
        ''' 


        # old code
        '''
        nextPair = self.nextPair[(state, action)]

        location = state[:1]
        states = state[1:]
        
        rCurState = self.rewardAt(states) #reward = -1 * Number of dirty squres            
        futureReward = self.maxFuture(nextPair[0])    #Compares cleaning to moving in the future

        newValue = self.prevValue + self.alpha * (rCurState + self.gamma * futureReward - self.prevValue)
        #prevValue = newValue
        print(f"Pair = {(state, action)}, Q={newValue}")
        '''
        return qvalue    # Return the q-value for the state-action pair

    def policy(self, state):    # state is a string representation of a state
        # Examines all the actions for that state, returns maxmim Q value for a the state action pair ( dependent on Q value)
        
        # Return the optimal action under the learned policy
        return a
        
    def rewardAt(self, state):  #Returns the reward at a given state
        reward = 0
        for s in state:
            reward += int(s)        
        return -reward
    
    
    def maxFuture(self, state): #Returns the maximum of potential future options
        location = int(state[:1])
        states = state[1:]
        m1 = self.rewardAt(states)   #Move and don't clean
        m2 = self.rewardAt(f"{states[:location-1]}0{states[location:]}")   #Replace character at location with cleaned state 0

        return max(m1, m2)


def main():

    tdQLearn = td_qlearning("Assignment3/Example1/trajectory.csv")
    #Input parsing and santizing
    #txtInput = np.genfromtxt("/Users/margievenes/Desktop/COMP 4106/A1/COMP4106-Projects/Assignment2/Example2/input.txt", delimiter=",", dtype="str")  #Input as string so string operations can be performed
    #txtInput = np.char.strip(txtInput)              #Remove whitespace
    #txtInput = np.char.replace(txtInput, "[", "")   #Remove random extra brackets
    #txtInput = np.char.replace(txtInput, "]", "")   #Remove random extra brackets



    return

if (__name__ == "__main__"):
    main()