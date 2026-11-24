from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to our E-Commerce API"}

@app.get("/products")
def get_products():
    return {
        "products": [
            {
                "id": 1,
                "name": "iPhone 16",
                "price": 250000
            },
            {
                "id": 2,
                "name": "Samsung S25",
                "price": 200000
            }
        ]
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "name": "iPhone 16",
        "price": 250000
    } 