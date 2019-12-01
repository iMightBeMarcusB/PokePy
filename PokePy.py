import pygame

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

########### BUTTONS AND ARROWS ###########

#POSIÇÃO DAS OPÇÕES DE BATALHA
fight_a = (425, 468)
pokemon_a = (425, 528)
bag_a = (611, 468)
run_a = (611, 528)
upper_a = 468
bottom_a = 528
left_a = 425
right_a = 611

#POSIÇÃO DOS BOTÕES DE ATAQUE
left_attack_b = 50
right_attack_b = 300
upper_attack_b = 460
bottom_attack_b = 520

#POSIÇÕES DA SETA DE ATAQUE
left_attack_a = left_attack_b - 25
right_attack_a = right_attack_b - 25
upper_attack_a = upper_attack_b - 5
bottom_attack_a = bottom_attack_b - 5

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
atk_bar = img('./InterfaceSprites/pp_bar.png')
title = img('./InterfaceSprites/PokePy.png')
python = img('./InterfaceSprites/python_logo.png')

########### SCALE ADJUSTMENTS ###########

battle_arena = scale(battle_arena, (800, 420))
txt_bar = scale(txt_bar, (800, 180))
fgt_options = scale(fgt_options, (400, 180))
arrow = scale(arrow, (20, 38))
atk_bar = scale(atk_bar, (800, 180))
title = scale(title, (500, 221))
python = scale(python, (200, 200))

########### ARROW ###########

class Arrow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)



battle_arrow = Arrow(left_a, upper_a)
attack_arrow = Arrow(left_attack_a, upper_attack_a)

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



class GameState(object):
    """
    Parent class for individual game states to inherit from.
    """

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font(None, 24)

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
    def write_text(insertion,surface, ttf, size, text, x, y, color):
        pygame.font.init()
        font = pygame.font.Font(ttf, size)
        text_object = font.render(text, True, (color))

        if insertion == 'center':
            text_rect = text_object.get_rect(center=(x, y))
            surface.blit(text_object, text_rect)

        if insertion == 'lefttop':
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


class BattleOptions():

    def __init__(self):
        super().__init__()
        self.quit = False
        self.done = False


    def draw(self, surface):
        surface.blit(battle_arena, (0, 0))
        surface.blit(txt_bar, (0, 420))
        surface.blit(fgt_options, (400, 420))

        surface.blit(arrow, (battle_arrow.x, battle_arrow.y))

    def get_event(self, event):

        if event.type == pygame.QUIT:
            self.quit = True
            self.done = True

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and battle_arrow.x == left_a:
            battle_arrow.x += 186
        if pressed[pygame.K_LEFT] and battle_arrow.x == right_a:
            battle_arrow.x -= 186
        if pressed[pygame.K_UP] and battle_arrow.y == bottom_a:
            battle_arrow.y -= 60
        if pressed[pygame.K_DOWN] and battle_arrow.y == upper_a:
            battle_arrow.y += 60

        if pressed[pygame.K_RETURN] and (battle_arrow.x, battle_arrow.y) == fight_a:
            self.done = True
            self.next_state = 'ATTACK OPTIONS'

    def persist(self):
        pass


    def update(self, dt):
        pass


class AttackOptions(GameState):

    def __init__(self):
        super().__init__()
        self.done = False
        self.quit = False

    def draw(self, surface):
        surface.blit(battle_arena, (0, 0))
        surface.blit(atk_bar, (0, 420))
        surface.blit(arrow, (attack_arrow.x, attack_arrow.y))

        self.write_text('lefttop', surface, monospace, 20, 'passa zap', left_attack_b, upper_attack_b, GRAY)
        self.write_text('lefttop', surface, monospace, 20, 'quick attack', right_attack_b, upper_attack_b, GRAY)
        self.write_text('lefttop', surface, monospace, 20, 'thunder wave', left_attack_b, bottom_attack_b, GRAY)
        self.write_text('lefttop', surface, monospace, 20, 'bite', right_attack_b, bottom_attack_b, GRAY)

    def get_event(self, event):

        if event.type == pygame.QUIT:
            self.quit = True
            self.done = True

        pressed = pygame.key.get_pressed()





if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    states = {"SPLASH": SplashScreen(),
              "BATTLE OPTIONS": BattleOptions(),
              "ATTACK OPTIONS": AttackOptions()}
    game = Game(screen, states, "SPLASH")
    game.run()
    pygame.quit()
