import Config as c, pygame

########### ARROW ###########

class Arrow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)

battle_arrow = Arrow(c.left_a, c.upper_a)
attack_arrow = Arrow(c.left_attack_a, c.upper_attack_a)
bag_arrow = Arrow(380, 78)

########### GAMEPLAY ###########


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
        surface.blit(c.rayquasa_background, (0, 0))
        surface.blit(c.title, (150, 30))
        self.write_text('center', surface, c.monospace, 25, 'PRESS ANYTHING TO START', 400, 500, c.WHITE)


class ChooseMode(GameState):
    def __init__(self):
        super().__init__()
        self.next_state = 'SELECT POKEMON'

    def startup(self, persistent):
        pass

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass


class SelectPokemon(GameState):
    def __init__(self):
        super().__init__()
        self.next_state = 'BATTLE OPTIONS'


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

        if pressed[pygame.K_RIGHT] and battle_arrow.x == c.left_a:
            battle_arrow.x -= c.left_a - c.right_a
        if pressed[pygame.K_LEFT] and battle_arrow.x == c.right_a:
            battle_arrow.x += c.left_a - c.right_a
        if pressed[pygame.K_UP] and battle_arrow.y == c.bottom_a:
            battle_arrow.y -= c.bottom_a - c.upper_a
        if pressed[pygame.K_DOWN] and battle_arrow.y == c.upper_a:
            battle_arrow.y += c.bottom_a - c.upper_a

        if pressed[pygame.K_RETURN] and (battle_arrow.x, battle_arrow.y) == c.fight_a:
            self.done = True
            self.next_state = 'ATTACK OPTIONS'
            attack_arrow.x, attack_arrow.y = c.left_attack_a, c.upper_attack_a  # Faz a seta voltar para a posição inicial

        if pressed[pygame.K_RETURN] and (battle_arrow.x, battle_arrow.y) == c.bag_a:
            self.done = True
            self.next_state = "BACKPACK"

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(c.battle_arena, (0, 0))
        surface.blit(c.txt_bar, (0, 420))
        surface.blit(c.fgt_options, (400, 420))

        surface.blit(c.arrow, (battle_arrow.x, battle_arrow.y))

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

        if pressed[pygame.K_RIGHT] and attack_arrow.x == c.left_attack_a:
            attack_arrow.x -= c.left_attack_a - c.right_attack_a
        if pressed[pygame.K_LEFT] and attack_arrow.x == c.right_attack_a:
            attack_arrow.x += c.left_attack_a - c.right_attack_a
        if pressed[pygame.K_UP] and attack_arrow.y == c.bottom_attack_a:
            attack_arrow.y -= c.bottom_attack_a - c.upper_attack_a
        if pressed[pygame.K_DOWN] and attack_arrow.y == c.upper_attack_a:
            attack_arrow.y += c.bottom_attack_a - c.upper_attack_a

        if pressed[pygame.K_ESCAPE]:
            self.done = True
            self.next_state = 'BATTLE OPTIONS'

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(c.battle_arena, (0, 0))
        surface.blit(c.atk_bar, (0, 420))
        surface.blit(c.arrow, (attack_arrow.x, attack_arrow.y))

        attack1 = 'cala'
        attack2 = 'a boca'
        attack3 = 'vadia'
        attack4 = 'puta'

        self.write_text('topleft', surface, c.monospace, 20, attack1, c.left_attack_b, c.upper_attack_b, c.GRAY)
        self.write_text('topleft', surface, c.monospace, 20, attack2, c.right_attack_b, c.upper_attack_b, c.GRAY)
        self.write_text('topleft', surface, c.monospace, 20, attack3, c.left_attack_b, c.bottom_attack_b, c.GRAY)
        self.write_text('topleft', surface, c.monospace, 20, attack4, c.right_attack_b, c.bottom_attack_b, c.GRAY)


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

        if pressed[pygame.K_UP] and not bag_arrow.y == c.close_bag_a:
            bag_arrow.y += c.close_bag_a - c.first_item_a
        if pressed[pygame.K_DOWN] and not bag_arrow.y == c.second_item_a:
            bag_arrow.y -= c.close_bag_a - c.first_item_a

        if pressed[pygame.K_ESCAPE]:
            self.done = True
            self.next_state = 'BATTLE OPTIONS'
            bag_arrow.x = c.left_bag_a
            bag_arrow.y = c.close_bag_a

        if pressed[pygame.K_RETURN] and (bag_arrow.x, bag_arrow.y) == (c.left_bag_a, c.close_bag_a):
            self.done = True
            self.next_state = "BATTLE OPTIONS"

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(c.bag_menu, (0, 0))
        text1 = 'What would you like'
        text2 = 'to do?'

        self.write_text('topleft', surface, c.monospace, 20, text1, 24, 410, c.BLACK)
        self.write_text('topleft', surface, c.monospace, 20, text2, 24, 440, c.BLACK)

        self.write_text('topleft', surface, c.monospace, 30, 'CLOSE BAG', 420, 74, c.BLACK)
        self.write_text('topleft', surface, c.monospace, 30, 'POTION', 420, 114, c.BLACK)
        self.write_text('topleft', surface, c.monospace, 30, 'SUPERPOTION', 420, 154, c.BLACK)

        surface.blit(c.arrow2, (bag_arrow.x, bag_arrow.y))