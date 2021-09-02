import numpy as np
import cv2
import pandas as pd
from collections import Counter
from random import shuffle

training_data = np.load('training_data.npy')
shuffle(training_data)

df = pd.DataFrame(training_data)
print(Counter(df[1].apply(str)))

#for data in training_data:
#    image = data[0]
#    choice = data[1]
#    cv2.imshow('test', image)
#    print(choice)
#    
#    if cv2.waitKey(25) & 0xFF == ord('q'):
#            cv2.destroyAllWindows()
#            break            