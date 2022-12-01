
import numpy as np
from numpy import array
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import csv
import matplotlib.pyplot as plt

def split_sequence(sequence, n_steps):
   X, y = [], []
   for i in range(len(sequence)):
       eix = i + n_steps
       if eix > len(sequence)-1: break
       seq_x, seq_y = sequence[i:eix], sequence[eix]
       X.append(seq_x)
       y.append(seq_y)
   return array(X), array(y)
'''
   len(stockPrice) = 30, predict next 7 days stock price.
'''
def LSTM_Predict(stockPrice, days):
   if len(stockPrice) != 30: return None
   n_steps = days
   X, y = split_sequence(stockPrice, n_steps)
   n_features = 1
   X = X.reshape((X.shape[0], X.shape[1], n_features))

   # Build the model
   model = Sequential()
   model.add(LSTM(20, activation='relu', return_sequences=True, input_shape=(n_steps, n_features)))
   model.add(LSTM(20, activation='relu'))
   model.add(Dense(1))
   model.compile(optimizer='adam', loss='mse')
   model.fit(X, y, epochs=200, verbose=0)
   x_input = array(stockPrice[-days:])
   pVal = None
   res = []
   # Predict
   for i in range(7):
       if i != 0:
           x_input = np.append(x_input, pVal)
           x_input = np.delete(x_input, [0])
       x_input = x_input.reshape((1, n_steps, n_features))
       pVal = model.predict(x_input, verbose=0)
       res.append(pVal[0][0])
   return res

def readData(filename):
   with open(filename, 'r') as f:
       inp = csv.reader(f, delimiter=',', quotechar='|')
       date, close = [], []
       count = 0
       for r in inp:
           if count == 0:
               count = 1
               continue
           date.append(r[0])
           close.append(float(r[4]))
   return close
