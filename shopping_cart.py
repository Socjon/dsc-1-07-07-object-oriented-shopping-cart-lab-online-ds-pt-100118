class ShoppingCart:
    
    def __init__(self, employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, list_of_items):
        self._items = list_of_items
        return self._items
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, new_total):
        self._total = new_total
        return self.total
    
    @property
    def employee_discount(self):
        return self._employee_discount
    
    @employee_discount.setter
    def employee_discount(self, new_amount):
        self._employee_discount = new_amount
        return self._employee_discount
        
    
    def add_item(self, name, price, quantity=1):
        for item in list(range(quantity)):
            self._items.append({'name' : name,'price' :price})
            self._total += price
        return self._total
    
    def mean_item_price(self):
        run_total = []
        for cost in list(range(len(self._items))):
            run_total.append(self._items[cost]['price'])
        return (sum(run_total)/len(self._items))
    
    def median_item_price(self):
        run_total = []
        for cost in list(range(len(self._items))):
            run_total.append(self._items[cost]['price'])
        ranked = sorted(run_total)
        if len(ranked) % 2 == 0:
            return ( ranked[len(ranked)/2] + ranked[(len(ranked)/2)+1] )/2 #median value
        else:
            return ranked[(len(ranked)+1)//2]
    
    def apply_discount(self): 
        if self._employee_discount:
            return ((self._total) - (self._total * (self._employee_discount /100)))
        else:
            return 'Sorry, there is no discount to apply for your cart'
        
    def item_names(self):
        names_from_cart = []
        for count in list(range(len(self._items))):
            names_from_cart.append(self._items[count]['name'])
        return names_from_cart
    
    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return 'There are no items in your cart'
        self.total -= removed_item['price']
        
            