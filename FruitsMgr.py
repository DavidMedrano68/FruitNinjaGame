import pygame
import random
from pygame.locals import *
import pygwidgets


from Fruits import *
# Created a class to manage the Fruit
class FruitsMgr():
    def __init__(self, window , maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

    def start(self):
        self.other_list = []
        self.FruitList = []
        self.Sliced = 0
        self.score = 0
        self.lives = 10
# Spawn in the fruits and add the fruits as objects to a list
        for Fruit_num in range(0, FRUITS_MAX):
            randomFruitClass = random.choice((Banana, Kiwi, Mango, Pineapple, Apple))
            o_fruit = randomFruitClass(self.window, self.maxWidth, self.maxHeight)
            self.FruitList.append(o_fruit)
        for boss in range(0, BOSSES):
            o_fruit = Pome(self.window, self.maxWidth, self.maxHeight)
            self.other_list.append(o_fruit)
# Check if User clicked on the Fruit and award score and delete object from the list
    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for o_fruit in reversed(self.FruitList):
                wasHit, Points = o_fruit.clickedInside(event.pos)
                if wasHit:
                    if Points > 0:
                        self.FruitList.remove(o_fruit)
                        self.Sliced = self.Sliced + 1
                        self.score = self.score + Points
                    return
# Special event for when the Pome Fruit Appears
    def handleEvent2(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for o_fruit in reversed(self.other_list):
                wasHit, Points = o_fruit.clickedInside(event.pos)
                if wasHit:
                    if Points > 0:
                        self.lives = self.lives - 1
                        self.Sliced = self.Sliced + 1
                        self.score = self.score + Points
                        if self.lives == 0:
                            self.other_list.remove(o_fruit)
                    return

# Update the all the fruits in the two list
    def update(self):
        for o_fruit in self.FruitList:
            o_fruit.update()
        for o_fruit in self.other_list:
            o_fruit.update()
# Give score back
    def get_score(self):
        return self.score
# Give how many times you've sliced back
    def get_amount_sliced(self):
        return self.Sliced
# Draw the Fruits in the list
    def draw(self):
        for o_fruit in self.FruitList:
            o_fruit.draw()

    def draw2(self):
        for o_fruit in self.other_list:
            o_fruit.draw()







