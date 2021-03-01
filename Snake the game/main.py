import pygame
from Board import Board
from Snake import Snake
from Food import Food

WIDTH, HEIGHT = 800, 600


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Змейка')

        running = True

        board = Board(20, 15, 40)
        snake = Snake(board)
        # snake.set_self_onboard()

        food = Food(board)
        # food.set_self_onboard()

        board.add_food(food)
        board.add_snake(snake)

        fps = 6
        clock = pygame.time.Clock()

        if board.start_screen(screen, clock):
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:  # пауза
                            print('main.py:"SPACE"')
                            board.pause_play()
                        elif event.scancode == pygame.KSCAN_R:  # перезапуск
                            food.restart()
                            snake.restart()
                            board.pause_play()
                        elif board.playing:
                            # управление стрелками
                            if event.key == pygame.K_UP:
                                snake.UP()
                                break
                            elif event.key == pygame.K_RIGHT:
                                snake.RIGHT()
                                break
                            elif event.key == pygame.K_DOWN:
                                snake.DOWN()
                                break
                            elif event.key == pygame.K_LEFT:
                                snake.LEFT()
                                break
                screen.fill((0, 0, 0))

                # food.set_self_onboard()
                if board.playing:
                    snake.next_frame(screen)
                board.render(screen)
                pygame.display.flip()
                clock.tick(fps)
    except Exception as e:
        print(e)
    pygame.quit()


if __name__ == '__main__':
    main()
