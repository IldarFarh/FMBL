import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 25
        mgh = self.magic[i]["dmg"] + 25
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell(self, i):
        return self.magic[i]
    
    def get_stats(self):
        return {"hp": self.hp,
                "maxhp": self.maxhp,
                "mp": self.mp,
                "maxmp": self.maxmp,}

    def choose_action(self):
        i = 1
        answer = {"text": "Choose from actions", "quick_replies":[]}
        for item in self.actions:
            answer["quick_replies"].append({
                "content_type":"text",
                "title":item,
                "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_"+item.capitalize() 
            })
            i += 1
        print(answer)
        return answer

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1
    