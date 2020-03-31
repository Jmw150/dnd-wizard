
# code assistance
from random import randint
from math import floor

# dice rolls
dn   = lambda n : randint(1,n)
d2   = lambda : randint(1,2)
d4   = lambda : randint(1,4)
d6   = lambda : randint(1,6)
d8   = lambda : randint(1,8)
d10  = lambda : randint(1,10)
d12  = lambda : randint(1,12)
d20  = lambda : randint(1,20)
d100 = lambda : randint(1,100)

lvl = 9

class Varis :
    """
gem
7 charges (recharges d6 charges at dawn)
- use extra charge to upcast a level 
lightining bolt (1 charge, dc 15) 
chain lighting (5 charges, dc 15)

if you use 5 charges at once, (xd4 lighting damage to self, x=charges)
acrobatics [dex]
animal handeling [wis]
arcana [int] prof 
athletics [str]
deception [cha]
historm [int]
insight [wis]
intimidation [cha]
investigation [int]
medicine [wis]
nature [int]
perception [wis]
persuation [cha]
religion [int]
sleight of hand [dex]
stealth [dex]
survival [wis]
necessarily

# cantrip
mage hand
mending
prestidigitation
fire bolt: d20 + (3+4)[prof_bon, int mod] to hit, d10 to dmg

lvl 1 [3|4]
(*) magic missile 
//(*) catapult: spell-save = 15 = 8 + 3[prof_bon] + 4[int_mod],
    3d8()
(r) find familiar
(*) feather fall
(*) detect magic
(r) identify
( ) charm person

lvl 2 [3|3] 
( ) invisibility
( ) see invisibility
(*) mirror image
(*) misty step
(*) knock

lvl 3 [2|3] 
(*) fireball
//( ) magic weapon
(*) haste 
(*) fly

lvl 4 [2|2]
( ) fabricate
(*) otiluke's resilient sphere

lvl 5 [1|1]
(*) passwall
( ) wall of force

4/7 lightning bolts 
can do chain lightning

"ultimate healing potion, 3 doses"
hell hound dust
turn scroll spells into books spells (25gp, 2 hours)
scrolls:
    fly (copied to spell book)
    charm person (copied to spell book)
    web 
    sleet storm
    fog cloud
    enlarge/reduce
    Tasha's hideous laughter
    Expeditious retreat
    Melf's acid arrow
    evards black tentacles
    ottos irresistable dance

needs to collect everything

    """
    class Main_stat :
        def __init__(self,score):
            self.score = score
            self.mod = floor(score/2)-5
        def __repr__(self):
            return str(self.score) 
        def __add__(self, o): 
            return self.score + o

    name = 'Varis'
    #raven_name = 'Bertrand'
    # from a college in NeverWinter
    lvl = 9
    lvl_type = 'wizard'
    race = 'high elf'

    strength = Main_stat(10)     # 10, 0
    dexterity = Main_stat(16)    # 16, 3
    constitution = Main_stat(10) # 10, 0
    intelligence = Main_stat(18) # 18, 4
    wisdom = Main_stat(13)       # 13, 1
    charisma = Main_stat(10)     # 10, 0
    
    proficiency_bonus = [0,
                       2,2,2,2,
                       3,3,3,3,
                       4,4,4,4,
                       5,5,5,5,
                       6,6,6,6][lvl]
    
    armor_class = 15
    initiative = dexterity.mod # 3
    speed = 30 
    max_hp = 6+4*lvl# 44
    hp = max_hp
    passive_perception = 10 + wisdom.mod # 10+2=12
    spell_save_dc = 8 + proficiency_bonus+intelligence.mod # 15
    spell_attack_mod = proficiency_bonus+intelligence.mod # 7
    
    advantage = 0
    can_see_invisible_stuff = 0
    duplicates = 0
    bardic_inpspiration = 0 #d6()  on saves or att roll
    hp_pots = 1 # drank two
    money = "money: 3gold_pieces + 30copper_pieces"
    stuff = [
        'hell hound dust',
        'gem of lighting bolts',
        'super heal potion (3 doses)',
        'regular heal potion',
        'philosphers stone (Resistance to acid, cold, fire, lightning, or thunder damage)'
    ]

    def heal(x):
        if x < 0 :
            return 'no...'
        elif x+hp > max_hp :
            hp = max_hp

    def damage(x):
        if x < 0 :
            return 'no...'
        elif 0 < hp-x :
            hp -= x
        elif 0 >= hp-x :
            hp = 0
            return "You are down"
        elif 2*max_hp <= x :
            return "You died"

    def use_hp_pot(): 
        hp_pots -= 1
        heal(d4()+d4()+2)
    
    concentration_save = lambda : d20() + constitution.mod

    class Spell_book :
        
        class Cantrip :
            def known(x): 
                if lvl >= 1 and lvl <= 3 :
                    return 3
                elif lvl >= 4 and lvl <= 9 :
                    return 4
                elif lvl >= 10 and lvl <= 20 :
                    return 5
            known = known(lvl)
            mage_hand = 1
            mending = 1
            prestidigitation = 1
            def fire_bolt(i=''): 
                """ #d20 + (3+4)[prof_bon, int mod] to hit, 2d10 to dmg"""
                # roll for attack
                # used inspiration
                if i == 'i' and inspiration > 0 : 
                    att = max(d20(),d20())
                    inspiration -= 1
                elif advantage == 1 :
                    att = max(d20(),d20())
                else :
                    att = d20()

                # crit hit
                if att == 20 : 
                    dmg = d10()+d10()+d10()+d10()
                else :
                    dmg = d10()+d10()

                return 1 #d20 + (3+4)[prof_bon, int mod] to hit, d10 to dmg
        cantrip = Cantrip()
        class Lvl1:
            def max_spells_slots(x): 
                if lvl == 1 :
                    return 2
                elif lvl == 2 :
                    return 3
                elif lvl >= 3 and lvl <= 20 :
                    return 4
            max_spells_slots = max_spells_slots(lvl)
            spells_slots = max_spells_slots
            magic_missile = 1
            #(*) catapult: spell-save = 15 = 8 + 3[prof_bon] + 4[int_mod], 3d8()
            find_familiar = 1
            feather_fall = 1
            detect_magic = 1
            identify = 1
        lvl1 = Lvl1()
        class Lvl2: # 0/3
            def max_spells_slots(x): 
                if lvl == 1 and lvl == 2 :
                    return 'none'
                elif lvl == 3 :
                    return 2
                elif lvl >= 4 and lvl <= 20 :
                    return 3
            max_spells_slots = max_spells_slots(lvl)
            spells_slots = max_spells_slots
            spell_slots = 3
            invisibility = 0
            see_invisibility = 0
            mirror_image = 1
            misty_step = 1
        lvl2 = Lvl2()
        class Lvl3: # 0/3
            def max_spells_slots(x): 
                if lvl == 1 and lvl == 2 :
                    return 'none'
                elif lvl == 3 :
                    return 2
                elif lvl >= 4 and lvl <= 20 :
                    return 3
            max_spells_slots = max_spells_slots(lvl)
            spells_slots = max_spells_slots
            def fire_ball(Lvl=3) :
                Sum = 0
                for i in range(1,5+Lvl) :
                    Sum += d6()
                return Sum
            #( ) magic weapon
            haste = 1
        lvl3 = Lvl3()
        class Lvl4: 
            def max_spells_slots(x): 
                if lvl >= 1 and lvl <= 6 :
                    return 'none'
                elif lvl == 7 :
                    return 1
                elif lvl == 8 :
                    return 2
                elif lvl >= 9 and lvl <= 20 :
                    return 3
            max_spells_slots = max_spells_slots(lvl)
            spells_slots = max_spells_slots
            Otilukes_Resilient_Sphere = 0
            Stone_Shape = 0
        lvl4 = Lvl4()
        
    spell_book = Spell_book()
            
    def __init__(self, 
                 hp=max_hp, 
                 inspired=0):
        self.hp = hp
        self.inspiration=inspired


varis = Varis()


def interact():
    import code
    code.InteractiveConsole(locals=globals()).interact()
interact()

