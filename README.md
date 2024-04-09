# Cricket07Automation

This is a small project to automate batting in Cricket 07!

Using neural networks, the shot selection for different kinds of deliveries is selected.

Here's a small demo of the network choosing the shots.

https://github.com/saat-sy/Cricket07Automation/assets/67848108/62419d9b-1bf7-43e6-805f-ae43a697f99c

The framerate is quite low as my CPU usage maxed out

# How does the code work?

## Network
This project uses a CNN specifically an AlexNet to make the predictions.
It is trained on a sample size of 1000 (which I know is very small sample set)
The accuracy of the model after 30 epochs was around 40%

## Controls
This project uses PyVjoy to create a virtual controller that takes in the output from the model and gives input to the game.

## Training
create_training_data.py describes how the screenshots are captured and converted into training data.

Once that's done, enjoy watching your PC play 100x times better than you!
