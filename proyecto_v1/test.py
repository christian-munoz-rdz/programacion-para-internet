import requests

url = 'http://127.0.0.1:8000/predict/'
data = {
    "embarazos": 5,
    "glucosa": 116,
    "presion_arterial": 74,
    "espesor_triceps": 0,
    "insulina": 0,
    "bmi": 25.6,
    "diabetes_pedigree_function": 0.201,
    "edad": 30
}

response = requests.post(url, json=data)
print(response.json())