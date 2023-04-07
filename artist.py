import time
from pynput.mouse import Button, Controller
from common import v2, Line


class Mouse(Controller):

    origin: v2
    drawing: bool

    def __init__(self) -> None:
        super().__init__()
        self.drawing, self.origin = False, self.get_position()

    def get_position(self) -> v2:
        p = self.position
        return v2(x=p[0], y=p[1])

    def release(self, button: Button) -> None:
        self.drawing = False
        return super().release(button)

    def press(self, button: Button) -> None:
        self.drawing = True
        return super().press(button)

class Artist:
    mouse: Mouse = None

    def __init__(self) -> None:
        self.mouse = Mouse()

    def draw_line(self, line: Line):
        self.mouse.move(
            *line.begin.sub(self.mouse.get_position())._list()
        )

        self.mouse.press(button=Button.left)
        self.mouse.move(*line.end.sub(self.mouse.get_position())._list())
        self.mouse.release(button=Button.left)

    def move_mouse(self, xy: v2):
        self.mouse.move(*xy._list())

    def continue_drawing(self, xy: v2):
        if not self.mouse.drawing:
            self.mouse.press(button=Button.left)
        self.move_mouse(xy)

    def draw_points(self, points: list[v2], scale: v2, draw_delay=0.001):
        time.sleep(3.0)

        last = v2()
        for p in points:
            time.sleep(draw_delay)
            delta = p.sub(last)
            delta = delta.scale(scale)
            udx, udy = abs(delta.x), abs(delta.y)
            # Pick up pen if there's space between the points
            if (udx > scale.x or udy > scale.x):
                self.mouse.release(button=Button.left)
                self.move_mouse(delta)
            else:
                self.continue_drawing(delta)
            last = p

        self.mouse.release(button=Button.left)
