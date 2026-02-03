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

    result = analyzer(text)[0]
    
    # Mapeamos las etiquetas del modelo

    label_map = {

        "POS": "Positivo",
        "NEG": "Negativo",
        "NEU": "Neutral"
    }
    
    return {

        "sentiment": label_map.get(result['label'], "Neutral"),
        "score": round(result['score'], 4)
    }

# --- BLOQUE DE PRUEBA  ---

if __name__ == "__main__":

    # Estas pruebas manuales sirven para verificar el motor de NLP de forma aislada
    
    print("--- Verificación Manual del Motor de Análisis ---")
    
    samples = [
        "El servicio fue increíble, muy rápido.",
        "No me gustó para nada, la atención fue pésima.",
        "Es un producto normal, cumple su función."
    ]
    
    for sample in samples:
        print(f"Texto: {sample}")
        print(f"Resultado: {analyze_sentiment(sample)}")
        print("-" * 20)