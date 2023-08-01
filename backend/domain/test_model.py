from model import Casher, Customer, Product


class Test_Casher_合計金額:
    def test_カゴの商品の合計金額を算出する(self):
        # Given
        customer = Customer("test", 30, False)
        product_list = [Product("", 1000), Product("", 2000)]

        # When
        sut = Casher(customer, product_list)

        # THen
        assert sut.calculate_total_price() == 3000

    def test_カゴに商品がない場合は0円(self):
        customer = Customer("test", 30, False)
        product_list = []

        sut = Casher(customer, product_list)

        assert sut.calculate_total_price() == 0


class Test_Casher_減額:
    def test_登録済み顧客の場合_10パー割引(self):
        customer = Customer("test", 30, True)
        product_list = [Product("", 1000)]

        sut = Casher(customer, product_list)

        assert sut.calculate_discount() == 100

    def test_未登録の顧客の場合_割引なし(self):
        customer = Customer("test", 30, False)
        product_list = [Product("", 1000)]

        sut = Casher(customer, product_list)

        assert sut.calculate_discount() == 0

    # def test_未登録の35歳以上の顧客の場合_5パー割引(self):
    #     customer = Customer("test", 35, False)
    #     product_list = [Product("", 1000)]

    #     sut = Casher(customer, product_list)

    #     assert sut.calculate_discount() == 50
