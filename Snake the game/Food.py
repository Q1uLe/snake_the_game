from random import randint
import pygame


class Food:
    def __init__(self, board):
        self.x, self.y = 13, 7  # in contrast "Snake" class, first coord is "x", second is "y"
        self.board = board

    def recreate(self):
        key = True
        while key:
            x, y = randint(0, 19), randint(0, 14)
            if self.check_cell(x, y):
                self.x, self.y = x, y
                self.board.add_food(self)
                key = False

    def check_cell(self, x, y):  # method checking if cell is free
        if (y, x) not in self.board.snake.get_coord_list():
            return True
        return False

    def render(self, surface):  # method is rendering Food cell on board
        cell_size = self.board.cell_size
        x, y = self.x * cell_size, self.y * cell_size
        pygame.draw.rect(surface, pygame.Color('red'),
                         [x, y, cell_size, cell_size]
                         )

    def get_coords(self):  # method return food coords
        return self.x, self.y

    def restart(self):
        self.x, self.y = 13, 7
