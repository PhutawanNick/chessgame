import pygame
from board import Board
pygame.init()

WINDOW_SIZE = (800,800)

screen = pygame.display.set_mode(WINDOW_SIZE)
board = Board(WINDOW_SIZE[0],WINDOW_SIZE[1])

def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()

if __name__ == "__main__":    
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # click left mouse button
                if event.button == 1:
                    board.handle_click(mx, my)
                    # เช็ค checkmate หลังเดินหมากเท่านั้น
                    if board.is_in_checkmate('black'):
                        print('White Wins')
                        running = False
                    elif board.is_in_checkmate('white'):
                        print('Black Wins')
                        running = False
        # draw
        draw(screen)