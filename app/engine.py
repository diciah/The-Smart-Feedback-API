from transformers import pipeline

# Cargamos el modelo, voy a usar uno pre-entrenado para español, ya que las reviews vienen en español
# pysentimiento/robertuito-sentiment-analysis es excelente para español
# https://huggingface.co/pysentimiento/robertuito-sentiment-analysis

model_path = "pysentimiento/robertuito-sentiment-analysis"
analyzer = pipeline("sentiment-analysis", model=model_path)

def analyze_sentiment(text: str):
    """
    Recibe un texto y devuelve el sentimiento (Positivo, Negativo, Neutral)
    y el score de confianza.
    """
    if not text.strip():
        return {"sentiment": "Neutral", "score": 0.0}

    # El modelo devuelve una lista con un diccionario: [{'label': 'POS', 'score': 0.99}]
    # Usamos truncation=True para manejar textos que excedan el límite de tokens
    result = analyzer(text, truncation=True, max_length=512)[0]
    
    # Mapeo las etiquetas por defecto del modelo

    label_map = {

        "POS": "Positivo",
        "NEG": "Negativo",
        "NEU": "Neutral"
    }
    
    return {

        "sentiment": label_map.get(result['label'], "Neutral"),
        "score": round(result['score'], 4)
    }

