# Importar las librerías necesarias
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar el dataset de diabetes
df = pd.read_csv("diabetes.csv")

# Separar las variables independientes (X) y la variable dependiente (y)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Dividir el dataset en conjunto de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Escalar las variables independientes
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Crear la red neuronal
ann = tf.keras.models.Sequential()
# Añadir la capa de entrada y la primera capa oculta
ann.add(tf.keras.layers.Dense(units=8, activation='relu'))
# Añadir la segunda capa oculta
ann.add(tf.keras.layers.Dense(units=8, activation='relu'))
# Añadir la capa de salida
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Compilar la red neuronal
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Entrenar la red neuronal
ann.fit(X_train, y_train, batch_size = 32, epochs = 100)

#Exportar el modelo en formato .keras
ann.save("model.keras")

