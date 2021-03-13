import numpy as np
import csv
import math
import sys
from io import StringIO


class Prob: #Probability class for all base probabilities and values
    def __init__(self):
        #Dog Breed: Girth, Hiehgt, Weight, Probability
        self.breeds = [ ["beagle",  ["girth", 41, 6],   ["height", 37, 4],  ["weight", 10,2], 0.3], 
                        ["corgi",   ["girth", 53, 9],   ["height", 27, 3],  ["weight", 12,2], 0.21], 
                        ["husky",   ["girth", 66, 10],  ["height", 55, 6],  ["weight", 22,6], 0.14], 
                        ["poodle",  ["girth", 61, 9],   ["height", 52, 7],  ["weight", 26,8], 0.35]]


# P(characterstic | breed) = (1/sqrt(2*math.pi*(o**2))) * e **(-0.5((inputVar = u)/o)**2)
def breedCharacteristic(dogDimension, u, o):         #returns probability of dog characterstic, calculated in parts to avoid computational errors
    part1 = 1 / (math.sqrt(2 * math.pi * (o ** 2)))
    eExponent = -0.5 * (((dogDimension - u) / o) ** 2)
    part2 = math.exp(eExponent)

    PCharBreed = part1 * part2
    return PCharBreed


#Input is a three element list with [girth, height, weight]
def naive_bayes_classifier(input):
    #Get variables
    girth = input[0]
    height = input[1]
    weight = input[2]

    prob = Prob()   #Probability class
    probabilities = {}  #Probability dictionary of Breed: Probability

    summedForEachBreed = 0   #Our end denominator, ends up as the sum of each breed with (P(Girth | breed) * P(Height | Breed) * P3(Weight | Breed) * P(Breed)).
    for breed in prob.breeds:  
        dogBreed = breed[0]  
        probGirthBreed = breedCharacteristic(girth, breed[1][1], breed[1][2])   #P(Girth | Breed)
        probHeightBreed = breedCharacteristic(height, breed[2][1], breed[2][2]) #P(Height | Breed)
        probWeightBreed = breedCharacteristic(weight, breed[3][1], breed[3][2]) #P(Weight | Breed)

        breedNumerator = probGirthBreed * probHeightBreed * probWeightBreed * breed[4]    #Numerator in final calculation
        probabilities[breed[0]] = breedNumerator    #Set our dictionary values for final calc later
        summedForEachBreed += breedNumerator        #Add to our final denominator

    mostLikelyClass = ""  #Final Class output
    highestProb = 0         #Probability tracker
    classProbabilities = []

    for b in probabilities.keys():  #For each rough probability (just numerator)
        breedProb = probabilities[b] / summedForEachBreed    #Divide by SummedForEachBreed
        probabilities[b] = breedProb    #Prob remove later
        classProbabilities.append(breedProb)    #Add to our return list
        if (breedProb > highestProb):
            highestProb = breedProb     #Update highest probabilitiy
            mostLikelyClass = b       #Update most likely class string       

    print(probabilities)        #Probability dictionary output (Comment out later, debugging purposes)
    print(mostLikelyClass)      #Most likely class output (Comment out later, debugging purposes)
    print(classProbabilities)   #class probability output (Comment out later, debugging purposes)

    return mostLikelyClass, classProbabilities


# input is a three element list with [girth, height, weight]
def fuzzy_classifier(input):

    # highest_membership_class is a string indicating the highest membership class, either "beagle", "corgi", "husky", or "poodle"
    # class_memberships is a four element list indicating the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]

    #dictionary for girth small, medium, and large values
    #value is an array for a,b,c,d
    
    girth = {'small': [0.0,0.0, 40.0, 50.0],'medium': [ 40.0, 50.0, 60.0, 70.0],'large': [60.0, 70.0, 100.0, 100.0]}
    height = {'short': [0.0,0.0, 25.0, 40.0],'medium': [ 25.0,40.0, 50.0, 60.0],'tall': [50.0, 60.0, 100.0, 100.0]}
    weight = {'light': [0.0,0.0, 5.0, 15.0],'medium': [5.0, 15.0, 20.0, 40.0],'heavy': [20.0, 40.0, 100.0, 100.0]}
   
    
    girthList = newList(input[0], girth)
    heightList = newList(input[1], height)
    weightList = newList(input[2], weight)

    secondB = sNorm(girthList.get('small'), weightList.get('light'))
    beagle = tNorm(heightList.get('medium'), secondB )
    #print('beagle: ', str(beagle))

    corgi = tNorm(tNorm(girthList.get('medium'),heightList.get('short')), weightList.get('medium'))
    #print('corgi: ', str(corgi))

    firstHusky = tNorm(girthList.get('large'), heightList.get('tall'))
    
    husky = tNorm( firstHusky, weightList.get('medium'))
    #print('husky: ', str(husky))

    poodle = tNorm( sNorm(girthList.get('medium'),heightList.get('medium')), weightList.get('heavy'))
    #print('poodle: ', str(poodle))

    doggos = {"beagle": beagle, "corgi": corgi, "husky": husky, "poodle":poodle }
    #print(doggos)

    highest_membership_class = ''
    class_memberships = doggos.values()
    maxValue = max(doggos.values())

    for key in doggos.keys():
        if (doggos[key] == maxValue):
            highest_membership_class = key
    
    print(highest_membership_class)
    print(class_memberships)

    #return highest_membership_class, class_memberships

# this function returns a new list 
def newList(x, sizeList):

    newDictionary = {}
    for key in sizeList.keys():
        #print("key: " + str(key))
        #print(sizeList.get(key)[0])
        a = sizeList.get(key)[0]
        b = sizeList.get(key)[1]
        c = sizeList.get(key)[2]
        d = sizeList.get(key)[3]
        '''
        print("a: " + str(a))
        print("b: " + str(b))
        print("c: " + str(c))
        print("d: " + str(d))
        '''
        
        if (x<=a):
            #print("x<=a")
            newDictionary[key] = 0

        elif ((a<x) and (x<b)):
            #print("(a<x) and (x<b)")
            newDictionary[key] = ((x-a)/(b-a))
            #print(x-a)
            #print(b-a)
            #print(round(((x-a)/(b-a)),2 ) )

        elif ((b<=x)and(x<=c)):
            #print("((b<=x)and(x<=c))")
            newDictionary[key] = 1

        elif ((c<x) and (x<d)):
            #print("((c<x) and (x<d)))")
            newDictionary[key] = ((d-x)/(d-c))
        else:
            #print("else")
            newDictionary[key] = 0

    return newDictionary

def tNorm(x,y):

    return x*y

def sNorm(x,y):

    return x+y-(x*y)

def main():
    txtInput = np.genfromtxt("/Users/margievenes/Desktop/COMP 4106/A1/COMP4106-Projects/Assignment2/Example2/input.txt", delimiter=",", dtype="str")  #Input as string so string operations can be performed
    txtInput = np.char.strip(txtInput)              #Remove whitespace
    txtInput = np.char.replace(txtInput, "[", "")   #Remove random extra brackets
    txtInput = np.char.replace(txtInput, "]", "")   #Remove random extra brackets

    classifierInput = [int(txtInput[0]), int(txtInput[1]), int(txtInput[2])]
    
    #Run naive bayes
    naive_bayes_classifier(classifierInput)

    #Run fuzzy
    fuzzy_classifier(classifierInput)

    return


if (__name__ == "__main__"):
    main()
