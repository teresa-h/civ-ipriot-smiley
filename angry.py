from smiley import Smiley
import time

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrows()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes in a smiley
        :param wide_open : Render eyes wide open or shut
        """
        eyes = [18, 21, 26, 29]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.RED
            self.pixels[pixel] = eyes

    def draw_eyebrows(self):
        eyebrow = [9, 14]
        for pixel in eyebrow:
            self.pixels[pixel] = self.BLANK
