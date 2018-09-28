# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:45:33 2018

@author: ISInc
"""
#from flask import Flask
from types import SimpleNamespace
import GameSettings
import gametext
import DungeonDie
import Encounter
import Character
import textwrap
import random
import os



def fightTurn(attacker,defender):

    if d20.roll() + attacker.atkBonus >= defender.toHit:
        atkDie = DungeonDie.Die(attacker.damageDieType)
        dmg = 0
        for i in range(1, attacker.damageDieNumber + 1):
            dmg = dmg + atkDie.roll()
            i = i + i - i #stupid statement to stop it complaining that i isn't used
        
        dmg = dmg + attacker.damageBonus
        defender.hp = defender.hp - dmg
        attacker.atkSuccess = True
        attacker.atkDamage = dmg

        msgChunks = {"hit":True,
                     "dmg":dmg}
    else:
        msgChunks = {"hit":False}
    return(msgChunks)







        
""" TO DO:
Accepts a dictionary of objects in the form "enemy": enemy, 
"pc": pc etc., and parses
tags in the format <object~property> to access the property from the 
specified object and subsitute the resulting value for the tag. 
property must be a string   """      
def displayText(msg, obj = None, padTop = 1, padBottom = 0):  
    import re
    matchCount = 0
    # this is so that if there are no matches, the original string gets printed
    formatMsg = msg
    formatStrings = []

    if isinstance(obj,dict):
       
        # converts the objects stored as values to dictionaries, 
        # still as values for the same keys in the outer dictionary
        obj = {key:vars(value) for (key,value) in obj.items()}

        # matches a <tag> or <tag.tag> in a string
        matchTags = re.compile(r'''
        <       # opening bracket of the tag
        \S+[^~~]     # one or more non-whitespace characters, immediately...
        >       # ... followed by the closing bracket of the tag
        ''', re.VERBOSE) # returns the entire match, including brackets

        # matches <tag~tag> but only retrieves the contents, without brackets
        matchTagContents = re.compile(r'''
        <       # same as the above except for the ()
        (\S+)   # return the letter groupings before and after a tilde delimiter
        ~
        (\S+)   # so this will return a tuple of ('key','value') from each tag <key~value>
        >       
        ''', re.VERBOSE)

        # find all instances that match the above regular expressions
        moTag = matchTags.findall(msg)
        moContents = matchTagContents.findall(msg)
        # print(repr(moTag))
        # print(repr(moContents))
        if moTag and moContents:
            for index, match in enumerate(moTag):
                matchCount = matchCount + 1
                # compile the search expression matching a specific tag
                subPattern = re.compile(match)
                # print("subPattern: ", repr(subPattern), "count: ", repr(matchCount))
                which = moContents[index][0]
                key = moContents[index][1]
                getFrom = obj[which]
                if isinstance(getFrom[key],str):
                    value = getFrom[key]
                else:
                    value = str(getFrom[key])
                # print("getFrom[", repr(key), "] = ", repr(getFrom[key]))
                # print("which", repr(which), ", key = ", repr(key))
                # replace <match> in formatMsg with stats["key"] ... the key to pass
                        # to the stats dictionary is retrieved from moContents[index]
                formatMsg = subPattern.sub(value, formatMsg)
                formatStrings = formatMsg.split("~~n")
    if formatStrings != []:
        for string in formatStrings:  
           wrapText(string,padTop,padBottom)    
    else:
        wrapText(formatMsg)

def wrapText(msg,padTop = 1, padBottom = 0):
    textwrapper = textwrap.TextWrapper(width = SCREENWIDTH)

    dedented_text = textwrap.dedent(msg)
    if padTop:
        print("\n"*padTop)
    print(textwrapper.fill(dedented_text))
    if padBottom:
        print("\n"*padBottom)

''' Accepts a dictionary object and randomly selects a key.
If the dictionary is nested and the result is an inner dictionary,
recursively makes choices until a non-dictionary value is found to return.
'''
def getStrings(someDict,key):
    # if it's not a dictionary, make it one
    if isinstance(someDict,Character.Adventurer):
        someDict = vars(someDict)

    chooseFrom = someDict[key]
    choice = random.choice(list(chooseFrom))
    result = chooseFrom[choice]
    if isinstance(result,dict):
        getStrings(result,choice)
    else:
        return result







        

def main():
    # set pad variables to True, only include them as parameters if the output should have a 
    # blank line before and/or after it 
    # The default pad values are False in functions that accept them as parameters

    padTop = s.padTopDefault
    padBottom = s.padBottomDefault

    # Change padTop and padBottom to be integers designating the number of blank lines
    # to print using syntax:
    # print(" ")* 10

    print("\n\n\n\n\n")
    print("Time to go adventuring!".center(SCREENWIDTH))

    firstAdventure = True
    goAdventuring = True
    foe = Encounter.Foe()
    enemy = foe.stats
    initDict = {"enemy":enemy,"pc":pc}
    msg = "After having heard tales of a fearsome <enemy~name> making its lair " \
            + "in the SuperSpooky Forest, you decide to hunt it. ~~nBecause reasons. "
    displayText(msg,initDict,padTop=2, padBottom = 1)

    msg = "Press Enter to... ENTER... the forest..."
    displayText(msg,padBottom=3)
    print("")
    input()

    while goAdventuring:

        enemy = foe.stats
        objDict = {"enemy":enemy,"pc":pc}

        ''' some of the time, add a description before the next encounter '''
        ''' break this stuff out into its own function, eventually '''
        if firstAdventure:
            msg = getStrings(gt.env,"adventureStart")
            displayText(msg,initDict)
            firstAdventure = False
        else:
            # 20 here indicates how many sides on the die being rolled
            beat = s.getChance(s.closeCallChance,20)
            if d20.roll() <= beat:
                msg = getStrings(gt.env,"closeCall")
            else:
                msg = getStrings(gt.env,"moreAdventure")
            displayText(msg,objDict)

        foe = Encounter.Foe()
        # stats is a SimpleNamespace object, which allows access to the creature's properties,
        # which are actually in a dictionary, as if they were properties -- so the pc and the enemy
        # can be referenced by this code in the same way regardless of the internal object structure
        

        displayText("~~nYou have encountered <enemy~article> <enemy~name>! <enemy~description>", 
                    objDict,padTop,padBottom)

          
        pc.init = d20.roll()
        enemy.init = d20.roll()
        pcInit = pc.init
        enemyInit = enemy.init
        justEncountered = True
        displayText("~~nRolling for initiative! You roll... <pc~init>",objDict)
        
        if pcInit < enemyInit:
            playerTurn = False
        else:
            playerTurn = True
            
        notDeadYet = True
        

        while notDeadYet:
            # fight or flee
            if playerTurn:
                print("")
                chickenOption = input("Press C to run away, or hit Enter to fight!\t")
                print("")
                if chickenOption.lower() != "c":
                    outcome = fightTurn(pc,enemy)
                    if justEncountered:
                        justEncountered = False
                        scream = getStrings(pc.strings,"encounterScream")
                        scream = "As you attack, you scream " + scream
                        displayText(scream,objDict,padTop)                    
                else:
                    chickenFlee = "~~n~~nYou bravely run away, clucking at the top of your lungs," \
                    + " as ~~nthe <enemy~name> rages behind you. Somehow you know " \
                    + "it is daring you to ~~ngrow a spine someday and face it again."
                    displayText(chickenFlee,objDict)
                    if pc.treasure > 0:
                        chickenDrop = "~~nAlthough you manage to keep a grip on your " \
                        + "weapon, you leave ~~nscattered behind you the grotesque " \
                        + "trophies that would have ~~nbrought you <pc~treasure> gold."
                        displayText(chickenDrop,objDict)
                    displayText("~~nYou had <pc~hp> hit points remaining.",objDict)
                    goAdventuring = False
                    input("\n\n\nPress any key to exit")
                    break
                    
            else:
                if justEncountered:
                    justEncountered = False
                    msg = "Too late -- while you stand there in terror, the <enemy~name> attacks!"
                    displayText(msg,objDict)
                outcome = fightTurn(enemy,pc)
                
            # If fighting, handle a hit 
            if outcome["hit"]:
                if playerTurn:
                    msg = "You swing your <pc~weapon> and hit the creature " \
                    + "for <pc~atkDamage> damage!"
                    playerTurn = False
                    
                else:
                    msg = "The <enemy~name> hits you for <enemy~atkDamage> damage!"
                    playerTurn = True

            # If fighting, handle a miss
            else:
                if playerTurn:
                    msg = "You miss the <enemy~name>!"
                    playerTurn = False
                else:
                    msg = "The <enemy~name> misses!"
                    playerTurn = True
            displayText(msg,objDict,padTop=0,padBottom=0)
                
            # see if anyone died
            if pc.hp <= 0 or enemy.hp <= 0:
                notDeadYet = False
                lastGaspRoll = d20.roll()
        # if you died...
        if pc.hp <= 0:
            goAdventuring = False
            if lastGaspRoll > pc.lastGaspThreshold:
                msg = "~~n~~nYou fall, mortally wounded, and with a whiny bleat you lash out one more time... "
                outcome = fightTurn(pc,enemy)
                if enemy.hp <= 0:
                    msg = msg + "~~n~~nSomehow, you manage to take down your mighty foe " \
                    + "the <enemy~name> even as you fall beneath its vicious onslaught. "
                else:
                    msg = msg + "~~n~~nYour resistance is futile, though. Your weapon falls to " \
                    + "the ground ~~nand you lie crushed and bleeding, the light fading from " \
                    + "your eyes. "
            else:
                msg = "~~nYou fall beneath the <enemy~name>'s vicious onslaught. Your weapon " \
                + "falls to the ground ~~nand you lie crushed and bleeding, the light fading " \
                + "from your eyes. "
            
            msg = msg + "~~n~~nThe <enemy~name> begins to feast. "

            displayText(msg,objDict,padTop=0)

            input("\n\n\nPress any key to exit. Come kill more things soon! ")

        # if the monster died...
        elif enemy.hp <= 0:
            if lastGaspRoll >= enemy.lastGaspThreshold:
                msg = "~~nWith an unearthly shriek, the <enemy~name> keels " \
                    + "over and breathes its last, ~~ntaking a final swipe at you " \
                    + "before slamming into the earth. "
                fightTurn(enemy,pc)

                if pc.hp <= 0:
                    msg = msg + "~~n~~nIts blow rakes your face and your world turns red, " \
                    + "then ~~ntilts sideways and you thump to the ground facing the " \
                    + "<enemy~name> ~~nwhere you remain, one dead thing staring at another. "
                
                else:
                   msg = msg + "~~n~~nYou narrowly avoid what might have been a death blow, and take " \
                    + "~~na few moments to recover your composure before approaching the still-warm ~~ncorpse. "
   
                msg = msg + "<enemy~dropDescription> which you estimate will bring " \
                    + "you <enemy~dropValue> gold."
            else:
                msg = "<enemy~dropDescription> which you estimate ~~nwill bring " \
                    + "you <enemy~dropValue> gold. "
            displayText(msg,objDict,padTop=0)
            pc.treasure = pc.treasure + enemy.dropValue
            if pc.hp < 10:
                print("\nYou're hurt so badly you're walking like a drunken Jack Sparrow.")
            elif pc.hp < 20:
                print("\nYou're starting to feel pretty banged up.")
            elif pc.hp < 30:
                print("\nYou feel a little tired.")
            elif pc.hp < 40:
                print("\nYou feel pretty good.")
            hunt = input("Continue adventure? (Y/N)\t")
            if hunt.lower() != "y":
                goAdventuring = False
                msg = "~~nYou decide your grisly haul worth <pc~treasure> gold pieces " \
                + "is enough for one day. Whistling, ~~nyou shoulder your " \
                + "trusty <pc~weapon> and head for home " \
                + "where, ~~nyou hope, no monsters lurk."
                displayText(msg,objDict)
                input("\n\n\nPress any key to exit. Come kill more things soon!")
    













if __name__ == "__main__":
    #app = Flask(__name__)
    #@app.route('/')

    os.system('cls')

    PC = True
    FOE = False
    SCREENWIDTH = 80
    playerTurn = True

    s = GameSettings.Settings()
    gt = gametext.GameText()

    d20 = DungeonDie.Die(20)
    d10 = DungeonDie.Die(10)
    d8 = DungeonDie.Die(8)
    d6 = DungeonDie.Die(6)
    d4 = DungeonDie.Die(4)
    

    pc = Character.Adventurer()
    main()
    #displayText("This is <enemy~article> <enemy~name> test string.",objDict)
    
    # https://stackoverflow.com/questions/4979542/python-use-list-as-function-parameters

    
    