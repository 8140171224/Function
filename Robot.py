class Robot:
    def __init__(self, name, colour, weight):
        self.name = name
        self.colour = colour
        self.weignt = weight

    def introduce_self(self):
        print("")
        print("My name is " + self.name)

class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
r1.introduce_self()
r2.introduce_self()

p1 = Person("aakash", "Nice", False)
p2 = Person("Dhaval", "Aggressive", True)

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()
