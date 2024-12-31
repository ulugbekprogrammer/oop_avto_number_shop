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

        

class User:
    def __init__(self, user_id, name, address):
        self.user_id = user_id
        self.name = name
        self.address = address


class Customer(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.cart = []

    def add_to_cart(self, product):
        if not product.is_sold:
            self.cart.append(product)
            product.sold()
            print(f"{self.name} bought {product.avto_number} number.")
        else:
            print(f"{product.avto_number} number is not available for purchase.")

    def get_available_products(self, products):
        print("\nAvailable Products:")
        for product in products:
            if not product.is_sold:
                print(f"{product.avto_number} number at ${product.price}")

    def purchase_history(self):
        print("\nPurchase History:")
        if not self.cart:
            print("No products bought yet.")
            return
        for product in self.cart: 
            print(f"{product.avto_number} at ${product.price}")

class Seller(User):
    def __init__(self, user_id, name, address):
        super().__init__(user_id, name, address)
        self.products = []  

    def add_product(self, product_id, avto_number, price):
        new_product = Product(product_id, avto_number, price)
        self.products.append(new_product)
        print(f"{self.name} added {new_product.avto_number} number at ${new_product.price}.")

    def search_product_by_name(self, avto_number):
        found_products = [product for product in self.products if avto_number in product.avto_number]
        if found_products:
            print("\nSearch Results:")
            for product in found_products:
                status = "Sold" if product.is_sold else "Available"
                print(f"{product.avto_number} at ${product.price} ({status})")
        else:
            print(f"No products found with the avto number '{avto_number}'.")

    def information_about_customer(self, customer):
        print("\nCustomer Information:")
        print(f"ID: {customer.user_id}")
        print(f"Name: {customer.name}")
        print(f"Email: {customer.address}")
        print("Purchases:")
        for product in customer.cart:
            print(f"{product.avto_number} at ${product.price}")

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


if __name__ == "__main__":
    seller1 = Seller(1, "Bob", "bob@example.com")

    seller1.add_product(1, "Laptop", 1000)
    seller1.add_product(2, "Phone", 500)
    seller1.add_product(3, "Tablet", 300)

    seller1.search_product_by_name("Laptop")  # Search for Laptop
    seller1.search_product_by_name("Phone")    # Search for Phone
    seller1.search_product_by_name("Watch")    # Search for a non-existent product

    # Create a buyer
    customer1 = Customer(2, "Alice", "alice@example.com")

    # Buyer views available products
    customer1.get_available_products(seller1.products)

    # Buyer attempts to buy products
    customer1.add_to_cart(seller1.products[0])  # Alice buys a laptop
    customer1.add_to_cart(seller1.products[1])  # Alice buys a phone

    # Buyer views purchase history
    customer1.purchase_history()

    # Buyer views available products again
    customer1.get_available_products(seller1.products)

    # Seller views buyer's purchases
    seller1.information_about_customer(customer1)

    # # Display product info
    seller1.get_product_info()