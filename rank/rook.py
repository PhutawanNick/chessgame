import pygame

from piece import Piece

class Rook(Piece):
    def __init__(self, position, color, board):
        super().__init__(position, color, board)
        img_path = f'assets/{color[0]}_rook.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.width // 8 - 20, board.height // 8 - 20))
        self.notation ='Rook'

    def get_possible_moves(self,board):
        output =[]
        moves_north =[]
        for y in range(self.y)[::-1]:
            moves_north.append(board.get_square_from_pos((self.x,y)))
        output.append(moves_north)
        
        moves_east=[]
        for x in range(self.x + 1,8):
            moves_east.append(board.get_square_from_pos((x,self.y)))  # แก้ตรงนี้
        output.append(moves_east)
        
        moves_south=[]
        for y in range(self.y +1,8):
            moves_south.append(board.get_square_from_pos((self.x,y)))
        output.append(moves_south)

        moves_west =[]
        for x in range(self.x)[::-1]:
            moves_west.append(board.get_square_from_pos((x,self.y)))
        output.append(moves_west)
        return output