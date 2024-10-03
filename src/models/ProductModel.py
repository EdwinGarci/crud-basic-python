class Product():
    def  __init__(self, id, name, description, price, stock) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock
        }
