import random

brands_of_car = {
    "bmw": {"fuel": 100, "strength": 100, "consumption": 6},
    "opel": {"fuel": 65, "strength": 100, "consumption": 9},
    "ferrari": {"fuel": 80, "strength": 100, "consumption": 14},
    "lada": {"fuel": 50, "strength": 100, "consumption": 10}
}

job_list = {
    "java developer": {"salary": 50, "gladness_less": 10},
    "python developer": {"salary": 40, "gladness_less": 3},
    "c++ developer": {"salary": 45, "gladness_less": 25}
}

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.strength = brand_list[self.brand]["strength"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print("The car cannot move!")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job_name = random.choice(list(job_list))
        self.salary = job_list[self.job_name]["salary"]
        self.gladness_less = job_list[self.job_name]["gladness_less"]

class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.gladness = 50
        self.money = 100
        self.satiety = 50
        self.car = None
        self.home = None
        self.job = None

    def get_car(self):
        self.car = Auto(brands_of_car)
        print(f"{self.name} bought a {self.car.brand}")

    def get_home(self):
        self.home = House()
        print(f"{self.name} got a home")

    def get_job(self):
        if self.car and self.car.drive():
            self.job = Job(job_list)
            print(f"{self.name} got a job: {self.job.job_name}")
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            self.satiety += 5
            self.home.food -= 5
            if self.satiety > 100:
                self.satiety = 100
            print(f"{self.name} ate. Satiety: {self.satiety}")

    def work(self):
        if self.car and self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 5
            print(f"{self.name} worked. Money: {self.money}, Gladness: {self.gladness}")
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()

    def shopping(self, manage):
        if self.car and not self.car.drive():
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("Bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def to_repair(self):
        self.car.strength = 100
        self.money -= 50

    def days_indexes(self, day):
        print(f"today the {day} of {self.name} life")
        print(f"money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        print("Home")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        print("Car")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def chill(self):
        self.gladness += 10
        self.satiety -= 5
        print(f"{self.name} relaxed. Gladness: {self.gladness}")

    def is_alive(self):
        if self.gladness <= 0:
            print(f"{self.name} depressed...")
            return False
        if self.satiety <= 0:
            print(f"{self.name} is dead of hunger...")
            return False
        if self.money < -500:
            print(f"{self.name} is bankrupt...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
            print(f"{self.job.job_name}")
        self.days_indexes(day)

        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()

        return True

    def clean_home(self):
        self.home.mess = 0
        self.gladness -= 5
        print(f"{self.name} cleaned the home. Gladness: {self.gladness}")

human = Human("Bob")
for day in range(1, 8):
    if not human.live(day):
        break
