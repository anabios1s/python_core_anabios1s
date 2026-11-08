
class Flower:
    def __init__(self, name, price, lifetime):
        self.name = name
        self.price = price
        self.lifetime = lifetime

    def __str__(self):
        return f"{self.name}: {self.price} руб., живет {self.lifetime} дней"

class Rose(Flower):
    def __init__(self):
        super().__init__("Роза", 150, 7)


class Tulip(Flower):
    def __init__(self):
        super().__init__("Тюльпан", 100, 5)

class Lily(Flower):
    def __init__(self):
        super().__init__("Лилия", 200, 10)

class Accessory:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def total_price(self):
        flowers_price = sum(f.price for f in self.flowers)
        accessories_price = sum(a.price for a in self.accessories)
        return flowers_price + accessories_price

    def wilting_time(self):
        if not self.flowers:
            return 0

        total_lifetime = sum(f.lifetime for f in self.flowers)
        return total_lifetime / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda f: f.price)

    def has_flower(self, name):
        return any(f.name.lower() == name.lower() for f in self.flowers)

    def show_info(self):
        print("Цветы в букете:")
        for flower in self.flowers:
            print(flower)

        print("\nАксессуары:")
        for accessory in self.accessories:
            print(f"{accessory.name}: {accessory.price} руб.")

        print(f"\nСтоимость букета: {self.total_price()} руб.")
        print(f"Время увядания: {self.wilting_time():.1f} дней")

bouquet = Bouquet()

bouquet.add_flower(Rose())
bouquet.add_flower(Tulip())
bouquet.add_flower(Lily())
bouquet.add_flower(Rose())

bouquet.add_accessory(Accessory("Лента", 50))
bouquet.add_accessory(Accessory("Упаковка", 100))

bouquet.show_info()

print("\nЦветы после сортировки по стоимости:")
bouquet.sort_by_price()

for flower in bouquet.flowers:
    print(flower)

print("\nЕсть ли роза?", bouquet.has_flower("Роза"))
print("Есть ли ромашка?", bouquet.has_flower("Ромашка"))