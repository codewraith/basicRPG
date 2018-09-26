# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:15:30 2018

@author: ISInc
"""

class Foe:
    
    def __init__(self):
        import random
        self.__creatures = {"bugbear": {"name":"bugbear",
                                        "article":"a",
                                        "description":"It's a bear with six legs"
                                        + "-- fortunately, it's kind of small. You might stand a chance.",
                                        "toHit":12,
                                        "HP":32,
                                        "atkBonus":2,
                                        "damageDieType":8,
                                        "damageDieNumber":1,
                                        "damageBonus":0,
                                        "dropValue":random.randint(4,12),
                                        "dropDescription":"You're able to collect a pelt,"
                                        },
                            "owlbear": {"name":"owlbear",
                                        "article":"an",
                                        "description":"It's fast, feathery, and far " 
                                        + "too scary for you to tell if it's wise or not.",
                                        "toHit":16,
                                        "HP":23,
                                        "atkBonus":4,
                                        "damageDieType":4,
                                        "damageDieNumber":2,
                                        "damageBonus":2,
                                        "dropValue":random.randint(1,30),
                                        "dropDescription":"A few golden feathers flutter to the ground,"
                                        }
                            }
        self.__numCreatures = self.__creatures.__len__()
        self.name = list(self.__creatures.keys())[random.randint(0,self.__numCreatures - 1)]
        self.detail = self.__creatures[self.name]
        self.stats = dict(list(self.detail.items()))
        
        self.description = self.stats["description"]
        self.article = self.stats["article"]
        self.toHit = self.stats["toHit"]
        self.hp = self.stats["HP"]
        self.atkBonus = self.stats["atkBonus"]
        self.damageDieType = self.stats["damageDieType"]
        self.damageDieNumber = self.stats["damageDieNumber"]
        self.damageBonus = self.stats["damageBonus"]
        self.dropDescription = self.stats["dropDescription"]
        self.dropValue = self.stats["dropValue"]
        
        self.init = -1
        

    
    