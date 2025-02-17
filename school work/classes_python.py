''''
class Vehicle:

    def __init__(self, listing_id, prive, max_speed, number_of_seats, year_of_produciton):
        self.id = listing_id
        self.price = prive
        self.max = max_speed
        self.seats = number_of_seats
        self.year = year_of_produciton

    def print_vehicle_type(self):
        print("Base Vehicle")
        
    def listing_info(self) -> str:
        return str(self.id) + " " + str(self.price) + " " +str(self.year) +" "+ str(self.max) + " " + str(self.seats)

class Bicycle(Vehicle):
    def __init__(self, listing_id, prive, max_speed, number_of_seats, year_of_produciton, make, is_mountain):
        super(Bicycle. self).__init__(listing_id, prive, max_speed, number_of_seats, year_of_produciton)
        self.brand = make
        self.MTB = is_mountain
    	
    def print_vehicle_type(self):
        print("Bicycle")

    def listing_info(self) -> str:
        return str(self.id) + " " + str(self.price) + " " +str(self.year) +" "+ str(self.max) + " " + str(self.seats) + " " + str(self.brand) + " " + str(self.MTB)

class Engine:
    def __init__(self, fuel_type, engine_size):
        self.fuel = fuel_type
        self. kapatsitet = engine_size

class Motor_Vechicle(Vehicle, Engine):
        def __init__(self, listing_id, prive, max_speed, number_of_seats, year_of_produciton, weight, is_accident_free):
            Vehicle.__init__(self, listing_id, prive, max_speed, number_of_seats, year_of_produciton)
            Engine.__init__(self, fuel_type, engine_size)

            self.is_free = is_accident_free
            self.weight = weight

        def print_vehicle_type(self):
            print ("Motor Vehicle")
        
        def listing_info(self) -> str:
          ##  return f"{self.id} {}
          '''

f =1 

x = int

for i in range(1, x+1):
    f *= i
    
print (f)