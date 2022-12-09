#!/usr/bin/env python
# coding: utf-8

from keras.models import Sequential
import numpy as np
from keras.layers.core import Dense
import tensorflow as tf
from sklearn.metrics import confusion_matrix
import pandas as pd
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

conjunto_datos = pd.read_csv('entrenamiento.csv', header=None, sep=',', skiprows=range(1))
datos_entrada = conjunto_datos.iloc[:,0:3].values
datos_salida = conjunto_datos.iloc[:,3:4].values

modelo = Sequential()
modelo.add(Dense(2, input_dim = 3,activation ='relu'))
modelo.add(Dense(1, activation = 'sigmoid'))
modelo.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['binary_accuracy'])
modelo.fit(datos_entrada, datos_salida, epochs = 500)

p,b = modelo.layers[0].get_weights()
p2,b2 = modelo.layers[1].get_weights()
print(p, b)
x = [0, 102, 0]
#x = [997, 673, 823]
h1 = max(tf.keras.activations.relu(x[0]*p[0][0] + x[1]*p[1][0] + x[2]*p[2][0] + b[0]),0).numpy()
h2 = max(tf.keras.activations.relu(x[0]*p[0][1] + x[1]*p[1][1] + x[2]*p[2][1] + b[1]),0).numpy()
y = tf.keras.activations.sigmoid(h1*p2[0] + h2*p2[1] + b2[0]).numpy()
print(y)
print(y.round())
datos = modelo.evaluate(datos_entrada, datos_salida)
print("\n%s: %.2f%%" %(modelo.metrics[1], datos[1]*100))
y_pred = modelo.predict(datos_entrada).round()
print(y_pred)
y_pred = (y_pred >=.5)
cm = confusion_matrix(datos_salida, y_pred)
print(cm)

p,b = modelo.layers[0].get_weights()
p2,b2 = modelo.layers[1].get_weights()
print(p, b)
print("----")
print(p2,b2)
