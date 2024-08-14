cities = list()    # cities = []   # cities = ["Pittsburgh", ...]

print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
cities.append("Topeka")
cities.append("Durham")
cities.append("Sacramento")
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(1, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)  # append each element of more_cities
print(f"cities: {cities}\n")

# LIST.append(obj)   LIST.insert(index, obj)  LIST.extend(iterable)

del cities[3]   # 
print(f"cities: {cities}\n")

if "Buffalo" in cities:   # cities.contains("Buffalo")
    cities.remove('Buffalo')
    print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

#  del LIST[index]      LIST.remove(value)    LIST.pop()   LIST.pop(index)






