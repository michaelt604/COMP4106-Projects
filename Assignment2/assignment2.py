
import numpy as np
import csv
import math
import sys



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




    #For all types
    #P(type | inputs)
    #P(girth = x | type) * P(height = y | type) * P (weight = z | type)
    #/ P(girth = x ^ height = y ^ weight = z)
    #Put estimate into a list then go next

    #most_likely_class is a string indicating the most likely class, either "beagle", "corgi", "husky", or "poodle"
    #class_probabilities is a four element list indicating the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    return most_likely_class, class_probabilities

# input is a three element list with [girth, height, weight]
def fuzzy_classifier(input):

    # highest_membership_class is a string indicating the highest membership class, either "beagle", "corgi", "husky", or "poodle"
    # class_memberships is a four element list indicating the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
    return highest_membership_class, class_memberships



def main():

    return

if (__name__ == "__main__"):
    main()