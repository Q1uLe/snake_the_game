import pygame


class Snake:
    def __init__(self, board):
        self.board = board
        self.head = (7, 10, 'right')
        self.body = [(7, 9, 'right'), (7, 8, 'right'), (7, 7, 'right')]
        self.score = 0
        # first coord is "y", second is "x"

    def next_frame(self, screen):
        """
        method is moving snake, checking loose and eat
        :param screen: pygame.display
        :return: None
        """
        previous_head = self.head
        previous_tail = self.body[-1][0:3]
        self.head = self.move_part(self.head)
        if not self.check_loose():
            self.body = self.move_chain(previous_head, self.body)
            if self.check_eat():
                self.add_part(previous_tail)
                self.board.food.recreate()
                self.score += 1
        else:
            self.head = previous_head
            self.board.loose(screen)

    def move_part(self, part):
        """
        change cell coord in dependence cell direction
        :param part: tuple
        :return: None
        """
        if part[2] == 'right':
            return part[0], part[1] + 1, 'right'
        elif part[2] == 'up':
            return part[0] - 1, part[1], 'up'
        elif part[2] == 'left':
            return part[0], part[1] - 1, 'left'
        elif part[2] == 'down':
            return part[0] + 1, part[1], 'down'

    def move_chain(self, head, body):
        """
        return transferred snake body
        :param head: tuple
        :param body: list
        :return: list
        """
        new_body = [(head[0], head[1], head[2])]
        for i in range(len(body) - 1):
            new_body.append(body[i])
        return new_body

    def check_loose(self):
        """
        method checking if snake bite herself or bumped into frame
        :return: Boolean
        """
        if not 0 <= self.head[0] <= 14 or not 0 <= self.head[1] <= 19:
            return True
        for cell in self.body:
            if self.head[0:2] == cell[0:2]:
                return True
        return False

    def UP(self):  # change head direction to "UP"
        if self.head[2] == 'right' or self.head[2] == 'left':
            self.head = self.head[0], self.head[1], 'up'

    def DOWN(self):  # change head direction to "DOWN"
        if self.head[2] == 'right' or self.head[2] == 'left':
            self.head = self.head[0], self.head[1], 'down'

    def LEFT(self):  # change head direction to "LEFT"
        if self.head[2] == 'down' or self.head[2] == 'up':
            self.head = self.head[0], self.head[1], 'left'

    def RIGHT(self):  # change head direction to "RIGHT"
        if self.head[2] == 'down' or self.head[2] == 'up':
            self.head = self.head[0], self.head[1], 'right'

    def restart(self):
        """
        restarting game
        :return: None
        """
        self.head = (7, 10, 'right')
        self.body = [(7, 9, 'right'), (7, 8, 'right'), (7, 7, 'right')]
        self.score = 0

    def check_eat(self):
        """
        check if snake ate apple
        :return: Boolean
        """
        y, x = self.head[0], self.head[1]
        if self.board.food.get_coords() == (x, y):
            return True
        return False

    def add_part(self, tail):
        """
        add new cell if snake ate apple
        :param tail: tuple
        :return: None
        """
        self.body.append(tail)

    def render(self, surface):
        """
        rendering snake on surface
        :param surface: pygame.display
        :return: None
        """
        cell_size = self.board.cell_size
        x, y = self.head[1] * cell_size, self.head[0] * cell_size
        pygame.draw.rect(surface, pygame.Color('yellow'),
                         [x, y, cell_size, cell_size]
                         )
        for x, y, direction in self.body:
            x, y = y * cell_size, x * cell_size
            pygame.draw.rect(surface, pygame.Color('yellow'),
                             [x, y, cell_size, cell_size]
                             )

    def get_coord_list(self):
        """
        returning list with all cells of snake
        :return:  list
        """
        loc_lst = self.body.copy()
        loc_lst.append(self.head)
        return [(x, y) for x, y, direction in loc_lst]
