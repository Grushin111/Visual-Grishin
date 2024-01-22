from fastapi import FastAPI, HTTPException
import requests

app_intermediary = FastAPI()

# Эндпоинт для запроса книги из Marketplace и создания заказа в OrderService
@app_intermediary.get("/order_book")
def order_book(author: str):
    # Запрос информации о книге из Marketplace
    marketplace_url = "http://127.0.0.1:5001/books?author="
    response = requests.get(f"{marketplace_url}{author}")

    if response.status_code == 200:

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app_intermediary, host="127.0.0.1", port=5002)