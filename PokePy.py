import pygame

########### INITIATE ###########

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('PokePy')


########### ANTI REPETITION ###########

def img(name):
    return pygame.image.load(name)


def scale(name, resolution):
    return pygame.transform.scale(name, resolution)


########### BUTTONS ###########

fight_b = (425, 468)
pokemon_b = (425, 528)
bag_b = (611, 468)
run_b = (611, 528)
upper_b = 468
bottom_b = 528
left_b = 425
right_b = 611

########### TEXT MESSAGES ###########

no_run = 'you can´t run from a batlle'



########### BACKGROUND ELEMENTS ###########

battle = img('./InterfaceSprites/fgt_background.png')
txt_bar = img('./InterfaceSprites/text_bar.png')
fgt_options = img('./InterfaceSprites/fgt_options.png')
arrow = img('./InterfaceSprites/arrow.png')
atk_bar = img('./InterfaceSprites/pp_bar.png')

########### SCALE ADJUSTMENTS ###########

battle = scale(battle, (800, 420))
txt_bar = scale(txt_bar, (800, 180))
fgt_options = scale(fgt_options, (400, 180))
arrow = scale(arrow, (20, 38))
atk_bar = scale(atk_bar, (800, 180))

########### WINDOW ###########

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def returnWinSize(self):
        return (self.width, self.height)


w = Window(800, 600)
win = pygame.display.set_mode(w.returnWinSize())

bs = True


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('PKMN RBYGSC.ttf', size)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)


########### ARROW ###########

class Arrow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)

    def draw(self):
        win.blit(arrow, (self.x, self.y))
        self.move()

    def move(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and self.x == left_b:
            self.x += 186
        if pressed[pygame.K_LEFT] and self.x == right_b:
            self.x -= 186
        if pressed[pygame.K_UP] and self.y == bottom_b:
            self.y -= 60
        if pressed[pygame.K_DOWN] and self.y == upper_b:
            self.y += 60

def select():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN] and battle_arrow.position == fight_b:
        fight()
    if pressed[pygame.K_RETURN] and battle_arrow.position == run_b:
        draw_text(win, str(no_run), 400, 420, 120)


battle_arrow = Arrow(left_b, upper_b)

def battleScreen():

    win.blit(battle, (0, 0))
    win.blit(txt_bar, (0, 420))
    win.blit(fgt_options, (400, 420))

    battle_arrow.draw()
    select()
    pygame.display.update()

def fight():
    win.blit(battle, (0,0))
    win.blit(atk_bar, (0, 420))

    pygame.display.update()


run = True

while run:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    battleScreen()


