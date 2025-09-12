import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 20
        self.alive = True

    def to_study(self):
        print(" Час вчитися")
        self.progress += 0.2
        self.gladness -= 3

    def to_sleep(self):
        print("💤 Час спати")
        self.gladness += 3

    def to_chill(self):
        print("Відпочинок")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 2  # під час відпочинку витрачає гроші

    def to_work(self):
        print(" Працюю")
        self.money += 10
        self.gladness -= 2

    def is_alive(self):
        if self.progress < -0.5:
            print("Відрахували...")
            self.alive = False
        elif self.gladness <= 0:
            print("Депресія...")
            self.alive = False
        elif self.progress >= 5:
            print("Склав екстерном!")
            self.alive = False

    def end_of_day(self):
        print(f"Радість = {self.gladness}")
        print(f"Успішність = {round(self.progress, 2)}")
        print(f"Гроші = {self.money}")

    def live(self, day):
        day_str = f"Day {day} of {self.name}'s life"
        print(f"{day_str:=^50}")

        cube = random.randint(1, 4)
        if cube == 1:
            self.to_study()
        elif cube == 2:
            self.to_sleep()
        elif cube == 3:
            self.to_chill()
        elif cube == 4:
            self.to_work()

        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
for day in range(1, 366):
    if not nick.alive:
        break
    nick.live(day)




