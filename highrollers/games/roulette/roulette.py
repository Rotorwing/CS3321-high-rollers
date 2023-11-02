import random_api

"""
Luna Steed
High Rollers Roulette Class
Contains the logic for the game of Roulette.
"""

class Roulette:
    def __init__(self):
        rednums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 36]
        blacknums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

        """37 will represent 00"""
        greennums = [0, 37]

        firstrow = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        secondrow = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        thirdrow = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    def spin(self,
             numbers: list[int] = None,
             colors: int = 0,
             evens: bool = False,
             odds: bool = False,
             row1: int = 0,
             row2: int = 0,
             row3: int = 0,
             first12: int = 0,
             second12: int = 0,
             third12: int = 0,
             firsthalf: bool = False,
             secondhalf: bool = False):
            rand = random_api.RandomAPI


