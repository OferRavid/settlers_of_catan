from tkinter import BOTTOM, LEFT, NW, Entry, Frame, Label, StringVar, Tk, BOTH, Canvas, Button
from PIL import Image, ImageDraw, ImageFont, ImageTk

running = False
def main():
    root = Tk()
    root.title("testing graphics")
    img = Image.open('hexes.jpg')
    root.protocol("WM_DELETE_WINDOW", close)
    points = [100, 100, 200, 100, 250, 150, 200, 200, 100, 200, 50, 150]
    canvas = Canvas(root, height=750, width=1000)
    canvas.create_polygon(points, outline='black', fill='white', width=2)
    hex = ImageTk.PhotoImage(img)
    canvas.create_image(500, 500, anchor=NW, image=hex)
    canvas.pack(fill=BOTH, expand=1)
    wait_for_close(root)


def redraw(root):
    root.update_idletasks()
    root.update()

def wait_for_close(root):
    global running
    running = True
    while running:
        redraw(root)
    print("window closed...")

def close():
    global running
    running = False

def clear_canvas(canvas):
    canvas.delete("all")


main()

# from tkinter import Tk, Canvas, Frame, BOTH, NW
# from PIL import Image, ImageTk

# class Example(Frame):

#     def __init__(self):
#         super().__init__()

#         self.initUI()


#     def initUI(self):

#         self.master.title("High Tatras")
#         self.pack(fill=BOTH, expand=1)

#         self.img = Image.open("hexes.png")
#         self.tatras = ImageTk.PhotoImage(self.img)

#         canvas = Canvas(self, width=self.img.size[0]+20,
#            height=self.img.size[1]+20)
#         canvas.create_image(10, 10, anchor=NW, image=self.tatras)
#         canvas.pack(fill=BOTH, expand=1)


# def main():

#     root = Tk()
#     ex = Example()
#     root.mainloop()


# if __name__ == '__main__':
#     main()