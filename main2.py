# s = 'men maktabga boraman'

# def fn(x):
#     for i in x:
#         if i in 'men':
#             return True 
#         return False
    
# print(fn(s))


# def fn(a):
#     list = []
#     for i in range(len(a)-1, -1, -1):
#         list.append(a[i])
#     print(list)
# fn('salom')


# oyoq_kiyim = ['sapog', 'krasovka', 'butsi']
# isavailable = [True, True, False]
# narxi = [1200, 2300, 2400]

# def fn(a, b, c):
#     summa = 0
#     while True:
#         tanlash = input('Tanlash: ')
#         for i in range(len(a)):
#             if tanlash == a[i]:
#                 if b[i] == True:
#                     print(f"{a[i]} sotib olindi")
#                     summa += c[i]
#                     break
#                 else:
#                     print(f"{a[i]} sotuvda mavjud emas")
#         if tanlash == 'stop':
#             print(f"Jami summa: {summa}")
#             break
    

# fn(oyoq_kiyim, isavailable, narxi)


# class User:
#     def __init__(self, id, name, address):    
#         self.id = id
#         self.name = name
#         self.address = address

# class Customer(User):
#     def __init__(self, id, name, address):
#         super().__init__(id, name, address)
#         self.cart = []

#     def add_to_cart(self, product):
#         self.cart.append(product)
    
#     def remove_to_cart(self, product):
#         self.cart.remove(product)
    
#     def view_cart(self):
#         print("Items in your cart: ")
#         for product in self.cart:
#             print(product.name)


# class Seller(User):
#     def __init__(self, id, name, address):
#         super().__init__(id, name, address)
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#         else:
#             print("Product not found!")
    
#     def view_products(self):
#         print("Available products: ")
#         for product in self.products:
#             print(product.name)

#     def sold_products(self):
#         print("Sold products: ")
#         for product in self.products:
#             print(product.name)

#     def total_revenue(self):
#         total = 0
#         for product in self.products:
#             total += product.price
#         return total
    
# class Product:
#     def __init__(self, id, name, price):
#         self.id = id
#         self.name = name
#         self.price = price

#     def get_info(self):
#         print(f"ID: {self.id}")
#         print(f"Name: {self.name}")
#         print(f"PRice: {self.price}")

        

# class User:
#     def __init__(self, user_id, name, address):
#         self.user_id = user_id
#         self.name = name
#         self.address = address


# class Customer(User):
#     def __init__(self, user_id, name, email):
#         super().__init__(user_id, name, email)
#         self.cart = []

#     def add_to_cart(self, product):
#         if not product.is_sold:
#             self.cart.append(product)
#             product.sold()
#             print(f"{self.name} bought {product.avto_number} number.")
#         else:
#             print(f"{product.avto_number} number is not available for purchase.")

#     def get_available_products(self, products):
#         print("\nAvailable Products:")
#         for product in products:
#             if not product.is_sold:
#                 print(f"{product.avto_number} number at ${product.price}")

#     def purchase_history(self):
#         print("\nPurchase History:")
#         if not self.cart:
#             print("No products bought yet.")
#             return
#         for product in self.cart: 
#             print(f"{product.avto_number} at ${product.price}")

# class Seller(User):
#     def __init__(self, user_id, name, address):
#         super().__init__(user_id, name, address)
#         self.products = []

#     def add_product(self, product_id, avto_number, price):
#         new_product = Product(product_id, avto_number, price)
#         self.products.append(new_product)
#         print(f"{self.name} added {new_product.avto_number} number at ${new_product.price}.")

#     def search_product_by_name(self, avto_number):
#         found_products = [product for product in self.products if avto_number in product.avto_number]
#         if found_products:
#             print("\nSearch Results:")
#             for product in found_products:
#                 status = "Sold" if product.is_sold else "Available"
#                 print(f"{product.avto_number} at ${product.price} ({status})")
#         else:
#             print(f"No products found with the avto number '{avto_number}'.")

#     def information_about_customer(self, customer):
#         print("\nCustomer Information:")
#         print(f"ID: {customer.user_id}")
#         print(f"Name: {customer.name}")
#         print(f"Email: {customer.address}")
#         print("Purchases:")
#         for product in customer.cart:
#             print(f"{product.avto_number} at ${product.price}")

#     def get_product_info(self):
#         print("\nProducts Info:")
#         for product in self.products:
#             status = "Sold" if product.is_sold else "Available"
#             print(f"Product: {product.avto_number}, Price: {product.price}, Status: {status}")


# class Product:
#     def __init__(self, product_id, avto_number, price):
#         self.product_id = product_id
#         self.avto_number = avto_number
#         self.price = price
#         self.is_sold = False

#     def sold(self):
#         self.is_sold = True


# seller1 = Seller(1, "Bob", "bob@example.com")

# seller1.add_product(1, "Laptop", 1000)
# seller1.add_product(2, "Phone", 500)
# seller1.add_product(3, "Tablet", 300)

# seller1.search_product_by_name("Laptop")  
# seller1.search_product_by_name("Phone")   
# seller1.search_product_by_name("Watch")    

# customer1 = Customer(2, "Alice", "alice@example.com")

# customer1.get_available_products(seller1.products)

# customer1.add_to_cart(seller1.products[0])
# customer1.add_to_cart(seller1.products[1])

# customer1.purchase_history()

# customer1.get_available_products(seller1.products)

# seller1.information_about_customer(customer1)

# seller1.get_product_info()

class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_info(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(name, email)
        self.user_id = user_id
        self.password = password  
        self.cart = []

    def display_info(self):
        print(f"Customer ID: {self.user_id}, Name: {self.name}, Email: {self.address}")

    def add_to_cart(self, avto_number, seller):
        product = None
        for p in seller.products:
            if p.avto_number == avto_number:
                product = p
                break

        if product:
            if not product.is_sold:
                self.cart.append(product)
                product.sold()
                print(f"{self.name} bought {product.avto_number} number.")
            else:
                print(f"{product.avto_number} number is not available for purchase.")
        else:
            print(f"No product found with the avto number '{avto_number}'.")

    def get_available_products(self, seller):
        print("\nAvailable Products:")
        for product in seller.products:
            if not product.is_sold:
                print(f"{product.avto_number} number at ${product.price}")

    def transaction(self):
        if not self.cart:
            print("Your cart is empty. No transactions to process.")
            return
        
        print("\nProcessing your transaction for the following items:")
        for product in self.cart:
            print(f"- {product.avto_number} at ${product.price}")
        print("Transaction completed successfully!")

class Seller(User):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.username = "admin" 
        self.password = "admin" 
        self.products = []  

    def display_info(self):
        print(f"Seller Name: {self.name}, Email: {self.address}")


    def add_product(self, product_id, avto_number, price):
        new_product = Product(product_id, avto_number, price)
        self.products.append(new_product)  
        print(f"Added {new_product.avto_number} number for ${new_product.price}.")

    def delete_product(self, avto_number):
        for product in self.products:
            if product.avto_number == avto_number:
                self.products.remove(product) 
                print(f"Product {avto_number} has been deleted.")
                return
        print(f"No product found with the avto number '{avto_number}'.")

    def update_product(self, avto_number, new_price, new_name):
        for product in self.products:
            if product.avto_number == avto_number:
                product.price = new_price
                product.avto_number = new_name 
                print(f"Product {avto_number} updated to {new_name} with price ${new_price}.")
                return
        print(f"No product found with the avto number '{avto_number}'.")

    def search_product_by_name(self, avto_number):
        found_products = [product for product in self.products if avto_number in product.avto_number]
        if found_products:
            print("\nSearch Results:")
            for product in found_products:
                status = "Sold" if product.is_sold else "Available"
                print(f"{product.avto_number} at ${product.price} ({status})")
        else:
            print(f"No products found with the avto number '{avto_number}'.")

    def get_product_info(self):
        print("\nProducts Info:")
        for product in self.products:
            status = "Sold" if product.is_sold else "Available"
            print(f"Product: {product.avto_number}, Price: {product.price}, Status: {status}")

class Product:
    def __init__(self, product_id, avto_number, price):
        self.product_id = product_id
        self.avto_number = avto_number
        self.price = price
        self.is_sold = False

    def sold(self):
        self.is_sold = True

class CustomerManager:
    def __init__(self):
        self.customers = []  
        self.next_user_id = 1  

    def add_customer(self, user_id, name, email, password):
        new_customer = Customer(user_id, name, email, password)
        self.customers.append(new_customer)  
        print(f"Customer {name} added with ID {user_id}.")

    def find_customer(self, name, password):
        for customer in self .customers:
            if customer.name == name and customer.password == password:
                return customer
        print("This customer does not exist.")

if __name__ == "__main__":
    seller1 = None 
    customer_manager = CustomerManager()  

    while True:
        print("1. Log in as Seller/Admin")
        print("2. Log in as Customer")
        print("3. Sign up as Customer")
        print("4. Exit")
        choice = int(input("Enter the user type: "))
        
        if choice == 4:
            break
        
        if choice == 1:
            username = input("Enter seller/admin username: ")
            password = input("Enter seller/admin password: ")
            if username == "admin" and password == "admin":  
                print("Seller/Admin logged in successfully.")
                if seller1 is None: 
                    seller_name = input("Enter seller name: ")
                    seller_address = input("Enter seller email: ")
                    seller1 = Seller(seller_name, seller_address)

                while True:
                    print("\nSeller Menu:")
                    print("1. Add Product")
                    print("2. Search Product by Name")
                    print("3. View Product Info")
                    print("4. Delete Product")
                    print("5. Update Product Price")
                    print("6. Display Info")
                    print("7. Exit to Main Menu")
                    choice = input("Select an option: ")

                    if choice == '1':
                        product_id = input("Enter product ID: ")
                        avto_number = input("Enter product avto number: ")
                        price = float(input("Enter product price: "))
                        seller1.add_product(product_id, avto_number, price)
                    elif choice == '2':
                        avto_number = input("Enter avto number to search: ")
                        seller1.search_product_by_name(avto_number)
                    elif choice == '3':
                        seller1.get_product_info()
                    elif choice == '4':
                        avto_number = input("Enter avto number of the product to delete: ")
                        seller1.delete_product(avto_number)
                    elif choice == '5':
                        avto_number = input("Enter avto number of the product to update: ")
                        new_price = float(input("Enter new price: "))
                        new_name = float(input("Enter new name: "))
                        seller1.update_product(avto_number, new_price, new_name)
                    elif choice == "6":
                        seller1.get_product_info()
                    elif choice == '7':
                        break
                    else:
                        print("Invalid option. Please try again.")

        elif choice == 2:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            customer = customer_manager.find_customer(name, password)
            if customer:
                print(f"Welcome back, {customer.name}!")
                while True:
                    print("\nCustomer Menu:")
                    print("1. View Available Products")
                    print("2. Add Product to Cart")
                    print("3. Checkout")
                    print("4. Display info")
                    print("5. Exit to Main Menu")
                    choice = input("Select an option: ")

                    if choice == '1':
                        customer.get_available_products(seller1)
                    elif choice == '2':
                        customer.get_available_products(seller1)  
                        avto_number = input("Enter the avto number of the product to add: ")
                        customer.add_to_cart(avto_number, seller1)
                    elif choice == '3':
                        customer.transaction()  
                    elif choice == '4':
                        customer.display_info()
                    elif choice == '5':
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid email or password.")

        elif choice == 3:
            user_id = int(input("Enter user ID: "))
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            customer_manager.add_customer(user_id, name, email, password)

        else:
            print("Invalid option. Please try again.")