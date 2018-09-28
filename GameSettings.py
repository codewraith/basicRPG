class Settings:
    def __init__(self):
        ''' Switches to enable/disable specific settings '''
        self.enemyLastGaspEnabled = True
        self.pcLastGaspEnabled = True
        self.pcEncounterScreamEnabled = True

        ''' values to use in generating random.randint() parameters for specific settings '''
        self.enemyLastGaspChance = .70
        self.pcLastGaspChance = .70
        self.pcEncounterScreamChance = .30

        ''' defaults for other settings '''
        self.enemyTreasureDropChance = 1.00
        self.padTopDefault = 1
        self.padBottomDefault = 0
        self.closeCallChance = .3

    def getChance(self,chance,dieSides):
        if isinstance(chance,float) and isinstance(dieSides,int):
            return(round(chance * float(dieSides)))
        else:
            return(dieSides)
        



