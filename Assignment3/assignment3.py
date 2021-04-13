import numpy as np
import csv
import math
import sys
from io import StringIO

class td_qlearning:
    alpha = 0.1
    gamma = 0.5

    def __init__(self, trajectory_filepath):    # trajectory_filepath is the path to a file containing a trajectory through state space
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

        return

    def qvalue(self, state, action):    #state is a string representation of a state, action is a string representation of an action
        nextPair = self.nextPair[(state, action)]

        location = state[:1]
        states = state[1:]
        
        rCurState = self.rewardAt(states) #reward = -1 * Number of dirty squres            
        futureReward = self.maxFuture(nextPair[0])    #Compares cleaning to moving in the future

        newValue = self.prevValue + self.alpha * (rCurState + self.gamma * futureReward - self.prevValue)
        #prevValue = newValue
        print(f"Pair = {(state, action)}, Q={newValue}")

        return newValue    # Return the q-value for the state-action pair

    def policy(self, state):    # state is a string representation of a state

        
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