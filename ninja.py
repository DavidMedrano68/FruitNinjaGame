import pygame, sys
from FruitsMgr import *

pygame.init()
clock = pygame.time.Clock()

# Constants And make Buttons and display Score
BLACK = (0, 0, 0)
PANEL_HEIGHT = 60
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
USABLE_WINDOW_H = SCREEN_HEIGHT - PANEL_HEIGHT
FPS = 30
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load('images/background.png')

oScoreDisplay = pygwidgets.DisplayText(WINDOW, (10, USABLE_WINDOW_H + 25),
                                       'Score: 0', textColor=BLACK,
                                       backgroundColor=None, width=140, fontSize=24)
oStatusDisplay = pygwidgets.DisplayText(WINDOW, (180, USABLE_WINDOW_H + 25),
                                        '', textColor=BLACK, backgroundColor=None,
                                        width=300, fontSize=24)
oStartButton = pygwidgets.TextButton(WINDOW,
                                     (SCREEN_HEIGHT - 110, USABLE_WINDOW_H + 10),
                                     'Start')

oResetButton = pygwidgets.TextButton(WINDOW, (400, 590), 'Reset', )

oFruitMgr = FruitsMgr(WINDOW, SCREEN_WIDTH, USABLE_WINDOW_H)
playing = False  # wait until user clicks Start

#  Loop forever
while True:
    WINDOW.blit(BACKGROUND, (0, 0))
    nPointsEarned = 0
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # When playing display correct score and make sure the game is ready to handle both events and buttons
        if playing:

            oFruitMgr.handleEvent(event)
            oFruitMgr.handleEvent2(event)
            theScore = oFruitMgr.get_score()
            oScoreDisplay.setValue('Score: ' + str(theScore))
        elif oStartButton.handleEvent(event):
            oFruitMgr.start()
            oScoreDisplay.setValue('Score: 0')
            playing = True
            oStartButton.disable()
        if oResetButton.handleEvent(event):
            playing = False
            oStartButton.enable()

        # update the Fruits
        if playing:
            oFruitMgr.update()
            Slice = oFruitMgr.get_amount_sliced()
            oStatusDisplay.setValue(
                'Sliced: ' + str(Slice))
            # after you've sliced all the fruits spawn in the Boss
            if (Slice) >= FRUITS_MAX:
                oFruitMgr.draw2()
    # Draw all window elements
    if playing:
        oFruitMgr.draw()

    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()
    oResetButton.draw()

    # Update the window
    pygame.display.update()

    clock.tick(FPS)
