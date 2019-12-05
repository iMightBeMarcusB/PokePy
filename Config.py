import pygame

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
