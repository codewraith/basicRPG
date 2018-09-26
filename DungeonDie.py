# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:23:14 2018

@author: ISInc
"""
class Die:
    
    def __init__(self, sides=20):
        
        self.__numSides = sides
        self.__lastRoll = False
        
    def roll(self):
        import random
        return  random.randint(1, self.__numSides)
    
    def rollAdvantage(self):
        roll1 = self.roll()
        roll2 = self.roll()
        if roll1 > roll2:
            self.__lastRoll = roll1
            return "{0} (other roll was: {1})".format(roll1, roll2)
        else:
            self.__lastRoll = roll2
            return "{0} (other roll was: {1})".format(roll2, roll1)
        
    def rollDisadvantage(self):
        roll1 = self.roll()
        roll2 = self.roll()
        if roll1 < roll2:
            self.__lastRoll = roll1
            return "{0} (other roll was: {1})".format(roll1, roll2)
        else:
            self.__lastRoll = roll2
            return "{0} (other roll was: {1})".format(roll2, roll1)
        
    def lastRoll(self):
        return self.__lastRoll
