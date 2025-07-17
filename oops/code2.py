class Store:

    def __init__(self, name): 
        self.name = name 
        self.items = [] 

    def add_item(self, name, price):
        item = {"name": name, "price": price} 
        self.items.append(item)

    def stock_price(self):
        return sum([item["price"] for item in self.items]) 
    

store1 = Store("smart point")
store1.add_item("Banana", 20)
store1.add_item("Apple", 30) 

print(store1.stock_price())