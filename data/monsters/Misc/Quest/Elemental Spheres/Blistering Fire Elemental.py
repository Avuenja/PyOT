blistering_fire_elemental = genMonster("Blistering Fire Elemental", 242, 8964)
blistering_fire_elemental.health(1500)
blistering_fire_elemental.type("blood")
blistering_fire_elemental.defense(armor=50, fire=0, earth=0.5, energy=0.8, ice=1.15, holy=0, death=0.6, physical=0.75, drown=1)
blistering_fire_elemental.experience(1300)
blistering_fire_elemental.speed(230)
blistering_fire_elemental.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
blistering_fire_elemental.walkAround(energy=1, fire=0, poison=1)
blistering_fire_elemental.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
blistering_fire_elemental.voices("FCHHHRRR")
blistering_fire_elemental.melee(350)
blistering_fire_elemental.loot( (2148, 100, 148), ("small ruby", 14.0, 2), ("fiery heart", 16.25), ("glimmering soil", 8.25), ("coal", 1.25) )