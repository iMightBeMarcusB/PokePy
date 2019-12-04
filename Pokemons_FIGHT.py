from random import randint

# Função para ataques que envolvem "sorte" ,por exemplo, queimar o adversário
def sorte(N):
    a = 0
    for i in range(N):
        if randint(1,100) % 2 == 0:
            a +=1
    if a > N or a > int((1/2)*N):
        return True
    else:
        return False


# Definindo a classe pokemon que oferece as propriedades de cada pokemon ofertado com nome os 4 ataques, tipo de pokemon, HP, pontos de defesa, Velocidade, Pontos de defesa especial
class pokemon:

    def __init__(self, pokemon_name, attack1, attack2, attack3, attack4, type, HP, Defense, Speed, Special_Defense):

        self.pokemon_name = pokemon_name
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
        self.type = type
        self.HP = HP
        self.defense = Defense
        self.speed = Speed
        self.special_defense = Special_Defense



#Definindo uma classe para os attacks dividindo em nome, poder, PP, tipo e se é especial, fisico ou de status
class Attack:
    def __init__(self, name, power, PP, type, Special):
        self.name = name
        self.power = power
        self.PP = PP
        self.type = type
        self.special = Special

#Attacks dos pokemon

Tackle = Attack("Tackle", 40, 35, "Normal","Physical")

Leech_Seed = Attack("Leech_Seed", 0, 10, "Grass","Special") # Planta sementes e rouba vida

Growl = Attack("Growl", 0, 25, "Normal", "Status") # Diminui a defesa do inimigo

Vine_Whip = Attack("Vine Whip", 45, 25, "Grass", "Physical")

Ember = Attack("Ember", 40, 25, "Fire", "Special") # Possui chance de queimar o inimigo

Scratch = Attack ("Scratch", 40, 25, "Normal", "Physical")

Fire_Fang = Attack("Fire Fang", 60, 15, "Fire", "Physical")

Water_Gun = Attack("Water Gun", 40, 25, "Water","Special")

Water_Pulse = Attack("Water Pulse", 60, 20, "Water","Special")

Withdraw = Attack("Withdraw", 0, 40, "Water", "Status") # Aumenta sua defesa

Thunder_Shock = Attack("Thunder Shock", 40, 30, "Electric", "Special")

Quick_Attack = Attack("Quick Attack", 40, 30, "Normal", "Physical") # Sempre Ataca Primeiro

Thunder_Wave = Attack("Thunder Wave", 0, 20, "Electric", "Status") # rever status e paralize

Bone_Club = Attack("Bone Club", 65, 20, "Ground", "Physical")

Headbutt = Attack("Headbutt", 70, 15, "Normal", "Physical")

Bonemerang = Attack("Bonemerang", 50, 10, "Ground", "Physical") # pode ir e voltar

Ice_Fang = Attack("Ice Fang", 65, 15, "Ice", "Special") #10% chance de congelar


Flail = Attack("Flail", 48, 15, "Normal", "Physical")

Shadow_Punch= Attack("Shadow Punch", 60, 20, "Ghost", "Physical")

Curse = Attack("Curse", 0, 10, "Ghost", "Special") #seu pokemon perde 25% do HP mas causa 50% do HP max do inimigo por round talvez STATUS

Payback = Attack("Payback", 50, 10, "Dark", "Physical")

Hex = Attack("Hex ", 65, 10, "Ghost", "Special") # dobra a força se o usuario ja possuir doença ou paralize e tal

Revenge = Attack("Revenge ", 60, 10, "Fighting", "Physical")# da mais dano se for devolvido

Fake_Out = Attack("Fake Out", 90, 10, "Normal", "Physical")


Reversal = Attack("Reversal", 48, 15, "fighting", "Physical")

Rock_Throw = Attack("Rock Throw", 50, 15, "Rock", "Physical")

Earthquake = Attack("Earthquake", 100, 10, "Ground", "Physical")

Explosion = Attack("Explosion", 250, 5, "Normal", "Physical")

Wing_Attack = Attack("Wing Attack", 60, 35, "Flying", "Physical")

Agility = Attack("Agility", 0, 30, "Psychic", "Status")

Razor_Wind = Attack("Razor Wind", 80, 10, "Normal", "Physical")

#Pokemons

Bulbasaur = pokemon("Bulbasaur", Tackle, Leech_Seed, Growl, Vine_Whip, "Grass", 120, 20, 25, 30)

Charmander = pokemon("Charmander", Scratch, Ember, Growl, Fire_Fang, "Fire", 130, 20, 30, 30)

Squirtle = pokemon("Squirtle", Tackle, Water_Gun, Water_Pulse, Withdraw,"Water", 110, 30, 35, 30)

Pikachu = pokemon("Pikachu", Quick_Attack, Thunder_Shock, Tackle, Thunder_Wave, "Electric", 160, 15, 45, 25)

Cubone = pokemon("Cubone", Bone_Club, Headbutt, Growl, Bonemerang, "Ground", 130, 35,25, 15)

Totodile = pokemon("Totodile", Ice_Fang, Flail, Scratch, Water_Gun, "Water", 130, 25, 30, 25)

Gengar = pokemon("Gengar", Hex, Payback, Curse, Shadow_Punch, "Ghost", 140, 200, 30, 20)

Hitmonlee = pokemon("Hitmonlee", Tackle, Reversal, Revenge, Fake_Out, "Fighting", 130, 35, 30,15)

Graveler = pokemon("Graveler", Tackle, Rock_Throw, Earthquake, Explosion, "Rock", 140, 35, 15, 15)

Pidgeot = pokemon("Pidgeot", Quick_Attack, Razor_Wind, Agility, Wing_Attack, "Flying", 120, 20, 50, 20)

#Definindo uma função especial para Burn (Queimará os inimigos causando 5 de dano para as proximas 4 partidas, se você tiver sorte e Seed que não depende da sorte.

def burn(Pokemon):
    return [Pokemon, 5]

def seed(Pokemon, HP0):
    return [Pokemon, int((1/8)*HP0)]

def paralized(attack,Pokemon1, Pokemon2):
    cursed = []
    Leech_Seed_Damage = 0
    if Pokemon1.HP > 0 and Pokemon2.HP > 0:

        # Função que permite a chamada do ataque e permite a checagem se ele traz alguma "maldição"
        Attack1 = attack

        if Pokemon1.speed >= Pokemon2.speed or Attack1 == Quick_Attack:
            info1 = Special(Attack1, Pokemon2, Pokemon1, 1, 1)

            if Attack1.special == "Physical":
                if info1[0] > Pokemon2.defense:
                    Pokemon2.HP -= info1[0] - Pokemon2.defense

            elif Attack1.special == "Special":
                if info1[0] > Pokemon2.special_defense and not Attack1 == Leech_Seed:
                    Pokemon2.HP -= info1[0] - Pokemon2.special_defense
                elif Attack1 == Leech_Seed:
                    Leech_Seed_Damage = int((1 / 8) * HP2)
                    Pokemon2.HP -= Leech_Seed_Damage
                1
            elif Attack1.special == "Status":
                if Attack1 == Growl:
                    Pokemon2.defense -= 12
                elif Attack1 == Withdraw:
                    Pokemon1.defense += 12

            if len(info1) > 1:
                if info1[1] not in cursed:
                    cursed.append(info1[1])

            if len(cursed) > 0:
                for c in range(len(cursed)):
                    cursed[c][0].HP -= cursed[c][1]

                    if cursed[c][1] == Leech_Seed_Damage and cursed[c][0] == Pokemon1:
                        Pokemon2.HP += int(Leech_Seed_Damage / 2)
                    elif cursed[c][1] == Leech_Seed_Damage and cursed[c][0] == Pokemon2:
                        Pokemon1.HP += int(Leech_Seed_Damage / 2)
                    if len(cursed[c]) > 3:
                        if cursed[c][3] == "Thunder Wave":
                            for i in range(0, 3):
                                Print("Só ", Pokemon1.pokemon_name, "pode jogar")
                                if cursed[c][0] == Pokemon1:
                                    Paralized(pcs_turn(Pokemon2), Pokemon1, Pokemon2)
                                elif cursed[c][0] == Pokemon2:
                                    Paralized(player1(Pokemon1), Pokemon1, Pokemon2)

                    for i in range(0, len(cursed) - len(turn)):
                        turn.append(0)
                    turn[c] += 1
                if turn[c] == 4:
                    cursed.pop(c)
    return Pokemon2.HP



def player1(Pokemon1):
    # Escolha seu ataque
    a = int(input())
    if a == 1:
        Attack0 = Pokemon1.attack1
    elif a == 2:
        Attack0 = Pokemon1.attack2
    elif a == 3:
        Attack0 = Pokemon1.attack3
    elif a == 4:
        Attack0 = Pokemon1.attack4
    return Attack0


def pcs_turn(Pokemon2):

    a = randint(1,4)

    if a == 1:
        Attack0 = Pokemon2.attack1
    elif a == 2:
        Attack0 = Pokemon2.attack2
    elif a == 3:
        Attack0 = Pokemon2.attack3
    elif a == 4:
        Attack0 = Pokemon2.attack4

    return Attack0

def Special(attack, Pokemon2, Pokemon1, HP0, HP1):
    N = int((48 * Pokemon1.HP) / HP1)

    if attack == Leech_Seed:

        return [int((1/8)*HP0), seed(Pokemon2, HP0)]

    elif attack == Ember:
        if sorte(4):
            return [Ember.power, burn(Pokemon2)]
        else:
            return [Ember.power]

    elif attack == Reversal or attack == Flail:
        return [96 - N]
    elif attack == Thunder_Wave:
        if sorte(1):
            return[0, [Pokemon2, 0,"Thunder Wave"]]
        else:
            return[0]
    else:
        return [attack.power]

turn = []


def fight_1P(Pokemon1,Pokemon2):
    HP1 = Pokemon1.HP
    HP2 = Pokemon2.HP
    cursed = []
    Leech_Seed_Damage = 0
    while Pokemon1.HP > 0 and Pokemon2.HP > 0:

        # Função que permite a chamada do ataque e permite a checagem se ele traz alguma "maldição"
        Attack1 = player1(Pokemon1)
        Attack2 = pcs_turn(Pokemon2)

        if Pokemon1.speed >= Pokemon2.speed or Attack1 == Quick_Attack:
            info1 = Special(Attack1, Pokemon2, Pokemon1, HP2, HP1)

            if Attack1.special == "Physical":
                if info1[0] > Pokemon2.defense:
                    Pokemon2.HP -= info1[0] - Pokemon2.defense

            elif Attack1.special == "Special":
                if info1[0] > Pokemon2.special_defense and not Attack1 == Leech_Seed:
                    Pokemon2.HP -= info1[0] - Pokemon2.special_defense
                elif Attack1 == Leech_Seed:
                    Leech_Seed_Damage = int((1/8)*HP2)
                    Pokemon2.HP -= Leech_Seed_Damage

            elif Attack1.special == "Status":
                if Attack1 == Growl:
                    Pokemon2.defense -= 12
                elif Attack1 == Withdraw:
                    Pokemon1.defense += 12

            if len(info1) > 1:
                if info1[1] not in cursed:
                    cursed.append(info1[1])

            # Colocar aqui as informações de quando um round passa pro round do outro ou seja, quanto de HP perdeu e tal
            info2 = Special(Attack2, Pokemon1, Pokemon2, HP1, HP2)

            if Attack2.special == "Physical":
                if info2[0] > Pokemon1.defense:
                    Pokemon1.HP -= info2[0] - Pokemon1.defense

            elif Attack2.special == "Special":
                if info2[0] > Pokemon1.special_defense and not Attack2 == Leech_Seed:
                    Pokemon1.HP -= info2[0] - Pokemon1.special_defense
                elif Attack2 == Leech_Seed:
                    Leech_Seed_Damage = int((1 / 8) * HP1)
                    Pokemon1.HP -= Leech_Seed_Damage

            elif Attack2.special == "Status":
                if Attack2 == Growl:
                    Pokemon1.defense -= 12
                elif Attack1 == Withdraw:
                    Pokemon1.defense += 12


            if len(info2) > 1:
                if info2[1] not in cursed:
                    cursed.append(info2[1])

            if len(cursed) > 0:
                for c in range(len(cursed)):
                    cursed[c][0].HP -= cursed[c][1]

                    if cursed[c][1] == Leech_Seed_Damage and cursed[c][0] == Pokemon1:
                        Pokemon2.HP += int(Leech_Seed_Damage/2)
                    elif cursed[c][1] == Leech_Seed_Damage and cursed[c][0] == Pokemon2:
                        Pokemon1.HP += int(Leech_Seed_Damage/2)

                    if len(cursed[c]) > 2:
                        if cursed[c][2] == "Thunder Wave":
                            for i in range(0, 3):
                                print("Só",Pokemon1.pokemon_name,"pode jogar")
                                if Pokemon2 not in cursed and Pokemon1 not in cursed:
                                    if cursed[c][0] == Pokemon1:
                                        Pokemon1.HP = paralized(pcs_turn(Pokemon2), Pokemon1, Pokemon2)
                                    elif cursed[c][0] == Pokemon2:
                                        Pokemon2.HP = paralized(player1(Pokemon1), Pokemon1, Pokemon2)
                                if i < 2:
                                    print(Pokemon1.HP)
                                    print(Pokemon2.HP)
                            cursed.pop(c)



                    for i in range(0, len(cursed)-len(turn)):
                        turn.append(0)
                    if len(cursed)> 0:
                        turn[c] += 1
                        if turn[c] >= 4:
                            cursed.pop(c)

         #por conta da velocidade
        elif Pokemon2.speed > Pokemon1.speed or Attack2 == Quick_Attack:
            info1 = Special(Attack1, Pokemon2, Pokemon1, HP2, HP1)

            if Attack1.special == "Physical":
                if info1[0] > Pokemon2.defense:
                    Pokemon2.HP -= info1[0] - Pokemon2.defense

            elif Attack1.special == "Special":
                if info1[0] > Pokemon2.special_defense and not Attack1 == Leech_Seed:
                    Pokemon2.HP -= info1[0] - Pokemon2.special_defense
                elif Attack1 == Leech_Seed:
                    Leech_Seed_Damage = int((1 / 8) * HP2)
                    Pokemon2.HP -= Leech_Seed_Damage

            elif Attack1.special == "Status":
                if Attack1 == Growl:
                    Pokemon2.defense -= 12
                elif Attack1 == Withdraw:
                    Pokemon1.defense += 12

            if len(info1) > 1:
                if info1[1] not in cursed:
                    cursed.append(info1[1])

            info2 = Special(Attack2, Pokemon1, Pokemon2, HP1, HP2)

            if Attack2.special == "Physical":
                if info2[0] > Pokemon1.defense:
                    Pokemon1.HP -= info2[0] - Pokemon1.defense

            elif Attack2.special == "Special":
                if info2[0] > Pokemon1.special_defense and not Attack2 == Leech_Seed:
                    Pokemon1.HP -= info2[0] - Pokemon1.special_defense
                elif Attack2 == Leech_Seed:
                    Leech_Seed_Damage = int((1 / 8) * HP1)
                    Pokemon1.HP -= Leech_Seed_Damage

            elif Attack2.special == "Status":
                if Attack2 == Growl:
                    Pokemon1.defense -= 12
                elif Attack1 == Withdraw:
                    Pokemon1.defense += 12

            if len(info2) > 1:
                if info2[1] not in cursed:
                    cursed.append(info2[1])

            if len(cursed) > 0:
                for c in range(len(cursed)):
                    cursed[c][0].HP -= cursed[c][1]

                    if cursed[c][1] == Leech_Seed_Damage and cursed[c][0] == Pokemon1:
                        Pokemon2.HP += int(Leech_Seed_Damage/2)
                    elif cursed[c][1] == Leech_Seed_Damage and cursed[c][0] == Pokemon2:
                        Pokemon1.HP += int(Leech_Seed_Damage/2)
                    if len(cursed[c]) > 3:
                        if cursed[c][3] == "Thunder Wave":
                            for i in range(0, 3):
                                Print("Só ", Pokemon1.pokemon_name, "pode jogar")
                                if cursed[c][0] == Pokemon1:
                                    Paralized(pcs_turn(Pokemon2), Pokemon1, Pokemon2)
                                elif cursed[c][0] == Pokemon2:
                                    Paralized(player1(Pokemon1), Pokemon1, Pokemon2)
                            cursed.pop(0)

                    for i in range(len(cursed) - len(turn)):
                        turn.append(0)
                    if len(turn) > 0:
                        turn[c] += 1

                if len(turn) > 0:
                    if turn[c] == 4:
                        cursed.pop(c)

fight_1P(Pikachu, Charmander)
