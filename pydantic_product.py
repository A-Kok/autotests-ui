from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="The price must be greater than 0")
    tags: list[str] = []
    market: Market


product_data = {
    "name": "Product A",
    "price": 10.0,
    "tags": ["tag1", "tag2"],
    "market": {
        "id": 1,
        "name": "Market A"
    }
}

product = Product(**product_data)
print(product.market.name)

new_product = Product(name="Product B", price=444.0, tags=["tag3"], market=Market(id=2, name="Market B"))
print(new_product)
