
#Task 1
class Customer:
    def __init__(self):
        self.name = None
        self.mobile_number = None
        self.year_of_birth = None
        self.current_city = None
        self.email = None

    def get_details(self):
        self.name = input("Enter your name: ")
        self.mobile_number = input("Enter your mobile number: ")
        self.year_of_birth = int(input("Enter your year of birth: "))
        self.current_city = input("Enter your current city: ")
        self.email = input("Enter your email address: ")

    def calculate_age(self):
        current_year = 2023
        age = current_year - self.year_of_birth
        return age

    def display_greeting(self):
        age = self.calculate_age()
        if age > 21:
            print(f"Hello {self.name}, thank you for creating an account!\n"
                  f"Here are your details:\n"
                  f"Name: {self.name}\n"
                  f"Mobile number(10): {self.mobile_number}\n"
                  f"Year of birth(xxxx): {self.year_of_birth}\n"
                  f"Current city: {self.current_city}\n"
                  f"Email address: {self.email}\n"
                  f"You are {age} years old and eligible for promotions.")
        else:
            print(f"Hello {self.name}, thank you for creating an account!\n"
                  f"Here are your details:\n"
                  f"Name: {self.name}\n"
                  f"Mobile number: {self.mobile_number}\n"
                  f"Year of birth: {self.year_of_birth}\n"
                  f"Current city: {self.current_city}\n"
                  f"Email address: {self.email}\n"
                  f"Sorry, you are not eligible for promotions as you are under 21 years old.")

#Task 2
class RestaurantCapacity:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_capacity(self):
        area = self.width * self.length
        capacity = int(area / 1.2)
        if capacity > 60:
            print("A maximum of 60 persons are allowed.")
            capacity = 60
        return capacity


#Task 3
class SaleAnalyzer:
    def __init__(self):
        self.current_week_sales = []
        self.previous_week_sales = []

    def get_sales(self):
        current_week_input = input("Enter total prices of orders for current week (Orders separated by space): ")
        self.current_week_sales = list(map(float, current_week_input.split()))

        previous_week_input = input("Enter total prices of orders for previous week (Orders separated by space): ")
        self.previous_week_sales = list(map(float, previous_week_input.split()))

    def analyze_sales(self):
        current_week_visitors = len(self.current_week_sales)
        previous_week_visitors = len(self.previous_week_sales)

        current_week_total_sale = sum(self.current_week_sales)
        previous_week_total_sale = sum(self.previous_week_sales)

        current_week_per_person_sale = current_week_total_sale / current_week_visitors
        previous_week_per_person_sale = previous_week_total_sale / previous_week_visitors

        print(f"Current Week per person average sale: {current_week_per_person_sale:.2f} AUD")
        print(f"Last Week per person average sale: {previous_week_per_person_sale:.2f} AUD")


#Task 4
class PaymentCalculator:

    def calculate_change(self):

        # Get inputs from the user
        total_invoice_amount = float(input("Total Invoice amount (In Dollars): "))
        tip_amount = float(input("Amount of Tip (In Cents): ")) / 100
        card_payment_received = float(input("Total Payment received by Card: "))
        service_charge_percent = float(input("Service Charge on Payment made by Card %: ").replace("%", "")) / 100
        cash_payment_received = float(input("Total Payment received in Cash (In Dollars): "))

        # Calculate the total payment received
        total_payment_received = card_payment_received / (1 + service_charge_percent) + cash_payment_received

        # Calculate the change to be returned to the customer
        change = total_payment_received - total_invoice_amount - tip_amount-0.25

        # Check if change is positive or negative
        if change >= 0:
            print("Change to be returned to the customer (In Dollars): {:.2f}".format(change))
        else:
            print("Outstanding amount and need to be paid by customer: {:.2f}".format(-change))


#Task 5
class DeliveryChargeCalculator:
    def __init__(self):
        self.rates = {
            "0-5": 5,
            "5-10": 8,
            "10-12": 10
        }

    def calculate_delivery_charge(self, address, distance):
        if distance <= 0:
            return "Invalid distance"
        elif distance <= 5:
            return f"Delivery charge to {address}: ${self.rates['0-5']}"
        elif distance <= 10:
            return f"Delivery charge to {address}: ${self.rates['5-10']}"
        elif distance <= 12:
            return f"Delivery charge to {address}: ${self.rates['10-12']}"
        else:
            return f"No delivery available for {distance}km distance from restaurant"

#Task 6
class OrderCalculator:
    def calculate_order_charges(self):
        base_cost = float(input("Enter the order base cost in AUD: "))
        order_type = int(input("Enter the order type (1 for dine in, 2 for pick up, 3 for delivery): "))

        if order_type == 1:
            total_cost = base_cost * 1.08
        elif order_type == 2:
            total_cost = base_cost
        elif order_type == 3:
            total_cost = base_cost * 1.1
        else:
            print("Invalid order type entered. Please try again.")
            return

        print("Total amount to be paid: AUD {:.2f}".format(total_cost))

#Task 7
class TemperatureConverter:

    def __init__(self):
        pass

    def from_celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit

    def from_fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    def convert_temperature(self):
        temperature = input("Enter temperature value  Celsius or Fahrenheit: ")
        try:
            temperature = float(temperature)
        except ValueError:
            print("Invalid temperature value!")
            return

        conversion_type = input("Select conversion type (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius): ")

        if conversion_type == '1':
            fahrenheit = self.from_celsius_to_fahrenheit(temperature)
            print(f"{temperature} Celsius = {fahrenheit} Fahrenheit")
        elif conversion_type == '2':
            celsius = self.from_fahrenheit_to_celsius(temperature)
            print(f"{temperature} Fahrenheit = {celsius} Celsius")
        else:
            print("Invalid conversion type!")
            return

#Task 8
class Employee:
    def __init__(self, position, hourly_rate):
        self.position = position
        self.hourly_rate = hourly_rate

    def calculate_pay(self, hours_worked):
        gross_pay = self.hourly_rate * hours_worked
        tax = 0.2 * gross_pay
        net_pay = gross_pay - tax
        return net_pay


class Chef(Employee):
    def __init__(self):
        super().__init__("Chef", 50)


class Waiter(Employee):
    def __init__(self):
        super().__init__("Waiter", 40)


class DeliveryPerson(Employee):
    def __init__(self):
        super().__init__("Delivery Person", 35)


class IncomeCalculator:
    def __init__(self):
        self.employee_types = {
            "chef": Chef,
            "waiter": Waiter,
            "delivery": DeliveryPerson
        }

    def calculate_net_income(self):
        position = input("Enter the position of the employee (chef, waiter or delivery): ").lower()
        if position not in self.employee_types:
            print("Invalid position entered.")
            return

        hours_worked = float(input("Enter the number of monthly hours worked: "))
        if hours_worked < 0:
            print("Invalid hours worked entered.")
            return

        employee = self.employee_types[position]()
        net_income = employee.calculate_pay(hours_worked)
        print("The net monthly income of the employee is: ${:.2f}".format(net_income))

#Task 9
class UserCredentials:
    def register(self):
        mobile_number = input("Enter your mobile number: ")
        password = input("Enter a password (minimum 8 characters): ")

        if len(mobile_number) == 10 and len(password) >= 8:
            print("Valid credentials.")
        else:
            print("Invalid credentials.")





def main_menu():
    print("Welcome to the AZA Restaurant Mobile Order management platform! Please select one of the following options:")
    print("1. Create a new customer account")
    print("2. Check restaurant capacity")
    print("3. Calculate per person average sale for two weeks")
    print("4. Calculate change to be returned to customer")
    print("5. Estimate order delivery charges")
    print("6. Calculate total charges for an order")
    print("7. Convert temperature")
    print("8. Calculate employee net monthly income after tax")
    print("9. Sign up for a new account with AZA.")
    print("0. Exit")
    choice = input("Enter your choice: ")
    #return int(choice)
    if choice == '':
        return None
    else:
        return int(choice)

def create_customer_account():
    print("Customers Details...")
    customer = Customer()
    customer.get_details()
    customer.display_greeting()
    print()
    return_to_menu()

def check_restaurant_capacity():
    print("Restaurant Capacity...")
    def main():
        width = float(input("Enter the width of the restaurant (in meters): "))
        length = float(input("Enter the length of the restaurant (in meters): "))
        capacity_calculator = RestaurantCapacity(width, length)
        capacity = capacity_calculator.calculate_capacity()
        print(f"The restaurant can accommodate {capacity} persons.")

    if __name__ == '__main__':
        main()
    print()
    return_to_menu()

def calculate_average_sale():
    print("Executing Calculate per person average sale for two weeks...")
    analyzer = SaleAnalyzer()
    analyzer.get_sales()
    analyzer.analyze_sales()
    print()
    return_to_menu()

def calculate_change():
    print("Executing Calculate change to be returned to customer...")
    calculator = PaymentCalculator()
    calculator.calculate_change()
    print()
    return_to_menu()

def estimate_delivery_charges():
    print("Executing Estimate order delivery charges...")
    if __name__ == '__main__':
        calculator = DeliveryChargeCalculator()

        address = input("Enter your full address: ")
        distance = float(input("Enter the distance (in km) between your address and the restaurant: "))

        delivery_charge = calculator.calculate_delivery_charge(address, distance)

        print(delivery_charge)

    print()
    return_to_menu()

def calculate_total_charges():
    print("Executing Calculate total charges for an order...")
    order_calculator = OrderCalculator()
    order_calculator.calculate_order_charges()
    print()
    return_to_menu()

def convert_temperature():
    print("Executing Convert temperature...")

    temp_converter = TemperatureConverter()
    temp_converter.convert_temperature()

    print()
    return_to_menu()

def calculate_net_income():
    print("Executing Calculate employee net monthly income after tax...")
    if __name__ == "__main__":
        income_calculator = IncomeCalculator()
        income_calculator.calculate_net_income()
    print()
    return_to_menu()

def sign_up_for_account():
    print("Executing Sign up for a new account with AZA...")
    creds = UserCredentials()
    creds.register()
    print()
    return_to_menu()

def return_to_menu():
    choice = input("Do you want to go back to the main menu? (Y/N) ")
    if choice.lower() == "y":
        print()
        main()
    else:
        exit()

def main():
    choice = main_menu()
    while choice != 0:
        if choice == 1:
            create_customer_account()
        elif choice == 2:
            check_restaurant_capacity()
        elif choice == 3:
            calculate_average_sale()
        elif choice == 4:
            calculate_change()
        elif choice == 5:
            estimate_delivery_charges()
        elif choice == 6:
            calculate_total_charges()
        elif choice == 7:
            convert_temperature()
        elif choice == 8:
            calculate_net_income()
        elif choice == 9:
            sign_up_for_account()
        else:
            print("Invalid choice. Please try again..")
        choice = main_menu()

    print("Thank you for using the AZA Restaurant digital management platform!")

if __name__ == "__main__":
    main()
