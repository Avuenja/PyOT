instant = spell.Spell("Groundshaker", "exori mas", icon=106, group=ATTACK_GROUP)
instant.require(mana=160, level=33, maglevel=0, learned=0, vocations=(4, 8))
instant.cooldowns(8, 2)
instant.area(AREA_CIRCLE3)
instant.targetEffect(callback=spell.meleeBased(1, 1, 0.5, 1.1, PHYSICAL))
instant.effects(area=EFFECT_GROUNDSHAKER)