# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:15:30 2018

>>> from types import SimpleNamespace
>>> d = {'key1': 'value1', 'key2': 'value2'}
>>> n = SimpleNamespace(**d)
>>> print(n)
namespace(key1='value1', key2='value2')
>>> n.key2
'value2'

Adding, modifying and removing values is achieved with regular attribute access, i.e. you can use statements like n.key = val and del n.key.

To go back to a dict again:

>>> vars(n)
{'key1': 'value1', 'key2': 'value2'}
The keys in your dict should be string identifiers for attribute access to work properly.


"""

class Foe:
    
    def __init__(self):
        from types import SimpleNamespace
        import random
        self.__creatures = {"bugbear": {"name":"bugbear",
                                        "article":"a",
                                        "description":"It's a bear with six legs"
                                        + "-- fortunately, it's kind of small. You might stand a chance.",
                                        "toHit":12,
                                        "hp":32,
                                        "atkBonus":2,
                                        "damageDieType":8,
                                        "damageDieNumber":1,
                                        "damageBonus":0,
                                        "dropValue":random.randint(4,12),
                                        "dropDescription":"You're able to collect a pelt,",
                                        "lastGaspThreshold":random.randint(1,5)
                                        },
                            "owlbear": {"name":"owlbear",
                                        "article":"an",
                                        "description":"It's fast, feathery, and far " 
                                        + "too scary for you to tell if it's wise or not.",
                                        "toHit":16,
                                        "hp":23,
                                        "atkBonus":4,
                                        "damageDieType":4,
                                        "damageDieNumber":2,
                                        "damageBonus":2,
                                        "dropValue":random.randint(1,30),
                                        "dropDescription":"A few golden feathers flutter to the ground,",
                                        "lastGaspThreshold":random.randint(1,5)
                                        }
                            }
        self.name = random.choice(list(self.__creatures))
        self.stats = SimpleNamespace(**self.__creatures[self.name])
        self.objType = "enemy"
        self.atkSuccess = False
        self.atkDamage = -1

    # These properties are so that objType, atkSuccess, and atkDamage don't need to be added 
    # to the dictionary for every creature. They are set once on instantiation and apply to
    # all creatures, and get added to the dictionary for the creature actually being used
    # when it's instantiated.
    @property
    def objType(self):
        return self.stats.objType
    
    @objType.setter
    def objType(self,objType):
        self.stats.objType = objType

    @property
    def atkSuccess(self):
        return self.stats.atkSuccess
    
    @atkSuccess.setter
    def atkSuccess(self,atkSuccess):
        self.stats.atkSuccess = atkSuccess

    @property
    def atkDamage(self):
        return self.stats.atkDamage
    
    @atkDamage.setter
    def atkDamage(self,atkDamage):
        self.stats.atkDamage = atkDamage



""" 
        original code... I just knew there had to be a better way!
        self.detail = self.__creatures[self.name]
        self.stats = dict(list(self.detail.items()))
        
        self.objType = self.stats["objType"]
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
        self.atkSuccess = False
        self.atkDamage = self.stats["atkDamage"]
        self.init = -1
        # parameter for formatText()
 """
    