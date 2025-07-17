import pygame 

# สร้างกระเบื้อง
class Square:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x*width
        self.abs_y = y*height
        self.abs_pos = (self.abs_x,self.abs_y)
        self.color = 'light' if (x+y)%2 ==0 else 'dark'
        self.draw_color = (220,208,194)if self.color == 'light'else (53,53,53)
        self.highlight_color = (100,249,83) if self.color == 'light' else (0,228,10)
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )
        self.pos = (self.x,self.y)
    
    # สัญลักษณ์ของกระเบื้อง
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1 )

    def draw(self,display):
        # กำหนดค่าว่ากระเบื้องควรเป็นสีอ่อนหรือสีเข้มหรือเน้นกระเบื้อง
        if self.highlight:
            pygame.draw.rect(display,self.highlight_color,self.rect)
        else:
            pygame.draw.rect(display,self.draw_color,self.rect)
        #เพิ่มไอคอนตัวหมากรุก
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img,centering_rect)


