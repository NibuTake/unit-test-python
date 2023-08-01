import dataclasses
from typing import List


@dataclasses.dataclass
class Customer:
    name: str
    age: int
    is_registered: bool


@dataclasses.dataclass
class Product:
    name: str
    price: int


@dataclasses.dataclass
class Casher:
    customer: Customer
    products: List[Product]

    def calculate_total_price(self) -> int:
        price = 0
        for product in self.products:
            price += product.price
        return price

    def calculate_discount(self) -> int:
        if self.customer.is_registered:
            return self.calculate_total_price() * 0.1
        else:
            return 0

    # def calculate_discount(self) -> int:
    #     return self._discount_by_register() + self._discount_by_age()

    def _discount_by_register(self) -> int:
        if self.customer.is_registered:
            return self.calculate_total_price() * 0.1
        else:
            return 0

    def _discount_by_age(self) -> int:
        if self.customer.age >= 35:
            return self.calculate_total_price() * 0.05
        else:
            return 0
