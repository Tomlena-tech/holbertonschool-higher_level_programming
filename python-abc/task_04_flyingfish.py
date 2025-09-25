#!/usr/bin/env python3
"""Buil a flying fish !!from Fish and Bird"""


class Fish:
    def swim(self):
        print ("The fish is swimming")
    
    def habitat(self):
        print ("The fish lives in water")
        
class Bird:
    def fly(self):
        print ("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")
        
        


class FlyingFish(Fish, Bird):
    def fly (self):
        print("The flying fish is soaring!")
    def swim(self):
        print("The flying fish is swimming!")  
    def habitat(self):
        print("The flying fish livesboth in water and the sky!")


