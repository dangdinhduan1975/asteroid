import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    Shot.containers = (updatable,drawable,shots)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    my_player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(my_player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__=="__main__":
    main()