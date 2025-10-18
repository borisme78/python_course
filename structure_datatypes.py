# list (список)
cars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cars.append(1)
print(cars)
cars.remove(2)
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# set(множина)
bus = {1, 1, 1, 2, 3, 3, 5, 5,}
print(bus)
bus.add(9)
print(bus)
bus.add(5)
print(bus)
# tuple (кортеж)
car = (1, 2, 3)
print(car)
# dict (словник)
capital_city = {"Ukraine": "Kyiv" , "Italy": "Rome"}
print(capital_city)
capital_city["Japan"] = "Tokyo"
print(capital_city)
capital_city["Ukraine"] = "LVIV"
print(capital_city)
print(capital_city["Italy"])
personal_data = {"names" : ["Oleg", "Boris"] }
print(personal_data)
names = personal_data["names"] 
tnames = type(names)
print(tnames)
print(id(names))
print(id(personal_data["names"]))
names.append("Igor")
print(personal_data)
print(type(personal_data["names"]))
oleg = personal_data["names"][1]
print(oleg)


