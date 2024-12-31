# class App:
#     def __init__(self, user, storage, username):
#         self.user = user
#         self.srorage = storage
#         self.username = username

#     def login(self):
#         if self.username == "owner" and self.user >= 1:
#             print('Welcome', self.username)
#             print('Your storgae is', self.srorage)
#         else:
#             print("You are not user")
        
#     def increase_capacity(self, number):
#         self.srorage += number
#         print("Updated storage", self.srorage)

#     def check_upgrade(self):
#         if self.user >= self.srorage:
#             upgrade_amt = int(input("Enter amount to upgrade: "))
#             self.srorage += upgrade_amt
#         else:
#             print("You still have", self.srorage - self.user, "space left")   


# product_one = App(35, 256, "owner")
# product_one.login()
# product_one.increase_capacity(44)    
# print()
# product_two = App(13, 42, "Josh")
# product_two.login()
# product_two.check_upgrade()


# class OnlineCourse:
#     def __init__(self, course_name, teacher_name):
#         self.course_name = course_name
#         self.teacher_name = teacher_name
#         self.students = []
        
#     def enroll_student(self, student_name):
#         self.students.append(student_name)
#         print(f"{student_name} has been enrolled in the course.")
#         print(f"There are now {len(self.students)} students in the course.")

#     def get_course_details(self):
#         print(f'The course name is {self.course_name}, the teacher {self.teacher_name} is teaching the course and there are {', '.join(self.students)} students in the course.')

#     def completed_corse(self, student_name):
#         if student_name in self.students:
#             self.students.remove(student_name)  
#             print(f"{student_name} has completed the course.")
#         else: 
#             print(f"{student_name} is not enrolled in the course.")

#     def avg_grade(self, grades):
#         total = sum(grades)
#         avarage = total / len(grades)
#         print(f"The average grade for the course is {avarage}")

# course_input = input('Enter the course: ').lower()
# name = input('Enter a Instructor name: ').lower()
# student = input('Enter a student name: ').lower()
# student_name = input('Enter the name: ').lower()

# # course = OnlineCourse('Python', 'John Doe')
# course = OnlineCourse(course_input, name)
# # student = 'muslim'
# grades = [90, 85, 92, 78, 80]

# course.avg_grade(grades)
# course.enroll_student(student)
# course.get_course_details()
# # course.completed_corse(student_name="muslim")
# course.completed_corse(student_name=student_name)




# More harder
# class OnlineCourse:
#     def __init__(self, course, instructor):
#         self.course = course
#         self.instructor = instructor
#         self.students = []
        
#     def encroll_students(self, student):
#         self.students.append(student)
#         print(f"{student.name} has been enrolled in the {self.course} course.")

#     def get_course_details(self):
#         print(f'Course: {self.course}')
#         print(f'Instructor name: {self.instructor}')
#         print(f'Enrolled Students: ')
#         for student in self.students:
#             print(student.name)

#     def completed_corse(self, name):
#         for student in self.students:
#             if student.name in name:
#                 self.students.remove(student)  
#                 print(f"{name} has completed the course.")
#         print(f"{name} is not enrolled in the course.")

#     def avg_grade(self, student):
#         total = sum(student.grades)
#         avarage = total / len(student.grades)
#         print(f"The average grade for the course is {round(avarage, 1)}")

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

# course_input = input('Enter the course: ').lower()
# name = input('Enter a Instructor name: ').lower()
# course = OnlineCourse(course_input, name)

# num_students = int(input('Enter number of students: '))

# for _ in range(num_students):
#     student_name = input("Enter the student name: ").lower()
#     grades = []
#     for _ in range(3):
#         grade = int(input("Enter the grade: "))
#         grades.append(grade)
#     student = Student(student_name, grades)
#     course.encroll_students(student)
#     course.avg_grade(student)
# course.get_course_details()



# Travel
# class Travel:
#     def __init__(self, country, month, type):
#         self.country = country
#         self.month = int(month)
#         self.type = type
#         self.price = 0

#     def trip_info(self):
#         if self.month >= 10 and self.month <= 3:
#             print(f"You are going to {self.country} on Winter! This is a {self.type} trip!")
#         elif self.month > 3 and self.month < 10:
#             print(f"You are going to {self.country} on Summer! This is a {self.type} trip!")
#         else:
#             print("Invalid input")
        
#     def calc_cost(self, cost):
#         costs = []
#         while cost != 0:
#             self.price += cost
#             costs.append(cost)
#             cost = int(input("Enter another cost: "))

#         advice = self.advice(self.price)
#         inspects = self.list_inspects(costs)
#         return advice, inspects

#     def advice(self, num):
#         if num < 500:
#             print('Low budget')
#         elif num >= 500 and num < 1500:
#             print("Take a flight to anywhere...")
#         else:
#             print("Luxury Trip")

#     def list_inspects(self, costs):
#         less_than_ten = 0
#         for i in costs:
#             if i >= 10:
#                 less_than_ten += 1

#             if less_than_ten <= 10:
#                 self.price += 100
#                 print(f"Updated price: {self.price}")


# location = input("Enter the country: ").capitalize()
# trip_type = input("Business or Leisure: ").capitalize()
# month = input("Enter a month: ")

# test = Travel(location, month, trip_type)
# test.trip_info()

# flight = int(input("Enter the flight cost: "))
# test.calc_cost(flight)



# Guest 
# class Guest:
#     def __init__(self, last, first, rank, age):
#         self.last_name = last
#         self.first_name = first
#         self.rank = int(rank)
#         self.age = int(age)

#     def guest_info(self, all_guests):
#         for guest in all_guests:
#             print(guest.first_name, guest.last_name, "Age: ",guest.age)

#     def loyalty_program(self, all_guests):
#         gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
#         if gold_members:
#             print("Gold members: ")
#             for member in gold_members:
#                 print("\t Guest: ", member)

#     def guest_avg(self, all_guests):
#         total_age = 0
#         for guest in all_guests:
#             total_age += guest.age
#         avg_age = total_age / len(all_guests)
#         print('Avarage age: ', avg_age)


# all_guests = list()
# num_guests = int(input("Enter the number of guests: "))
# for i in range(num_guests):
#     data = input("First Name/Last Name/Rank/Age: ").split("/")
#     guest = Guest(data[0], data[1], int(data[2]), int(data[3]))
#     all_guests.append(guest)

# guest = all_guests[0]
# guest.guest_info(all_guests)
# guest.loyalty_program(all_guests)
# guest.guest_avg(all_guests)



# Inhertence
# class Main:
#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location

#     def info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Location: {self.location}")

# class UserScore(Main):
#     def __init__(self, name, age, location, score):
#         super().__init__(name, age, location)
#         self.score = score

#     def check_avg(self, list1):
#         x = round(self.score / len(list1) * 100, 1)
#         return ("Result: ",x)

# test_list = [4,4,4,5,5,5]

# user = UserScore('John Doe', 30, 'New York', 5)
# print(user.check_avg(test_list))


# Inhertance Animal
# class Animal:
#     def __init__(self, region, animal_type, color, lethal):
#         self.region = region
#         self.animal_type = animal_type
#         self.color = color
#         self.lethal = lethal

#     def animal_bio(self):
#         print("Animal Passport: ")
#         print('Animal Type: ', self.animal_type)
#         print('Region: ', self.region)  
#         print('Color: ', self.color)
#         print('Dangerous: ', self.lethal)

# class Clinic(Animal):
#     def animal_info(self):
#         print(f'This is a {self.animal_type} from {self.region}')

#     def search(self, animals):
#         region = input("Enter the region: ")
#         for animal in animals:
#             if animal.region ==  region:
#                 print("Species: ",animal.animal_type)


# animals = []
# amn_animals = int(input("Enter the number of animals: "))
# for i in range(amn_animals):
#     region = input("Enter the region: ")
#     animal_type = input("Enter the animal type: ")
#     color = input("Enter the color: ")
#     lethal = input("Is it dangerous: ")
#     lethal = lethal == "yes"

#     animal = Animal(region, animal_type, color, lethal)
#     animals.append(animal)

# clinic = Clinic("America", "dog", "white", "no")
# clinic.animal_bio()
# clinic.animal_info()
# clinic.search(animals)



# Superhero
# class Superhero:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def use_power(self):
#         print(f'{self.name} is using {self.power} power')

#     def intro_hero(self):
#         print(f'I am {self.name} and I have the power {self.power}')
    
#     def save_day(self):
#         print(f'{self.name} has saved the day')

#     def power_level(self):
#         length = len(self.power)
#         level = length*10
#         return level

# class Flying(Superhero):
#     def __init__(self, name, power, speed):
#         super().__init__(name, power)
#         self.speed = speed
    
#     def use_power(self):
#         print(f"{self.name} is flying at the speed of {self.speed} miles per hour")

#     def calc_distance(self, flight_time):
#         distance = self.speed * flight_time
#         return distance


# batman = Superhero('Batman', 'Intelligence')
# batman.save_day()
# print(batman.power_level())

# print()
# superman = Flying('Superman', 'Flight', 1000)
# superman.intro_hero()
# superman.use_power()
# fly_dist = 30
# attack = superman.calc_distance(fly_dist)
# print(f"{superman.name} can fly a distance of {attack} miles in {fly_dist} hours")



# Book
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


#     def info(self):
#         print(f'Title: {self.title}')
#         print(f'Author: {self.author}')
#         print(f'Year: {self.year}')
    

# class FictionBook(Book):
#     def __init__(self, title, author, year, genre):
#         super().__init__(title, author, year)
#         self.genre = genre
    

#     def info(self):
#         super().info()
#         print(f'Genre: {self.genre}')


# class NonFictionBook(Book):
#     def __init__(self, title, author, year, topic):
#         super().__init__(title, author, year)
#         self.topic = topic

#     def info(self):
#         super().info()
#         print(f'Topic: {self.topic}')    

    


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self):
#         for book in self.books:
#             self.books.append(book)

#     def display_books(self):
#         for book in self.books:
#             book.info()
#             print()

#     def search_author(self, author):
#         found_book = []
#         for book in self.books:
#             if book.author == author:
#                 found_book.append(book)
#         if found_book:
#             print(f"Book by {author}: ")
#             for book in found_book:
#                 book.info()
#                 print()
#         else:
#             print(f"Book by {author} not found")

#     def search_year(self, start_year, end_year):
#         found_book = []
#         for book in self.books:
#             if start_year <= book.year <= end_year:
#                 found_book.append(book)
#         if found_book:
#             print(f"Book between {start_year} and {end_year}: ")
#             for book in found_book:
#                 book.info()
#                 print()
#         else: 
#             print("Error")

# library = Library()


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def display_books(self):
#         for book in self.books:
#             book.info()
#             print()

#     def search_author(self, author):
#         found_book = []
#         for book in self.books:
#             if book.author == author:
#                 found_book.append(book)
#         if found_book:
#             print(f"Book by {author}: ")
#             for book in found_book:
#                 book.info()
#                 print()
#         else:
#             print(f"Book by {author} not found") 


#     def search_year(self, start_year, end_year):
#         found_book = []
#         for book in self.books:
#             if start_year <= book.year <= end_year:
#                     found_book.append(book)
#         if found_book:
#             print(f"Book between {start_year} and {end_year}: ")
#             for book in found_book:
#                 book.info()
#                 print()
#         else: 
#             print("Error")


# library = Library()

# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
# book2 = FictionBook('Harry Potter', "J.K Rowling", 2005, "Advanture")
# book3 = NonFictionBook('The Power of Now', "Yuval Noah Harari", 1997, "History")


# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # library.display_books()
# # library.search_author("J.K Rowling")
# library.search_year(1900, 2000)



# class Country:
#     def __init__(self, name, capital, population):
#         self.name = name
#         self.capital = capital
#         self.pop = population
        
#     def get_info(self):
#         return {
#             "name": self.name,
#             "capital": self.capital,
#             "population": self.pop
#         }


# class DevelopCountry(Country):
#     def __init__(self, name, capital, population, gdp):
#         super().__init__(name, capital, population) 
#         self.gdp = gdp

#     def get_info(self):
#         info = super().get_info()
#         info["gdp"] = self.gdp
#         return info


# class DevelopingCountry(Country):
#     def __init__(self, name, capital, population, hdi):
#         super().__init__(name, capital, population)
#         self.hdi = hdi

#     def get_info(self):
#         info = super().get_info()
#         info["hdi"] = self.hdi
#         return info



# class World:
#     def __init__(self):
#         self.countries = []

#     def add_country(self, country):
#         self.countries.append(country)

#     def get_country_info(self, country_name):
#         for country in self.countries:
#             if country.name == country_name:
#                 return country.get_info()

# world = World()

# usa = DevelopCountry("United States", "Washington D.C.", 330000000, 1.5)
# canada = DevelopingCountry("Canada", "Ottawa", 38000000, 0.9)
# uzb = DevelopingCountry('Uzbekistan', 'Tashkent', 35000000, 0.7)

# world.add_country(usa)
# world.add_country(canada)
# world.add_country(uzb)

# # for country in world.countries:
# #     print(country.get_info())
# #     print()

# country_search = world.get_country_info("Uzbekistan")
# if country_search:
#     print('Country info: ')
#     for key, value in country_search.items():
#         print(f"{key}: {value}")
# else:
#     print("Country not found") 



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} is eating')


# class CanFly:
#     def fly(self):
#         print(f'{self.name} is flying')


# class Bird(Animal, CanFly):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color

#     def sleep(self):
#         print(f'The {self.color} bird is sleeping')


# my_bird = Bird('Parrot', 'blue')
# my_bird.fly()
# my_bird.sleep()
# my_bird.eat()


# class Account:
#     def __init__(self, act_num, balance):
#         self.act_num = act_num
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdrawl(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Not enough money")
        
#     def get_balance(self):
#         return self.balance


# class InterestAccount(Account):
#     def __init__(self, act_num, balance, interest_rate):
#         Account.__init__(self, act_num, balance)
#         self.interest_rate = interest_rate

#     def calc_interest(self):
#         return self.balance * self.interest_rate


# class Transition:
#     def __init__(self):
#         self.transitions = []

#     def add_transition(self, transtion):
#         self.transitions.append(transtion)

#     def history(self):
#         for history in self.transitions:
#             print(history)


# class SavingsAccount(InterestAccount, Transition):
#     def __init__(self, act_num, balance, interest_rate):
#         InterestAccount.__init__(self, act_num, balance, interest_rate)
#         Transition.__init__(self)


# savings = SavingsAccount("12345", 1000, 0.08)
# savings.deposit(2000)
# savings.withdrawl(600)

# interest = savings.calc_interest()
# balance = savings.get_balance()

# savings.add_transition("Deposit: 2000")
# savings.add_transition("Withdrawl: 600")

# savings.history()

# print("Balance: ", balance)
# print("Interest", interest)



# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# class ElectricCar:
#     def __init__(self, battery_capacity):
#         self.battery_cap = battery_capacity

#     def charge(self):
#         return self.battery_cap

#     def get_range(self):
#         return self.battery_cap * 5


# class GasCar:
#     def __init__(self, fuel_capacity):
#         self.fuel_cap = fuel_capacity

#     def refuel(self):
#         return self.fuel_cap 

#     def get_range(self):
#         return self.fuel_cap * 20


# class Hybrid(Vehicle, ElectricCar, GasCar):
#     def __init__(self, make, model, year, battery_capacity, fuel_capacity):
#         super().__init__(make, model, year)
#         super().__init__(battery_capacity)
#         super().__init__(fuel_capacity)


# car =  Hybrid("Toyota", "Prius", 2023, 5, 40)

# battery_charge = car.charge()
# print(battery_charge)



# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# class ElectricCar:
#     def __init__(self, battery_capacity):
#         self.battery_cap = battery_capacity

#     def charge(self):
#         return self.battery_cap

#     def get_range(self):
#         return self.battery_cap * 5

# class GasCar:
#     def __init__(self, fuel_capacity):
#         self.fuel_cap = fuel_capacity

#     def refuel(self):
#         return self.fuel_cap 

#     def get_range(self):
#         return self.fuel_cap * 20

# class Hybrid(Vehicle, ElectricCar, GasCar):
#     def __init__(self, make, model, year, battery_capacity, fuel_capacity):
#         Vehicle.__init__(self, make, model, year)
#         ElectricCar.__init__(self, battery_capacity)
#         GasCar.__init__(self, fuel_capacity)

# car = Hybrid("Toyota", "Prius", 2023, 5, 40)

# for cars in [car]:
#     print("Make: ", cars.make)
#     print("Model: ", cars.model)
#     print("Year: ", cars.year) 
#     print("Battery: ", cars.battery_cap)
#     print("Fuel: ", cars.fuel_cap)
#     print("Range: ", cars.get_range())

# battery_capacity = car.charge()
# print(battery_capacity)
# gas_capacity = car.refuel()
# print(gas_capacity)



# class User:
#     def __init__(self, username, email):    
#         self.username = username
#         self.email = email

# class Customer(User):
#     def __init__(self, username, email):
#         super().__init__(username, email)
#         self.cart = []

#     def add_to_cart(self, product):
#         self.cart.append(product)
    
#     def remove_to_cart(self, product):
#         if product in self.cart:
#             self.cart.remove(product)
#         else:
#             print("Item is not on your cart")

#     def view_cart(self):
#         print("Items in your cart: ")
#         for product in self.cart:
#             print(product.name)

#     def save_cart(self, filename):
#         with open(filename, "w") as file:
#             for product in self.cart:
#                 file.write(f"{product.name}, {product.price}\n")
#         print(f"Cart saved to {filename}")

# class Seller(User):
#     def __init__(self, username, email):
#         super().__init__(username, email)
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

#     def save_products(self, filename):
#         with open(filename, "w") as file:
#             for product in self.products:
#                 file.write(f"{product.name}, {product.price}\n")
#         print(f"Products saved to {filename}")

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def get_info(self):
#         print(f"Name: {self.name}")
#         print(f"PRice: {self.price}")

# customer = Customer("BillyBob123", "billy@hoolo.com")
# seller = Seller("JohnDoe", "john@doe.com")

# product1 = Product("Shirt", 10.00)
# product2 = Product("Pants", 20.00)
# product3 = Product("Shoes", 30.00)

# customer.add_to_cart(product1)
# customer.add_to_cart(product2)
# customer.add_to_cart(product3)

# customer.view_cart()

# customer.save_cart("customer_cart.txt")

# customer.remove_to_cart(product2)
# customer.view_cart()

# seller.add_product(product1)
# seller.add_product(product2)
# seller.add_product(product3)

# seller.view_products()

# seller.save_products("seller_products.txt")



# class Employee:
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.emplyee_id = employee_id

#     def __str__(self):
#         return f"Employee: {self.name}, (ID: {self.emplyee_id})"
        
#     def __eq__(self, other):
#         if isinstance(other, Employee):
#             return self.emplyee_id == other.emplyee_id
#         return False

#     def __add__(self, other):
#         raise ValueError("Can not add employee!")

# class Manager(Employee):
#     def __init__(self, name, employee_id, department):
#         super().__init__(name, employee_id)
#         self.department = department

#     def __str__(self):
#         return f"Manager: {self.name}, (ID: {self.emplyee_id}), (Department: {self.department})"

#     def __eq__(self, other):
#         if isinstance(other, Employee):
#             return self.emplyee_id == other.emplyee_id
#         return False

#     def __add__(self, other):
#         raise ValueError("Can not add manager!")


# class Staff(Employee):
#     def __init__(self, name, employee_id, role):
#         super().__init__(name, employee_id)
#         self.role = role

#     def __str__(self):
#         return f"Manager: {self.name}, (ID: {self.emplyee_id}), (Role: {self.role})"

#     def __eq__(self, other):
#         if isinstance(other, Employee):
#             return self.emplyee_id == other.emplyee_id
#         return False

#     def __add__(self, other):
#         raise ValueError("Can not add staff member!")


# employee1 = Employee("John Doe", 1)
# employee2 = Employee("Sarah Hardie", 2)

# manager1 = Manager("Bruce Bruce", 9, "marketing")
# manager2 = Manager("Sarah Janie", 28, "sales")

# staff1 = Staff("Mark Jones", 12, "Marketing Ops Dev")
# staff2 = Staff("Emily Davis", 14, "Software Engineer")


# print(employee1)
# print(manager1)
# print(staff1)

# print(employee1 == employee2)
# print(manager1 == manager2)

# print(manager1 + manager2)


# class Sport:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f"This is {self.name}"

#     def __add__(self, other):
#         raise TypeError("Not Possible")

#     def __sub__(self, other):
#         raise TypeError("Not Possible")

# class Football(Sport):
#     def __init__(self, name, team):
#         super().__init__(name)
#         self.team = team

#     def __str__(self):
#         return f"This is {self.name} team, mathed with {', '.join(self.team)}"

#     def __eq__(self, other):
#         if isinstance(other, Football):
#             return self.name == other.name and self.team == other.team
#         return False

#     def __sub__(self, other):
#         if isinstance(other, Football):
#             shared_teams = list(set(self.team) & set(other.team))
#             if shared_teams:
#                 return Football(f"{self.name}: ", shared_teams)
#             else:
#                 return "No common teams between them"
#         return "Not Possible"


# class Basketball(Sport):
#     def __init__(self, name, team):
#         super().__init__(name)
#         self.team = team

#     def __str__(self):
#         return f"This is {self.name} team, mathed with {', '.join(self.team)}"

#     def __eq__(self, other):
#         if isinstance(other, Basketball):
#             return self.name == other.name and self.team == other.team
#         return False

#     def __sub__(self, other):
#         if isinstance(other, Basketball):
#             shared_teams = list(set(self.team) & set(other.team))
#             if shared_teams:
#                 return Basketball(f"{self.name}: ", shared_teams)
#             else:
#                 return "No common teams between them"
#         return "Not Possible"


# sport = Sport("This is super basic!")
# # print(sport + sport)

# football1 = Football("Football", ["Barcelona", "Real Madrid"])
# football2 = Football("Football", ["Barcelona", "Real Madrid"])

# basketball1 = Basketball("Basketball", ["Los Angeles Lakers", "Golden State Warriors"])
# basketball2 = Basketball("Basketball", ["New York Knicks", "Los Angeles Lakers"])

# # print(sport)
# # print(football1)
# # print(basketball1)

# print(football1 == football2)
# print(basketball1 == basketball2)

# print(basketball1 - basketball2)



# class Item:
#     def __init__(self, title, author):
#         self.name = title
#         self.autor = author

#     def __str__(self):
#         return f"{self.name} is by {self.autor}"

# class Book(Item):
#     def __init__(self, title, author, pages):
#         Item.__init__(self, title, author)
#         self.pages = pages

#     def __len__(self):
#         return self.pages

# class DVD(Item):
#     def __init__(self, title, director, duration):
#         Item.__init__(self, title, director)
#         self.duration = duration
    
#     def __len__(self):
#         return self.duration

# class LibraryItem(Book, DVD):
#     def __init__(self, title, author, pages, director, duration, copies):
#         Book.__init__(self, title, author, pages)
#         DVD.__init__(self, title, director, duration)
#         self.copies = copies

#     def __str__(self):
#         return f"{self.name} by {self.autor} (Book: {self.pages}, DVD: {self.duration} minutes), Copies: {self.copies}"

#     def __add__(self, other):
#         if isinstance(other, LibraryItem) and self.copies == other.copies:
#             combo = self.copies + other.copies
#             return LibraryItem(self.name, self.copies, self.pages, self.autor, self.duration,  combo)
#         else:
#             raise TypeError("Can not add two different objects together!")


# book1 = Book("The Great Gatsby", "F Scott Fitzgerald", 1925)
# # book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# dvd1 = DVD("The Shawshank Redemption", "Frank Darabont", 142)
# # dvd2 = DVD("The Godfather", "Francis Ford Coppola", 175)

# library_item = LibraryItem("Python Course", "Josh Wenner", 500, "James Cameron", 160, 10)
# library_item2 = LibraryItem("Python Course", "Josh Wenner", 500, "James Cameron", 160, 10)

# # print(book1)
# print(len(book1))
# print(dvd1)
# print(len(dvd1))
# print(library_item)
# print(library_item.__len__())
# print(library_item + library_item2)



# class Animal:
#     def __init__(self, name, region, animal_type):
#         self.name = name
#         self.region = region
#         self.animal_type = animal_type
    
#     def __str__(self):
#         return f"Name: {self.name}, Region: {self.region}, Animal Type: {self.animal_type}"

    
# class Bird(Animal):
#     def __init__(self, name, region, animal_type, sound):
#         super().__init__(name, region, animal_type)        
#         self.sound = sound

#     def bird_sound(self):
#         return f''


# class Crypto:
#     def __init__(self, name):
#         self.name = name
#         self.price = 0

#     def __str__(self):
#         return f"This is {self.name} a cryptocurrency"

#     def __eq__(self, other):
#         if isinstance(other, Crypto):
#             return self.name == other.name
#         return False

#     def __add__(self, other):
#         if isinstance(other, Crypto):
#             combo = self.name + " " + other.name
#             return Crypto(combo)
#         else: 
#             raise ValueError("Can not perform addition betweenn them")

#     def set_price(self, price):
#         self.price += price
        
#     def get_price(self):
#         if hasattr(self, "price"):
#             return self.price
#         else: 
#             print("Price not set")

#     def calc_value(self, quantity):
#         if hasattr(self, "price"):
#             return self.price * quantity
#         else: 
#             print("Price not set")

# class Bitcoin(Crypto):
#     def __init__(self):
#         super().__init__("Bitcoin")

#     def __str__(self):
#         return f"Bitcoin is decentralized"

#     def mine(self):
#         return f"Mining the next Block..."

# class Ethereum(Crypto):
#     def __init__(self):
#         super().__init__("Ethereum")

#     def __str__(self):
#         return f"Ethereum uses smart contracts!"

#     def mine(self):
#         return f"Minting tokens..."

# crypto1 = Crypto(22)
# crypto2 = Crypto("Cardano")
# crypto3 = Crypto("Bitcoin")

# bitcoin = Bitcoin()
# ethereum = Ethereum()

# print(crypto1)

# print(bitcoin == crypto3)
# print(bitcoin == ethereum)
# print(bitcoin + ethereum)

# ethereum.set_price(100)
# ethereum.set_price(300)
# ethereum.set_price(300)
# print(ethereum.get_price())

# portfolio = [
#     {"crypto":bitcoin, "quantity":2},
#     {"crypto":ethereum, "quantity":3}
# ]

# print(portfolio[0])


# class Library:
#     def __init__(self):
#         self.books = []

#     def info_books(self):
#         return [f"{book.title} by {book.author} relased in {book.released_year}" for book in self.books]
#         # for book in self.books:
#             # print(f"{book.title} by {book.author} relased in {book.released_year}")

#     def add_book(self, book):
#         self.books.append(book)

#     def remove_book(self, book):
#         self.books.remove(book)

#     def update_book(self, book, new_book_title, new_book_author, new_book_released_year):
#         if book in self.books:
#             self.books.remove(book)
#             new_book = Book(new_book_title, new_book_author, new_book_released_year)
#             self.books.append(new_book)
#         else: 
#             print("Book not found")

#     def search_title(self, title):
#         for book in self.books:
#             if book.title == title:
#                 print("Book info: ")
#                 print(f"{book.title} by {book.author} relased in {book.released_year}")
#             else:
#                 print(f"Book with this {book.title} title not found")

#     def search_author(self, author):
#         for book in self.books:
#             if book.author == author:
#                 print("Book info: ")
#                 print(f"{book.title} by {book.author} relased in {book.released_year}")
#             else: 
#                 print(f"Book with this {book.author} author not found")

#     def search_year(self, released_year):
#         for book in self.books:
#             if book.released_year == released_year:
#                 print("Book info: ")
#                 print(f"{book.title} by {book.author} relased in {book.released_year}")
#             else: 
#                 print(f"Book with this {book.released_year} year not found")

# class Book:
#     def __init__(self, title, author, released_year):
#         self.title = title
#         self.author = author
#         self.released_year = released_year


# library = Library()
# book1 = Book("The Great Gatsby", "F Scott Fitzgerald", 1925)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# book3 = Book("1984", "George Orwell", 1949)

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # for book in library.info_books():
# #     print(book)

# library.remove_book(book1)

# # for book in library.info_books():
# #     print(book)

# library.update_book(book2, "Naruto", "Kishimota", 1998)

# for book in library.info_books():
#     print(book)
# # library.info_books() 

# library.search_title('Naruto')




# class User:
#     def __init__(self, username, email):    
#         self.username = username
#         self.email = email

# class Customer(User):
#     def __init__(self, username, email):
#         super().__init__(username, email)
#         self.cart = []

#     def add_to_cart(self, product):
#         self.cart.append(product)
    
#     def remove_to_cart(self, product):
#         if product in self.cart:
#             self.cart.remove(product)
#         else:
#             print("Item is not on your cart")

#     def view_cart(self):
#         print("Items in your cart: ")
#         for product in self.cart:
#             print(product.name)

#     def save_cart(self, filename):
#         with open(filename, "w") as file:
#             for product in self.cart:
#                 file.write(f"{product.name}, {product.price}\n")
#         print(f"Cart saved to {filename}")

# class Seller(User):
#     def __init__(self, username, email):
#         super().__init__(username, email)
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

#     def save_products(self, filename):
#         with open(filename, "w") as file:
#             for product in self.products:
#                 file.write(f"{product.name}, {product.price}\n")
#         print(f"Products saved to {filename}")

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def get_info(self):
#         print(f"Name: {self.name}")
#         print(f"PRice: {self.price}")

# customer = Customer("BillyBob123", "billy@hoolo.com")
# seller = Seller("JohnDoe", "john@doe.com")

# product1 = Product("Shirt", 10.00)
# product2 = Product("Pants", 20.00)
# product3 = Product("Shoes", 30.00)

# customer.add_to_cart(product1)
# customer.add_to_cart(product2)
# customer.add_to_cart(product3)

# customer.view_cart()

# customer.save_cart("customer_cart.txt")

# customer.remove_to_cart(product2)
# customer.view_cart()

# seller.add_product(product1)
# seller.add_product(product2)
# seller.add_product(product3)

# seller.view_products()

# seller.save_products("seller_products.txt")



