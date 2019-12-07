########### ATTACKS ###########

class Attack:
    def __init__(self, name, power, PP, type, Special):
        self.name = name
        self.power = power
        self.PP = PP
        self.type = type
        self.special = Special


class pokemon:

    def __init__(self, pokemon_name, sprite, atk1, atk2, atk3, atk4, type, HP, Defense, Speed, Special_Defense):

        self.pokemon_name = pokemon_name
        self.sprite = sprite
        self.atk1 = atk1
        self.atk2 = atk2
        self.atk3 = atk3
        self.atk4 = atk4
        self.type = type
        self.HP = HP
        self.defense = Defense
        self.speed = Speed
        self.special_defense = Special_Defense
