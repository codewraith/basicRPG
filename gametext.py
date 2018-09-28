"""
Eventually, these will be in database tables

"""

class GameText:
    def __init__(self):
        self.env = {"adventureStart": {"eldritch":"You enter the nearby forest in search of adventure and riches. " \
                                        + "You're not exactly sure what eldritch means, but you're pretty " \
                                        + "sure someone has used that word when describing these woods. ",
                                        "saunter":"You saunter into the woods, swinging your <pc~weapon>. "
                                        },
                    "moreAdventure": {"venture":"Danger is nothing to you! You venture deeper into " \
                                        + "the darkening woods. ",
                                        "badIdea":{"denial":"You tell yourself that <enemy.name> wasn't so bad, " \
                                                    + "showing a prodigious ability to ignore reality, and " \
                                                    + "wander on in search of another chance to die. ",
                                                    "bawkbawk":"You really want to go home, but your " \
                                                    + "friends would make fun of you so you tiptoe " \
                                                    + "down the path. "
                                                    }
                                        },
                            "closeCall":{"ridinghood":"There's a rustling in the brush nearby. " \
                                        + "Fearing that the slain <enemy.name> had a mate nearby, " \
                                        + "you hide behind a tree, heart pounding, till a " \
                                        + "little girl in a crimson cloak with a hood skips " \
                                        + "past, swinging a basket. Hoping she didn't see you, " \
                                        + "you wait a few minutes then head in the opposite " \
                                        + "direction. ",
                                        "birds":"Some birds burst out of a cluster of trees beside " \
                                        + "you, almost making you wet yourself. They sound like they're " \
                                        + "laughing. Grumbling, you stalk onwards. "
                                        }
                            }                    
                    