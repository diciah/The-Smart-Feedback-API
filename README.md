The Smart Feedback API:
Esta solución permite analizar automáticamente el sentimiento de los mensajes de feedback (Positivo, Negativo o Neutral) para ayudar al equipo de Operaciones a priorizar casos críticos de manera eficiente.

Decisiones Técnicas:
Para el desarrollo de esta API se tomaron las siguientes decisiones estratégicas:

FastAPI: Se eligió este framework por su alto rendimiento, la facilidad para validar datos mediante Pydantic y la generación automática de documentación interactiva (Swagger).

Modularización: Se separó la lógica del Motor de Análisis (app/engine.py) de la Interfaz de la API (app/main.py) para facilitar el mantenimiento y escalabilidad del sistema.

NLP Core: El motor utiliza un enfoque basado en léxico/polaridad que permite devolver no solo el sentimiento, sino también un Score de confianza, cumpliendo con los requisitos de la solución.

Instalación y Ejecución:
Segui estos pasos para poner en marcha la API en tu entorno local:

Clonar el repositorio:

git clone https://github.com/diciah/The-Smart-Feedback-API.git
cd The-Smart-Feedback-API

Crear un entorno virtual:

python -m venv venv
# En Windows: venv\Scripts\activate
# En Linux/Mac: source venv/bin/activate

Instalar dependencias:
pip install -r requirements.txt

Iniciar la API:
uvicorn app.main:app --reload

La API estará disponible en http://127.0.0.1:8000. Se accede a la documentación interactiva en /docs.

Uso del Endpoint Principal

El servicio expone un endpoint POST /analyze que recibe un texto y devuelve el análisis estructurado.

Ejemplo de Request:

{
  "text": "No estoy satisfecho con la plataforma. A pesar de que prometen muchas cosas interesantes, he tenido muchos problemas técnicos desde que la empecé a usar. A veces se queda congelada y tengo que reiniciar todo, lo cual es super frustrante. Además, la navegación no es muy intuitiva, pasé mucho tiempo buscando algunas funciones que deberían ser más fáciles de encontrar. Y ni hablar del soporte al cliente, he enviado varias consultas y la respuesta tardó días en llegar. Siento que me han desperdiciado el tiempo y la verdad, ya no tengo ganas de seguir intentando."
}


Ejemplo de Response:

{
  "status": "success",
  "input_text": "No estoy satisfecho con la plataforma. A pesar de que prometen muchas cosas interesantes, he tenido muchos problemas técnicos desde que la empecé a usar. A veces se queda congelada y tengo que reiniciar todo, lo cual es super frustrante. Además, la navegación no es muy intuitiva, pasé mucho tiempo buscando algunas funciones que deberían ser más fáciles de encontrar. Y ni hablar del soporte al cliente, he enviado varias consultas y la respuesta tardó días en llegar. Siento que me han desperdiciado el tiempo y la verdad, ya no tengo ganas de seguir intentando.",
  "analysis": {
    "sentiment": "Negativo",
    "score": 0.9819
  }
}

Validación del Modelo

Se realizaron pruebas de consistencia utilizando el contenido del archivo data/reviews.csv. El motor demostró ser capaz de:

Identificar correctamente sentimientos favorables (Positivos).
Detectar críticas y feedback que requiere atención inmediata (Negativos).
Clasificar comentarios informativos o sin carga emocional clara (Neutrales).