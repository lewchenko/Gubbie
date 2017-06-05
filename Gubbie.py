# Gubbie Simulator - June 2017
# This project will simulate "Gubbie" , an elderly dog with Diabetes, Cushings, Blind and Gall Bladder Removed
# The purpose of the simulation will be to act as a reference for the real dog Gubbie
# in order to assist with dosage predictability.

# Version 0.1

#Build an object called DOG. Dog has core attributes for Name, Weight, Age
class Dog:
    Dog_ID = 0
    Diabetes_Status = 1
    BGcurve=("00:00",0,0)
    BGvalues=0


    def __init__(self,Dog_Name,Age,Weight):

        self.Name = Dog_Name
        self.Age = Age
        self.Weight = Weight
        self.Dog_ID +=1


#Method to summarise a Dog Instance
    def show_data(self):
        print self.Name + "'s age is " + str(self.Age) + " and weight is " + str(self.Weight)
        print "Gubbie's ID Reference is " + str(self.Dog_ID)

#Method to create a blood curve by adding entries to a list
    def add_BG_point(self,BGtime, BGlowvalue, BGhighvalue):
        self.BGcurve = self.BGcurve + (BGtime,BGlowvalue, BGhighvalue);
        self.BGvalues +=1

#Method to display full curve
    def show_curve(self):
        for count in self.BGcurve:
            print count




import sys

#Create an instance of Gubbie, aged 13, weight 12.1Kg
Gubbie=Dog("Gubbie",13,12.1)

#Call the method show data to confirm creation of Gubbie
Dog.show_data(Gubbie)

#Add an entry point to Gub's Blood Curve
Dog.add_BG_point(Gubbie,"07:00",9,26)
Dog.add_BG_point(Gubbie,"08:00",10,18)



#Display full curve
Dog.show_curve(Gubbie)







