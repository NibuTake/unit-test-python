from typing import List

from domain.model import Casher, Customer, Product


def provide_total_price_with_discount(customer: Customer, products: List[Product]):
    casher = Casher(customer, products)

    return {
        "total": casher.calculate_total_price(),
        "discount": casher.calculate_discount(),
    }
