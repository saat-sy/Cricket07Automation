from controls.controller import Controller
from helper.screen import Screen
from model.predict import Prediction

screen = Screen()
prediction = Prediction()
controller = Controller()
ALL_MOVES = ['shift+s+right+down', 'shift+s+left+down', 'shift+s+down', 'shift+s+right', 'shift+s+left', "NO_KEY_SELECTED"]

while True:
    screen.processFrame()

    if screen.play:

        pred = prediction.predict(screen.screenshot)
        print(ALL_MOVES[pred])

        controller.play(pred)