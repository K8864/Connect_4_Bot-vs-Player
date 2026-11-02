import pygame
import Connect4Engine

class Connect4Game:
    engine = Connect4Engine.Connect4Engine()
    x_size = 700
    y_size = 600
    running = False
    screen = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Connect4Game.x_size, Connect4Game.y_size), pygame.RESIZABLE)
        pygame.display.set_caption("Connect 4")
        self.font = pygame.font.SysFont(None, 64)
        self.running = True
        self.engine.set_turn(self.engine.get_turn())

    # draws the board on the screen, which is just a 7x6 grid of rectangles, with red for player 1, yellow for player 2, and white for unclaimed
    def draw_board(self):
        x_size, y_size = self.screen.get_size()
        self.screen.fill((255, 255, 255))
        for row in range(6):
            for col in range(7):
                color = (255, 0, 0) if Connect4Game.engine.board[row][col] == 'x' else (255, 255, 0) if Connect4Game.engine.board[row][col] == 'o' else (255, 255, 255)
                pygame.draw.rect(self.screen, color, (col * (x_size // 7), row * (y_size // 6), x_size // 7, y_size // 6))
                pygame.draw.rect(self.screen, (0, 0, 0), (col * (x_size // 7), row * (y_size // 6), x_size // 7, y_size // 6), 1)

    def run(self):
        while self.running:
            winner = Connect4Game.engine.checkWin()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and winner == '-':
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    x_size, _ = self.screen.get_size()
                    column = mouse_x // (x_size // 7)
                    try:
                        Connect4Game.engine.playTurn(Connect4Game.engine.get_turn(), column)
                    except ValueError as e:
                        print(e)

            self.draw_board()

            winner = Connect4Game.engine.checkWin()
            if winner != '-':
                x_size, y_size = self.screen.get_size()
                
                # darken the board with a semi-transparent overlay
                overlay = pygame.Surface((x_size, y_size), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 150))
                self.screen.blit(overlay, (0, 0))

                # draw centered win text
                win_text = self.font.render(f"Player {winner.upper()} wins", True, (255, 255, 255))
                text_rect = win_text.get_rect(center=(x_size // 2, y_size // 2))
                self.screen.blit(win_text, text_rect)

            pygame.display.flip()