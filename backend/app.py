# NOTE: ここにはFastAPIやAWS Lambda handlerなど定義する
# NOTE: 一旦悪いコードで記載している

from domain.model import Customer, Product
from service.service import provide_total_price_with_discount

customer = Customer("test", 30, True)
products = [Product("A", 1000), Product("A", 1500)]

res = provide_total_price_with_discount(customer, products)

print(res)
