import dataclasses
from typing import List


@dataclasses.dataclass
class Customer:
    name: str
    age: int
    is_registered: bool


@dataclasses.dataclass
class Product:
    title: str
    price: int


@dataclasses.dataclass
class Casher:
    customer: Customer
    products: List[Product]

    def calculate_total_price(self) -> int:
        return sum([product.price for product in self.products])

    def calculate_discount(self) -> int:
        if self.customer.is_registered:
            return self.calculate_total_price() * 0.05
        else:
            return 0
