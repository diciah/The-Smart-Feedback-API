import csv

def load_reviews_from_csv(path: str) -> list[str]:
    reviews = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Verificamos que la fila tenga contenido en la columna 'message'
            if row and "message" in row and row["message"].strip():
                reviews.append(row["message"])

    return reviews
