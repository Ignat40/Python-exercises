'''
class PersonIdentification:
    def __init__(self, first_name: str, last_name: str, id_number:str):
        self.fn = first_name
        self.ln = last_name
        self.id = id_number

class BankAccountWallet(PersonIdentification):
    def __init__(self, owner:PersonIdentification, balance: float, accountIdentificator: int):
        self.owner = owner
        self.accountID = accountIdentificator
        self.balace = 0.0

    def deposit(self, amount: float):
        self.float += amount

    def withdraw(self, amount: float):
        if self.balace < amount:
            print("Durpay")
        else: 
            self.balace -= amount

    def print_balance(self):
        print("Balance: " + str(self.balace))

owner = PersonIdentification(PersonIdentification("Petar", "Atanasov", "0441234123"))
wallet = BankAccountWallet(owner, 1)
wallet.deposit(1000.0)
wallet.print_balance()
wallet.withdraw(755.3)
wallet.print_balance()
'''

#####################################################################################

'''
class Shape:
  
    def area(self):
        pass
    def perimeter(self):
        pass


class Cirle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return 3.14 * (self.r **2)
    
    def perimeter(self):
        return 2 * 3,14 * self.r
    
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.len = length

    def area(self):
        return self.width * self.len

    def perimeter(self):
        return 2 * (self.width + self.len)

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self). __init__(length, length)


if __name__ == '__main__':
    shapes = [Cirle(5), Rectangle(10, 3), Square(5)]

    for shape in shapes:
        print(f"shape: {type(shape)}, area: {shape.area()}, perimeter: {shape.perimeter()}")

###############################################################################################################################

class Student:
    id_auto_increment = 1

    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
        

        Student.id_auto_increment += 1



    def average(self):
        if len(self.grades) == 0:
            return 0

        return sum(self.grades) / len(self.grades)

    def add_grade(self, new_grade: float):
        if 2.0 <= new_grade <= 6.0:
            self.grades.append(new_grade)

    def get_score(self) -> str:
        return f"{self.id}, {self.first_name}, {self.last_name}, {self.average}"

#############################################################################################
class Person:
    def __init__(self, first_name, last_name, blood_type):
        self.first_name = first_name
        self.last_name  = last_name
        self.blood_type = blood_type

        @property
        def blood_type(self):
            return self.blood_type

        def __is_valid_blood_type(self, b_type:str) -> bool:
             allowed_blood_types = ["A", "B", "AB", "0"]

             for allowed_blood_types in allowed_blood_types:
                 if allowed_blood_types == b_type:
                     return True
                    
                 return False

        @blood_type.setter
        def blood_type(self, new_bloo_type:str):
           if self.__is_valid_blood_type(new_bloo_type):
               self.blood_type = blood_type


'''
###############################################################################################################







