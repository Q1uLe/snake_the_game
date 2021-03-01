import pygame


class Board:
    # создание поля
    def __init__(self, width, height, cell_size):
        self.key = 'paused'  # key for play/pause/loose
        self.playing = True
        self.food = None
        self.snake = None

        self.width = width  # cell quantity by width
        self.height = height  # quantity by height

        self.left = 0  # left coord of first cell
        self.top = 0  # top coord of first cell
        self.cell_size = cell_size

    def get_coord(self, row, col):  # returns coord of cell in dependence her location
        return self.left + self.cell_size * row, self.top + self.cell_size * col

    def render(self, surface):  # renders snake, food and board's grid
        self.snake.render(surface)
        self.food.render(surface)
        for i in range(15):
            y = i * self.cell_size + self.top
            for j in range(20):
                x = j * self.cell_size + self.left
                pygame.draw.rect(surface, pygame.Color('white'),
                                 [x, y, self.cell_size, self.cell_size],
                                 1)

    def add_food(self, food):  # remember food
        self.food = food

    def add_snake(self, snake):  # remember snake
        self.snake = snake

    def pause_play(self):  # pausing and starting game
        self.playing = not self.playing

    def loose(self, screen):
        self.playing = False
        loose_text = ["Вы проиграли",
                      f"Ваш счет: {self.snake.score}",
                      "Нажмите 'пробел', чтобы продолжить"]
        self.snake.restart()
        self.food.restart()
        font = pygame.font.Font(None, 30)
        text_coord = 100
        screen.fill((0, 0, 0))
        for line in loose_text:  # text render
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 170
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
            pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('board.py:"SPACE"')
                        self.pause_play()
                        return

    def start_screen(self, screen, clock):
        screen.fill((0, 0, 0))
        intro_text = ["ИГРА 'ЗМЕЙКА'",
                      "Управление стрелками клавиатуры",
                      "'Пробел' для паузы",
                      "Клавиша 'R' для перезапуска",
                      "Нажмите 'ПРОБЕЛ', чтобы продолжить"]
        font = pygame.font.Font(None, 30)
        text_coord = 100
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 170
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return True
            pygame.display.flip()
            clock.tick(50)
