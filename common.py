from pydantic import BaseModel


class v2(BaseModel):
    x: int = 0
    y: int = 0
    def __init__(self, x = 0, y = 0) -> None:
        super().__init__(x=x, y=y)
    def add(self, b):
        return v2(self.x + b.x, self.y + b.y)
    def sub(self, b):
        return v2(self.x - b.x, self.y - b.y)
    def scale(self, b):
        return v2(self.x * b.x, self.y * b.y)
    def _list(self):
        return self.x, self.y

class Line(BaseModel):
    begin: v2
    end: v2
