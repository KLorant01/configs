import random
import Data

class Crew_Member:
    morale: int = 100
    def __init__(self, gender=None, is_lega=None, name=None, profession=None, AG: int=0, IQ: int=0, ST: int=0, CH: int=0, CN: int=0):
        self.gender = gender
        self.is_lega = is_lega
        self.name: str = name
        self.profession: str = profession
        self.AG: int = AG
        self.IQ: int = IQ
        self.ST: int = ST
        self.CH: int = CH
        self.CN: int = CN
        self.conditions: list = []
    def new_condition(self, new_condition):
        match new_condition:
            case 'Chessmaster':
                self.IQ += 1
            case 'Genius':
                self.IQ += 2
            case 'Athlete':
                self.AG += 1
                self.ST += 1
            case 'Durable':
                self.CN += 2
                self.health += 3
            case 'The perfect solder':
                self.AG += 1
                self.ST += 1
                self.CN += 1
            case 'Bear':
                self.ST += 3
            case 'bossy':
                self.CH += 2
            case 'Wise':
                self.IQ += 1
                self.CH += 1
            case 'Runner':
                self.AG += 1
            case 'Bahu Bali':
                self.AG += 2
                self.ST += 2
                self.CN += 2
        self.conditions.append(new_condition)

    def make(self, profession, skill_points, dice):
        skill_points: int = skill_points + random.randint(1, dice)
        skill_list: list = ['AG', 'IQ', 'ST', 'CH', 'CN']
        self.IQ = 0
        self.ST = 0
        self.AG = 0
        self.CH = 0
        self.CN = 0
        self.profession = profession
        self.is_lega = False

        self.gender = random.choice([0, 1])  # 0 == female
        if random.randint(0, 20) == 0:
            self.is_lega = True

        if self.gender == 0:
            if self.is_lega:    self.name = random.choice(Data.legendary_female_names)
            else:               self.name = random.choice(Data.popular_female_names)

        else:
            if self.is_lega:    self.name = random.choice(Data.legendary_male_names)
            else:               self.name = random.choice(Data.popular_male_names)

        for i in Data.professions[profession][0]:
            for _ in range(Data.professions[profession][0][i] * 2):
                skill_list.append(i)

        for i in range(skill_points):
            match random.choice(skill_list):
                case 'AG':
                    self.AG += 1
                case 'IQ':
                    self.IQ += 1
                case 'ST':
                    self.ST += 1
                case 'CH':
                    self.CH += 1
                case 'CN':
                    self.CN += 1

        self.health = 6 +self.CN

#        Crew_Member.new_condition(self, random.choices(Data.conditions)[0])

if False:
    One = Crew_Member()
    Two = Crew_Member()
    Tree = Crew_Member()

    Crew_Member.make(One, 'commander', 10, 4)
    Crew_Member.make(Two, 'diplomat', 10, 4)
    Crew_Member.make(Tree, 'biologist', 10, 4)

    print(One.gender)
    print(One.is_lega)
    print(One.name)
    print(One.profession)
    print('')
    print(One.AG)
    print(One.IQ)
    print(One.ST)
    print(One.CH)
    print(One.CN)
    print('')
    print(One.health)
    print(One.morale)
    print(One.conditions)

    print('/////////////////////////////////')

    print(Two.gender)
    print(Two.is_lega)
    print(Two.name)
    print(Two.profession)
    print('')
    print(Two.AG)
    print(Two.IQ)
    print(Two.ST)
    print(Two.CH)
    print(Two.CN)
    print('')
    print(Two.health)
    print(Two.morale)
    print(Two.conditions)

    print('/////////////////////////////////')

    print(Tree.gender)
    print(Tree.is_lega)
    print(Tree.name)
    print(Tree.profession)
    print('')
    print(Tree.AG)
    print(Tree.IQ)
    print(Tree.ST)
    print(Tree.CH)
    print(Tree.CN)
    print('')
    print(Tree.health)
    print(Tree.morale)
    print(Tree.conditions)