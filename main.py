from fooditem import Fooditem
from menu import Menu
from user import customer,admin,employee
from Restaurant import Restaurant
from orders import order

kacchi_dyne=Restaurant('Kacchi_dyne')
def customer_menu():
    name=input('Enter your name: ')
    email=input('Enter you email: ')
    phone=input('Enter you phone: ')
    address=input('Enter you address: ')
    customer1=customer(name=name,email=email,phone=phone,address=address)
    
    while True:
        print(f'welcome {name}!!!')
        print('1.view menu')
        print('2.add item to cart')
        print('3.view cart')
        print('4.paybill')
        print('5.Exit')
        choice=int(input('Enter your choice:'))
        if choice==1:
            customer1.view_menu(kacchi_dyne)
        elif choice==2:
            item_name=input('Enter item to add to cart: ')
            quantity=int(input("Enter quantity: "))
            customer1.add_to_cart(kacchi_dyne,item_name,quantity)
        elif choice==3:
            customer1.view_cart()
        elif choice==4:
            customer1.pay_bill()
        elif choice==5:
            print("Exiting from the system")
            break
        else:
            print("Invalid option try 1 to 5 !!")



def Admin_menu():
    name=input('Enter your name: ')
    email=input('Enter you email: ')
    phone=input('Enter you phone: ')
    address=input('Enter you address: ')
    AD1=admin(name=name,email=email,phone=phone,address=address)
    
    while True:
        print(f'welcome {name}!!!')
        print('1.Add_new_item')
        print('2.Remove_item')
        print('3.Add_employee')
        print('4.view_employee')
        print('5.View_menu')
        print('6.Exit')
        choice=int(input('Enter your choice:'))
        if choice==1:
            item_name=input('enter the item to add:')
            item_price=int(input('enter the price:'))
            quantity=int(input('enter the quantity:'))
            item1=Fooditem(item_name,item_price,quantity)
            AD1.add_new_item(kacchi_dyne,item1)      
            
        elif choice==2:
            item=input("Enter the item name: ")
            AD1.remove_item(kacchi_dyne,item)
            
        elif choice==3:
            e_name=input('Enter employee name: ')
            phone=input('Enter employee phone num: ')
            email=input('Enter employee email: ')
            address=input('Enter the employee address: ')
            designation=input('Enter employee designation: ')
            age=input('Enter employee age: ')
            salary=input('Enter employee salary: ')
            emp=employee(name=e_name,phone=phone,email=email,designation=designation,age=age,salary=salary,address=address)
            AD1.add_employee(kacchi_dyne,emp)
            
        elif choice==4:
            AD1.view_employee(kacchi_dyne)
        elif choice ==5:
            AD1.view_menu(kacchi_dyne)
        elif choice==6:
            print("Exiting from the system")
            break
        else:
            print("Invalid option try 1 to 5 !!")

while True:
        print("--------Welcom-------")
        print('1.Customer')
        print('2.Admin')
        print('3.Exit')
        choice=int(input("Enter your choice: "))
        if choice==1:
            customer_menu()
        elif choice==2:
            Admin_menu()
        elif choice==3:
            print("Exiting from the system")
            break
        else:
            print("Invalid option")
            
            