import pytest

from test_home_work.models.homework_8 import Cart, Product


@pytest.fixture
def product() -> Product:
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart() -> Cart:
    return Cart()


class TestProducts:
    check_quantity = [(-1, True), (0, True), (1, False), ]

    @pytest.mark.parametrize("count, result", check_quantity, indirect=False)
    def test_product_check_quantity(self, product: Product, count: int, result: bool):
        """
        Проверка метода Product.check_quantity с учетом пограничных значений количества продукта в наличии
        :param product: экземпляр класса продукта
        :param count: значение на которое надо изменить текущее количество продукта
        :param result: ожидаемый результат проверки
        :return:
        """
        assert product.check_quantity(product.quantity + count) == result, "Фактический результат не соответствует ожидаемому."

    def test_product_buy(self, product: Product):
        """
        Проверка метода Product.buy с использованием половины значения Product.quantity
        :param product: экземпляр класса продукта
        :return:
        """
        half_quantity = int(product.quantity / 2)
        result = product.quantity - half_quantity
        product.buy(half_quantity)
        assert product.quantity == result, "Количество оставшегося продукта не соответствует ожидаемому."

    def test_product_buy_more_than_available(self, product: Product):
        """
        Проверка метода Product.buy на выкидывание ошибки ValueError
        :param product: экземпляр класса продукта
        :return:
        """
        more_quantity = product.quantity * 2
        with pytest.raises(ValueError):
            product.buy(more_quantity)


class TestCart:

    @pytest.fixture
    def products(self) -> (Product, Product):
        book = Product("book", 10, "This is a book", 100)
        pen = Product("pen", 2, "This is a pen", 1000)
        return book, pen

    def test_cart_add_product(self, cart: Cart, products: (Product, Product)):
        """
        Проверка заполнения корзины
        :param cart: экземпляр класса корзины
        :param products: 2 экземпляра класса продукта
        :return:
        """
        product_1, product_2 = products
        # Добавляем продукты в корзину
        cart.add_product(product_1, 3)
        cart.add_product(product_2, 5)
        assert len(cart.products) == 2
        assert cart.products.get(product_1) == 3
        # Повторно добавляем один из продуктов в корзину
        cart.add_product(product_1, 4)
        assert cart.products.get(product_1) == 7

    def test_cart_remove_product(self, cart: Cart, products: (Product, Product)):
        """
        Проверка удаления продуктов из корзины
        :param cart: экземпляр класса корзины
        :param products: 2 экземпляра класса продукта
        :return:
        """
        product_1, product_2 = products
        # Заполняем "корзину" напрямую
        cart.products.update({product_1: 10})
        cart.products.update({product_2: 52})
        assert len(cart.products) == 2
        # Удаляем некоторое количество продукта из корзины
        cart.remove_product(product_2, 12)
        assert cart.products.get(product_2) == 40
        # Удаляем оставшееся количество продукта из корзины
        cart.remove_product(product_2, 40)
        assert cart.products.get(product_2) is None
        assert len(cart.products) == 1
        # Удаляем весь продукт разом
        cart.remove_product(product_1)
        assert cart.products.get(product_1) is None
        assert len(cart.products) == 0

    def test_cart_remove_product_more_than_available(self, cart: Cart, products: (Product, Product)):
        """
        Проверка выкидывания ошибки при некорректном удалении продуктов из корзины
        :param cart: экземпляр класса корзины
        :param products: 2 экземпляра класса продукта
        :return:
        """
        product_1, product_2 = products
        # Удаляем не добавленный продукт из корзины
        with pytest.raises(ValueError):
            cart.remove_product(product_1)

        cart.products.update({product_1: 10})
        # Удаляем из корзины некорректное количество продукта
        with pytest.raises(ValueError):
            cart.remove_product(product_1, 0)
            cart.remove_product(product_1, -5)

    def test_cart_clear(self, cart: Cart, products: (Product, Product)):
        """
        Проверка очищения корзины
        :param cart: экземпляр класса корзины
        :param products: 2 экземпляра класса продукта
        :return:
        """
        product_1, product_2 = products
        # Заполняем "корзину" напрямую
        cart.products.update({product_1: 10})
        cart.products.update({product_2: 52})
        assert len(cart.products) == 2
        # Проверяем очистку корзины
        cart.clear()
        assert len(cart.products) == 0

    def test_cart_get_total_price(self, cart: Cart, products: (Product, Product)):
        """
        Проверка подсчета общей стоимости корзины
        :param cart: экземпляр класса корзины
        :param products: 2 экземпляра класса продукта
        :return:
        """
        product_1, product_2 = products
        # Заполняем "корзину" напрямую
        cart.products.update({product_1: 2})
        cart.products.update({product_2: 4})
        expected_price = product_1.price * 2 + product_2.price * 4
        assert cart.get_total_price() == expected_price

    def test_cart_buy(self, cart: Cart, products: (Product, Product)):
        """
        Проверка покупки продуктов в корзине
        :param cart: экземпляр класса корзины
        :param products: 2 экземпляра класса продукта
        :return:
        """
        product_1, product_2 = products
        half_product_1 = int(product_1.quantity / 2)
        half_product_2 = int(product_2.quantity / 2)
        # Заполняем "корзину" напрямую
        cart.products.update({product_1: half_product_1})
        cart.products.update({product_2: half_product_2})
        # Подготавливаем ожидаемые значения
        cnt_product_1 = product_1.quantity - half_product_1
        cnt_product_2 = product_2.quantity - half_product_2

        cart.buy()
        assert product_1.quantity == cnt_product_1 and product_2.quantity == cnt_product_2, "Количество оставшегося продукта не соответствует ожидаемому."

    def test_cart_buy_more_than_available(self, cart: Cart, products: (Product, Product)):
        """
        Проверка покупки некорректного количества продуктов в корзине
        :param cart: экземпляр класса корзины
        :param products: 2 экземпляра класса продукта
        :return:
        """
        product_1, product_2 = products
        half_product_1 = int(product_1.quantity / 2)
        more_product_2 = int(product_2.quantity * 2)
        # Заполняем "корзину" напрямую
        cart.products.update({product_1: half_product_1})
        cart.products.update({product_2: more_product_2})

        with pytest.raises(ValueError):
            cart.buy()
