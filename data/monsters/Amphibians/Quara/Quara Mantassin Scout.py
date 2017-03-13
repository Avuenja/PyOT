quara_mantassin_scout = genMonster("Quara Mantassin Scout", 72, 6064)
quara_mantassin_scout.health(220)
quara_mantassin_scout.type("blood")
quara_mantassin_scout.defense(armor=7, fire=0, earth=1.1, energy=1.1, ice=0, holy=1, death=1, physical=1, drown=0)
quara_mantassin_scout.experience(100)
quara_mantassin_scout.speed(270)
quara_mantassin_scout.behavior(summonable=0, hostile=True, illusionable=False, convinceable=480, pushable=False, pushItems=True, pushCreatures=False, targetDistance=1, runOnHealth=40)
quara_mantassin_scout.walkAround(energy=1, fire=0, poison=1)
quara_mantassin_scout.immunity(paralyze=1, invisible=0, lifedrain=0, drunk=1)
quara_mantassin_scout.voices("Shrrrr", "Zuerk Pachak!")
quara_mantassin_scout.loot( (2148, 100, 30), ("chain armor", 5.0), ("two handed sword", 0.5), ("skull", 1.25), ("mantassin tail", 1.25), ("stealth ring", 0.25), ("fish fin", 0.5, 3) )

quara_mantassin_scout.melee(110)