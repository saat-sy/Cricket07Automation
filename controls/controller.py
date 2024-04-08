import pyvjoy
import time

class Controller:
    def __init__(self) -> None:
        self.j = pyvjoy.VJoyDevice(1)
        self.initDirection()
        self.buttons = 18
        # S - 2
        # Shift - 16

    def initDirection(self):
        self.j.reset()
        self.j.data.wAxisX= 0x4000
        self.j.update()
        self.j.data.wAxisY= 0x4000
        self.j.update()

    def play(self, index):       
        if index == 0:
            # shift+s+right+down
            self.playShot(x=0x8000, y=0x8000)
        elif index == 1:
            # shift+s+left+down
            self.playShot(x=0x0000, y=0x8000)
        elif index == 2:
            # shift+s+down
            self.playShot(x=0x4000, y=0x8000)
        elif index == 3:
            # shift+s+right
            self.playShot(x=0x8000, y=0x4000)
        elif index == 4:
            # shift+s+left
            self.playShot(x=0x0000, y=0x4000)

    def playShot(self, x, y):
        self.j.data.wAxisX= x
        self.j.update()
        self.j.data.wAxisY= y
        self.j.update()
        self.j.data.lButtons = self.buttons
        self.j.update()

        time.sleep(0.15)

        self.j.data.wAxisX= 0x4000
        self.j.update()
        self.j.data.wAxisY= 0x4000
        self.j.update()
        self.j.data.lButtons = 0
        self.j.update()

        time.sleep(0.15)