import pygame
import Coordinates as cord

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

battle_arena = img('./InterfaceSprites/fgt_background.png')
txt_bar = img('./InterfaceSprites/text_bar.png')
fgt_options = img('./InterfaceSprites/fgt_options.png')
arrow = img('./InterfaceSprites/arrow.png')
arrow2 = img('./InterfaceSprites/Arrow2.0.png')
atk_bar = img('./InterfaceSprites/pp_bar.png')
title = img('./InterfaceSprites/PokePy.png')
python = img('./InterfaceSprites/python_logo.png')
bag_menu = img('./InterfaceSprites/Backpack_menu.png')

########### SCALE ADJUSTMENTS ###########

battle_arena = scale(battle_arena, (800, 420))
txt_bar = scale(txt_bar, (800, 180))
fgt_options = scale(fgt_options, (400, 180))
arrow = scale(arrow, (20, 38))
arrow2 = scale(arrow2, (33, 33))
atk_bar = scale(atk_bar, (800, 180))
title = scale(title, (500, 221))
python = scale(python, (200, 200))
bag_menu = scale(bag_menu, (800, 600))

########### ARROW ###########

class Arrow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)

battle_arrow = Arrow(cord.left_a, cord.upper_a)
attack_arrow = Arrow(cord.left_attack_a, cord.upper_attack_a)
bag_arrow = Arrow(380, 78)

########### GAMEPLAY ###########

class Game:

    def __init__(self, screen, states, first_state):

        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.frame_rate = 50
        self.states = states
        self.state_name = first_state
        self.state = self.states[self.state_name]


    def event_handling(self):
        for event in pygame.event.get():
            self.state.get_event(event)


    def update_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]


    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.update_state()
        self.state.update(dt)

    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.frame_rate)
            self.event_handling()
            self.update(dt)
            self.draw()
            pygame.display.update()



class GameState:
    """
    Parent class for individual game states to inherit from.
    """

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.persist = {}

    def startup(self, persistent):
        """
        Permite que informações sejam passadas entre estágios.

        persistent: dicionario de informações passadas entre estágios
        """
        self.persist = persistent

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.
        """
        pass

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame.

        dt: time since last frame
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen.
        """
        pass

    @staticmethod
    def write_text(insertion, surface, ttf, size, text, x, y, color):
        pygame.font.init()
        font = pygame.font.Font(ttf, size)
        text_object = font.render(text, True, (color))

        if insertion == 'center':
            text_rect = text_object.get_rect(center=(x, y))
            surface.blit(text_object, text_rect)

        if insertion == 'topleft':
            text_rect = text_object.get_rect()
            text_rect.topleft = (x, y)
            surface.blit(text_object, text_rect)



class SplashScreen(GameState):


    def __init__(self):
        super().__init__()
        self.next_state = "BATTLE OPTIONS"


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYUP:
            self.done = True

    def draw(self, surface):
        surface.fill(BLACK)
        surface.blit(title, (29,30))
        surface.blit(python, (550, 30))
        self.write_text('center', surface, monospace, 25, 'PRESS ANYTHING TO START', 400, 500, WHITE )



class PokemonSelection(GameState):


    def __init__(self):
        super().__init__()
        self.done = False
        self.quit = False



    def update(self, dt):
        pass


class BattleOptions(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        pass


    def get_event(self, event):

        if event.type == pygame.QUIT:
            self.quit = True
            self.done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and battle_arrow.x == cord.left_a:
            battle_arrow.x -= cord.left_a - cord.right_a
        if pressed[pygame.K_LEFT] and battle_arrow.x == cord.right_a:
            battle_arrow.x += cord.left_a - cord.right_a
        if pressed[pygame.K_UP] and battle_arrow.y == cord.bottom_a:
            battle_arrow.y -= cord.bottom_a - cord.upper_a
        if pressed[pygame.K_DOWN] and battle_arrow.y == cord.upper_a:
            battle_arrow.y += cord.bottom_a - cord.upper_a

        if pressed[pygame.K_RETURN] and (battle_arrow.x, battle_arrow.y) == cord.fight_a:
            self.done = True
            self.next_state = 'ATTACK OPTIONS'
            attack_arrow.x, attack_arrow.y = cord.left_attack_a, cord.upper_attack_a  # Faz a seta voltar para a posição inicial

        if pressed[pygame.K_RETURN] and (battle_arrow.x, battle_arrow.y) == cord.bag_a:
            self.done = True
            self.next_state = "BACKPACK"

    def update(self, dt):
        pass


    def draw(self, surface):
        surface.blit(battle_arena, (0, 0))
        surface.blit(txt_bar, (0, 420))
        surface.blit(fgt_options, (400, 420))

        surface.blit(arrow, (battle_arrow.x, battle_arrow.y))


    def persist(self):
        pass


    def update(self, dt):
        pass


class AttackOptions(GameState):

    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        pass

    def get_event(self, event):

        if event.type == pygame.QUIT:
            self.quit = True
            self.done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and attack_arrow.x == cord.left_attack_a:
            attack_arrow.x -= cord.left_attack_a - cord.right_attack_a
        if pressed[pygame.K_LEFT] and attack_arrow.x == cord.right_attack_a:
            attack_arrow.x += cord.left_attack_a - cord.right_attack_a
        if pressed[pygame.K_UP] and attack_arrow.y == cord.bottom_attack_a:
            attack_arrow.y -= cord.bottom_attack_a - cord.upper_attack_a
        if pressed[pygame.K_DOWN] and attack_arrow.y == cord.upper_attack_a:
            attack_arrow.y += cord.bottom_attack_a - cord.upper_attack_a

        if pressed[pygame.K_ESCAPE]:
            self.done = True
            self.next_state = 'BATTLE OPTIONS'

    def update(self, dt):
        pass


    def draw(self, surface):
        surface.blit(battle_arena, (0, 0))
        surface.blit(atk_bar, (0, 420))
        surface.blit(arrow, (attack_arrow.x, attack_arrow.y))

        attack1 = 'cala'
        attack2 = 'a boca'
        attack3 = 'vadia'
        attack4 = 'puta'

        self.write_text('topleft', surface, monospace, 20, attack1, cord.left_attack_b, cord.upper_attack_b, GRAY)
        self.write_text('topleft', surface, monospace, 20, attack2, cord.right_attack_b, cord.upper_attack_b, GRAY)
        self.write_text('topleft', surface, monospace, 20, attack3, cord.left_attack_b, cord.bottom_attack_b, GRAY)
        self.write_text('topleft', surface, monospace, 20, attack4, cord.right_attack_b, cord.bottom_attack_b, GRAY)



class Backpack(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        pass

    def get_event(self, event):

        if event.type == pygame.QUIT:
            self.quit = True
            self.done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and not bag_arrow.y == cord.close_bag_a:
            bag_arrow.y += cord.close_bag_a - cord.first_item_a
        if pressed[pygame.K_DOWN] and not bag_arrow.y == cord.second_item_a:
            bag_arrow.y -= cord.close_bag_a - cord.first_item_a

        if pressed[pygame.K_ESCAPE]:
            self.done = True
            self.next_state = 'BATTLE OPTIONS'
            bag_arrow.x = cord.left_bag_a
            bag_arrow.y = cord.close_bag_a

        if pressed[pygame.K_RETURN] and (bag_arrow.x, bag_arrow.y) == (cord.left_bag_a, cord.close_bag_a):
            self.done = True
            self.next_state = "BATTLE OPTIONS"

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(bag_menu, (0,0))
        text1 = 'What would you like'
        text2 = 'to do?'

        self.write_text('topleft', surface , monospace, 20, text1 , 24, 410, BLACK)
        self.write_text('topleft', surface , monospace, 20, text2 , 24, 440, BLACK)

        self.write_text('topleft', surface, monospace, 30, 'CLOSE BAG', 420, 74, BLACK)
        self.write_text('topleft', surface, monospace, 30, 'POTION', 420, 114, BLACK)
        self.write_text('topleft', surface, monospace, 30, 'SUPERPOTION', 420, 154, BLACK)

        surface.blit(arrow2, (bag_arrow.x, bag_arrow.y))




if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('PokePy')
    screen = pygame.display.set_mode((800, 600))
    states = {"SPLASH": SplashScreen(),
              "BATTLE OPTIONS": BattleOptions(),
              "ATTACK OPTIONS": AttackOptions(),
              "BACKPACK": Backpack()}
    game = Game(screen, states, "SPLASH")
    game.run()
    pygame.quit()
