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
