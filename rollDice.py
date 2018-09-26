# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:45:33 2018

@author: ISInc
"""

import DungeonDie
import Encounter
import Character

def fightTurn(attacker,defender):
    
    if d20.roll() + attacker.atkBonus >= defender.toHit:
        atkDie = DungeonDie.Die(attacker.damageDieType)
        dmg = 0
        
        for i in range(1, attacker.damageDieNumber + 1):
            dmg = dmg + atkDie.roll()
            
        dmg = dmg + attacker.damageBonus
        defender.hp = defender.hp - dmg
        msgChunks = {"hit":True,
                     "dmg":dmg}
    else:
        msgChunks = {"hit":False}
    return(msgChunks)
        

def formatDescription(msg, obj, objType):  
    import re
    if objType == "enemy":
        details = obj.stats
   # else:
   #    details = obj
    matches = re.findall("\[\S*\]",msg)
    if matches:
        print(matches[0])
    
    
        

def main():
    formatDescription("This is [article] [name] test string.",test,"enemy")
    goAdventuring = True
    
    while goAdventuring:
        
        enemy = Encounter.Foe()
        
        print("\n\nYou have encountered {0} {1}!".format(enemy.article,enemy.name))
        print(enemy.description)
          
        pcInit = d20.roll()
        enemyInit = d20.roll()
        
        print("\nRolling for initiative! You rolled a {0}...".format(pcInit))
        
        if pcInit < enemyInit:
            print("While you stand there in terror, the {0} attacks!".format(enemy.name))
            playerTurn = False
        else:
            playerTurn = True
            
        notDeadYet = True
        
        while notDeadYet:
            # fight or flee
            if playerTurn:
                chickenOption = input("Press C to run away, any other key to fight!\t")
                if chickenOption.lower() != "c":
                    outcome = fightTurn(pc,enemy)
                else:
                    print("\n\nYou bravely run away, clucking at the top of your lungs," 
                    + " as the {0} rages behind you. Somehow you know ".format(enemy.name) 
                    + "it is daring you to grow a spine someday and face it again.")
                    if pc.treasure > 0:
                        print("\nAlthough you manage to keep a grip on your weapon, you leave " 
                              + "scattered behind you the grotesque trophies that " 
                              + "would have brought you {0} gold.".format(pc.treasure))
                    
                    print("\nYou had {0} hit points remaining.".format(pc.hp))
                    goAdventuring = False
                    break
            else:
                outcome = fightTurn(enemy,pc)
                
            # If fighting, handle a hit 
            if outcome["hit"]:
                if playerTurn:
                    msg = "You swing your {0} and hit the {1} for {2} damage!"
                    playerTurn = False
                    print(msg.format(pc.weapon,enemy.name,outcome["dmg"]))
                else:
                    msg = "The {0} hits you for {1} damage!"
                    playerTurn = True
                    print(msg.format(enemy.name,outcome["dmg"]))
                
            # If fighting, handle a miss
            else:
                if playerTurn:
                    msg = "You miss the {0}!"
                    playerTurn = False
                else:
                    msg = "The {0} misses!"
                    playerTurn = True
                print(msg.format(enemy.name))
                
            # see if anyone died
            if pc.hp <= 0 or enemy.hp <= 0:
                notDeadYet = False
        
        # if you died...
        if pc.hp <= 0:
            print("\nYou fall beneath the onslaught. Your weapon falls to the ground" 
                  + " and you lie crushed and bleeding, the light fading from your eyes.")
            if enemy.hp <= 0:
                print("Somehow, you managed to kill " 
                      + "the {0}, but you're still dead.".format(enemy.name))
                goAdventuring = False
            else:
                print("\nThe {0} begins to feast.".format(enemy.name))
                goAdventuring = False
            
        # if the monster died...
        elif enemy.hp <= 0:
            print("\nWith an unearthly shriek, the {0} keels ".format(enemy.name)
                  + "over and breathes its last.")
            print("{0} which you estimate will bring you {1} gold.".format(enemy.dropDescription, enemy.dropValue))
            pc.treasure = pc.treasure + enemy.dropValue
            if pc.hp < 10:
                print("\nYou're hurt so badly you're walking like a drunk Jack Sparrow.")
            elif pc.hp < 20:
                print("\nYou're starting to feel pretty banged up.")
            hunt = input("Continue adventure? (Y/N)\t")
            if hunt.lower() != "y":
                goAdventuring = False
                print("\nYou decide your grisly haul worth {0} gold pieces ".format(pc.treasure) 
                + "is enough for one day. Whistling, you shoulder your " 
                + "trusty {0} and head for home ".format(pc.weapon) 
                + "where, you hope, no monsters lurk.")
    

if __name__ == "__main__":
    PC = True
    FOE = False
    playerTurn = True
    
    d20 = DungeonDie.Die(20)
    d10 = DungeonDie.Die(10)
    d8 = DungeonDie.Die(8)
    d6 = DungeonDie.Die(6)
    d4 = DungeonDie.Die(4)
    
    pc = Character.Adventurer()
    test = Encounter.Foe()
    main()
    
    