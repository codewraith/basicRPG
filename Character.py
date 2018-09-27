# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 10:41:13 2018

@author: ISInc
"""

class Adventurer:
    
    def __init__(self):
        self.name = "Purple Vengeance"
        self.hp = 80
        self.weapon = "+1 Sword of Peskiness"
        self.atkBonus = 1
        self.toHit = 12
        self.damageDieType = 8
        self.damageDieNumber = 1
        self.damageBonus = 2
        self.init = -1
        self.treasure = 0
        self.atkSuccess = False
        self.atkDamage = -1
        self.objType = "player"
        self.lastGaspThreshold = 1
        self.strings = { "encounterScream" : { "no" : '"NO!!!" like your mommy taught you',
                                                "wtf" : "out a mighty battle cry -- at least, " \
                                                + "that was the plan, but instead you burp.",
                                                "ew":'"Gross!! Stay away from me!"',
                                                "lj":'"Leeeeeeroooy Jeeenkiiiiins!!!!!'
                                                },
                         "taunt": "Your mother was a hamster and your father smelt of elderberries!"}

"""    @property
    def getString(self):
        return self.__getString

    @getString.setter
    def getString(self,getString):
        import random
        choose = self.strings[getString]
        key = random.choice(choose)
        self.__getString = choose[key] """
