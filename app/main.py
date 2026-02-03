from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.engine import analyze_sentiment

# Inicializamos la aplicación

app = FastAPI(
    title="Smart Feedback API",
    description="API para el análisis de sentimiento de reviews usando NLP",
    version="1.0.0"
)

# Definimos el esquema de entrada usando Pydantic

class ReviewInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la Smart Feedback API",
        "instructions": "Envía un POST a /analyze con un JSON que contenga el campo 'text'"
    }

@app.post("/analyze")
async def analyze(input_data: ReviewInput):

    # Validación básica: que el texto no esté vacío
    
    if not input_data.text.strip():

        raise HTTPException(status_code=400, detail="El campo 'text' no puede estar vacío")
    
    # Llamamos a nuestra lógica de NLP en engine.py

    analysis_result = analyze_sentiment(input_data.text)
    
    return {
        "status": "success",
        "input_text": input_data.text,
        "analysis": analysis_result
    }