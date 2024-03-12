# Ejemplo con FastAPI en Python

Este programa proporciona una API sencilla para gestionar una lista de nombres utilizando FastAPI.

La API permite listar todos los nombres disponibles y buscar un nombre específico dentro de la lista. La lista de nombres se inicializa con tres entradas: "Juan", "María" y "Pedro".

Para ejecutar este programa, necesitará Python 3.6 o superior y FastAPI. Además, se utiliza `uvicorn` como servidor ASGI para servir la aplicación.

Instale los requisitos usando pip:

```bash
pip install fastapi uvicorn
```

## Código

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Inicializar la lista de nombres como variable global
nombres = ["Juan", "María", "Pedro"]

@app.get("/nombres")
async def obtener_nombres():
    return nombres

@app.get("/nombres/{nombre}")
async def buscar_nombre(nombre: str):
    if nombre not in nombres:
        raise HTTPException(status_code=404, detail="Nombre no encontrado")
    return {"nombre": nombre}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

## Endpoints disponibles

La API proporciona los siguientes endpoints:

### Obtener todos los nombres

- **GET** `/nombres`: Devuelve una lista con todos los nombres disponibles.

### Buscar un nombre específico

- **GET** `/nombres/{nombre}`: Busca un nombre específico en la lista. Si el nombre no se encuentra, devuelve un error 404 con el detalle "Nombre no encontrado".

## Ejemplos de uso

Para obtener la lista completa de nombres, realice una solicitud GET a `http://127.0.0.1:8000/nombres`.

Para buscar un nombre específico, por ejemplo, "Juan", realice una solicitud GET a `http://127.0.0.1:8000/nombres/Juan`.

## Manejo de errores

Si intenta buscar un nombre que no existe en la lista, la API devolverá un error HTTP 404 con un mensaje indicando que el nombre no fue encontrado.