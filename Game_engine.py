import pygame

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