
color = "blue"  # global

def spam():    
#    color = "pink"
    print(f"{color = }")
    animal = "wombat"   # local
    print(f"{animal = }")

spam()
print(f"{color = }")

# print(f"{animal = }")


def get_value():
    thing = 42
    return thing


x = get_value()
print(f"{x = }")



