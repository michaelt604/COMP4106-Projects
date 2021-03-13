#import numpy as np
import csv
import math
import sys



class Prob:
    def __init__(self):
        # need to add weights of to each dimensions 2 variables next to dogs to easily call on them
        self.breeds = [["beagle",["girth", 41,6],["height", 37,4],["weight", 10,2], 0.3], ["corgi",["girth", 53,9],["height", 27,3],["weight", 12,2],0.21], ["husky",["girth", 66,10],["height", 55,6],["weight", 22,6],0.14], ["poodle",["girth", 61,9],["height", 52,7],["weight", 26,8],0.35]]
        # Could replace with hashmap as well to speed up efficienty 
        #self.breeds = ["beagle", "corgi", "husky", "poodle"]   # all dimensions given for dog
        #self.breedOds = {"beagle": 0.3, "corgi": 0.21, "husky": 0.14, "poodle": 0.35}




#Input is a three element list with [girth, height, weight]
def naive_bayes_classifier(input):
    #Get variables
    girth = input[0]
    height = input[1]
    weight = input[2]

    prob = Prob()   #Probability class
    class_probabilities= []
    most_likely_class = " best Dog"
    highestProb = 0

     # P(characterstic | breed) = (1/sqrt(2*math.pi*(o**2))) * e **(-0.5((inputVar = u)/o)**2)
    def breedCharacteristic(dogdimension, u,o):         #returns probability of dog characterstic
        #to avoid any computing errors with PEDMAS, calculating it in parts
        part1 = (1 / math.sqrt(2*math.pi*(o**2))) 
        part2 = math.exp(-0.5 * (((dogdimension - u ) / o ) ** 2))
        return (part1 * part2)

    for breed in prob.breeds:

        #P(A|B) = P(A ^ B) / P(B)
        #P(Girth | Dog) / P()
       
        #after computing the 3 values for each dogs, those will be used in the probabilty to calculate their likely hood
        # Then compute likly hoood of dog combining those peices of evidence
        dogBreed= breed[0]  
        probGirthBreed = breedCharacteristic(girth,breed[1][1],breed[1][2])  
        probHeightBreed = breedCharacteristic(height,breed[2][1],breed[2][2])
        probWeightBreed = breedCharacteristic(weight,breed[3][1],breed[3][2])



        # P(breed| girth, weight, height)= P(Girth| dog)P(Height| dog)P(weight| dog)P(Breed)
        # don't need to devide by sum of all conditional probabilities since all of them would be devided by same  thing
        breedSum = probGirthBreed * probHeightBreed * probWeightBreed * breed[4]


        
       
        class_probabilities.append([dogBreed,breedSum]) #Add breed probability in list
       
        #argmax( breeds)
        if breedSum > highestProb: #return breed heighest probability
            most_likely_class = dogBreed
        

    #most_likely_class is a string indicating the most likely class, either "beagle", "corgi", "husky", or "poodle"
    #class_probabilities is a four element list indicating the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    print(most_likely_class)
    print(class_probabilities)
    return most_likely_class, class_probabilities

# input is a three element list with [girth, height, weight]
#def fuzzy_classifier(input):

    # highest_membership_class is a string indicating the highest membership class, either "beagle", "corgi", "husky", or "poodle"
    # class_memberships is a four element list indicating the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    #return highest_membership_class, class_memberships



def main():


    naive_bayes_classifier([59, 32, 17])
    return

if (__name__ == "__main__"):
    main()
