import pygame

from piece import Piece

class Queen(Piece):
    def __init__(self, position, color, board):
        super().__init__(position, color, board)
        img_path = f'assets/{color[0]}_queen.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'Queen'

    def get_possible_moves(self, board):
        output = []

        # North
        moves_north = []
        for y in range(self.y - 1, -1, -1):
            moves_north.append(board.get_square_from_pos((self.x, y)))
        output.append(moves_north)

        # Northeast
        moves_ne = []
        for i in range(1, 8):
            nx, ny = self.x + i, self.y - i
            if nx > 7 or ny < 0:
                break
            moves_ne.append(board.get_square_from_pos((nx, ny)))
        output.append(moves_ne)

        # East
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board.get_square_from_pos((x, self.y)))
        output.append(moves_east)

        # Southeast
        moves_se = []
        for i in range(1, 8):
            nx, ny = self.x + i, self.y + i
            if nx > 7 or ny > 7:
                break
            moves_se.append(board.get_square_from_pos((nx, ny)))
        output.append(moves_se)

        # South
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board.get_square_from_pos((self.x, y)))
        output.append(moves_south)

        # Southwest
        moves_sw = []
        for i in range(1, 8):
            nx, ny = self.x - i, self.y + i
            if nx < 0 or ny > 7:
                break
            moves_sw.append(board.get_square_from_pos((nx, ny)))
        output.append(moves_sw)

        # West
        moves_west = []
        for x in range(self.x - 1, -1, -1):
            moves_west.append(board.get_square_from_pos((x, self.y)))
        output.append(moves_west)

        # Northwest
        moves_nw = []
        for i in range(1, 8):
            nx, ny = self.x - i, self.y - i
            if nx < 0 or ny < 0:
                break
            moves_nw.append(board.get_square_from_pos((nx, ny)))
        output.append(moves_nw)

        return output
