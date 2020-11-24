# from PIL import Image, ImageTk
# img = Image.open("*.jpg")
# img_name = ImageTk.PhotoImage(img)

from tkinter import *
from random import *
import time


class const:
    WIDTH_SIZE = 800
    HEIGHT_SIZE = 600

    WIDTH_HALF = WIDTH_SIZE//2
    HEIGHT_HALF = HEIGHT_SIZE//2

    COLOR = "BLUE"
    RECTANGLE_TAG = "RECTANGLE"


root = Tk()
canvas = Canvas(root, width=const.WIDTH_SIZE, height=const.HEIGHT_SIZE, bg="black")
canvas.pack()


mapping = {}


def get_coord():
    x, y = randrange(0, const.WIDTH_SIZE, 5), randrange(0, const.WIDTH_SIZE, 5)
    # print(f"{x} {y}")
    return x, y



class Rectangle:
    def __init__(self):
        self.x, self.y = get_coord()
        self.id = canvas.create_rectangle(self.x, self.y, self.x + 5, self.y + 5,
                                          fill=const.COLOR, tags=const.RECTANGLE_TAG)
        self.coord = [round(number) for number in canvas.coords(self.id)]

    def move(self):
        if self.coord[0] < const.WIDTH_SIZE//2 and self.coord[1] < const.HEIGHT_SIZE//2:
            canvas.move(self.id, 0, randint(1, 10))  # down
        elif self.coord[0] > const.WIDTH_SIZE//2 and self.coord[1] < const.HEIGHT_SIZE//2:
            canvas.move(self.id, -(randint(1, 10)), 0)  # left
        elif self.coord[0] < const.WIDTH_SIZE//2 and self.coord[1] > const.HEIGHT_SIZE//2:
            canvas.move(self.id, randint(1, 10), 0)  # right
            #if self.coord[0] or self.coord[2] >= 800:
            #    random_move()
        elif self.coord[0] > const.WIDTH_SIZE//2 and self.coord[1] > const.HEIGHT_SIZE//2:
            canvas.move(self.id, 0, -(randint(1, 10)))  # up


    def random_move(self):
        pass



for _ in range(500):
    obj = Rectangle()
    mapping[obj.id] = obj


def moves():
    for obj_id in canvas.find_withtag(const.RECTANGLE_TAG):
        mapping[obj_id].move()

    root.after(2500, moves)


def mouse_coord(event):
    pointxy = (event.x, event.y)
    print(pointxy)


# canvas.bind('<Motion>', mouse_coord)


if __name__ == "__main__":
    root.after(2500, moves)
    root.mainloop()
