from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.engine import analyze_sentiment
from app.utils import load_reviews_from_csv


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

    # Validamos que el texto no esté vacío antes de procesarlo
    
    if not input_data.text.strip():

        raise HTTPException(status_code=400, detail="El campo 'text' no puede estar vacío.")
    
    # Enviamos el texto al motor de NLP (engine.py) para obtener el análisis

    analysis_result = analyze_sentiment(input_data.text)
    
    return {
        "status": "success",
        "input_text": input_data.text,
        "analysis": analysis_result
    }

@app.post("/analyze/csv")
def analyze_csv():
    # Cargamos las reviews desde el CSV
    texts = load_reviews_from_csv("data/reviews.csv")

    results = []

    for text in texts:
        # Analizamos cada una
        analysis = analyze_sentiment(text)
        results.append({
            "text": text,
            "sentiment": analysis["sentiment"],
            "score": analysis["score"]
        })

    return {
        "total_rows": len(texts),
        "processed": len(results),
        "results": results
    }