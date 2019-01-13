class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        cent_x = int((self.x1 + self.x2)/2)
        cent_y = int((self.y1 + self.y2)/2)
        return (cent_x, cent_y)
    def intersect(self, new_rect):
        return (self.x1 <= new_rect.x2 and self.x2 >= new_rect.x1 and
                self.y1 <= new_rect.y2 and self.y2 >= new_rect.y1)