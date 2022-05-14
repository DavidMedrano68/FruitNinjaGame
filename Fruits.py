import pygame , random, pygwidgets
# Constants
FRUITS_MAX = 10
BOSSES = 1

FRUIT_MOVING = 'fruit moving'

# Fruits class to display on the window
class Fruits():
    slice_loaded = False
    slice_sound = None

    def __init__(self, window, maxWidth, maxHeight,
                 oImage, Points, speedY):
        self.window = window
        self.FruitImage = oImage
        self.Points = Points
        self.speedY = speedY
        fruitRect = self.FruitImage.getRect()
        self.width = fruitRect.width
        self.height = fruitRect.height
        self.x = random.randrange(maxWidth - self.width)
        self.y = maxHeight + random.randrange(75)
        self.FruitImage.setLoc((self.x, self.y))
        if not Fruits.slice_loaded:
            Fruits.slice_loaded = True
            Fruits.slice_sound = pygame.mixer.Sound('sounds/slice.wav')
# Check if user Clicked and play sound and reward the points
    def clickedInside(self, mousePoint):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):
            Fruits.slice_sound.play()
            return True, self.Points  # True here means it was hit
        else:
            return False, 0  # not hit, no points
# move the Fruits upwards then once it hits the top move them downwards
    def update(self):
        self.y = self.y - self.speedY  # update y position by speed
        self.FruitImage.setLoc((self.x, self.y))
        if self.y < -self.height:
            self.speedY = -self.speedY
        else:
            return FRUIT_MOVING

    def draw(self):
        self.FruitImage.draw()

# 6 different subclasses inherit from the Fruits Super class
class Banana(Fruits):
    FruitImage = pygame.image.load('images/banana.png')

    def __init__(self, window, maxWidth, maxHeight):
        oImage = pygwidgets.Image(window, (0, 0), Banana.FruitImage)
        super().__init__(window, maxWidth, maxHeight, oImage, 20, 3.1)


class Pineapple(Fruits):
    FruitImage = pygame.image.load('images/PINEAPPLE.png')

    def __init__(self, window, maxWidth, maxHeight):
        oImage = pygwidgets.Image(window, (0, 0), Pineapple.FruitImage)
        super().__init__(window, maxWidth, maxHeight, oImage, 20, 3.1)


class Apple(Fruits):
    FruitImage = pygame.image.load('images/apple 2.png')

    def __init__(self, window, maxWidth, maxHeight):
        oImage = pygwidgets.Image(window, (0, 0), Apple.FruitImage)
        super().__init__(window, maxWidth, maxHeight, oImage, 20, 3.1)


class Kiwi(Fruits):
    FruitImage = pygame.image.load('images/kiwi.png')

    def __init__(self, window, maxWidth, maxHeight):
        oImage = pygwidgets.Image(window, (0, 0), Kiwi.FruitImage)
        super().__init__(window, maxWidth, maxHeight, oImage, 20, 3.1)


class Mango(Fruits):
    FruitImage = pygame.image.load('images/mango.png')

    def __init__(self, window, maxWidth, maxHeight):
        oImage = pygwidgets.Image(window, (0, 0), Mango.FruitImage)
        super().__init__(window, maxWidth, maxHeight, oImage, 20, 3.1)

class Pome (Fruits):
    FruitImage = pygame.image.load('images/pome.png')

    def __init__(self, window, maxWidth, maxHeight):
        oImage = pygwidgets.Image(window, (0, 0), Pome.FruitImage)
        super().__init__(window, maxWidth, maxHeight, oImage, 20, 2)
