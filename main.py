from controls.controller import Controller
from helper.screen import Screen
from model.predict import Prediction

screen = Screen()
prediction = Prediction()
controller = Controller()
ALL_MOVES = ['shift+s+right+down', 'shift+s+left+down', 'shift+s+down', 'shift+s+right', 'shift+s+left']

while True:
    screen.processFrame()

    if screen.play:

        pred, percentage = prediction.predict(screen.screenshot)
        print(ALL_MOVES[pred], "-", str(percentage) + "%")

        controller.play(pred)