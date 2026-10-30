import pygame
import Connect4Engine

class Connect4Game:
    engine = Connect4Engine.Connect4Engine()
    init_x = 700
    init_y = 600
    running = False

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Connect4Game.init_x, Connect4Game.init_y), pygame.RESIZABLE)
        pygame.display.set_caption("Connect 4")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = mouse_x // (Connect4Game.init_x // 7)
                    try:
                        Connect4Game.engine.playTurn(Connect4Game.engine.getTurn(), column)
                    except ValueError as e:
                        print(e)

            self.screen.fill((0, 0, 0))
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(60)

            if Connect4Game.engine.checkWin() != '-':
                self.running = False