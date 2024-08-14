person = "Dolly Parton"
city = "Nashville"
value = 32.339383838392

print(person)
print(person, city)
print(person, city, value)

print(person, city, sep="#")
print(person, city, value, sep="//")

print(person, end=" ")
print(value)

# "Nashville: Dolly Parton"

print(f"{city}: {person}")
print(f"{person} lives in {city}")

# .format() method
print("{}: {}".format(city, person))
print("{} lives in {}".format(person, city))

print(city, person, sep=": ")

print(value)
print(f"{value:.2f}")

print(f"2 + 2 = {2 + 2}")

print(city)
print(f"city = {city}")

print(f"{city=}")
print(f"{city = }")   # repr()   vs  str()

x = f"{person} lives in {city}"
print(x)


