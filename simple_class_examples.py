colors = list()    #  list colors = new list();
colors.append('red')
colors.append('purple')
colors.insert(0, "pink")
colors.sort()
print(f"{colors = }\n")
print(f"{type(colors) = }\n")

cities = list()
cities.append("Durham")

class Dog:
    def bark(self):   #  self == 'this'
        print("Woof! Woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
d2.bark()
