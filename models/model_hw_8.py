class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name: str, price: float, description: str, quantity: int):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity: int) -> bool:
        """
        True если количество продукта больше или равно запрашиваемому, иначе False
        """
        return True if self.quantity >= quantity else False

    def buy(self, quantity: int):
        """
        Если продуктов не хватает, то выкинется исключение ValueError.
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
            # return self.price * self.quantity
        else:
            raise ValueError(f"Запрашиваемого продукта {self.name} меньше, чем требуется.")

    def __hash__(self):
        return hash(self.name + self.description)

    def __str__(self):
        return f"{self.name} - '{self.description}'"


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        """
        По-умолчанию корзина пустая
        """
        self.products = {}

    def add_product(self, product: Product, buy_count: int = 1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        self.products.update({product: self.products.get(product, 0) + buy_count})

    def remove_product(self, product: Product, remove_count: int = None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше или равно количеству продуктов в позиции, то удаляется вся позиция
        """
        if not self.products.get(product, False):
            raise ValueError(f"нельзя удалить из корзины продукт (product: {product.name}), который туда не был добавлен")
        if remove_count is not None and (remove_count < 1):
            raise ValueError(f"количество удаляемого продукта (remove_count: {remove_count}) не может быть меньше единицы")

        if remove_count is None:
            self.products.pop(product)
        else:
            cnt_product = self.products.get(product)
            if remove_count >= cnt_product:
                self.products.pop(product)
            else:
                self.products.update({product: cnt_product - remove_count})

    def clear(self):
        """
        Очищаем корзину
        """
        self.products = {}

    def get_total_price(self) -> float:
        """
        Общая цена корзины
        """
        total_price = 0
        for key, value in self.products.items():
            total_price += key.price * value
        return total_price

    def buy(self):
        """
        Метод покупки.
        """
        for key, value in self.products.items():
            key.buy(value)  # Если товара не будет хватать, то исключение ValueError выкинется в классе продукта Product в методе buy
