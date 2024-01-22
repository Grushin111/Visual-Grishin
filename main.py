from fastapi import FastAPI, HTTPException

app_order_service = FastAPI()

books_database = {
    1: {"title": "Book 1", "author": "ARTAMONOV", "price": 20.0},
    2: {"title": "Book 2", "author": "Author 2", "price": 25.0},
    3: {"title": "Book 2", "author": "Author 2", "price": 25.0},
    4: {"title": "Book 2", "author": "Author 2", "price": 25.0},
    5: {"title": "Book 2", "author": "ARTAMONOV", "price": 25.0},
    6: {"title": "Book 2", "author": "ARTAMONOV", "price": 25.0},
    7: {"title": "Book 2", "author": "ARTAMONOV", "price": 25.0},
    8: {"title": "Book 2", "author": "Author 2", "price": 25.0},
    9: {"title": "Book 2", "author": "Author 2", "price": 25.0},
    10: {"title": "Book 2", "author": "Author 2", "price": 25.0},
    11: {"title": "Book 2", "author": "ARTAMONOV", "price": 25.0},
    # Добавьте дополнительные книги по необходимости
}

# Эндпоинт для создания заказа
@app_order_service.get("/books")
def books(author: str):
    # Пример простой обработки заказа (в реальном проекте необходимо добавить более сложную логику)
    bks = []
    for idx in books_database:
        author_book = books_database[idx]["author"]
        if author == author_book:
            bks.append(books_database[idx])
    return bks

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app_order_service, host="127.0.0.1", port=5001)