import pygame

class Piece:
    def __init__(self, position, color, board):
        self.pos = position 
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.has_moved = False
        
    def get_moves(self,board):
        output = []
        for direction in self.get_possible_moves(board):
            for square in direction:
                if square.occupying_piece is not None:
                    if square.occupying_piece.color == self.color:
                        break
                    else:
                        output.append(square)
                        break
                else:
                    output.append(square)
            return output
    
    def get_valid_moves(self,board):
        output = []
        for square in self.get_moves(board):
            if not board.is_in_check(self.color,board_change=[self.pos,square.pos]):
                output.append(square)
        return output
    
    def move(self,board,square,force=False):
        for i in board.squares:  # แก้จาก board.square เป็น board.squares
            i.highlight = False
        if square in self.get_valid_moves(board) or force:
            prev_square = board.get_square_from_pos(self.pos)
            self.pos, self.x,self.y = square.pos,square.x,square.y
            prev_square.occupying_piece = None
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True
            #pawn promo
            if self.notation == '':
                # เงื่อนไขโปรโมทเฉพาะเมื่อถึงแถวสุดท้าย
                if (self.color == 'white' and self.y == 0) or (self.color == 'black' and self.y == 7):
                    from rank.queen import Queen
                    square.occupying_piece = Queen(
                        (self.x, self.y), self.color, board
                    )
            #Move rook if king castles
            if self.notation == 'King':
                if prev_square.x - self.x == 2:
                    rook = board.get_piece_from_pos((0,self.y))
                    rook.move(board,board.get_square_from_pos((3,self.y)),force = True)
                elif prev_square.x - self.x == -2:
                    rook = board.get_piece_from_pos((7,self.y))
                    rook.move(board,board.get_square_from_pos((5,self.y)),force = True)
            return True
        else:
            board.selected_piece = None
            return False
        
    def attacking_squares(self,board):
        return self.get_moves(board)
            
                