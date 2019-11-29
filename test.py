import pygame

########### INITIATE ###########
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('PokePy')




########### BUTTONS CORDENATES ###########

fight_b = (425, 468)
pokemon_b = (425, 528)
bag_b = (611, 468)
run_b = (611, 528)
upper_b = 468
bottom_b = 528
left_b = 425
right_b = 611

########### BACKGROUND ELEMENTS ###########

battle = img('./InterfaceSprites/fgt_background.png')
txt_bar = img('./InterfaceSprites/text_bar.png')
fgt_options = img('./InterfaceSprites/fgt_options.png')
arrow = img('./InterfaceSprites/arrow.png')

########### SCALE ADJUSTMENTS ###########

battle = scale(battle, (800, 420))
txt_bar = scale(txt_bar, (800, 180))
fgt_options = scale(fgt_options, (400, 180))
arrow = scale(arrow, (20, 38))


########### WINDOW ###########

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def returnWinSize(self):
        return (self.width, self.height)


w = Window(800, 600)
win = pygame.display.set_mode(w.returnWinSize())


########### ARROW ###########

class Arrow:
    def __init__(self, x, y, x_diff, y_diff):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.x_diff = x_diff
        self.y_diff = y_diff

    def draw(self):
        win.blit(arrow, (self.x, self.y))
        self.move(self.x_diff, self.y_diff)

    def move(self, x_diff, y_diff):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and self.x == left_b:
            self.x += x_diff
        if pressed[pygame.K_LEFT] and self.x == right_b:
            self.x -= x_diff
        if pressed[pygame.K_UP] and self.y == bottom_b:
            self.y -= y_diff
        if pressed[pygame.K_DOWN] and self.y == upper_b:
            self.y += y_diff


battle_arrow = Arrow(left_b, upper_b, 186, 60)

def battleScreen():
    win.blit(battle, (0, 0))
    win.blit(txt_bar, (0, 420))
    win.blit(fgt_options, (400, 420))

    battle_arrow.draw()


    pygame.display.update()


run = True

while run:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    battleScreen()

