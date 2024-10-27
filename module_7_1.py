class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products):
        try:
            existing_products = self.get_products().splitlines()
            existing_names = {product.split(', ')[0] for product in existing_products}

            with open(self.__file_name, 'a') as file:
                for product in products:
                    if product.name in existing_names:
                        print(f'Продукт {product.name} уже есть в магазине')
                    else:
                        file.write(str(product) + '\n')
        except Exception as e:
            print(f"Произошла ошибка: {e}")



if __name__ == "__main__":
    shop = Shop()


    potato = Product('Potato', 50.0, 'Vegetables')
    tomato = Product('Tomato', 20.5, 'Vegetables')

    shop.add(potato, tomato)


    print("Все продукты в магазине:")
    print(shop.get_products())