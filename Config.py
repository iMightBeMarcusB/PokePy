import pygame
import PokemonsAttacks as pa
################### COORDINATES ###################

'''
    posição da seta durante o estágio de
    opções de batalha
'''
fight_a = (425, 468)
pokemon_a = (425, 528)
bag_a = (611, 468)
run_a = (611, 528)
upper_a = 468
bottom_a = 528
left_a = 425
right_a = 611

#######################################
''' 
    posição do texto referente aos
    ataques de cada pokemon, no
    estágio de selção de ataque
'''

left_attack_b = 50
right_attack_b = 300
upper_attack_b = 460
bottom_attack_b = 520

#######################################
'''
    posição da seta durante o estágio 
    de seleção de ataque
'''

left_attack_a = left_attack_b - 25
right_attack_a = right_attack_b - 25
upper_attack_a = upper_attack_b - 5
bottom_attack_a = bottom_attack_b - 5

#######################################
'''
   posição da seta durante o estágio
    da mochila
'''

close_bag_a =(78)
left_bag_a = (380)
first_item_a = (118)
second_item_a = (158)

#######################################
'''
    posição dos sprites dos pokemons
    durante a seleção de pokemons
'''

#######################################
'''
    posição da seta durante a
    seleção de pokemons
'''

left_selection = 23
right_selection = 318
upper_selection = 94
bottom_selection = 392

bulbasaur_selection = (23, 94)
charmander_selection = (23, 156)
squirtle_selection = (23, 218)
pikachu_selection = (23, 280)
pidgeot_selection = (23, 342)

graveler_selection = (318, 94)
gengar_selection = (318, 156)
cubone_selection = (318, 218)
hitmonlee_selection = (318, 280)
totodile_selection = (318, 342)

######### COLORS #########

            #R    G    B
BLUE =     (0,    0,   255 )
GREEN =    (0,    128, 0   )
PURPLE =   (128,  0,   128 )
RED =      (255,  0,    0  )
YELLOW =   (255,  255,  0  )
NAVYBLUE = (0,    0,    128)
WHITE =    (255,  255,  255)
BLACK =    (0,     0,   0  )
ALPHA =    (255,   0,   255)
GRAY =     (72,   72,   72 )


######### FONTS #########

monospace = ('./Font/joystix monospace.ttf')
pixel = ('./Font/Pixel.ttf')
verdana = ('./Font/PixelFJVerdana12pt.ttf')
manaspc = ('./Font/manaspc.ttf')

######### ANTI REPETITION #########

def img(name):
    return pygame.image.load(name)


def scale(name, resolution):
    return pygame.transform.scale(name, resolution)

######### BACKGROUND ELEMENTS #########

title = img('./InterfaceSprites/PokePy.png')
rayquasa_background = img('./InterfaceSprites/Rayquasa_background.png')


arrow = img('./InterfaceSprites/arrow.png')
arrow2 = img('./InterfaceSprites/Arrow2.0.png')
pokeball_pointer = img('./InterfaceSprites/pokeball_pointer.png')

selection_menu = img('./InterfaceSprites/PokemonSelection2.png')

battle_arena = img('./InterfaceSprites/fgt_background.png')
txt_bar = img('./InterfaceSprites/text_bar.png')
fgt_options = img('./InterfaceSprites/fgt_options.png')
atk_bar = img('./InterfaceSprites/pp_bar.png')
bag_menu = img('./InterfaceSprites/Backpack_menu.png')

######### POKEMON SPRITES #########

bulba_back = scale(img('./PokemonsSprites/Bulbasaur_back.png'), (213, 213))
bulba_front = scale(img('./PokemonsSprites/Bulbasaur_front.png'), (213, 213))

char_back = scale(img('./PokemonsSprites/Charmander_back.png'), (213, 213))
char_front = scale(img('./PokemonsSprites/Charmander_front.png'), (213, 213))

cubo_back = scale(img('./PokemonsSprites/Cubone_back.png'), (213, 213))
cubo_front = scale(img('./PokemonsSprites/Cubone_front.png'), (213, 213))

gengar_back = scale(img('./PokemonsSprites/Gengar_back.png'), (213, 213))
gengar_front = scale(img('./PokemonsSprites/Gengar_front.png'), (213, 213))

grave_back = scale(img('./PokemonsSprites/Graveler_back.png'), (213, 213))
grave_front = scale(img('./PokemonsSprites/Graveler_front.png'), (213, 213))

hitmon_back = scale(img('./PokemonsSprites/Hitmonlee_back.png'), (213, 213))
hitmon_front = scale(img('./PokemonsSprites/Hitmonlee_front.png'), (213, 213))

pidgeot_back = scale(img('./PokemonsSprites/Pidgeot_back.png'), (213, 213))
pidgeot_front = scale(img('./PokemonsSprites/Pidgeot_front.png'), (213, 213))

pikachu_back = scale(img('./PokemonsSprites/Pikachu_back.png'), (213, 213))
pikachu_front = scale(img('./PokemonsSprites/Pikachu_front.png'), (213, 213))

squirtle_back = scale(img('./PokemonsSprites/Squirtle_back.png'), (213, 213))
squirtle_front = scale(img('./PokemonsSprites/Squirtle_front.png'), (213, 213))

#toto_back = scale(img('./PokemonsSprites/'), (213, 213))
#toto_front = scale(img('./PokemonsSprites/'), (213, 213))

bulbaSPR = [bulba_back, bulba_front]
charSPR = [char_back, char_front]
sqrtlSPR = [squirtle_back, squirtle_front]
pikaSPR = [pikachu_back, pikachu_front]
cuboSPR =  [cubo_back, cubo_front]
totoSPR =  []
gengarSPR = [gengar_back, gengar_front]
hitmonSPR = [hitmon_back, hitmon_front]
graveSPR = [grave_back, grave_front]
pidgSPR = [pidgeot_back, pidgeot_front]


########### SCALE ADJUSTMENTS ###########

battle_arena = scale(battle_arena, (800, 420))
txt_bar = scale(txt_bar, (800, 180))
fgt_options = scale(fgt_options, (400, 180))
arrow = scale(arrow, (20, 38))
arrow2 = scale(arrow2, (33, 33))
atk_bar = scale(atk_bar, (800, 180))
title = scale(title, (500, 221))
bag_menu = scale(bag_menu, (800, 600))
rayquasa_background = scale(rayquasa_background, (800, 600))

#Attacks dos pokemon

Tackle = pa.Attack("Tackle", 40, 35, "Normal", "Physical")
Vine_Whip = pa.Attack("Vine Whip", 45, 25, "Grass", "Physical")
Scratch = pa.Attack("Scratch", 40, 25, "Normal", "Physical")
Fire_Fang = pa.Attack("Fire Fang", 60, 15, "Fire", "Physical")
Quick_Attack = pa.Attack("Quick Attack", 40, 30, "Normal", "Physical")    #Sempre Ataca Primeiro
Bone_Club = pa.Attack("Bone Club", 65, 20, "Ground", "Physical")
Headbutt = pa.Attack("Headbutt", 70, 15, "Normal", "Physical")
Bonemerang = pa.Attack("Bonemerang", 50, 10, "Ground", "Physical")    #Pode ir e voltar
Flail = pa.Attack("Flail", 48, 15, "Normal", "Physical")
Shadow_Punch= pa.Attack("Shadow Punch", 60, 20, "Ghost", "Physical")
Payback = pa.Attack("Payback", 50, 10, "Dark", "Physical")
Revenge = pa.Attack("Revenge ", 60, 10, "Fighting", "Physical")    # Mais dano se for devolvido
Fake_Out = pa.Attack("Fake Out", 90, 10, "Normal", "Physical")
Reversal = pa.Attack("Reversal", 48, 15, "fighting", "Physical")
Rock_Throw = pa.Attack("Rock Throw", 50, 15, "Rock", "Physical")
Earthquake = pa.Attack("Earthquake", 100, 10, "Ground", "Physical")
Explosion = pa.Attack("Explosion", 250, 5, "Normal", "Physical")
Wing_Attack = pa.Attack("Wing Attack", 60, 35, "Flying", "Physical")
Razor_Wind = pa.Attack("Razor Wind", 80, 10, "Normal", "Physical")

########### STATUS UPGRADE ATTACKS ###########
'''
    Esse tipo de ataque muda os status do
    própio pokemon, ou do adversário
'''

Agility = pa.Attack("Agility", 0, 30, "Psychic", "Status")
Thunder_Wave = pa.Attack("Thunder Wave", 0, 20, "Electric", "Status")     #Rever status e paralize
Withdraw = pa.Attack("Withdraw", 0, 40, "Water", "Status")    #Aumenta sua defesa
Growl = pa.Attack("Growl", 0, 25, "Normal", "Status")     #Diminui a defesa do inimigo


########### SPECIAL ATTACKS ###########
'''
    Esse tipo de ataque o patrick explica  q eu não sei

'''
Leech_Seed = pa.Attack("Leech_Seed", 0, 10, "Grass","Special")    #Planta sementes e rouba vida
Curse = pa.Attack("Curse", 0, 10, "Ghost", "Special")  #Perca 25% de vida, mas pode tirar 50% por round do adversario
Ice_Fang = pa.Attack("Ice Fang", 65, 15, "Ice", "Special")    #10% chance de congelar
Hex = pa.Attack("Hex ", 65, 10, "Ghost", "Special")    # Dobro de dano se alvo já tiver efeito de contato
Thunder_Shock = pa.Attack("Thunder Shock", 40, 30, "Electric", "Special")
Water_Pulse = pa.Attack("Water Pulse", 60, 20, "Water", "Special")
Water_Gun = pa.Attack("Water Gun", 40, 25, "Water", "Special")
Ember = pa.Attack("Ember", 40, 25, "Fire", "Special") # Possui chance de queimar o inimigo


########### FIRST PLAYER POKEMONS ###########
p1_sprite = 0

Bulbasaur = pa.pokemon("Bulbasaur", bulba_back, Tackle, Leech_Seed, Growl, Vine_Whip, "Grass", 120, 20, 25, 30)
Charmander = pa.pokemon("Charmander", charSPR[p1_sprite], Scratch, Ember, Growl, Fire_Fang, "Fire", 130, 20, 30, 30)
Squirtle = pa.pokemon("Squirtle", sqrtlSPR[p1_sprite], Tackle, Water_Gun, Water_Pulse, Withdraw, "Water", 110, 30, 35, 30)
Pikachu = pa.pokemon("Pikachu", pikaSPR[p1_sprite], Quick_Attack, Thunder_Shock, Tackle, Thunder_Wave, "Electric", 160, 15, 45, 25)
Cubone = pa.pokemon("Cubone", cuboSPR[p1_sprite], Bone_Club, Headbutt, Growl, Bonemerang, "Ground", 130, 35,25, 15)
#Totodile = pa.pokemon("Totodile", totoSPR[p1_sprite], Ice_Fang, Flail, Scratch, Water_Gun, "Water", 130, 25, 30, 25)
Gengar = pa.pokemon("Gengar", gengarSPR[p1_sprite], Hex, Payback, Curse, Shadow_Punch, "Ghost", 140, 200, 30, 20)
Hitmonlee = pa.pokemon("Hitmonlee", hitmonSPR[p1_sprite], Tackle, Reversal, Revenge, Fake_Out, "Fighting", 130, 35, 30,15)
Graveler = pa.pokemon("Graveler", graveSPR[p1_sprite], Tackle, Rock_Throw, Earthquake, Explosion, "Rock", 140, 35, 15, 15)
Pidgeot = pa.pokemon("Pidgeot", pidgSPR[p1_sprite], Quick_Attack, Razor_Wind, Agility, Wing_Attack, "Flying", 120, 20, 50, 20)

########### SECOND PLAYER/CPU POKEMONS ###########
p2_sprite = 1

Bulbasaur_ = pa.pokemon("Bulbasaur", bulbaSPR[p2_sprite], Tackle, Leech_Seed, Growl, Vine_Whip, "Grass", 120, 20, 25, 30)
Charmander_ = pa.pokemon("Charmander", charSPR[p2_sprite], Scratch, Ember, Growl, Fire_Fang, "Fire", 130, 20, 30, 30)
Squirtle_ = pa.pokemon("Squirtle", sqrtlSPR[p2_sprite], Tackle, Water_Gun, Water_Pulse, Withdraw, "Water", 110, 30, 35, 30)
Pikachu_ = pa.pokemon("Pikachu", pikaSPR[p2_sprite], Quick_Attack, Thunder_Shock, Tackle, Thunder_Wave, "Electric", 160, 15, 45, 25)
Cubone_ = pa.pokemon("Cubone", cuboSPR[p2_sprite], Bone_Club, Headbutt, Growl, Bonemerang, "Ground", 130, 35,25, 15)
#Totodile_ = pa.pokemon("Totodile", totoSPR[p2_sprite], Ice_Fang, Flail, Scratch, Water_Gun, "Water", 130, 25, 30, 25)
Gengar_ = pa.pokemon("Gengar", gengarSPR[p2_sprite], Hex, Payback, Curse, Shadow_Punch, "Ghost", 140, 200, 30, 20)
Hitmonlee_ = pa.pokemon("Hitmonlee", hitmonSPR[p2_sprite], Tackle, Reversal, Revenge, Fake_Out, "Fighting", 130, 35, 30,15)
Graveler_ = pa.pokemon("Graveler", graveSPR[p2_sprite], Tackle, Rock_Throw, Earthquake, Explosion, "Rock", 140, 35, 15, 15)
Pidgeot_ = pa.pokemon("Pidgeot", pidgSPR[p2_sprite], Quick_Attack, Razor_Wind, Agility, Wing_Attack, "Flying", 120, 20, 50, 20)

