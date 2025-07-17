import pygame

from square import Square
from rank.king import King
from rank.queen import Queen
from rank.rook import Rook
from rank.bishop import Bishop
from rank.knight import Knight
from rank.pawn import Pawn

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        self.selected_piece = None
        self.turn = 'white'
        self.config = [
            [('b', 'Rook'), ('b', 'Knight'), ('b', 'Bishop'), ('b', 'Queen'), ('b', 'King'), ('b', 'Bishop'), ('b', 'Knight'), ('b', 'Rook')],
            [('b', 'Pawn'), ('b', 'Pawn'), ('b', 'Pawn'), ('b', 'Pawn'), ('b', 'Pawn'), ('b', 'Pawn'), ('b', 'Pawn'), ('b', 'Pawn')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [('w', 'Pawn'), ('w', 'Pawn'), ('w', 'Pawn'), ('w', 'Pawn'), ('w', 'Pawn'), ('w', 'Pawn'), ('w', 'Pawn'), ('w', 'Pawn')],
            [('w', 'Rook'), ('w', 'Knight'), ('w', 'Bishop'), ('w', 'Queen'), ('w', 'King'), ('w', 'Bishop'), ('w', 'Knight'), ('w', 'Rook')]
        ]
        self.squares = self.generate_squares()
        self.setup_board()

    def generate_squares(self):
        output = []
        for y in range(8):
            for x in range(8):
                output.append(Square(x, y, self.tile_width, self.tile_height))
        return output

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
                
    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
        
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece is not None:
                    color = 'white' if piece[0] == 'w' else 'black'
                    square = self.get_square_from_pos((x, y))
                    if piece[1] == 'Rook':
                        square.occupying_piece = Rook((x, y), color, self)
                    elif piece[1] == 'Knight':
                        square.occupying_piece = Knight((x, y), color, self)
                    elif piece[1] == 'Bishop':
                        square.occupying_piece = Bishop((x, y), color, self)
                    elif piece[1] == 'Queen':
                        square.occupying_piece = Queen((x, y), color, self)
                    elif piece[1] == 'King':
                        square.occupying_piece = King((x, y), color, self)
                    elif piece[1] == 'Pawn':
                        square.occupying_piece = Pawn((x, y), color, self)
    
    #รับพิกัด x (mx) และ y (my) ของตำแหน่งที่คุณคลิก
    def handle_click(self,mx,my):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x,y))
        if self.selected_piece is None:
            if clicked_square.occupying_piece is not None:
                if clicked_square.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupying_piece
        elif self.selected_piece.move(self,clicked_square):
            self.turn = 'white' if self.turn == 'black' else 'black'
        elif clicked_square.occupying_piece is not None:
            if clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece
                
    #ตัวตรวจสอบสถานะ
    def is_in_check(self,color,board_change=None):
        output = False
        king_pos =None
        changing_piece = None
        old_square = None
        new_square = None
        new_square_old_piece = None
        if board_change is not None:
            for square in self.squares:
                if square.pos == board_change[0]:
                    changing_piece = square.occupying_piece
                    old_square = square
                    old_square.occupying_piece = None
            for square in self.squares:
                if square.pos == board_change[1]:
                    new_square = square 
                    new_square_old_piece = square.occupying_piece
                    new_square.occupying_piece = changing_piece
        pieces = [
            i.occupying_piece for i in self.squares if i.occupying_piece is not None
        ]
        if changing_piece is not None:
            if changing_piece.notation == 'King':
                king_pos = new_square.pos
        if king_pos == None:
            for piece in pieces:
                if piece.notation == 'King' and piece.color == color:
                    king_pos = piece.pos
        for piece in pieces:
            if piece.color !=color:
                for square in piece.attacking_squares(self):  # แก้ชื่อฟังก์ชัน
                    if square.pos == king_pos:
                        output = True
        if board_change is not None:
            old_square.occupying_piece = changing_piece
            new_square.occupying_piece = new_square_old_piece
        return output
    #ตรวจสอบสถานะการรุกฆาต
    def is_in_checkmate(self,color):
        output = False
        king = None
        for piece in [i.occupying_piece for i in self.squares]:
            if piece !=None:
                if piece.notation == 'King' and piece.color == color:
                    king = piece
        if king and king.get_valid_moves(self) == []:
            if self.is_in_check(color):
                    output = True
        return output
    #ตรวจสอบสถานะการเสมอ
    def draw(self,display):
        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            for square in self.selected_piece.get_valid_moves(self): 
                square.highlight = True
        for square in self.squares:
            square.draw(display)
