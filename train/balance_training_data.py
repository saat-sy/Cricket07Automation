import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import os
import ast

inputFilename = input("Enter the input filename: ")
FILE_NAME = os.path.join("train", "data", "raw", inputFilename)
ALL_MOVES = ['shift+s+right+down', 'shift+s+left+down', 'shift+s+down', 'shift+s+right', 'shift+s+left', "NO_KEY_SELECTED"]

data = np.load(FILE_NAME)
X = data['X']
Y = data['Y']

trainingData = zip(X, Y)

print("Current length", len(X))

df = pd.DataFrame(trainingData)

eachMove = Counter(df[1].apply(str))

one_hot_dict_int = {ALL_MOVES[(ast.literal_eval(k.replace(' ', ','))).index(1)]: v for k, v in eachMove.items()}

df = pd.DataFrame(list(one_hot_dict_int.items()), columns=['Move', 'Frequency'])

print()
print(df)
print()

print("Will be balanced to:", min(eachMove.values()) * 6)
print()

proceed = input("Do you want to proceed? ")
if proceed.lower() == "y":
    print()
    min_count = min(eachMove.values())
    selected_counts = {str(move): 0 for move in eachMove.keys()}
    balanced_data = []

    listOfTrainingData = [list(a) for a in zip(X, Y)]
    shuffle(listOfTrainingData)

    for img, move in listOfTrainingData:
        if selected_counts.get(str(move)) < min_count:
            balanced_data.append((img, move))
            selected_counts[str(move)] += 1

    print("New Length:", len(balanced_data))
    df2 = pd.DataFrame(balanced_data)
    print(Counter(df2[1].apply(str)))
    print()

    balanced_X, balanced_Y = zip(*balanced_data)

    filename = input("Enter the filename: ")

    np.savez(os.path.join("train", "data", "balanced", filename), X=list(balanced_X), Y=list(balanced_Y))