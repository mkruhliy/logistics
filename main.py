"""
Logistic  System
"""
import random

class Location:
    """
    Assigning user's location
    """
    def __init__(self, city, postoffice):
        self.city = city
        self.postoffice = postoffice

class Item:
    """
    Assigning Item and its price
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f'{self.price}'


class Vehicle:
    """
    Assigning vehicles
    """
    def __init__(self, vehicleNo):
        self.vehicleNo = vehicleNo
        self.isAvailable = True

class Order:
    """
    Making orders
    """
    def __init__(self, user_name, location, items):
        self.id = random.randint(1000, 4000)
        self.user_name = user_name
        self.city = location.city
        self.postoffice = location.postoffice
        self.items = items
    def __str__(self):
        return f'Your order number is {self.id}'
    def calculateAmount(self):
        """
        Calculating the sum of an order
        """
        sum = 0
        for i in self.items:
            sum += float(str(i))
        return sum
    def assignVehicle(self, vehicle):
        """
        Assign vehicle if one is available
        """
        vehicle.isAvailable = False

class LogisticsSystem:
    """
    Placing and tracking orders
    """
    def __init__(self,vehicles):
        self.vehicles = vehicles
        self.ord = []
    def placeOrder(self, my_order):
        """
        Assigning vehicle and adding an order
        """
        count = 0
        for i in self.vehicles:
            if i.isAvailable == True:
                count += 1
                my_order.assignVehicle(i)
                self.ord.append(my_order)
                break
        if count == 0:
            print("There is no available vehicle to deliver an order.")
    def trackOrder(self, id):
        """
        Tracking orders
        """
        for i in self.ord:
            if i.id == id:
                return f"Your order #{id} is sent to {i.city}. Total \
price: {i.calculateAmount()} UAH."
        return 'No such order.'




if __name__ == "__main__":

    vehicles = [Vehicle(1), Vehicle(2)]
    LogSystem = LogisticsSystem(vehicles)

    my_items = [Item('book',110), Item('chupachups',44)]
    location = Location('Lviv', 53)
    my_order = Order(user_name = 'Oleg', location=location, items = my_items)
    print(my_order)
    LogSystem.placeOrder(my_order)
    print(LogSystem.trackOrder(my_order.id))

    my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
    location2 = Location('Odessa', 3)
    my_order2 = Order('Andrii', location2, my_items2)
    print(my_order2)
    LogSystem.placeOrder(my_order2)
    print(LogSystem.trackOrder(my_order2.id))

    my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
    location3 = Location('Kharkiv', 17)
    my_order3 = Order('Olesya', location3, my_items3)
    print(my_order3)
    LogSystem.placeOrder(my_order3)
    print(LogSystem.trackOrder(my_order3.id))
