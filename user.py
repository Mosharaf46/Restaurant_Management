#customer
#employee
#Admin
from orders import order
from abc import ABC, abstractmethod

class user(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class customer(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=order()
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
        
    def add_to_cart(self,restaurant,item_name,quantity):
        item=restaurant.menu.find_item(item_name)
        if item:
            if item.quantity<quantity:
                print('Item limit exceeded!!')
                return 
            item.quantity=quantity
            self.cart.add_item(item)
            print('Item added')
        else:
            print("Item is not Avialable")
            
    def view_cart(self):
        print('-------------Item In Your cart--------------')
        print("Name:\t\tprice:\t\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t\t{item.price}\t\t{quantity}')
        print("Total Price:",self.cart.total_price)
        
    def pay_bill(self):
        print(f"Total: {self.cart.total_price} paid successfully")
        self.cart.clear()

class employee(user):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)    
        self.age=age
        self.designation=designation
        self.salary=salary
        

class admin(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_new_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)
        
    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)
        
    def add_employee(self,restaurant,employee):
        restaurant.add_employees(employee)
    
    def view_employee(self,restaurant):
        restaurant.view_employees()
        
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
         
