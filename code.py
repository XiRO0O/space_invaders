import pygame, sys
from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((screen_width/2,screen_height - 10),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        pass

    def run(self):
        self.player.update()
        self.player.draw(screen)

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    icon = pygame.image.load('graphics/icon.png').convert_alpha()
    pygame.display.set_caption('Earth Invaders')
    pygame.display.set_icon(icon)
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60)