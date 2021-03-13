
import numpy as np
import csv
import math
import sys



'''
class Prob:
    def __init__(self):
        self.breeds = ["beagle", "corgi", "husky", "poodle"]
        self.breedOds = {"beagle": 0.3, "corgi": 0.21, "husky": 0.14, "poodle": 0.35}




#Input is a three element list with [girth, height, weight]
def naive_bayes_classifier(input):
    #Get variables
    girth = input[0]
    height = input[1]
    weight = input[2]

    prob = Prob()   #Probability class

    for breed in prob.breeds:
        calc = 0

        #P(A|B) = P(A ^ B) / P(B)

        #P(Girth | Dog) / P()

        probGirthBreed = 0  
        probHeightBreed = 0 
        probWeightBreed = 0



        #P(e1 AND e2 AND e3 | h) = P(e1 | h) * P(e2 | h) * P3(e3 | h)
        #SumForEachHypothesis(P(e1 | h) * P2(e2 | h) * P3(e3 | h) * P(h))


        #P(girth=x AND height=y AND weight=z)
        #= SummedForEachHypothesis(P(e1 AND e2 AND e3 | h) * P(h))
        #= SumForEachHypothesis(P(e1 | h) * P2(e2 | h) * P3(e3 | h) * P(h))   ***DENUMERATOR Still not sure how to get the actual probabilities


    #For all types
    #P(type | inputs)
    #P(girth = x | type) * P(height = y | type) * P (weight = z | type)
    #/ P(girth = x ^ height = y ^ weight = z)
    #Put estimate into a list then go next

    #most_likely_class is a string indicating the most likely class, either "beagle", "corgi", "husky", or "poodle"
    #class_probabilities is a four element list indicating the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    return most_likely_class, class_probabilities
'''
# input is a three element list with [girth, height, weight]
def fuzzy_classifier(input):

    # highest_membership_class is a string indicating the highest membership class, either "beagle", "corgi", "husky", or "poodle"
    # class_memberships is a four element list indicating the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    '''
    if (height is medium and girth is small) 
    then: beagle

    if (girth is medium and height is short and weight is medium)
    then: corgi

    if (girth is large and height is tall and weight is medium) 
    then: husky

    if (girth is medium or height is medium) and weight is heavy
    then: poodle
    '''

    #dictionary for girth small, medium, and large values
    #value is an array for a,b,c,d
    
    girth = {'small': [0.0,0.0, 40.0, 50.0],'medium': [ 40.0, 50.0, 60.0, 0.0],'large': [60.0, 70.0, 100.0, 100.0]}
    height = {'short': [0.0,0.0, 25.0, 40.0],'medium': [ 25.0,40.0, 50.0, 60.0],'heavy': [50.0, 60.0, 100.0, 100.0]}
    weight = {'light': [0.0,0.0, 5.0, 15.0],'medium': [5.0, 15.0, 20.0, 40.0],'heavy': [20.0, 40.0, 100.0, 100.0]}
   
    
    girthList = newList(input[0], girth)
    heightList = newList(input[1], height)
    weightList = newList(input[2], weight)
    '''
    if (height is medium and girth is small) 
    then: beagle

    if (girth is medium and height is short and weight is medium)
    then: corgi

    if (girth is large and height is tall and weight is medium) 
    then: husky

    if (girth is medium or height is medium) and weight is heavy
    then: poodle
    '''
    beagle = tNorm(heightList.get('medium'), sNorm(girthList.get('small'), weightList.get('light')))
    print(beagle)
    corgi = tNorm(tNorm(girthList.get('medium'),heightList.get('short')),weightList.get('medium'))
    print(corgi)
    husky = tNorm(tNorm(girthList.get('large'),heightList.get('short')),weightList.get('medium'))
    print(husky)
    poodle = tNorm(sNorm(girthList.get('medium'),heightList.get('medium')),weightList.get('heavy'))
    print(poodle)

    '''
    corgi =
    husky = 
    poodle = 
    '''

    #doggoArray = [beagle, corgi, husky, poodle]
    #return highest_membership_class, class_memberships

# this function returns a new list 
def newList(x, sizeList):

    newDictionary = {}
    for key in sizeList.keys():
        print("key: " + str(key))
        #print(sizeList.get(key)[0])
        a = sizeList.get(key)[0]
        b = sizeList.get(key)[1]
        c = sizeList.get(key)[2]
        d = sizeList.get(key)[3]
        print("a: " + str(a))
        print("b: " + str(b))
        print("c: " + str(c))
        print("d: " + str(d))
        
        if (x<=a):
            print("x<=a")
            newDictionary[key] = 0

        elif ((a<x) and (x<b)):
            print("(a<x) and (x<b)")
            newDictionary[key] = ((x-a)/(b-a))
            print(x-a)
            print(b-a)
            print(round(((x-a)/(b-a)),2 ) )

        elif ((b<=x)and(x<=c)):
            print("((b<=x)and(x<=c))")
            newDictionary[key] = 1

        elif ((c<x) and (x<d)):
            print("((c<x) and (x<d)))")
            newDictionary[key] = ((d-x)/(d-c))
        else:
            print("else")
            newDictionary[key] = 0

    print("newDictionary: " + str(newDictionary))
    #return a dictionary
    return newDictionary

def tNorm(x,y):
    return x*y

def sNorm(x,y):
    return x+y-(x*y)

def main():
    input = [65, 55, 30]
    fuzzy_classifier(input)
    return

if (__name__ == "__main__"):
    main()