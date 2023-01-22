import sys
import pygame
from pygame.locals import DOUBLEBUF
from map import Map


class Display3D(object):
    def __init__(self, W, H):
        self.mapp = Map()
        self.W = W
        self.H = H


class Display2D(object):
    def __init__(self, W, H):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H), DOUBLEBUF)
        self.surface = pygame.Surface((W, H)
                                      # self.screen.get_size()
                                      ).convert()

    def paint(self, img):
        # junk
        for event in pygame.event.get():
            pass

        img = img.swapaxes(0, 1)[:, :, [2, 1, 0]]
        print(f"img:{img}")
        # print(
        #     f"{self.surface.get_size()==img.shape} --> {self.surface.get_size()}=={img.shape}")
        # print(dir(self.surface))
        # exit(0)

        # draw
        #pygame.surfarray.blit_array(self.surface, img.swapaxes(0,1)[:, :, [2,1,0]])

        # RGB, not BGR (might have to switch in twitchslam)
        pygame.surfarray.blit_array(
            self.surface, img
            # .swapaxes(0, 1)[:, :, [0, 1, 2]]
        )

        self.screen.blit(self.surface, (0, 0))

        # blit
        pygame.display.flip()


if __name__ == "__main__":
    print("init pygame")
    pygame.init()

    size = width, height = 320, 240
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()

    while True:
        pygame.surfarray.blit_array()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (0x1 & 0xFF == ord('q')):
                sys.exit()
                break

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
