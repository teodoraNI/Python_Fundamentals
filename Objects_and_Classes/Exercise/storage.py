class Storage:
    storage = []

    def __init__(self, capacity: int):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            self.capacity -= 1
            Storage.storage.append(product)

    def get_products(self):
        return Storage.storage


storage = Storage(3)
storage.add_product('apple')
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
