#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential

TRAIN_X_FILENAME = './train_X.csv'
TRAIN_Y_FILENAME = './train_Y.csv'

TEST_X_FILENAME = './test_X.csv'
TEST_Y_FILENAME = './test_Y.csv'

X_train = np.genfromtxt(TRAIN_X_FILENAME, delimiter=',')
Y_train = np.genfromtxt(TRAIN_Y_FILENAME, delimiter=',')

X_test = np.genfromtxt(TEST_X_FILENAME, delimiter=',')
Y_test = np.genfromtxt(TEST_Y_FILENAME, delimiter=',')

HIDDEN_NODES=100

model = Sequential()
model.add(Dense(output_dim=HIDDEN_NODES, input_dim=1, bias=True))
model.add(Activation("relu"))
model.add(Dense(output_dim=1, activation='linear'))

model.compile(loss='mse', optimizer='sgd')
#model.fit(X_train, Y_train, batch_size=1000, nb_epoch=1000, validation_data=(X_test, Y_test))
model.fit(X_train, Y_train, batch_size=10, nb_epoch=1, validation_data=(X_test, Y_test))

Y_test_predict = model.predict(X_test)

plt.scatter(X_test, Y_test, color='b')
plt.scatter(X_test, Y_test_predict, color='r')
plt.show()






