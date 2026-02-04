# The Smart Feedback API

Esta API sirve para analizar el feedback que nos dejan los usuarios. Te dice si el comentario es Positivo, Negativo o Neutral, y con qué confianza lo dice. La idea es que Operaciones pueda filtrar rápido los problemas graves.

## Cómo levantar el proyecto

Para hacer andar esto en tu compu, seguí estos pasos:

1.  **Clonar el repo** (si no lo tenés ya):
    ```bash
    git clone https://github.com/diciah/The-Smart-Feedback-API.git
    cd The-Smart-Feedback-API
    ```

2.  **Crear un entorno virtual** (para no mezclar librerías):
    ```bash
    python -m venv venv
    # Si estás en Windows:
    venv\Scripts\activate
    # Si estás en Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instalar lo necesario**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Correr la API**:
    ```bash
    uvicorn app.main:app --reload
    ```
    
    Y listo, la API queda escuchando en `http://127.0.0.1:8000`.

## Documentación y Pruebas

Lo más fácil es ir directamente a `http://127.0.0.1:8000/docs`. Ahí tenés el Swagger que te deja probar los endpoints.

### Endpoints principales

-   **POST /analyze**: Le mandás un JSON con un texto y te devuelve el análisis.
    *Body:*
    ```json
    {
      "text": "El servicio es excelente, me encantó."
    }
    ```

-   **POST /analyze/csv**: Este lee directo el archivo `data/reviews.csv`, procesa todo y te devuelve un resumen estadístico junto con el detalle.
    *Respuesta de ejemplo:*
    ```json
    {
      "total_rows": 50,
      "processed": 50,
      "summary": {
        "Positivo": 20,
        "Negativo": 25,
        "Neutral": 5
      },
      "results": [...]
    }
    ```

## Estructura del proyecto

-   `app/main.py`: Acá están definidos los endpoints y la configuración de FastAPI.
-   `app/engine.py`: La lógica pesada de NLP está acá. Usé el modelo `robertuito` que anda joya para español.
-   `app/utils.py`: Funciones auxiliares, como la lectura del CSV.
-   `data/reviews.csv`: El archivo de prueba con reviews.