from fastapi import FastAPI
import numpy as np
import pandas as pd
import tensorflow as tf
from pydantic import BaseModel
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Definición del modelo de datos para las entradas del usuario
class DatosSalud(BaseModel):
    embarazos: int
    glucosa: float
    presion_arterial: float
    espesor_triceps: float
    insulina: float
    bmi: float
    diabetes_pedigree_function: float
    edad: int

app = FastAPI()

# Cargar y preparar el modelo (asumiendo que ya está entrenado y guardado)
# En este caso, deberá ajustar la carga según cómo guarde su modelo
modelo = tf.keras.models.load_model('model.keras')

# Este ejemplo asume que ya tiene un `scaler` guardado que puede cargar
# Para este ejemplo, simplemente reutilizaremos el `sc` definido anteriormente
# En un caso real, lo cargaría desde un archivo
sc = StandardScaler()  # Debe cargar su propio scaler aquí

@app.post('/predict/')
def predict(diabetes_data: DatosSalud):
    data = np.array([[diabetes_data.embarazos, diabetes_data.glucosa, diabetes_data.presion_arterial,
                    diabetes_data.espesor_triceps, diabetes_data.insulina, diabetes_data.bmi,
                    diabetes_data.diabetes_pedigree_function, diabetes_data.edad]])
    data = sc.transform(data)  # Asegúrese de escalar los datos como lo hizo durante el entrenamiento
    prediction = modelo.predict(data)
    probabilidad = prediction[0][0]
    return {"probabilidad": probabilidad}

# En este punto, necesitará tener su modelo y scaler ya entrenados y guardados.
# Luego, deberá cargarlos en este script para hacer las predicciones.
