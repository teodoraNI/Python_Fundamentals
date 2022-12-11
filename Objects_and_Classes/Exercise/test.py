#polimorphism -  function overriding
# class Animal:
#     multicellular = True
#     eukaryotic = True
#     def breathe(self):
#         print("I breathe oxygen.")
#     def feed(self):
#         print("I eat food.")
#
# class Herbivorous(Animal):
#     def feed(self):
#         print("I eat only plants. I am vegetarian.")
#
# herbi = Herbivorous()
# wolf = Animal()
# herbi.feed()
# wolf.feed()
#
# herbi.breathe()
# wolf.breathe()
#------------------------------------------------
# Python OOP Classes and Objects exercise
# class Vet:
#     animals = []
#     space = 5
#     def __init__(self, name: str):
#         self.name = name
#         self.animals = []
#     def register_animal(self, animal_name):
#         if Vet.space > 0:
#             Vet.space -= 1
#             self.animals.append(animal_name)
#             Vet.animals.append(animal_name)
#             return f"{animal_name} registered in the clinic"
#         else:
#             return "Not enough space"
#
#     def unregister_animal(self, animal_name):
#         if animal_name in Vet.animals:
#             self.animals.remove(animal_name)
#             Vet.animals.remove(animal_name)
#             Vet.space += 1
#             return f"{animal_name} unregistered successfully"
#         else:
#             return f"{animal_name} not in the clinic"
#
#     def info(self):
#         return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
#
#
# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())
#------------------------------------
class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    def next_second(self):
        if self.seconds == Time.max_seconds:
            self.seconds = 0
            if self.minutes == Time.max_minutes:
                self.minutes = 0
                if self.hours == Time.max_hours:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1
        return self.get_time()

time = Time(1, 20, 30)
print(time.next_second())
# ---------------------------------------------
# class Account:
#     def __init__(self, id: float, name: str, balance = 0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return self.balance
#         else:
#             return "Amount exceeded balance"
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"
#
# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())
#-----------------------------------------------
